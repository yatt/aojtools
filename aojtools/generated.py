#! /usr/bin/python2.6
# coding: utf-8

import time
import parse
import settings


def time2date(s):
    return time.gmtime(int(s) / 1000.)
def date2str(d):
    return  time.strftime('%Y/%m/%d %H:%M:%S', d)
def to_list(l):
    return isinstance(l, list) and l or [l]
def UserSearchAPI(id, **kwargs):
    # type check
    if type(id) not in [str, unicode]:
        raise Exception('parameter \'id\' must be string')
    # initialize url, fill if necessary
    url = 'http://judge.u-aizu.ac.jp/onlinejudge/webservice/user'
    # set parameter
    prm = kwargs.copy()
    prm['id'] = id
    # call api
    rsp = parse.fromweb(url, prm)
    # format
    rsp.id = str(rsp.id)
    rsp.name = str(rsp.name)
    rsp.affiliation = str(rsp.affiliation)
    rsp.registerdate = time2date(rsp.registerdate)
    rsp.lastsubmitdate = time2date(rsp.lastsubmitdate)
    s = rsp.status
    s.submission = int(s.submission)
    s.solved = int(s.solved)
    s.accepted = int(s.accepted)
    s.wronganswer = int(s.wronganswer)
    s.timelimit = int(s.timelimit)
    s.memorylimit = int(s.memorylimit)
    s.outputlimit = int(s.outputlimit)
    s.runtimeerror = int(s.runtimeerror)
    s.compileerror = int(s.compileerror)
    rsp.solved_list.problem = to_list(rsp.solved_list.problem)
    for p in rsp.solved_list.problem:
        p.id = str(p.id)
        p.submissiondate = time2date(p.submissiondate)
        p.language = str(p.language)
        p.cputime = int(p.cputime)
        p.memory = int(p.memory)
        p.code_size = int(p.code_size)
    return rsp

def ProblemSearchAPI(id, **kwargs):
    # type check
    #if type(id) not in [str, unicode]:
    #    raise Exception('parameter \'id\' must be string')
    if type(id) not in [str, unicode]:
        id = '%04d'%  id
    if 'status' in kwargs and type(kwargs['status']) not in [str, unicode]:
        raise Exception('parameter \'status\' must be string')
    # initialize url, fill if necessary
    url = 'http://judge.u-aizu.ac.jp/onlinejudge/webservice/problem'
    # set parameter
    prm = kwargs.copy()
    prm['id'] = id
    # call api
    rsp = parse.fromweb(url, prm)
    # format
    rsp.id = str(rsp.id)
    rsp.name = str(rsp.name)
    rsp.available = int(rsp.available)
    rsp.problemtimelimit = int(rsp.problemtimelimit)
    rsp.problemmemorylimit = int(rsp.problemmemorylimit)
    s = rsp.status
    s.submission = int(s.submission)
    s.accepted = int(s.accepted)
    s.wronganswer = int(s.wronganswer)
    s.timelimit = int(s.timelimit)
    s.memorylimit = int(s.memorylimit)
    s.outputlimit = int(s.outputlimit)
    s.runtimeerror = int(s.runtimeerror)
    rsp.solved_list.user = to_list(rsp.solved_list.user)
    for user in rsp.solved_list.user:
        user.id = str(user.id)
        user.submissiondate = time2date(user.submissiondate)
        user.language = str(user.language)
        user.cputime = int(user.cputime)
        user.memory = int(user.memory)
        user.code_size = int(user.code_size)
    return rsp
def ProblemListSearchAPI(volume, **kwargs):
    # type check
    if type(volume) not in [int, long]:
        raise Exception('parameter \'volume\' must be integer')
    # initialize url, fill if necessary
    url = 'http://judge.u-aizu.ac.jp/onlinejudge/webservice/problem_list'
    # set parameter
    prm = kwargs.copy()
    prm['volume'] = volume
    # call api
    rsp = parse.fromweb(url, prm)
    # format
    for p in rsp.problem:
        p.id = str(p.id)
        p.name = str(p.name)
        p.problemtimelimit = int(p.problemtimelimit)
        p.problemmemorylimit = int(p.problemmemorylimit)
    return rsp
