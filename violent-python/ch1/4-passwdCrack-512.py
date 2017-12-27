#!/usr/bin/env python

import crypt

def testPass(cryptPass):
    salt = cryptPass[3:11]
    # The default wordlist here will not crack the root pw - leaving out solution to avoid spoilers
    dictfile = open('dictionary.txt', 'r')
    # $6$ is SHA512
    insalt = '$6$' + salt
    for word in dictfile.readlines():
        cryptword = crypt.crypt(word.strip(), insalt)
        if (cryptword == cryptPass):
          print "[+] Found Password: " + word + "\n"
          return
    print '[-] Password Not Found.\n'
    return

def main():
    # The test password is 'password'
    password = "$6$GpNiWKnm$aToSshPrg45wXFuP/Hmkkpf8/GUYg0d/C4eU/BH7iG2QwM.C59NIVr/izGUGXzf7HjqQNmpFXhxtIxGtXNrmj0"
    #password = "$6$ms32yIGN$NyXj0YofkK14MpRwFHvXQW0yvUid.slJtgxHE2EuQqgD74S/GaGGs5VCnqeC.bS0MzTf/EFS3uspQMNeepIAc."
    testPass(password)

if __name__ == "__main__":
    main()
