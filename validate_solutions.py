#!/usr/bin/env python
"""Validate solutions by enforcing file and table formats
"""
import os
import re
import logging
import time
import random

import requests
from lxml import html as HTMLParser


def read_solutions_table(readme_fp):
    def parse_line(line):
        elems = [el for el in line.strip().split('|') if el]
        question_elem = elems[1]
        match = re.search(r'\[(.+?)\]\((.+)\)', question_elem)
        if not match:
            raise ValueError('{} is not a valid link'.format(question_elem))
        elems[1] = (match.group(1), match.group(2))
        solution_elem = elems[2]
        match = re.search(r'\[(.+?)\]\((.+)\)', solution_elem)
        if not match:
            raise ValueError('{} is not a valid link'.format(solution_elem))
        elems[2] = (match.group(1).split(','), match.group(2))
        return elems

    data = []
    in_content = begin_parsing = False
    with open(readme_fp) as ifile:
        for line in ifile:
            if line.startswith('### Contents'):
                in_content = True
            elif in_content and line.startswith('|---'):
                begin_parsing = True
            elif begin_parsing and line.startswith('|'):
                data.append(parse_line(line))
            elif begin_parsing and not line.strip():
                begin_parsing = False
                in_content = False
    return data


def validate_questions(solutions_data, retry=7, sleep=30, **kwargs):  #pylint: disable=unused-argument
    ua = (
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    )
    for elems in solutions_data:
        # question_number = elems[0]
        question_title, question_link = elems[1]
        for _ in range(retry):
            try:
                with requests.Session() as ses:
                    ses.headers.update({'User-Agent': ua})
                    res = ses.get(question_link, timeout=sleep)
                    parsed = HTMLParser.fromstring(res.content)
                    title = parsed.cssselect('title')
                    if not title:
                        raise ValueError('No question found')
                    cleaned_title = title[0].text.split(' - LeetCode')[0].strip()
                    if cleaned_title == question_title:
                        logging.getLogger(__name__).info(
                            'Question validation done for %s', cleaned_title
                        )
                        break
                    else:
                        raise ValueError('Not matched: {} vs {}'.format(
                            cleaned_title, question_title
                        ))
            except Exception as err:  #pylint: disable=broad-except
                logging.getLogger(__name__).warning(
                    'Error during validate question %s: %s', question_title, err
                )
                time.sleep(random.random() * sleep)
        else:
            raise ValueError('{} seems invalid'.format(question_link))
    logging.getLogger(__name__).info('%d questions verified', len(solutions_data))

def validate_solutions(solutions_data, **kwargs):
    curr_dir = kwargs['curr_dir']
    language_map = {
        'cpp': 'C++', 'py': 'Python', 'java': 'Java',
        'sql': 'SQL', 'sh': 'Shell',
    }
    for elems in solutions_data:
        track = set(elems[2][0])
        dirpath = os.path.join(curr_dir, elems[2][1])
        for fname in os.listdir(dirpath):
            fpart, ext = os.path.splitext(fname)
            if fpart != 'Solution':
                raise ValueError('{} is an invalid filename'.format(fpart))
            try:
                track.remove(language_map.get(ext[1:]))
            except KeyError:
                pass
        if track:
            raise ValueError('Langugage remaining: {}'.format(track))
        logging.getLogger(__name__).info(
            '%s solution validation done', elems[1][0]
        )
    logging.getLogger(__name__).info('%d solutions verified', len(solutions_data))


def main():
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    readme_fp = os.path.join(curr_dir, 'README.md')
    solutions_data = read_solutions_table(readme_fp)
    validate_questions(solutions_data, curr_dir=curr_dir)
    validate_solutions(solutions_data, curr_dir=curr_dir)


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO
    )
    try:
        main()
    except Exception as err:  #pylint: disable=broad-except
        logging.getLogger(__name__).exception('Exception: %s', err)
        raise