def AllUserListSearchAPI(**kwargs):
    # type check
    if 'criteria' in kwargs and type(kwargs['criteria']) not in [int, long]:
        raise Exception('parameter \'criteria\' must be integer')
    if 'affiliation' in kwargs and type(kwargs['affiliation']) not in [str, unicode]:
        raise Exception('parameter \'affiliation\' must be string')
    if 'solved_min' in kwargs and type(kwargs['solved_min']) not in [int, long]:
        raise Exception('parameter \'solved_min\' must be integer')
    if 'solved_max' in kwargs and type(kwargs['solved_max']) not in [int, long]:
        raise Exception('parameter \'solved_max\' must be integer')
    # initialize url, fill if necessary
    url = 'http://judge.u-aizu.ac.jp/onlinejudge/webservice/user_list'
    # set parameter
    prm = kwargs.copy()
    # call api
    rsp = parse.fromweb(url, prm)
    # format
    rsp.user = to_list(rsp.user)
    for user in rsp.user:
        user.rank = int(user.rank)
        user.id = str(user.id)
        user.name = str(user.name)
        user.affiliation = str(user.affiliation)
        user.solved = int(user.solved)
        user.rating = float(user.rating)
    return rsp
def SolvedRecordSearchAPI(**kwargs):
    # type check
    if 'user_id' in kwargs and type(kwargs['user_id']) not in [str, unicode]:
        raise Exception('parameter \'user_id\' must be string')
    if 'problem_id' in kwargs and type(kwargs['problem_id']) not in [str, unicode]:
        #raise Exception('parameter \'problem_id\' must be string')
        kwargs['problem_id'] = '%04d' % kwargs['problem_id']
    if 'language' in kwargs and type(kwargs['language']) not in [str, unicode]:
        raise Exception('parameter \'language\' must be string')
    if 'date_begin' in kwargs and type(kwargs['date_begin']) not in [int, long]:
        raise Exception('parameter \'date_begin\' must be integer')
    if 'date_end' in kwargs and type(kwargs['date_end']) not in [int, long]:
        raise Exception('parameter \'date_end\' must be integer')
    # initialize url, fill if necessary
    url = 'http://judge.u-aizu.ac.jp/onlinejudge/webservice/solved_record'
    # set parameter
    prm = kwargs.copy()
    # call api
    rsp = parse.fromweb(url, prm)
    # format
    rsp.solved = to_list(rsp.solved)
    for s in rsp.solved:
        s.run_id = int(s.run_id)
        s.user_id = str(s.user_id)
        s.problem_id = str(s.problem_id)
        s.date = time2date(s.date)
        s.language = str(s.language)
        s.cputime = int(s.cputime)
        s.memory = int(s.memory)
        s.code_size = int(s.code_size)
    return rsp
def StatusLogSearchAPI(**kwargs):
    # type check
    if 'user_id' in kwargs and type(kwargs['user_id']) not in [str, unicode]:
        raise Exception('parameter \'user_id\' must be string')
    if 'problem_id' in kwargs and type(kwargs['problem_id']) not in [str, unicode]:
        #raise Exception('parameter \'problem_id\' must be string')
        kwargs['problem_id'] = '%04d' % kwargs['problem_id']
    if 'start' in kwargs and type(kwargs['start']) not in [int, long]:
        raise Exception('parameter \'start\' must be integer')
    if 'limit' in kwargs and type(kwargs['limit']) not in [int, long]:
        raise Exception('parameter \'limit\' must be integer')
    # initialize url, fill if necessary
    url = 'http://judge.u-aizu.ac.jp/onlinejudge/webservice/status_log'
    # set parameter
    prm = kwargs.copy()
    # call api
    rsp = parse.fromweb(url, prm)
    # format
    for s in rsp.status:
        s.run_id = int(s.run_id)
        s.user_id = str(s.user_id)
        s.problem_id = str(s.problem_id)
        s.submission_date = time2date(s.submission_date)
        s.status = str(s.status)
        s.language = str(s.language)
        s.cputime = int(s.cputime)
        s.memory = int(s.memory)
        s.code_size = int(s.code_size)
    return rsp
def JudgeDetailSearchAPI(id, **kwargs):
    # type check
    if type(id) not in [str, unicode]:
        #raise Exception('parameter \'id\' must be string')
        id = '%04d' % id
    # initialize url, fill if necessary
    url = 'http://judge.u-aizu.ac.jp/onlinejudge/webservice/judge'
    # set parameter
    prm = kwargs.copy()
    prm['id'] = id
    # call api
    rsp = parse.fromweb(url, prm)
    # format
    rsp.judge_id = str(rsp.judge_id)
    rsp.judge_type_code = int(rsp.judge_type_code)
    rsp.judge_type = str(rsp.judge_type)
    rsp.submissiondate = time2date(rsp.submissiondate)
    rsp.judgedate = time2date(rsp.judgedate)
    rsp.language = str(rsp.language)
    rsp.cuptime = int(rsp.cuptime)
    rsp.memory = int(rsp.memory)
    rsp.code_size = int(rsp.code_size)
    rsp.status = int(rsp.status)
    rsp.accuracy = str(rsp.accuracy)
    rsp.problem_id = str(rsp.problem_id)
    rsp.problem_title = str(rsp.problem_title)
    rsp.submissions = int(rsp.submissions)
    rsp.accepted = int(rsp.accepted)
    rsp.user_id = str(rsp.user_id)
    rsp.user_name = str(rsp.user_name)
    rsp.affiliation = str(rsp.affiliation)
    return rsp
