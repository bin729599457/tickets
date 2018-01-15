# coding: utf-8
"""Train tickets query via command-line.

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help        显示帮助菜单
    -g               高铁
    -d               动车
    -t               特快
    -k               快速
    -z               直达

Example:

    tickets 南京 北京 2016-07-01
    tickets -dg 南京 北京 2016-07-01
    python3 tickets.py 上海 北京 2016-07-01
    output:{ '-d': False,
             '-g': False,
             '-k': False,
             '-t': False,
             '-z': False,
             '<date>': '2016-07-01',
             '<from>': '上海',
             '<to>': '北京'}


"""
from docopt import docopt

def cli():
    """command-line interface"""
    arguments = docopt(__doc__)
    print(arguments)

if __name__ == '__main__':
    cli()