#!/usr/bin/python
# -*- coding: UTF-8 -*-

from .map_r import map_r

def replace_r( x, s, r ):
    def test( x, s = s, r = r ):
        if x == s:
            return r
        else:
            return x
    
    return map_r( test, x )

def flatten( lst ):
    return [item for sublist in lst for item in sublist]
