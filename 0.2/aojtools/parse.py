#! /usr/bin/python2.6
# coding: utf-8
import urllib
from xml.etree.ElementTree import fromstring

class dictex(dict):
    # pretty dict
    def __init__(self, tag):
        self._tag = tag
    def __getattr__(self, name):
        return self.get(name, None)

def fromxml(xmlnode):
    fun = lambda x: len(c) and fromxml(x) or x.text.strip()
    d = dictex(xmlnode.tag)
    for c in xmlnode:
        k = c.tag
        if k in d:
            d[k] = isinstance(d[k], list) and d[k] or [d[k]]
            d[k].append(fun(c))
        else:
            d[k] = fun(c)
    return d

def fromweb(url, prm):
    try:
        cont = urllib.urlopen(url).read()
        # ここでdecode('utf-8', 'ignore')する必要あるかも
        tree = fromxml(fromstring(cont))
        return tree
    except Exception, e:
        raise e

if __name__ == '__main__':
    url = 'http://judge.u-aizu.ac.jp/onlinejudge/webservice/problem_list?volume=10'
    tree = fromxml(fromstring(urllib.urlopen(url).read()))
    #import code;code.InteractiveConsole(locals()).interact()
    for n in tree.problem: print n.name
