#!/usr/bin/python
# -*- coding: UTF-8 -*-

import doctest
import unittest

from MDmisc import binary
from MDmisc import string
from MDmisc import xfrange
from MDmisc import multiple_sample


def MDmisctsets():
    tests = unittest.TestSuite()
    
    tests.addTests( doctest.DocTestSuite( binary ) )
    tests.addTests( doctest.DocTestSuite( string ) )
    tests.addTests( doctest.DocTestSuite( xfrange ) )
    tests.addTests( doctest.DocTestSuite( multiple_sample ) )
    
    return tests

if __name__ == "__main__":
    unittest.TextTestRunner( verbosity = 2 ).run( MDmisctsets() )
    
else:
    def load_tests( loader, tests, ignore ):
        return MDmisctsets()
