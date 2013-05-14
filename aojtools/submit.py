# coding: utf-8
import urllib
import time
import socket

import api
import settings

def submit_noresult(info, timeout=None):
    assert sorted(info.keys()) == sorted(['user_id', 'code', 'problem_id', 'lang', 'password']), 'first argument must have keys ["user_id", "code", "problem_id", "lang", "password"]'
    assert (timeout is None) or (isinstance(timeout, int) and timeout > 0), 'timout must be a positive integer'
    if isinstance(info['problem_id'], int):
        info['problem_id'] = '%04d' % info['problem_id']
    #assert len(info['problem_id']) == 4, 'problem id must be a positive integer or four-length string'
    assert info['lang'] in ['C', 'C++', 'JAVA'], 'lang must be "C", "C++" or "JAVA"'
    
    url = settings.submiturl
    info = {
        'userID': info['user_id'],
        'sourceCode': info['code'],
        'problemNO': info['problem_id'],
        'language': info['lang'].upper(),
        'password': info['password'],
    }
    postdata = urllib.urlencode(info)
    if not timeout is None:
        socket.setefaulttimeout(timeout)
    resp = urllib.urlopen(url, postdata).read()
    return resp

def submit(info, timeout=None, waittime=2, maxtry=10):
    """
    usage:
        info = {
            'user_id': (user id),
            'password': (password),
            'code': (source code),
            'problem_id': (problem id, integer or string),
            'lang': (language "C","C++",or"JAVA")
        }
        submit(info)
        #submit(info, timeout=3) # seconds
    """
    # check last runid
    try:
        resp = api.statuslog(user_id=info['user_id'])
        rid = resp.status[0].run_id
    except Exception, e:
        raise e
   
    # submit
    ret = None
    try:
        ret = submit_noresult(info, timeout)
    except Exception, e:
        raise e
    if 'UserID or Password is Wrong.' in ret:
        raise Exception('userid or password is wrong.')
     
    # wait until update
    ntry = 0
    while True:
        try:
            resp = api.statuslog(user_id=info['user_id'])
        except Exception, e:
            raise e
        new_rid = resp.status[0].run_id
        if new_rid > rid:
            return resp.status[0]
        time.sleep(waittime)
        ntry += 1
        if ntry == maxtry:
            raise Exception('maximum try count exceeded')
    
