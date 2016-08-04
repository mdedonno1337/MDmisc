#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

class multiDirGet():
    def __init__( self, dirs = None ):
        if type( dirs ) == list:
            map( self.addFolder, dirs )
        
        elif type( dirs ) == str:
            self.addFolder( dirs )
        
        else:
            self.dirs = []
            
    def addFolder( self, f ):
        if os.path.isdir( f ):
            self.dirs.append( f )
            
    def get_file( self, g ):
        for d in self.dirs:
            if os.path.isfile( d + "/" + g ):
                return d + "/" + g
        
        else:
            raise IOError
        
    def get_dir( self, g ):
        for d in self.dirs:
            if os.path.isdir( d + "/" + g ):
                return d + "/" + g
        
        else:
            raise IOError
            
