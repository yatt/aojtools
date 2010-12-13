# coding: utf-8
import urllib
import time
import libxmlload
import settings

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

def problemlist(vid):
    return base('problemlist', volume=vid)

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

def solvedrecord():
    return base('solvedrecord', )

def statuslog(user_id='', problem_id='', start='', limit=''):
    kwargs = {}
    for arg in ['user_id', 'problem_id', 'start', 'limit']:
        if eval(arg + ' != \'\''):
            kwargs[arg] = eval(arg)
    lst = base('statuslog', **kwargs)
    for st in lst.status:
        st.submission_date = time2date(st.submission_date)
        st.submission_date_str = date2str(st.submission_date)
        st.code_size = int(st.code_size)
        st.cpu_time = int(st.cpu_time)
        st.run_id = int(st.run_id)
        st.memory = int(st.memory)
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