def ProblemCategorySearchAPI(**kwargs):
    # type check
    if 'id' in kwargs and type(kwargs['id']) not in [str, unicode]:
        #raise Exception('parameter \'id\' must be string')
        kwargs['id'] = '%04d' % kwargs['id']
    if 'category' in kwargs and type(kwargs['category']) not in [str, unicode]:
        raise Exception('parameter \'category\' must be string')
    # initialize url, fill if necessary
    url = 'http://judge.u-aizu.ac.jp/onlinejudge/webservice/problem_category'
    # set parameter
    prm = kwargs.copy()
    # call api
    rsp = parse.fromweb(url, prm)
    # format
    def fn(p):
        p.id = str(p.id)
        p.category = str(p.category)
        p.score = float(p.score)
    if type(rsp.problem) is list:
        for p in rsp.problem:
            fn(p)
    else:
        fn(rsp.problem)
        rsp.problem = [rsp.problem]
    return rsp
def SourceSearchAPI(id, **kwargs):
    # type check
    if type(id) not in [str, unicode]:
        #raise Exception('parameter \'id\' must be string')
        id = '%04d' % id
    # initialize url, fill if necessary
    url = 'http://judge.u-aizu.ac.jp/onlinejudge/webservice/source'
    # set parameter
    prm = kwargs.copy()
    prm['id'] = id
    # call api
    rsp = parse.fromweb(url, prm)
    # format
    rsp.id = str(rsp.id)
    rsp.title = str(rsp.title)
    rsp.subtitle = str(rsp.subtitle)
    rsp.place = str(rsp.place)
    rsp.abbr = str(rsp.abbr)
    rsp.author1 = str(rsp.author1)
    rsp.author2 = str(rsp.author2)
    rsp.year = str(rsp.year)
    rsp.month = str(rsp.month)
    rsp.day = str(rsp.day)
    rsp.note = str(rsp.note)
    rsp.url = str(rsp.url)
    rsp.judge = str(rsp.judge)
    return rsp
def ContestListSearchAPI(**kwargs):
    # type check
    # initialize url, fill if necessary
    url = 'http://judge.u-aizu.ac.jp/onlinejudge/webservice/contest_list'
    # set parameter
    prm = kwargs.copy()
    # call api
    rsp = parse.fromweb(url, prm)
    # format
    return rsp
def ContestInfoSearchAPI(id, **kwargs):
    # type check
    # initialize url, fill if necessary
    url = 'http://judge.u-aizu.ac.jp/onlinejudge/webservice/contest_info'
    # set parameter
    prm = kwargs.copy()
    prm['id'] = id
    # call api
    rsp = parse.fromweb(url, prm)
    # format
    return rsp
def ContestStandingSearchAPI(id, **kwargs):
    # type check
    # initialize url, fill if necessary
    url = 'http://judge.u-aizu.ac.jp/onlinejudge/webservice/contest_standing'
    # set parameter
    prm = kwargs.copy()
    prm['id'] = id
    # call api
    rsp = parse.fromweb(url, prm)
    # format
    return rsp
def ContestProblemSearchAPI(id, **kwargs):
    # type check
    # initialize url, fill if necessary
    url = 'http://judge.u-aizu.ac.jp/onlinejudge/webservice/contest_problem'
    # set parameter
    prm = kwargs.copy()
    prm['id'] = id
    # call api
    rsp = parse.fromweb(url, prm)
    # format
    return rsp
def ContestStatusLogSearchAPI(id, **kwargs):
    # type check
    # initialize url, fill if necessary
    url = 'http://judge.u-aizu.ac.jp/onlinejudge/webservice/contest_status_log'
    # set parameter
    prm = kwargs.copy()
    prm['id'] = id
    # call api
    # call api
    rsp = parse.fromweb(url, prm)
    # format
    return rsp


# TODO: implement.


def ThreadSearchAPI(**kwargs):
    # type check
    if 'id' in kwargs and type(kwargs['id']) not in [int, long]:
        raise Exception('parameter \'id\' must be integer')
    # initialize url, fill if necessary
    url = 'http://rose.u-aizu.ac.jp/aojbbs/webservice/thread/$.xml'
    url = url.replace('$', kwargs['id'], 1)
    # set parameter
    prm = kwargs.copy()
    # call api
    rsp = parse.fromweb(url, prm)
    # format
    rsp.id = int(rsp.id)
    rsp.name = str(rsp.name)
    rsp.problem_id = str(rsp.problem_id)
    rsp.user_id = str(rsp.user_id)
    rsp.update_time = date2str(rsp.update_time)
    return rsp
