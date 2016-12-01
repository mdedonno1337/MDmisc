#!/usr/bin/python
# -*- coding: UTF-8 -*-

import collections

from .map_r import map_r

def replace_r( x, s, r ):
    def test( x, s = s, r = r ):
        if x == s:
            return r
        else:
            return x
    
    return map_r( test, x )

def flatten( lst ):
    for e in lst:
        if isinstance( e, collections.Iterable ) and not isinstance( e, basestring ):
            for sublist in flatten( e ):
                yield sublist
        else:
            yield e

def ifany( a, b ):
    for i in a:
        if i in b:
            return True
    else:
        return False

def ifall( a, b ):
    for i in a:
        if i not in b:
            return False
    
    else:
        return True
