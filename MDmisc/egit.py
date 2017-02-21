#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import git

def git_version( wd = "./", name = None ):
    try:
        repo = git.Repo( wd, search_parent_directories = True )
        
    except git.exc.NoSuchPathError:
        return {}
    
    else:
        try:
            describe = repo.git.describe( "--dirty" )
            commit_count = repo.git.rev_list( "--count", "HEAD" )
        
        except:
            describe = "Unknown"
            commit_count = "Unknown"
        
        finally:
            hash = repo.head.object.hexsha
            date = repo.git.log( "-1", "--date=iso", "--pretty=format:%cd" )
             
            return {
                'name': name,
                'working_dir': repo.working_dir.replace( "\\", "/" ),
                'commit_describe': describe,
                'commit_count': commit_count,
                'commit_hash': hash,
                'commit_date': date
            }

def git_describe_split( describe ):
    try:
        return re.match( "^(.*)-([\d]+)-g([^-]*)(-(.*))?", describe ).groups()
    except:
        return None