def GETRecentThreadAPI(**kwargs):
    # type check
    if 'number' in kwargs and type(kwargs['number']) not in [int, long]:
        raise Exception('parameter \'number\' must be integer')
    # initialize url, fill if necessary
    url = 'http://rose.u-aizu.ac.jp/aojbbs/webservice/recent/thread/$'
    url = url.replace('$', kwargs['number'], 1)
    # set parameter
    prm = kwargs.copy()
    # call api
    rsp = parse.fromweb(url, prm)
    # format
    rsp.problem_id = str(rsp.problem_id)
    rsp.user_id = str(rsp.user_id)
    rsp.update_time = date2str(rsp.update_time)
    return rsp
def MessageSearchAPI(**kwargs):
    # type check
    if 'id' in kwargs and type(kwargs['id']) not in [int, long]:
        raise Exception('parameter \'id\' must be integer')
    # initialize url, fill if necessary
    url = 'http://rose.u-aizu.ac.jp/aojbbs/webservice/message/$.xml'
    url = url.replace('$', kwargs['id'], 1)
    # set parameter
    prm = kwargs.copy()
    # call api
    rsp = parse.fromweb(url, prm)
    # format
    rsp.id = int(rsp.id)
    rsp.thread_id = int(rsp.thread_id)
    rsp.problem_id = str(rsp.problem_id)
    rsp.user_id = str(rsp.user_id)
    rsp.content = str(rsp.content)
    rsp.url = str(rsp.url)
    rsp.update_time = date2str(rsp.update_time)
    return rsp
def ThreadSeachfromproblemIDAPI(**kwargs):
    # type check
    if 'problem_id' in kwargs and type(kwargs['problem_id']) not in [int, long]:
        raise Exception('parameter \'problem_id\' must be integer')
    # initialize url, fill if necessary
    url = 'http://rose.u-aizu.ac.jp/aojbbs/webservice/thread/problem/$.xml'
    url = url.replace('$', kwargs['problem_id'], 1)
    # set parameter
    prm = kwargs.copy()
    # call api
    rsp = parse.fromweb(url, prm)
    # format
    rsp.id = int(rsp.id)
    rsp.name = str(rsp.name)
    rsp.problem_id = int(rsp.problem_id)
    rsp.user_id = str(rsp.user_id)
    rsp.update_time = date2str(rsp.update_time)
    return rsp
def MessageSearchfromThreadIDAPI(**kwargs):
    # type check
    if 'id' in kwargs and type(kwargs['id']) not in [int, long]:
        raise Exception('parameter \'id\' must be integer')
    # initialize url, fill if necessary
    url = 'http://rose.u-aizu.ac.jp/aojbbs/webservice/message/thread/$.xml'
    url = url.replace('$', kwargs['id'], 1)
    # set parameter
    prm = kwargs.copy()
    # call api
    rsp = parse.fromweb(url, prm)
    # format
    rsp.id = int(rsp.id)
    rsp.thread_id = int(rsp.thread_id)
    rsp.problem_id = str(rsp.problem_id)
    rsp.user_id = str(rsp.user_id)
    rsp.content = str(rsp.content)
    rsp.url = str(rsp.url)
    rsp.update_time = date2str(rsp.update_time)
    return rsp
def GETRecentMessageAPI(**kwargs):
    # type check
    if 'id' in kwargs and type(kwargs['id']) not in [int, long]:
        raise Exception('parameter \'id\' must be integer')
    # initialize url, fill if necessary
    url = 'http://rose.u-aizu.ac.jp/aojbbs/webservice/recent/message/$.xml'
    url = url.replace('$', kwargs['id'], 1)
    # set parameter
    prm = kwargs.copy()
    # call api
    rsp = parse.fromweb(url, prm)
    # format
    rsp.id = int(rsp.id)
    rsp.thread_id = int(rsp.thread_id)
    rsp.problem_id = str(rsp.problem_id)
    rsp.user_id = str(rsp.user_id)
    rsp.content = str(rsp.content)
    rsp.url = str(rsp.url)
    rsp.update_time = date2str(rsp.update_time)
    return rsp


# for aojtools v0.1 compatible
user = UserSearchAPI
problem = ProblemSearchAPI
problemlist = ProblemListSearchAPI
alluserlist = AllUserListSearchAPI
solvedrecord = SolvedRecordSearchAPI
statuslog = StatusLogSearchAPI
problemcategory = ProblemCategorySearchAPI
