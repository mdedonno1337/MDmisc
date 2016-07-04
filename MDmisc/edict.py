#!/usr/bin/python
# -*- coding: UTF-8 -*-

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
    
    def search(self, searched ):
        for key, value in self.iteritems():
            if value == searched:
                return key
        
        else:
            return None
        
    def get_by_keys( self, lst ):
        return [ self.get( key ) for key in lst ]
    
dict = edict
