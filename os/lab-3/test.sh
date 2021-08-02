#!/bin/bash
a=0
b=1
s=0
for i in {1..$1}
do
	s=$(($a+$b))
	a=$b
	b=$s
	echo "$s "
done
