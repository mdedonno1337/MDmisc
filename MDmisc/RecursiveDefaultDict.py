#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from _collections import defaultdict

from MDmisc.DefaultOrderedDict import DefaultOrderedDict

class edefaultdict( defaultdict ):
    def get_by_keys( self, lst ):
        return [ self.get( key ) for key in lst ]

    def to_dict( self ):
        for key, value in self.iteritems():
            if isinstance( value, edefaultdict ):
                self[ key ] = value.to_dict()
            
        return dict( self )

defDict = lambda: edefaultdict( defDict )
defOrderedDict = lambda: DefaultOrderedDict( defOrderedDict )
