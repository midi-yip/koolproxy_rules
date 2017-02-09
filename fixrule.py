#!/usr/bin/python

import codecs
import sys

s = ""
with codecs.open(sys.argv[1], "r", encoding="utf-8") as f:
    for line0 in f:
        line = line0.strip()
        if line[0] == '!':
            s += line + "\n"
            continue
        pos = line.find("##")
        if pos < 0:
            s += line + "\n"
            continue
        text = line[0:pos]
        end = line[pos:]
        if text.find(",") < 0:
            if text.startswith("|"):
                s += line + "\n"
            else:
                s += "||" + line + "\n"
            continue

        start = 0
        prefix = ""
        if text.startswith("||http://"):
            prefix = "||http://"
            start = len(prefix)
        elif text.startswith("|http://"):
            prefix = "|http://"
            start = len(prefix)
        elif text.startswith("||https://"):
            prefix = "||https://"
            start = len(prefix)
        elif text.startswith("||"):
            prefix = "||"
            start = len(prefix)
        elif text.startswith("|"):
            start = 1
            prefix = "|"
        else:
            prefix = "||"
            start = 0
        for token in text[start:].split(","):
            if token[0] == '~':
                continue
            s += prefix + token + end + "\n"

print s
