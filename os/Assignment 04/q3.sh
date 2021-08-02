#!/bin/bash
for ((i=2;i<$1;i++))
do
	f=0
	for ((j=2;j<$i;j++))
	do
		if [ $(($i % $j)) = 0 ]
		then 
			f=1
		fi
	done
	if [ $f = 0 ]
	then
		echo $i
	fi
done
