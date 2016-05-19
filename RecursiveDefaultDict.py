#!/usr/bin/env python
#  *-* coding: cp850 *-*

from _collections import defaultdict

from lib.misc.DefaultOrderedDict import DefaultOrderedDict


defDict = lambda: defaultdict( defDict )
defOrderedDict = lambda: DefaultOrderedDict( defOrderedDict )
