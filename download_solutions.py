#!/usr/bin/env python
"""download solutions from leetcode account
"""
import os
from os import path
import re

import requests
from bs4 import BeautifulSoup


extension_mapping = {
    'cpp': 'cpp',
    'python': 'py',
    'python3': 'py',
    'java': 'java',
    'sql': 'sql',
    'shell': 'sh',
}
lang_name_mapping = {
    'cpp': 'C++',
    'py': 'Python',
    'java': 'Java',
    'sql': 'SQL',
    'sh': 'Shell',
}
comment_mapping = {
    'cpp': ['/*', '*/'],
    'python': ['"""', '"""'],
    'python3': ['"""', '"""'],
    'java': ['/*', '*/'],
    'sql': ['/*', '*/'],
    'shell': [": '", "'"],
}
diff_mapping = {
    1: ['Easy', 'https://img.shields.io/badge/-Easy-green'],
    2: ['Medium', 'https://img.shields.io/badge/-Medium-orange'],
    3: ['Hard', 'https://img.shields.io/badge/-Hard-red'],
}
cookie = ''


def get_question_meta(session):
    res = session.get('https://leetcode.com/api/problems/all/')
    total = res.json()['stat_status_pairs']
    return [stat for stat in total if stat.get('status') == 'ac' and not stat.get('paid')]


def get_question(session, question_meta):
    res = session.post('https://leetcode.com/graphql', json={
        "operationName": "questionData",
        "variables": {
            "titleSlug": question_meta['stat']['question__title_slug']
        },
        "query": "query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    boundTopicId\n    title\n    titleSlug\n    content\n    translatedTitle\n    translatedContent\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n    isLiked\n    similarQuestions\n    exampleTestcases\n    contributors {\n      username\n      profileUrl\n      avatarUrl\n      __typename\n    }\n    topicTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n    codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    }\n    stats\n    hints\n    solution {\n      id\n      canSeeDetail\n      paidOnly\n      hasVideoSolution\n      paidOnlyVideo\n      __typename\n    }\n    status\n    sampleTestCase\n    metaData\n    judgerAvailable\n    judgeType\n    mysqlSchemas\n    enableRunCode\n    enableTestMode\n    enableDebugger\n    envInfo\n    libraryUrl\n    adminUrl\n    __typename\n  }\n}\n",
    })
    content = res.json()['data']['question']['content']
    question = '<html>{}</html>'.format(content)
    soup = BeautifulSoup(question, features="html.parser")
    return soup.get_text()


def get_solution(session, question_meta):
    res = session.post('https://leetcode.com/graphql', json={
        "operationName": "Submissions",
        "variables": {
            "offset": 0,
            "limit": 20,
            "lastKey": None,
            "questionSlug": question_meta['stat']['question__title_slug']
        },
        "query": "query Submissions($offset: Int!, $limit: Int!, $lastKey: String, $questionSlug: String!) {\n  submissionList(offset: $offset, limit: $limit, lastKey: $lastKey, questionSlug: $questionSlug) {\n    lastKey\n    hasNext\n    submissions {\n      id\n      statusDisplay\n      lang\n      runtime\n      timestamp\n      url\n      isPending\n      memory\n      __typename\n    }\n    __typename\n  }\n}\n"
    })
    submissions = res.json()['data']['submissionList']['submissions']
    selected = None
    lang = None
    for submission in submissions:
        lang = submission['lang']
        status = submission['statusDisplay']
        if status == 'Accepted':
            selected = submission
            break
    if selected is None:
        return None
    res = session.get('https://leetcode.com{}'.format(selected['url']))
    code_line = ''
    for line in res.text.split('\n'):
        if 'submissionCode:' in line:
            code_line = line
            break
    match = re.search("submissionCode: '(.+)'", code_line)
    if match is None:
        print('cannot find solution: ', question_meta['stat']['question__title'])
        return None, None
    code_line = match.group(1)
    code_line = code_line.encode('utf-8').decode('unicode-escape')
    return code_line, lang


def get_solution_dir(question_meta):
    title_slug = question_meta['stat']['question__title_slug']
    return './questions/{}/'.format(title_slug)


def solution_exists(question_meta):
    return path.exists(get_solution_dir(question_meta))


def output_solution(question_meta, question, solution, lang):
    target_dir = get_solution_dir(question_meta)
    if not path.exists(target_dir):
        os.makedirs(target_dir)
    filepath = '{}{}.{}'.format(target_dir, 'Solution', extension_mapping[lang])
    opening, closing = comment_mapping[lang]
    with open(filepath, 'w') as ofile:
        ofile.write(opening + '\n')
        ofile.write('\n')
        ofile.write(question)
        ofile.write('\n')
        ofile.write(closing + '\n')
        ofile.write('\n\n')
        ofile.write(solution)
    return True


def output_newly_added_solutions(session, question_metas):
    print('The newly generated solutions table\n\n\n\n\n')
    for question_meta in question_metas:    
        if solution_exists(question_meta):
            continue
        question = get_question(session, question_meta)
        solution, lang = get_solution(session, question_meta)
        if solution is None:
            continue
        outputed = output_solution(question_meta, question, solution, lang)
        title = question_meta['stat']['question__title']
        if not outputed:
            print('ignore:', title)
        else:
            print('output:', title)


def output_solutions_table(question_metas):
    for question_meta in sorted(question_metas, key=lambda a: int(a['stat']['frontend_question_id'])):
        number = question_meta['stat']['frontend_question_id']
        title = question_meta['stat']['question__title']
        title_slug = question_meta['stat']['question__title_slug']
        link = 'https://leetcode.com/problems/{}/'.format(title_slug)
        difficulty = question_meta['difficulty']['level']
        target_dir = get_solution_dir(question_meta)
        if not solution_exists(question_meta):
            continue
        langs = []
        for fp in os.listdir(target_dir):
            ext = fp.split('.')[-1]
            langs.append(lang_name_mapping[ext])
        print('|{number}|[{title}]({link})|[{langs}]({relpath})|![{level}]({level_badge})|'.format(
            number=number, title=title, link=link, langs=','.join(langs), relpath=target_dir, 
            level=diff_mapping[difficulty][0], level_badge=diff_mapping[difficulty][1],
        ))


def main():
    with requests.Session() as session:
        session.headers.update({'Cookie': cookie})
        question_metas = get_question_meta(session)
        output_newly_added_solutions(session, question_metas)
        output_solutions_table(question_metas)
        



if __name__ == '__main__':
    main()
