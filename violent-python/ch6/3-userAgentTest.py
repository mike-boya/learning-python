#!/usr/bin/env python

import mechanize


def testUserAgent(url, userAgent):
    browser = mechanize.Browser()
    browser.addheaders = userAgent
    page = browser.open(url)
    source_code = page.read()
    print source_code


url = 'http://www.whatsmyua.info/'
userAgent = [('User-agent', 'Mozilla/5.0 (X11; U; ' +
  'Linux 2.4.2-2 i586; en-US; m18) Gecko/20010131 foo')]
testUserAgent(url, userAgent)

