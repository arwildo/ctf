#!/bin/bash

myname="bandit23"
mytarget=$(echo I am user $myname| md5sum | cut -d ' ' -f 1)

echo $myname
echo $mytarget

#echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"
#cat /etc/bandit_pass/$myname > /tmp/$mytarget
