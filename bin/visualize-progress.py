#!/usr/bin/env python3
'''Generate progress graph and overwrite to README.md'''

import os
import sys
import re
from textwrap import dedent
from glob import glob

def header():
    x = '''
    # HackerRank Golf

    We solve [HackerRank](https://www.hackerrank.com) for some knowledge and fun!
    Contact me if you want to join us!

    * Taihyun Hwang &lt;xenosoz.hwang at gmail.com&gt;
    '''
    return dedent(x)

def here():
    return os.path.dirname(sys.argv[0])

def hackerrank_golf_path():
    return os.path.join(here(), '..')

def domains_path():
    return os.path.join(hackerrank_golf_path(), 'domains')

def users():
    return ['xenosoz', 'daebak', '같이 해요!']

def filestats():
    pattern = '\.'.join([
        '(?P<user_id>[a-zA-Z0-9_-]+)',
        '(?P<challenge_id>[a-zA-Z0-9_-]+)',
        '(?P<language>[a-zA-Z0-9_-]+)',
    ])
    pattern = re.compile(pattern)

    for filepath in glob(os.path.join(domains_path(), '**', '*.py'), recursive=True):
        basename = os.path.basename(filepath)
        m = re.match(pattern, basename)
        if m:
            yield m.groupdict()


def chal_to_url(chal):
    return 'https://www.hackerrank.com/challenges/{}'.format(chal)


def chal_to_link(chal):
    url = chal_to_url(chal)
    return '<a href="{}">{}</a>'.format(url, chal)


def progress_table():
    ret = []
    def print(s):  # XXX
        ret.append(s)

    stats = list(filestats())
    challenges = sorted(set(x['challenge_id'] for x in stats))
    oracle = set((x['user_id'], x['challenge_id']) for x in stats)

    print('<table>')
    print('  <thead>')
    print('    <tr>')
    print('      <th>challenge</th>')
    for user in users():
        print('      <th>{}</th>'.format(user))
    print('    </tr>')
    print('  </thead>')

    print('  <tbody>')
    for chal in challenges:
        print('    <tr>')
        print('      <th>{}</th>'.format(chal_to_link(chal)))
        for user in users():
            solved = ((user, chal) in oracle)
            print('      <th>{}</th>'.format(['', '✔'][solved]))
        print('    </tr>')
    print('  </tbody>')
    print('</table>')

    return '\n'.join(ret)

print(header())
print('## Progress')
print(progress_table())
