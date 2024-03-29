"""---------------------------------------------------------------------------------------
    IMPORTS
---------------------------------------------------------------------------------------"""
from bottle import *
import os, os.path

"""---------------------------------------------------------------------------------------
    CONSTANTS
---------------------------------------------------------------------------------------"""
DATASTORE_LOGS_PATH = "datastore/logs/"

"""---------------------------------------------------------------------------------------
    WEBSERVER TEMPLATES
---------------------------------------------------------------------------------------"""
log_template = SimpleTemplate("% include('log.tpl')")


"""---------------------------------------------------------------------------------------
    WEBSERVER ROUTES
---------------------------------------------------------------------------------------"""
@route('/')
def index():
    return template('<b>Hello {{name}}</b>!', name="world")

@route('/log/<log>')
def index(log):
    print get_log_info(log)
    return log_template.render(log=get_log_info(log))
    
"""---------------------------------------------------------------------------------------
    ROUTINES
---------------------------------------------------------------------------------------"""
def get_log_info(log_name):
    return open(DATASTORE_LOGS_PATH + log_name, 'r').readlines()
    
"""---------------------------------------------------------------------------------------
    START WEBSERVER
---------------------------------------------------------------------------------------"""
run(host='localhost', port=8080, debug=True)


