#! /usr/bin/python2.6
# coding: utf-8

import parse

def time2date(s):
    return time.gmtime(int(s) / 1000.)
def date2str(d):
    return  time.strftime('%Y/%m/%d %H:%M:%S', d)
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
    for i0 in len(rsp.status):
        rsp.status[i0].submission = int(rsp.status[i0].submission)
        rsp.status[i0].solved = int(rsp.status[i0].solved)
        rsp.status[i0].accepted = int(rsp.status[i0].accepted)
        rsp.status[i0].wronganswer = int(rsp.status[i0].wronganswer)
        rsp.status[i0].timelimit = int(rsp.status[i0].timelimit)
        rsp.status[i0].memorylimit = int(rsp.status[i0].memorylimit)
        rsp.status[i0].outputlimit = int(rsp.status[i0].outputlimit)
        rsp.status[i0].runtimeerror = int(rsp.status[i0].runtimeerror)
        rsp.status[i0].compileerror = int(rsp.status[i0].compileerror)
    for i0 in len(rsp.status.solved_list):
        for i1 in len(rsp.status.solved_list.problem):
            rsp.status.solved_list[i0].problem[i1].id = str(rsp.status.solved_list[i0].problem[i1].id)
            rsp.status.solved_list[i0].problem[i1].submissiondate = time2date(rsp.status.solved_list[i0].problem[i1].submissiondate)
            rsp.status.solved_list[i0].problem[i1].language = str(rsp.status.solved_list[i0].problem[i1].language)
            rsp.status.solved_list[i0].problem[i1].cputime = int(rsp.status.solved_list[i0].problem[i1].cputime)
            rsp.status.solved_list[i0].problem[i1].memory = int(rsp.status.solved_list[i0].problem[i1].memory)
            rsp.status.solved_list[i0].problem[i1].code_size = int(rsp.status.solved_list[i0].problem[i1].code_size)
    return rsp
def ProblemSearchAPI(id, **kwargs):
    # type check
    if type(id) not in [str, unicode]:
        raise Exception('parameter \'id\' must be string')
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
    for i0 in len(rsp.status):
        rsp.status[i0].submission = int(rsp.status[i0].submission)
        rsp.status[i0].accepted = int(rsp.status[i0].accepted)
        rsp.status[i0].wronganswer = int(rsp.status[i0].wronganswer)
        rsp.status[i0].timelimit = int(rsp.status[i0].timelimit)
        rsp.status[i0].memorylimit = int(rsp.status[i0].memorylimit)
        rsp.status[i0].outputlimit = int(rsp.status[i0].outputlimit)
        rsp.status[i0].runtimeerror = int(rsp.status[i0].runtimeerror)
    for i0 in len(rsp.status.solved_list):
        for i1 in len(rsp.status.solved_list.user):
            rsp.status.solved_list[i0].user[i1].id = str(rsp.status.solved_list[i0].user[i1].id)
            rsp.status.solved_list[i0].user[i1].submissiondate = time2date(rsp.status.solved_list[i0].user[i1].submissiondate)
            rsp.status.solved_list[i0].user[i1].language = str(rsp.status.solved_list[i0].user[i1].language)
            rsp.status.solved_list[i0].user[i1].cputime = int(rsp.status.solved_list[i0].user[i1].cputime)
            rsp.status.solved_list[i0].user[i1].memory = int(rsp.status.solved_list[i0].user[i1].memory)
            rsp.status.solved_list[i0].user[i1].code_size = int(rsp.status.solved_list[i0].user[i1].code_size)
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
    for i0 in len(rsp.problem_list):
        for i1 in len(rsp.problem_list.problem):
            rsp.problem_list[i0].problem[i1].id = str(rsp.problem_list[i0].problem[i1].id)
            rsp.problem_list[i0].problem[i1].name = str(rsp.problem_list[i0].problem[i1].name)
            rsp.problem_list[i0].problem[i1].problemtimelimit = int(rsp.problem_list[i0].problem[i1].problemtimelimit)
            rsp.problem_list[i0].problem[i1].problemmemorylimit = int(rsp.problem_list[i0].problem[i1].problemmemorylimit)
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
    for i0 in len(rsp.user_list):
        for i1 in len(rsp.user_list.user):
            rsp.user_list[i0].user[i1].rank = int(rsp.user_list[i0].user[i1].rank)
            rsp.user_list[i0].user[i1].id = str(rsp.user_list[i0].user[i1].id)
            rsp.user_list[i0].user[i1].name = str(rsp.user_list[i0].user[i1].name)
            rsp.user_list[i0].user[i1].affiliation = str(rsp.user_list[i0].user[i1].affiliation)
            rsp.user_list[i0].user[i1].solved = int(rsp.user_list[i0].user[i1].solved)
            rsp.user_list[i0].user[i1].rating = float(rsp.user_list[i0].user[i1].rating)
    return rsp
