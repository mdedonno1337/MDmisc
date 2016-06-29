#!/usr/bin/python
# -*- coding: UTF-8 -*-

def upper( data ):
    return data.upper()

def join( i, c ):
    return c.join( i )

def split( i, c ):
    return c.split( i )

def split_r( lst, s ):
    try:
        return map( lambda x: split_r( lst[ 1: ], x ), s.split( lst[ 0 ] ) )
    except:
        return s

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
