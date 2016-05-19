#!/usr/bin/env python
#  *-* coding: cp850 *-*

def xfrange( start, stop = None, step = 1.0 ):
    if stop is None:
        stop = float( start )
        start = 0.0

    cur = float( start )

    while cur <= stop:
        yield cur
        cur += step