def SolvedRecordSearchAPI(**kwargs):
    # type check
    if 'user_id' in kwargs and type(kwargs['user_id']) not in [str, unicode]:
        raise Exception('parameter \'user_id\' must be string')
    if 'problem_id' in kwargs and type(kwargs['problem_id']) not in [str, unicode]:
        raise Exception('parameter \'problem_id\' must be string')
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
    for i0 in len(rsp.solved_record_list):
        for i1 in len(rsp.solved_record_list.solved):
            rsp.solved_record_list[i0].solved[i1].run_id = int(rsp.solved_record_list[i0].solved[i1].run_id)
            rsp.solved_record_list[i0].solved[i1].user_id = str(rsp.solved_record_list[i0].solved[i1].user_id)
            rsp.solved_record_list[i0].solved[i1].problem_id = str(rsp.solved_record_list[i0].solved[i1].problem_id)
            rsp.solved_record_list[i0].solved[i1].date = time2date(rsp.solved_record_list[i0].solved[i1].date)
            rsp.solved_record_list[i0].solved[i1].language = str(rsp.solved_record_list[i0].solved[i1].language)
            rsp.solved_record_list[i0].solved[i1].cputime = int(rsp.solved_record_list[i0].solved[i1].cputime)
            rsp.solved_record_list[i0].solved[i1].memory = int(rsp.solved_record_list[i0].solved[i1].memory)
            rsp.solved_record_list[i0].solved[i1].code_size = int(rsp.solved_record_list[i0].solved[i1].code_size)
    return rsp
def StatusLogSearchAPI(**kwargs):
    # type check
    if 'user_id' in kwargs and type(kwargs['user_id']) not in [str, unicode]:
        raise Exception('parameter \'user_id\' must be string')
    if 'problem_id' in kwargs and type(kwargs['problem_id']) not in [str, unicode]:
        raise Exception('parameter \'problem_id\' must be string')
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
    for i0 in len(rsp.status_list):
        for i1 in len(rsp.status_list.status):
            rsp.status_list[i0].status[i1].run_id = int(rsp.status_list[i0].status[i1].run_id)
            rsp.status_list[i0].status[i1].user_id = str(rsp.status_list[i0].status[i1].user_id)
            rsp.status_list[i0].status[i1].problem_id = str(rsp.status_list[i0].status[i1].problem_id)
            rsp.status_list[i0].status[i1].submission_date = time2date(rsp.status_list[i0].status[i1].submission_date)
            rsp.status_list[i0].status[i1].status = str(rsp.status_list[i0].status[i1].status)
            rsp.status_list[i0].status[i1].language = str(rsp.status_list[i0].status[i1].language)
            rsp.status_list[i0].status[i1].cputime = int(rsp.status_list[i0].status[i1].cputime)
            rsp.status_list[i0].status[i1].memory = int(rsp.status_list[i0].status[i1].memory)
            rsp.status_list[i0].status[i1].code_size = int(rsp.status_list[i0].status[i1].code_size)
    return rsp
