#! /usr/bin/python2.6
# coding: utf-8
import urllib
from xml.etree.ElementTree import fromstring

class dictex(dict):
    # pretty dict
    def __init__(self, tag):
        self.__dict__['_tag'] = tag
    def __getattr__(self, name):
        return self.get(name, None)
    def __setattr__(self, key, val):
        dict.__setitem__(self, key, val)

def fromxml(xmlnode):
    fun = lambda x: len(c) and fromxml(x) or (x.text and x.text.strip() or '')
    d = dictex(xmlnode.tag)
    for c in xmlnode:
        k = c.tag
        if k in d:
            d[k] = isinstance(d[k], list) and d[k] or [d[k]]
            d[k].append(fun(c))
        else:
            d[k] = fun(c)
    return d

def fromweb(url, prm={}):
    try:
        enc = '&'.join('%s=%s' % (k, prm[k]) for k in prm)
        httpparam = urllib.quote
        purl = url + (enc and '?' + enc or '')
        if False:
            print purl
        cont = urllib.urlopen(purl).read()
        tree = fromxml(fromstring(cont))
        return tree
    except Exception, e:
        raise e

if __name__ == '__main__':
    url = 'http://judge.u-aizu.ac.jp/onlinejudge/webservice/problem_list?volume=10'
    tree = fromxml(fromstring(urllib.urlopen(url).read()))
