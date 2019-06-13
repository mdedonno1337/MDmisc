#!/usr/bin/python
# -*- coding: UTF-8 -*-

import psycopg2
import psycopg2.extras
import re

def urlsplit( url ):
    data = re.match( '((?P<protocol>[^:]+)://)((?P<user>[^:]+)?(:(?P<password>[^@]+))?)?@(?P<host>[^:/]+)(:(?P<port>\d+))?(/(?P<database>[^&]+))?', url )
    return dict( [ ( key, data.group( key ) ) for key in [ 'user', 'password', 'host', 'port', 'database' ] ] )

class Database( object ):
    def __init__( self, url, docommit = True ):
        self.conn = psycopg2.connect( **urlsplit( url ) )
        self.docommit = docommit
            
    def cursor( self ):
        return self.conn.cursor()
    
    def commit( self ):
        if self.docommit:
            self.conn.commit()
    
    def close( self ):
        self.conn.close()
    
    def query( self, sql, *args, **kwargs ):
        try:
            c = self.conn.cursor( cursor_factory = psycopg2.extras.DictCursor )
            c.execute( sql, *args, **kwargs )
            return c
        except:
            self.conn.rollback()
            return False
    
    def query_fetchone( self, sql, data = () ):
        return self.query( sql, data ).fetchone()
    
    def query_fetchall( self, sql, data = () ):
        return self.query( sql, data ).fetchall()
    
    def __enter__( self ):
        return self
    
    def __exit__( self, exc_type, exc_val, exc_tb ):
        self.commit()
        self.close()