def JudgeDetailSearchAPI(id, **kwargs):
    # type check
    if type(id) not in [str, unicode]:
        raise Exception('parameter \'id\' must be string')
    # initialize url, fill if necessary
    url = 'http://judge.u-aizu.ac.jp/onlinejudge/webservice/judge'
    # set parameter
    prm = kwargs.copy()
    prm['id'] = id
    # call api
    rsp = parse.fromweb(url, prm)
    # format
    rsp.judge_id = str(rsp.judge_id)
    rsp.judge_type_code = undefined(rsp.judge_type_code)
    rsp.judge_type = str(rsp.judge_type)
    rsp.submissiondate = time2date(rsp.submissiondate)
    rsp.judgedate = time2date(rsp.judgedate)
    rsp.language = str(rsp.language)
    rsp.cuptime = undefined(rsp.cuptime)
    rsp.memory = undefined(rsp.memory)
    rsp.code_size = undefined(rsp.code_size)
    rsp.status = undefined(rsp.status)
    rsp.accuracy = str(rsp.accuracy)
    rsp.problem_id = str(rsp.problem_id)
    rsp.problem_title = str(rsp.problem_title)
    rsp.submissions = undefined(rsp.submissions)
    rsp.accepted = undefined(rsp.accepted)
    rsp.user_id = str(rsp.user_id)
    rsp.user_name = str(rsp.user_name)
    rsp.affiliation = str(rsp.affiliation)
    return rsp
def ProblemCategorySearchAPI(**kwargs):
    # type check
    if 'id' in kwargs and type(kwargs['id']) not in [str, unicode]:
        raise Exception('parameter \'id\' must be string')
    if 'category' in kwargs and type(kwargs['category']) not in [str, unicode]:
        raise Exception('parameter \'category\' must be string')
    # initialize url, fill if necessary
    url = 'http://judge.u-aizu.ac.jp/onlinejudge/webservice/problem_category'
    # set parameter
    prm = kwargs.copy()
    # call api
    rsp = parse.fromweb(url, prm)
    # format
    for i0 in len(rsp.problem_category):
        for i1 in len(rsp.problem_category.problem):
            rsp.problem_category[i0].problem[i1].id = str(rsp.problem_category[i0].problem[i1].id)
            rsp.problem_category[i0].problem[i1].category = str(rsp.problem_category[i0].problem[i1].category)
            rsp.problem_category[i0].problem[i1].score = float(rsp.problem_category[i0].problem[i1].score)
    return rsp
def SourceSearchAPI(id, **kwargs):
    # type check
    if type(id) not in [str, unicode]:
        raise Exception('parameter \'id\' must be string')
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
def ContestInfoSearchAPI(**kwargs):
    # type check
    # initialize url, fill if necessary
    url = 'http://judge.u-aizu.ac.jp/onlinejudge/webservice/contest_info'
    # set parameter
    prm = kwargs.copy()
    # call api
    rsp = parse.fromweb(url, prm)
    # format
    return rsp
def ContestStandingSearchAPI(**kwargs):
    # type check
    # initialize url, fill if necessary
    url = 'http://judge.u-aizu.ac.jp/onlinejudge/webservice/contest_standing'
    # set parameter
    prm = kwargs.copy()
    # call api
    rsp = parse.fromweb(url, prm)
    # format
    return rsp
def ContestProblemSearchAPI(**kwargs):
    # type check
    # initialize url, fill if necessary
    url = 'http://judge.u-aizu.ac.jp/onlinejudge/webservice/contest_problem'
    # set parameter
    prm = kwargs.copy()
    # call api
    rsp = parse.fromweb(url, prm)
    # format
    return rsp
def ContestStatusLogSearchAPI(**kwargs):
    # type check
    # initialize url, fill if necessary
    url = 'http://judge.u-aizu.ac.jp/onlinejudge/webservice/contest_status_log'
    # set parameter
    prm = kwargs.copy()
    # call api
    rsp = parse.fromweb(url, prm)
    # format
    return rsp
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
