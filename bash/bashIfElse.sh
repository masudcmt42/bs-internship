#!/usr/bin/bash
echo "this is test program"
if [ "$1" = "" ]; then 
	echo "sysntex: $0 word"
	echo "if you provide more then word, enclose them in quotes."
else
	echo "$1"
fi
