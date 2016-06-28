#!/usr/bin/python
# -*- coding: UTF-8 -*-

from PIL import Image

################################################################################
# 
#    Image processing functions
# 
################################################################################

def RAWToPIL( raw, size = ( 500, 500 ) ):
    """
        Convert a RAW string to PIL object.
        
        >>> RAWToPIL( chr( 255 ) * 250000, ( 500, 500 ) ) #doctest: +ELLIPSIS
        <PIL.Image.Image image mode=L size=500x500 at 0x...>
    """
    return Image.frombytes( 'L', size, raw )

def PILToRAW( pil ):
    """
        Convert a PIL object to RAW string.
        
        >>> p = Image.new( '1', ( 5, 5 ) )
        >>> r = PILToRAW( p )
        >>> r
        '\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00'
        >>> len( r )
        25
    """
    return pil.convert( 'L' ).tobytes()
