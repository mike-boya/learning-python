#!/usr/bin/env python

import mechanize


def testProxy(url, proxy):
    browser = mechanize.Browser()
    browser.set_proxies(proxy)
    page = browser.open(url)
    source_code = page.read()
    print source_code


url = 'http://canhazip.com/'
hideMeProxy = {'http': '223.202.126.104:8080'}

testProxy(url, hideMeProxy)

