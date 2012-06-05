# coding: utf-8

import sys
import time
from aojtools import api

if len(sys.argv) < 2:
    print 'usage: %s userid userid' % __file__
    sys.exit()

usr1 = api.user(sys.argv[1])
usr2 = api.user(sys.argv[2])

pset1 = set(p.id for p in usr1.solved_list.problem)
pset2 = set(p.id for p in usr2.solved_list.problem)


def diff(src, dst):
    d = src.difference(dst)
    for i,pid in enumerate(sorted(d)):
        print '%04d' % pid,
        if i % 15 == 0 and i > 0:
            print ''
diff(pset1, pset2)
diff(pset2, pset1)

