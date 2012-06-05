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
    return request.issue(url, prm)
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
    return request.issue(url, prm)
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
    return request.issue(url, prm)
def AllUserList(RankList)SearchAPI(**kwargs):
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
    return request.issue(url, prm)
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
    return request.issue(url, prm)
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
    return request.issue(url, prm)
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
    return request.issue(url, prm)
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
    return request.issue(url, prm)
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
    return request.issue(url, prm)
def ContestListSearchAPI(**kwargs):
    # type check
    # initialize url, fill if necessary
    url = 'http://judge.u-aizu.ac.jp/onlinejudge/webservice/contest_list'
    # set parameter
    prm = kwargs.copy()
    # call api
    return request.issue(url, prm)
def ContestInfoSearchAPI(**kwargs):
    # type check
    # initialize url, fill if necessary
    url = 'http://judge.u-aizu.ac.jp/onlinejudge/webservice/contest_info'
    # set parameter
    prm = kwargs.copy()
    # call api
    return request.issue(url, prm)
def ContestStandingSearchAPI(**kwargs):
    # type check
    # initialize url, fill if necessary
    url = 'http://judge.u-aizu.ac.jp/onlinejudge/webservice/contest_standing'
    # set parameter
    prm = kwargs.copy()
    # call api
    return request.issue(url, prm)
def ContestProblemSearchAPI(**kwargs):
    # type check
    # initialize url, fill if necessary
    url = 'http://judge.u-aizu.ac.jp/onlinejudge/webservice/contest_problem'
    # set parameter
    prm = kwargs.copy()
    # call api
    return request.issue(url, prm)
def ContestStatusLogSearchAPI(**kwargs):
    # type check
    # initialize url, fill if necessary
    url = 'http://judge.u-aizu.ac.jp/onlinejudge/webservice/contest_status_log'
    # set parameter
    prm = kwargs.copy()
    # call api
    return request.issue(url, prm)
def ThreadSearchAPI(**kwargs):
    # type check
    if 'id' in kwargs and type(kwargs['id']) not in [int, long]:
        raise Exception('parameter \'id\' must be integer')
    # initialize url, fill if necessary
    url = 'http://rose.u-aizu.ac.jp/aojbbs/webservice/thread/<threadId>.xml'
    # set parameter
    prm = kwargs.copy()
    # call api
    return request.issue(url, prm)
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
    return request.issue(url, prm)
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
    return request.issue(url, prm)
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
    return request.issue(url, prm)
def MessageSearchfromThreadIDAPI(**kwargs):
    # type check
    if 'id' in kwargs and type(kwargs['id']) not in [int, long]:
        raise Exception('parameter \'id\' must be integer')
    # initialize url, fill if necessary
    url = 'http://rose.u-aizu.ac.jp/aojbbs/webservice/message/thread/<threadId>.xml'
    # set parameter
    prm = kwargs.copy()
    # call api
    return request.issue(url, prm)
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
    return request.issue(url, prm)

