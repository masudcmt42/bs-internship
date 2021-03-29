#!/usr/bin/bash
echo "Print the seq 1 to 10"
seq 1 10
echo "print odd number"
seq 1 2 10
echo "print even Number"
seq 2 2 10
echo "print value of pi using leibniz series"
seq -f '4/%g' 1 2 99999 | paste -sd-+ | bc -l
echo "cal pi using arctan"
echo "scale=20; 4*a(1)" |bc -l
echo " Machin's formula has a significantly higher rate of convergence"

{ echo -n "scale=50;"; seq 1 2 100 | xargs -n1 -I{} echo '(16*(1/5)^{}/{}-4*(1/239)^{}/{})';} | paste -sd-+ | bc -l
