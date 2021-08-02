#!/bin/bash
gcd () {
	if [ $1 -lt $2 ]
	then 
		for ((i=$1;i>0;i--))
		do
			if [[ $(($1%$i)) = 0 && $(($2%$i)) = 0 ]]
			then  
				echo $i
				break
			fi
		done
	else
		for ((i=$2;i>0;i--))
		do
			if [[ $(($1%$i)) = 0 && $(($2%$i)) = 0 ]]
			then  
				echo $i
				break
			fi
		done
	fi
}

read n1 n2
gcd $n1 $n2
