# coding: utf-8
import urllib
import time
import libxmlload
import settings

__all__ = ['user', 'problem', 'problemlist', 'alluserlist', 'solvedrecord', 'statuslog', 'problemcategory']

def base(apiid, **args):
    assert apiid in settings.url.keys()
    url = settings.url[apiid]
    arg = urllib.urlencode(args)
    
    #otree = libxmlload.urlopen(url + '?' + arg)
    #return otree
    
    conn = urllib.urlopen(url + '?' + arg)
    ulst = []
    for n in conn.readlines():
        ulst.append(n.decode('utf-8', 'ignore'))
    xmldoc = libxmlload.fromstring(''.join(ulst))
    otree = libxmlload.xmltrans(xmldoc)
    return otree


def time2date(s):
    return time.gmtime(int(s) / 1000.)
def date2str(d):
    return  time.strftime('%Y/%m/%d %H:%M:%S', d)
def user(id):
    usr = base('user', id=id)
    usr.registerdate = time2date(usr.registerdate)
    usr.registerdate_str = date2str(usr.registerdate)
    usr.lastsubmitdate = time2date(usr.lastsubmitdate)
    usr.lastsubmitdate_str = date2str(usr.lastsubmitdate)
    s = usr.status
    target = [
        's.submission',
        's.memorylimit',
        's.runtimeerror',
        's.wronganswer',
        's.timelimit',
        's.compileerror',
        's.accepted',
        's.outputlimit',
        's.solved',
    ]
    for t in target:
        exec '@ = int(@)'.replace('@', t)
    if type(usr.solved_list.problem) != list:
        usr.solved_list.problem = [usr.solved_list.problem]
    for p in usr.solved_list.problem:
        target = [
            'p.cputime',
            'p.memory',
            'p.code_size',
            'p.id',
        ]
        for t in target:
            exec '@ = int(@)'.replace('@', t)
        p.submissiondate = time2date(p.submissiondate)
        p.submissiondate_str = date2str(p.submissiondate)
    return usr

def problem(id):
    p = base('problem', id=str(id).zfill(4))
    s = p.status
    target = [
        'p.id',
        'p.problemtimelimit',
        'p.problemmemorylimit',
        's.submission',
        's.memorylimit',
        's.runtimeerror',
        's.wronganswer',
        's.timelimit',
        's.accepted',
        's.outputlimit',
    ]
    for t in target:
        exec '@ = int(@)'.replace('@', t)
    if type(p.solved_list.user) is libxmlload.Node:
        p.solved_list.user = [p.solved_list.user]
    for usr in p.solved_list.user:
        target = [
            'usr.cputime',
            'usr.memory',
            'usr.code_size',
        ]
        for t in target:
            exec '@ = int(@)'.replace('@', t)
    return p

def problemlist(volume):
    resp = base('problemlist', volume=volume)
    for p in resp.problem:
        p.problemmemorylimit = int(p.problemmemorylimit)
        p.problemtimelimit = int(p.problemtimelimit)
    return resp

def alluserlist(criteria='', affiliation='', solved_min='', solved_max=''):
    kwargs = {}
    for arg in ['criteria', 'affiliation', 'solved_min', 'solved_max']:
        if eval(arg + ' != \'\''):
            kwargs[arg] = eval(arg)
    lst = base('alluserlist', **kwargs)
    for usr in lst.user:
        usr.solved = int(usr.solved)
        usr.rating = float(usr.rating)
        usr.rank   = int(usr.rank)
    return lst

def solvedrecord(user_id='', problem_id='', language='', date_begin='', date_end=''):
    kwargs = {}
    if user_id == '' and problem_id == '':
        raise Exception('user_id or problem_id should be specified.')
    for arg in ['user_id', 'problem_id', 'language', 'date_begin', 'date_end']:
        if eval(arg + ' != \'\''):
            kwargs[arg] = eval(arg)
    resp = base('solvedrecord', **kwargs)
    for n in resp.solved:
        n.date = time2date(n.date)
        n.date_str = date2str(n.date)
        n.problem_id = int(n.problem_id)
        n.run_id = int(n.run_id)
        n.cputime = int(n.cputime)
        n.memory = int(n.memory)
        n.code_size = int(n.code_size)
    return resp

def statuslog(user_id='', problem_id='', start='', limit=''):
    kwargs = {}
    for arg in ['user_id', 'problem_id', 'start', 'limit']:
        if eval(arg + ' != \'\''):
            kwargs[arg] = eval(arg)
    def f(st):
        st.submission_date = time2date(st.submission_date)
        st.submission_date_str = date2str(st.submission_date)
        st.code_size = int(st.code_size)
        st.cputime = int(st.cputime)
        st.run_id = int(st.run_id)
        st.memory = int(st.memory)
        return st
    lst = base('statuslog', **kwargs)
    if isinstance(lst.status, list):
        for st in lst.status:
            f(st)
    else:
        lst.status = [f(lst.status)]
    return lst

def problemcategory(id=None, category=None):
    cat = None
    kwargs = {}
    if id is not None:
        kwargs['id'] = str(id).zfill(4)
    if category is not None:
        kwargs['category'] = category
    cat =  base('problemcategory', **kwargs)
    if type(cat.problem) is not list:
        cat.problem.id = int(cat.problem.id)
        cat.problem.score = float(cat.problem.score)
        cat.problem = [cat.problem]
        return cat
    for p in cat.problem:
        p.id    = int(p.id)
        p.score = float(p.score)
    return cat
