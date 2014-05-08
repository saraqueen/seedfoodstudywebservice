#!/bin/sh

DIR=/var/lib/openshift/536aaf5c4382eca54f00019f/app-root/runtime/repo/apps
LOCKFILE=$DIR/seedfoodstudywebservice.py.pid


if ! [ -e ${LOCKFILE} ] && kill -0 `cat ${LOCKFILE}`; then
	echo "in if"
    nohup python $DIR/seedfoodstudywebservice.py &
	echo $! > "$LOCKFILE"  
fi