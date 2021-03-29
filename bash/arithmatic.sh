#!/usr/bin/bash
#$((expression))
#$(( n1+n2 ))
#$(( n1/n2 ))
#$(( n1-n2 ))
x=5
y=10
ans=$(( x+y ))
echo "$x + $y = $ans"

read -p "Enter Two numbers: " x y
echo "$x + $y = $(( x+y ))"
echo "$x - $y = $(( x-y ))"
echo "$x / $y = $(( x/y ))"
echo "$x % $y = $(( x%y ))"
echo "$x++  = $(( x++ ))"
echo "$y--  = $(( y-- ))"
echo "2^3 = $(( 2**3 ))"
((x=4,y=5,z=x*y,u=z/2)) ; echo $x $y $z $u




