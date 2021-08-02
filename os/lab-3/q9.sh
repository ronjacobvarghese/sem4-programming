#!/bin/bash
read -p "m: " m
read -p "n: " n
echo "matrix 1:"
declare -A arr1
for i in $(seq 0 $(($m-1)))
do
	read -a a
	j=0
        for k in ${a[@]}
        do
                arr1[$i,$j]=$k
		j=$(($j+1))
        done
done
echo "Final matrix:"
for i in $(seq 0 $(($m-1)))
do
        for j in $(seq 0 $(($n-1)))
        do
		printf "${arr1[$j,$i]} "
        done
	echo
done