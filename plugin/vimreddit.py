# -*- coding: utf-8 -*-

import textwrap
import json
import vim
import webbrowser
import urllib2
import re

def redditurl(subreddit):
    return 'http://www.reddit.com/r/' + subreddit + '/hot.json'

MARKDOWN_URL = 'http://fuckyeahmarkdown.com/go/?read=1&u='

def bufwrite(string):
    b = vim.current.buffer

    # Never write more than two blank lines in a row
    if not string.strip() and not b[-1].strip() and not b[-2].strip():
        return

    # Vim must be given UTF-8 rather than unicode
    if isinstance(string, unicode):
        string = string.encode('utf-8', errors='replace')

    # Code block markers for syntax highlighting
    if string and string[-1] == unichr(160).encode('utf-8'):
        b[-1] = string
        return

    if not b[0]:
        b[0] = string
        return

    if not b[0]:
        b[0] = string
    else:
        b.append(string)

urls = [None] * 1000 # urls[index]: url of link at index

def vim_reddit(sub):
    vim.command('edit .reddit')
    vim.command('setlocal noswapfile')
    vim.command('setlocal buftype=nofile')

    bufwrite('    ┌─o')
    bufwrite(' ((•  •))  r e d d i t')
    bufwrite(' http://www.reddit.com/r/' + sub)
    bufwrite('')

    items = json.loads(urllib2.urlopen(redditurl(sub)).read())
    for i, item in enumerate(items['data']['children']):
        item = item['data']
        try:
            # surround shorter numbers (e.g. 9) with padding
            # to align with longer numbers
            index = (2 - len(str(i + 1))) * ' ' + str(i + 1) + '. '

            line_1 = index + item['title'] + \
                     ' (' + item['domain'] + ')'
            line_2 = '    ' + str(item['score']) + ' points, by ' + \
                     item['author'] + ' | ' + str(item['num_comments']) + \
                     ' comments'
            bufwrite(line_1)
            bufwrite(line_2)
            bufwrite('')

            urls[i + 1] = item['url']
        except KeyError:
            pass

def vim_reddit_link(in_browser = False):
    line = vim.current.line
    print urls[int(line.split()[0].replace('.', ''))]

    regexp = re.compile(r'\d+\.')
    if regexp.search(line) is not None:
        id = line.split()[0].replace('.', '')
        if in_browser:
            browser = webbrowser.get()
            browser.open(urls[int(id)])
            return
        vim.command('edit .reddit')
        content = urllib2.urlopen(
            MARKDOWN_URL + urls[int(id)]
        ).read()
        for i, line in enumerate(content.split('\n')):
            if not line:
                bufwrite('')
                continue
            line = textwrap.wrap(line, width=80)
            for wrap in line:
                bufwrite(wrap)
        return
    print 'vim-reddit error: could not parse item'

