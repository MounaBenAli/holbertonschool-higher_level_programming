#!/usr/bin/python3
print(*["%c" % a for a in range(ord('a'),ord('z')+1) if "%c" % a not in 'qe'],sep='',end='')
