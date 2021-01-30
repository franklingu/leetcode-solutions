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
comment_mapping = {
    'cpp': ['/*', '*/'],
    'python': ['"""', '"""'],
    'python3': ['"""', '"""'],
    'java': ['/*', '*/'],
    'sql': ['/*', '*/'],
    'shell': [": '", "'"],
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


def solution_exists(question_meta, lang):
    if lang not in extension_mapping:
        print('unknown lang', lang)
        return True
    title = question_meta['stat']['question__title']
    title_slug = question_meta['stat']['question__title_slug']
    link = 'https://leetcode.com/problems/{}/'.format(title_slug)
    # difficulty = question_meta['stat']['difficulty']['level']
    target_dir = './questions/{}/'.format(title_slug)
    if not path.exists(target_dir):
        os.makedirs(target_dir)
    else:
        return True
    filepath = '{}{}.{}'.format(target_dir, 'Solution', extension_mapping[lang])
    if path.exists(filepath):
        return True
    return False


def output_solution(question_meta, question, solution, lang):
    title_slug = question_meta['stat']['question__title_slug']
    target_dir = './questions/{}/'.format(title_slug)
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
    


def main():
    with requests.Session() as session:
        session.headers.update({'Cookie': cookie})
        question_metas = get_question_meta(session)
        for question_meta in question_metas:
            if solution_exists(question_meta, 'python'):
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



if __name__ == '__main__':
    main()
