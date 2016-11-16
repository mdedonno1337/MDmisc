#!/usr/bin/python
# -*- coding: UTF-8 -*-

def scientific_format( number, digits = 3 ):
    """
        Return the scientific notation of the number passed in parameter (float,
        int or string format as input).
    """
    return ( "%%.%de" % digits ) % float( number )  
