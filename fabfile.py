from fabric.api import *
from fabric.operations import run, put
import config
import os
import json
import requests

appname = os.path.basename(os.path.normpath(os.getcwd()))

env.hosts = [config.dataomaha['user']]
env.password= config.dataomaha['pw']

def startRepo():
    descrip = raw_input("Describe your app: ")
    url = 'https://api.github.com/orgs/owh-projects/repos'
    git = {
      "name": appname,
      "description": descrip,
      "private": False,
      "auto_init": True
    }
    r = requests.post(url, data=json.dumps(git), auth=(config.git['user'], config.git['pw']))
    if str(r.status_code) == '201':
        print "Hooray, it worked."
    else:
        print "Something went wrong. The HTTP status code returned was " + str(r.status_code)

def deployLive():
    run('mkdir -p ' + config.livepath + appname)
    put('../' + appname, config.livepath + appname)
    
def deployDev():
    run('mkdir -p ' + config.devpath + appname)
    put('../' + appname, config.devpath + appname)