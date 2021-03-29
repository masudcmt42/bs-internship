#!/usr/bin/bash
#cat $0
printf "hello world\n"
printf "%s\n" "hello bash"
printf "%s " "masud" "Rana" "Shahin"
printf "\n"
#Formate Spaecifiers
echo "%d for integer"
echo "%s for string"
echo "%f for floting point"
echo "%lf for double"
printf "%s\n" "1" "2" "\n3"
printf "%b\n" "1" "2" "\n3" #%b specifier which is essentially the same by it allows us to interpret escape sequences with an argument
printf "%d\n" 255 0xff 0377 3.5 # dec hex oct floating
printf "%.1f\n" 255 0xff 0377 3.5 #octal can`nt support in %f specifier

divider===============================
divider=$divider$divider

header="\n %-10s %8s %10s %11s\n"
format=" %-10s %08d %10s %11.2f\n"

width=43

printf "$header" "ITEM NAME" "ITEM ID" "COLOR" "PRICE"

printf "%$width.${width}s\n" "$divider"

printf "$format" \
Triangle 13  red 20 \
Oval 204449 "dark blue" 65.656 \
Square 3145 orange .7
