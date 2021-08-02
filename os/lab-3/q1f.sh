#!/bin/bash
a=ron
b=jacob
c=$a$b
len=`echo $c | wc -c`
len=`expr $len - 1`
echo "resultant string is $c"
echo "Length of the string: $len"
