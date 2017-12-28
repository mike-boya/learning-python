#!/usr/bin/env python

import ftplib


def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'foo@bar.com')
        print '\n[*] ' + str(hostname) +\
          ' FTP Anonymous Logon Succeeded.'
        ftp.quit()
        return True
    except Exception, e:
        print '\n[-] ' + str(hostname) +\
        ' FTP Anonymous Logon Failed.'
        return False


host = '192.168.34.165'
anonLogin(host)
