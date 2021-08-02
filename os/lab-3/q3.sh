#!/bin/bash
echo "input a :"
read a
echo "input b :"
read b
echo "Menu \n1.Addition \n2.subtraction \n3.multiplication \n4.division \n5.modulos\n6.increment \n7.decrement"
echo "input option "
read opt
case "$opt" in
"1") echo "$(($a+$b))";;
"2") echo "$((a-b))";;
"3") echo "$(($a*$b))";;
"4") echo "$(($a/$b))";;
"5") echo "$(($a%$b))";;
"6") echo "$((++a)),$((++b))";;
"7") echo "$((--a)),$((--b))";;
esac
