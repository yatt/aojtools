# coding: utf-8
import urllib
from xml.etree.ElementTree import *

class Node(object):
    def __init__(self, name, info):
        self.__dict__['_info'] = info
        self.__dict__['_name'] = name
    def __getattr__(self, name):
        if name in self.__dict__['_info']:
            return self.__dict__['_info'][name]
        return self.__dict__[name]
    def __setattr__(self, name, value):
        self.__dict__['_info'][name] = value
    def __iter__(self):
        return self._info.iteritems()
    def __repr__(self):
        args = self._name, ','.join(self._info.keys())
        return "<%s keys=%s>" % args
    #def __dict__(self):
    #    return self.__dict__['_info']

def xmltrans(xmlnode):
    node = Node(xmlnode.tag, {})
    for child in xmlnode:
        key = child.tag
        if len(child) == 0:
            val = child.text
            if val is not None:
                val = val.strip()
            assign(node._info, key, val) 
        else:
            assign(node._info, key, xmltrans(child))
    return node

def assign(info, key, value):
    if key in info:
        if isinstance(info[key], list):
            info[key].append(value)
        else:
            info[key] = [info[key], value]
    else:
        info[key] = value

def urlopen(url):
    # http access
    conn = urllib.urlopen(url)
    xmlstr = conn.read()
    # create xml
    xmldoc = fromstring(xmlstr)
    # xml to object tree
    otree = xmltrans(xmldoc)
    return otree

def parse(filepath):
    fobj = open(filepath)
    xmlstr = fobj.read()
    xmldoc = fromstring(xmlstr)
    otree = xmltrans(xmldoc)
    return otree
