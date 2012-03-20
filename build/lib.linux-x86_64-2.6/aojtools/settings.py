host = 'judge.u-aizu.ac.jp'
hhost = 'http://' + host

# API url
url = {
    'user': hhost + '/onlinejudge/webservice/user',
    'problem': hhost + '/onlinejudge/webservice/problem',
    'problemlist': hhost + '/onlinejudge/webservice/problem_list',
    'alluserlist': hhost + '/onlinejudge/webservice/user_list',
    'solvedrecord': hhost + '/onlinejudge/webservice/solved_record',
    'statuslog': hhost + '/onlinejudge/webservice/status_log',
    'problemcategory': hhost + '/onlinejudge/webservice/problem_category',
}

# submit destination url
submiturl = hhost + '/onlinejudge/servlet/Submit'

# webpage encoding
SITEENCODING = 'sjis'

LANG_C = 'C'
LANG_CPP = 'C++'
LANG_JAVA = 'JAVA'
