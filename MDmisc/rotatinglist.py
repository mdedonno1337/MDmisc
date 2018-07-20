#!/usr/bin/python
# -*- coding: UTF-8 -*-

class rotating_list( object ):
    def __init__( self, data = None ):
        if data == None:
            self.data = []
        else:
            self.data = data
        self.i = 0
    
    def current( self ):
        return self.data[ self.i ]
    
    def last( self ):
        return self.data[ -1 ]
    
    def append( self, el ):
        return self.data.append( el )
    
    def next( self ):
        d = self.data[ self.i ]
        self.i = ( self.i + 1 ) % len( self.data )
        return d
    
    def rnext( self ):
        n = self.next()
        if isinstance( n, rotating_list ):
            return n.next()
        else:
            return n
    
    def __repr__( self, *args, **kwargs ):
        return str( self.data )
    
