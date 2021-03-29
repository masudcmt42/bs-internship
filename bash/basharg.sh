#!/usr/bin/bash
echo $0 $1 $2 $3
echo "script file name is $0"
if [ $1 = "" ]; then
	echo " there is no value in 1st argument"
else
	echo 1st argument is $1
fi
if [ $2 = "" ]; then
        echo " there is no value in 2nd argument"
else
        echo 2nd argument is $2
fi
if [ $3 = "" ]; then
        echo " there is no value in 3rd argument"
else
        echo 3rd argument is $3
fi


