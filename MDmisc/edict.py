#!/usr/bin/python
# -*- coding: UTF-8 -*-

import collections

class edict( dict ):
    def reverse( self ):
        d = {}
        for key, value in self.iteritems():
            if d.has_key( value ):
                if type( d[ value ] ) != list:
                    d[ value ] = [ d[ value ] ]
                    
                d[ value ].append( key )
            else:
                d[ value ] = key
            
        return d
    
    def search( self, searched ):
        for key, value in self.iteritems():
            if value == searched:
                return key
        
        else:
            return None
        
    def get_by_keys( self, lst ):
        return [ self.get( key ) for key in lst ]
    
    def get_r( self, path, split = "/" ):
        if isinstance( path, ( str, unicode ) ):
            path = path.split( split )
        
        tmp = self
        for key in path:
            if key in tmp.keys():
                tmp = tmp.get( key )
            else:
                raise KeyError( "'%s' key not found" % key )
          
        return tmp
    
def convert_unicode_to_str( data ):
    if isinstance( data, basestring ):
        return str( data )
    elif isinstance( data, collections.Mapping ):
        return dict( map( convert_unicode_to_str, data.iteritems() ) )
    elif isinstance( data, collections.Iterable ):
        return type( data )( map( convert_unicode_to_str, data ) )
    else:
        return data
