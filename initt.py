#!/usr/bin/env python
'''Utility for initializing project directories'''

import os
from typing import Dict
from argparse import ArgumentParser
from tarfile import open as taropen
from subprocess import call as subcall
from pathlib import Path


TEMPLATE_PATHS = [
    Path('./templates-bin').resolve(),
    Path('~/.local/share/initt').expanduser(),
    Path('/usr/share/initt/templates')
]
DIR_TXT = Path('dir.txt')
FILE_TXT = Path('file.txt')
INIT_SH = Path('init.sh')


def templates() -> Dict[str, Path]:
    '''Returns a dict of Pathnames and -objects'''
    temp = [arg.joinpath(x) for arg in TEMPLATE_PATHS if arg.exists()
            for x in arg.iterdir()]
    return {os.path.splitext(x.stem)[0]: x for x in temp
            if not x.is_dir() and not x.match('Makeppfile')}


if __name__ == '__main__':

    PARSER = ArgumentParser(prog='initt')
    PARSER.add_argument('templatename', default='empty', nargs='?',
                        help='One of the installed templates', choices=templates().keys())

    PARSER.add_argument('-n', '--name', help="Creates a subdir with this name")
    ARGS = PARSER.parse_args()

    if ARGS.name:
        os.makedirs(ARGS.name)
        os.chdir(ARGS.name)
    else:
        ARGS.name = os.path.basename(str(Path('.').resolve()))

    TEMPLATE = templates()[ARGS.templatename]
    with taropen(TEMPLATE, mode='r') as templtar:
        templtar.extractall()

    if DIR_TXT.exists():
        with open(DIR_TXT) as dtxt:
            for line in dtxt:
                os.makedirs(line.rstrip('\n'), exist_ok=True)

    if FILE_TXT.exists():
        with open(FILE_TXT) as ftxt:
            for line in ftxt:
                Path(line.rstrip('\n')).touch()

    if INIT_SH.exists():
        subcall([str(INIT_SH.resolve()), ARGS.name])

    for fi in [DIR_TXT, FILE_TXT, INIT_SH]:
        if fi.exists():
            fi.unlink()
