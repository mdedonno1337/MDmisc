#!/usr/bin/python
# -*- coding: UTF-8 -*-

from MDmisc import string, xfrange
import doctest
import unittest


def MDmisctsets():
    tests = unittest.TestSuite()
    
    tests.addTests( doctest.DocTestSuite( string ) )
    tests.addTests( doctest.DocTestSuite( xfrange ) )
    
    return tests

if __name__ == "__main__":
    unittest.TextTestRunner( verbosity = 2 ).run( MDmisctsets() )
else:
    def load_tests( loader, tests, ignore ):
        return MDmisctsets()
