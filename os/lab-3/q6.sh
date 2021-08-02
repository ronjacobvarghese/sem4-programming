#!/bin/sh
echo "input size of array"
read n
s=0
for i in $(seq 1 1 $n)
do
   echo "input integer into array:"
   read m
   s=$(($m+$s))
done
echo "average of array inputs $(($s/n))"
