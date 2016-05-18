#!/usr/bin/env python

import warnings

def deprecated( func ):
    """
        This is a decorator which can be used to mark functions as deprecated.
        It will result in a warning being emmitted when the function is used.
        
        http://stackoverflow.com/questions/2536307/decorators-in-the-python-standard-lib-deprecated-specifically
        Patrizio Bertoni
    """

    def new_func( *args, **kwargs ):
        warnings.simplefilter( 'always', DeprecationWarning ) # turn off filter 
        warnings.warn( "Call to deprecated function {}.".format( func.__name__ ), category = DeprecationWarning, stacklevel = 2 )
        warnings.simplefilter( 'default', DeprecationWarning ) # reset filter
        return func( *args, **kwargs )

    new_func.__name__ = func.__name__
    new_func.__doc__ = func.__doc__
    new_func.__dict__.update( func.__dict__ )
    return new_func
