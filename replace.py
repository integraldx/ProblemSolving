import sys

instream = sys.stdin.readlines(99999)
for s in instream:
    if s.startswith("#include \""):
        s = s[10:-2]
        f = open(s, 'r')
        for st in f.readlines(99999):
            print(st, end = '')
    else:
        print(s, end = '')