#!/bin/bash
echo "enter name:"
read name
echo "enter programme name:"
read P_name
echo "enter the enrolment number:"
read en_no
echo "Name:$name"
echo "Programme name:$P_name"
echo "Enrolment no:$en_no"

#b

echo "Enter 4 number:"
read a b c d
s=0
s=$(($a+$b+$c+$d))
echo "sum : $s"
echo "product : $(($a*$b*$c*$d))"
echo "average : $((s/4))"
