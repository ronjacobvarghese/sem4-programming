#!/bin/bash
echo "input n"
read num
factorial=1
count=$num 
while [[ $count -gt 0 ]];
do
   factorial=$(( $factorial * $count ))
   count=`expr $count - 1`
done
 
echo "factorial of $num is $factorial"
