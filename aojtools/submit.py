# coding: utf-8
import urllib
import time
import socket

import generated as api

def submit_noresult(info, timeout=None):
    assert sorted(info.keys()) == sorted(['user_id', 'code', 'problem_id', 'lang', 'password']), 'first argument must have keys ["user_id", "code", "problem_id", "lang", "password"]'
    assert (timeout is None) or (isinstance(timeout, int) and timeout > 0), 'timout must be a positive integer'
    if isinstance(info['problem_id'], int):
        info['problem_id'] = '%04d' % info['problem_id']
    #assert len(info['problem_id']) == 4, 'problem id must be a positive integer or four-length string'
    assert info['lang'] in ['C', 'C++', 'JAVA'], 'lang must be "C", "C++" or "JAVA"'
    
    url = 'http://judge.u-aizu.ac.jp/onlinejudge/servlet/Submit'
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



def tryntimes(fun, nmax = 10, interval = 2, timeout = 10):
    try:
        return fun()
    except Exception, e:
        if nmax:
            time.sleep(interval)
            return tryntimes(fun, nmax - 1, interval, timeout)
        else:
            raise Exception('maximum try times exceed')

def lastrunid(info):
    resp = api.StatusLogSearchAPI(user_id=info['user_id'])
    return resp.status[0], resp.status[0].run_id


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
    resp, rid = lastrunid(info)
    # submit
    try:
        submit_noresult(info, timeout)
    except Exception, e:
        raise e
    if 'UserID or Password is Wrong.' in resp:
        raise Exception('userid or password is wrong.')
    # wait until update
    def fun():
        resp, new_rid = lastrunid(info)
        if new_rid > rid:
            return resp
        else:
            raise Exception('fun')
    return tryntimes(fun, maxtry, waittime, timeout)
