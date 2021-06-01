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


class ParseReadmeState(Enum):
    Normal = 1
    Delete = 2


cookie = '_ga=GA1.2.1732111055.1582023294; csrftoken=JVDtuW3FZ2FWCe6xBS9pZ9V5kXfIqN4vzOoPyRuSgVH6efaj4UZIffVEXtsHzW2C; __cfduid=dc3dae53128fa248d50cfc8500b498e851620440034; gr_user_id=07f7668e-e948-4220-af44-bb5b2673a2e3; 87b5a3c3f1a55520_gr_last_sent_cs1=franklingu; _gid=GA1.2.897292705.1622357681; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMjA2ODk4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiYWxsYXV0aC5hY2NvdW50LmF1dGhfYmFja2VuZHMuQXV0aGVudGljYXRpb25CYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYWU5NjY1MzUxYmQzMTBjNjJlY2MyYzA4NmUxYTc1NWQ1NTI0MGQ1MiIsImlkIjoyMDY4OTgsImVtYWlsIjoiZnJhbmtsaW5ndWp1bmNoYW9AZ21haWwuY29tIiwidXNlcm5hbWUiOiJmcmFua2xpbmd1IiwidXNlcl9zbHVnIjoiZnJhbmtsaW5ndSIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLmNvbS91c2Vycy9mcmFua2xpbmd1L2F2YXRhcl8xNTI4MDEyMzMxLnBuZyIsInJlZnJlc2hlZF9hdCI6MTYyMjU0MDQ2MSwiaXAiOiIxMzIuMTQ3LjY0LjIzNyIsImlkZW50aXR5IjoiNGZhN2FlNzgyNDFlNTBkMzA0N2MxYTRlNTMzNWJmODUiLCJzZXNzaW9uX2lkIjoyMzI2NTc1fQ.MRIn6ELfcAZy7sQ8KJNrc6MSP4g3D59W4bCFi_0CekE; __atuvc=11%7C18%2C1%7C19%2C15%7C20%2C9%7C21%2C6%7C22; 87b5a3c3f1a55520_gr_cs1=franklingu; __cf_bm=9afdb3498a5a590668e26aed70da74ee0cdf307b-1622553003-1800-AcIDc4L5NMKbF3jR9fcxIAcOqtsNAzAX1E9Tx69SLATYMANEuKrfOg+uXkyGAaj5WcWrBBkf/sgvz5omp4ql4a8=; c_a_u="ZnJhbmtsaW5ndQ==:1lo49m:CvWvu0SyV5kBMQnHZ7LgXZPFf0M"; _gat=1'


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
