#!/bin/bash
for m in {1..5} 
do 
    for((a=i; a<=5; a++)) 
    do
      printf " " 
    done
  
    for((n=1; n<=m; n++)) 
    do
      printf "*" 
    done 
    for((i=1; i<m; i++)) 
    do
      printf "*" 
    done
  
    printf "\n"; 
done
