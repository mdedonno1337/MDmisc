#!/usr/bin/python
# -*- coding: UTF-8 -*-

class rotating_list( object ):
    def __init__( self, data ):
        self.data = data
        self.i = 0
        self.max = len( data )
    
    def next( self ):
        d = self.data[ self.i % self.max ]
        self.i += 1
        return d
