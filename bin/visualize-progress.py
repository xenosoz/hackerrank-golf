#!/usr/bin/env python3
'''Generate progress graph and overwrite to README.md'''

import sys
import re
from pathlib import Path
from textwrap import dedent
from glob import glob
from collections import defaultdict
from operator import itemgetter


def header():
    x = '''
    # HackerRank Golf

    We solve [HackerRank](https://www.hackerrank.com) for some knowledge and fun!
    Contact me if you want to join us!

    * Taihyun Hwang &lt;xenosoz.hwang at gmail.com&gt;
    '''
    return dedent(x)

def here():
    return Path(sys.argv[0]).parent

def hackerrank_golf_path():
    return here().joinpath('..')

def domains_path():
    return hackerrank_golf_path().joinpath('domains')

def replace_to_slash(s):
    return s.replace('\\', '/')

def users():
    return ['xenosoz', 'daebak', 'timewalker', 'Join us!']

def shorten_language(lang):
    if lang == 'python3': return 'py3'
    if lang == 'golang': return 'go'
    return lang

def filestats():
    pattern = '\.'.join([
        '(?P<user_id>[a-zA-Z0-9_-]+)',
        '(?P<challenge_id>[a-zA-Z0-9_-]+)',
        '(?P<language>[a-zA-Z0-9_-]+)',
    ])
    pattern = re.compile(pattern)

    for path in domains_path().glob('**/*'):
        m = re.match(pattern, path.name)
        if m:
            stat = m.groupdict()
            stat['path'] = path
            stat['name'] = path.name
            stat['language_short'] = shorten_language(stat['language'])
            stat['slash_path'] = replace_to_slash(str(path))
            yield stat


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
    oracle = defaultdict(list)
    for x in stats:
        oracle[(x['user_id'], x['challenge_id'])].append(x)

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
            links = []
            for stat in sorted(oracle.get((user, chal), []), key=itemgetter('language_short')):
                href = stat['slash_path']
                alt = stat['name']
                body = stat['language_short']  # OLD: U+2714; HEAVY CHECK MARK (✔)
                links.append('<a href="{}" alt="{}">{}</a>'.format(href, alt, body))
            link = ', '.join(links)
            print('      <th>{}</th>'.format(link))
        print('    </tr>')
    print('  </tbody>')
    print('</table>')

    return '\n'.join(ret)

print(header())
print('## Progress')
print(progress_table())
