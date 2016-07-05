#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from _collections import defaultdict

from MDmisc.DefaultOrderedDict import DefaultOrderedDict

class edefaultdict( defaultdict ):
    def get_by_keys( self, lst ):
        return [ self.get( key ) for key in lst ]

defDict = lambda: edefaultdict( defDict )
defOrderedDict = lambda: DefaultOrderedDict( defOrderedDict )
