#!/usr/bin/env python
#  *-* coding: utf-8 *-*

class stringIterator( object ):
    def __init__( self, data ):
        self.data = data
        self.index = 0
        
    def next( self ):
        ret = self.data[ self.index ]
        self.index += 1
        return ret
    
    def take( self, n ):
        ret = ''.join( self.data[ self.index: self.index + n ] )
        self.index += n
        return ret
    
    def __iter__( self ):
        return self
