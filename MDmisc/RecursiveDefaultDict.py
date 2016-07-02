#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from _collections import defaultdict

from MDmisc.DefaultOrderedDict import DefaultOrderedDict


defDict = lambda: defaultdict( defDict )
defOrderedDict = lambda: DefaultOrderedDict( defOrderedDict )
