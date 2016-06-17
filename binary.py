#!/usr/bin/env python
#  *-* coding: utf-8 *-*

import struct


def int_to_bin( x, digits = 0 ):
    """
        Return the binary value, zfilled at 'digits' caracter.
        
        >>> int_to_bin( 1337 )
        '10100111001'
        
        >>> int_to_bin( 1337, 32 )
        '00000000000000000000010100111001'
    """
    oct2bin = [ '000', '001', '010', '011', '100', '101', '110', '111' ] 
    binstring = [ oct2bin[int( n )] for n in oct( x ) ]
    binstring = ''.join( binstring ).lstrip( '0' )
    
    if digits == 'up':
        digits = 8 * ( len( binstring ) / 8 + 1 )
        
    return binstring.zfill( digits ) 

def bin_to_int( x ):
    """
        Return the int value of a binary string passed in parameter
        
        >>> bin_to_int( '00000000000000000000010100111001' )
        1337
    """
    return int( x, 2 )

def float_to_bin( f ):
    """
        convert float to binary string
        
        >>> float_to_bin( 13.37 )
        '0100000000101010101111010111000010100011110101110000101000111101'
    """
    ba = struct.pack( '>d', f )
    s = ''.join( '{:08b}'.format( ord( b ) ) for b in ba )
    return s

def bin_to_float( b ):
    """
        convert binary string to float
        
        >>> bin_to_float( '0100000000101010101111010111000010100011110101110000101000111101' )
        13.37
    """
    bf = int_to_bytes( int( b, 2 ), 8 )
    return struct.unpack( '>d', bf )[ 0 ]

def int_to_bytes( n, minlen = 0 ):
    nbits = n.bit_length() + ( 1 if n < 0 else 0 )
    nbytes = ( nbits + 7 ) / 8
    bytes = []
    
    for i in range( nbytes ):
        bytes.append( chr( n & 0xff ) )
        n >>= 8
    
    if minlen > 0 and len( bytes ) < minlen:
        bytes.extend( ( minlen - len( bytes ) ) * '0' )
    bytes.reverse()
    
    return ''.join( bytes )

def binstring_to_int( data ):
    """
        Convert string of character from binary to int
        
        >>> binstring_to_int( 'leet' )
        1818584436
    """
    b = ""
    for c in data:
        b += int_to_bin( ord( c ), 8 )
    
    return bin_to_int( b )

if __name__ == "__main__":
    import doctest
    doctest.testmod()
