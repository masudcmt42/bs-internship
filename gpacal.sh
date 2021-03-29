#!/usr/bin/bash
echo "this is a simple GPA calcluator"
read -p "Enter Your Marks: " num
pt=0.00
lt="F"
if [ $num -ge 80 ]; then 
	lt="A+";
	pt=5.00;
elif [ $num -ge 70 ]; then
        lt="A";
        pt=4.00;
elif [ $num -ge 60 ]; then
        lt="B+";
        pt=3.00;
elif [ $num -ge 50 ]; then
        lt="B";
        pt=2.50;
elif [ $num -ge 40 ]; then
        lt="C";
        pt=2.00;
elif [ $num -ge 33 ]; then
        lt="D";
        pt=1.00;

fi
echo "You Get $lt and point $pt"

#To compare two floating Number 
#use if (( $(echo "$num1 > $num2" |bc -l) ))
#ensure that you have the bc calculator package installed
#remember enclose the bc into either backticks or $() and then into (( ))
#bc - An arbitrary precision calculator language
#-l  --mathlib      use the predefined math routines
if (( $(echo "$pt >= 3.50" |bc -l) )); then
	echo "Excelent"
else
	echo "Try your level Best next"
fi
