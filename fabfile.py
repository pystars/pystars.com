#-*- coding: utf-8 -*-
from fabric.api import *

def syncdb():
    '''
    Makes local syncdb and load fixtures
    '''
    local('python ./manage.py reset_db --noinput --router=default')
    local('python ./manage.py syncdb --noinput --migrate')
    local('python ./manage.py loaddata fixtures/*.json')
    # Makes init of revisions
    local('python ./manage.py createinitialrevisions articles')