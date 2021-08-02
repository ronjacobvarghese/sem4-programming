#!/bin/bash
echo "input length: "
read l
echo "input breath  : "
read b
echo "input radius: "
read r
pi=3.14
area=$(echo "scale=2;$pi * ($r * $r)" | bc)
peri=$(echo "scale=2;2 * $pi* ($r)" | bc)
echo "area of rectangle : $(($l*$b))"
echo "perimeter of rectangle : $((2*$l+$b))"
echo "area of circle : " $area
echo "circumfrence of circle : " $peri

