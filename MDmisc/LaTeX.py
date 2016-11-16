#!/usr/bin/python
# -*- coding: UTF-8 -*-

from MDmisc.numbers import frexp10


def LaTeX_scientific_notation( nb, digits = 5 ):
    """
        Convert the scientific notation of python () to the 'traditionnal'
        annotation.
        
            >>> LaTeX_scientific_notation( 1.337e3 )
            '$1.33700 \\\\times 10^{+3}$'
    """
    mantisse, exp = frexp10( nb )
    sign = '+' if exp > 0 else ''
    return ( r"$%%.%df \times 10^{%%s%%d}$" % digits ) % ( mantisse, sign, exp )
