#!/usr/bin/env python
"""download solutions from leetcode account
"""
import os
from os import path
import re
from enum import Enum

import requests
from bs4 import BeautifulSoup


extension_mapping = {
    'cpp': 'cpp',
    'python': 'py',
    'python3': 'py',
    'java': 'java',
    'sql': 'sql',
    'mysql': 'sql',
    'shell': 'sh',
}
lang_name_mapping = {
    'cpp': 'C++',
    'py': 'Python',
    'java': 'Java',
    'sql': 'SQL',
    'mysql': 'SQL',
    'sh': 'Shell',
}
comment_mapping = {
    'cpp': ['/*', '*/'],
    'python': ['"""', '"""'],
    'python3': ['"""', '"""'],
    'java': ['/*', '*/'],
    'sql': ['/*', '*/'],
    'mysql': ['/*', '*/'],
    'shell': [": '", "'"],
}
diff_mapping = {
    1: ['Easy', 'https://img.shields.io/badge/-Easy-green'],
    2: ['Medium', 'https://img.shields.io/badge/-Medium-orange'],
    3: ['Hard', 'https://img.shields.io/badge/-Hard-red'],
}


class ParseReadmeState(Enum):
    Normal = 1
    Delete = 2


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
        "query": "\n    query submissionList($offset: Int!, $limit: Int!, $lastKey: String, $questionSlug: String!, $lang: Int, $status: Int) {\n  questionSubmissionList(\n    offset: $offset\n    limit: $limit\n    lastKey: $lastKey\n    questionSlug: $questionSlug\n    lang: $lang\n    status: $status\n  ) {\n    lastKey\n    hasNext\n    submissions {\n      id\n      title\n      titleSlug\n      status\n      statusDisplay\n      lang\n      langName\n      runtime\n      timestamp\n      url\n      isPending\n      memory\n      hasNotes\n    }\n  }\n}\n    ",
        "variables": {
            "questionSlug": question_meta['stat']['question__title_slug'],
            "offset": 0,
            "limit": 20,
            "lastKey": None,
        }
    })
    submissions = res.json()['data']['questionSubmissionList']['submissions']
    selected = None
    lang = None
    for submission in submissions:
        lang = submission['lang']
        status = submission['statusDisplay']
        if status == 'Accepted':
            selected = submission
            break
    if selected is None:
        print('no AC solution found: ', question_meta['stat']['question__title'])
        return None
    res = session.post('https://leetcode.com/graphql', json={
        "query": "\n    query submissionDetails($submissionId: Int!) {\n  submissionDetails(submissionId: $submissionId) {\n    runtime\n    runtimeDisplay\n    runtimePercentile\n    runtimeDistribution\n    memory\n    memoryDisplay\n    memoryPercentile\n    memoryDistribution\n    code\n    timestamp\n    statusCode\n    user {\n      username\n      profile {\n        realName\n        userAvatar\n      }\n    }\n    lang {\n      name\n      verboseName\n    }\n    question {\n      questionId\n    }\n    notes\n    topicTags {\n      tagId\n      slug\n      name\n    }\n    runtimeError\n    compileError\n    lastTestcase\n  }\n}\n    ",
        "variables": {
            "submissionId": selected['id'],
        },
    })
    submission_details = res.json()['data']['submissionDetails']
    return submission_details['code'], lang


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
    print('Generate new table')
    lines = []
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
        line = '|{number}|[{title}]({link})|[{langs}]({relpath})|![{level}]({level_badge})|\n'.format(
            number=number, title=title, link=link, langs=','.join(langs), relpath=target_dir, 
            level=diff_mapping[difficulty][0], level_badge=diff_mapping[difficulty][1],
        )
        lines.append(line)
    content_lines = []
    with open('./README.md', 'r') as ifile:
        state = ParseReadmeState.Normal
        for line in ifile:
            new_state = None
            if line.strip() == '### Contents':
                new_state = ParseReadmeState.Delete
            elif line.strip() == '### Features':
                new_state = ParseReadmeState.Normal
            prev_state = state
            if new_state is None:
                pass
            else:
                state = new_state
            if state == ParseReadmeState.Delete:
                if state != prev_state:
                    content_lines.append('### Contents\n\n| # | Title | Solution | Difficulty |\n|---| ----- | -------- | ---------- |\n')
                    content_lines.extend(lines)
                    content_lines.append('\n')
            elif state == ParseReadmeState.Normal:
                content_lines.append(line)
    with open('./README.md', 'w') as ofile:
        for line in content_lines:
            ofile.write(line)


def main():
    with requests.Session() as session:
        session.headers.update({'Cookie': cookie})
        question_metas = get_question_meta(session)
        output_newly_added_solutions(session, question_metas)
        output_solutions_table(question_metas)
        



if __name__ == '__main__':
    main()
