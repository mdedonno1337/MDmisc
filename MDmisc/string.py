#!/usr/bin/python
# -*- coding: UTF-8 -*-

from .boxer import boxer
from .logger import debug


def upper( data ):
    """
        Function equivalent of the str.upper() function.
    """
    return data.upper()

def join( c, i = None ):
    """
        Function equivalent of the str.join() function. If the function is
        called only with one argument, i.e. the list, the join is made without
        spacing between the elements of the list.
        
        >>> join( ";", ['1-2-3', '4-5-6', '7-8-9'] )
        '1-2-3;4-5-6;7-8-9'
        
        >>> join( ['1', '2', '3', '4', '5', '6'] )
        '123456'
    """
    if i == None:
        c, i = "", c
    
    try:
        return c.join( i )
    except:
        debug.critical( boxer( "Error in calling the join() function", "The separator have to be passed first, and the iterable second" ), 1 )
        return i.join( c )

def split( i, c ):
    """
        Function equivalent of str.split()
        
        >>> split( ";", "1-2-3;4-5-6;7-8-9" )
        ['1-2-3', '4-5-6', '7-8-9']
    """
    return c.split( i )

def split_r( lst, s ):
    """
        Recursive split a string.
        
        >>> split_r( [ ';', '-' ], "1-2-3;4-5-6;7-8-9" )
        [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    """
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
    
def split_no_empty( data, string ):
    return [ value for value in data.split( string ) if value != "" ]

