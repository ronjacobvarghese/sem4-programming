#!/bin/bash

 declare -a arr1=()
 declare -a arr2=()
 declare -a arr3=()
 echo "you're inputing array 3x3 size"
 echo "input matrix1" 
 for ((i=0; i<9; i++))
 do
     read m
     arr1=("${arr1[@]}" "$m")
 done
 echo "input matrix2"
  for ((i=0; i<9; i++))
 do
     read m
     arr2=("${arr2[@]}" "$m")
 done
 sum=0
 len=9
 for ((i=0; i<$len; i++))
 do
     sum=$(( ${arr1[$i]}+${arr2[$i]} )) 
     #echo $sum
     arr3=("${arr3[@]}" "$sum")
 done 
 echo "addition of two matrix is"
 
echo ${arr3[@]}