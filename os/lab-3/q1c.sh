#!/bin/bash
echo "enter number : "
read a

if [ $((a % 2)) -eq 0 ]
then
    echo "Even no"
else
    echo "Odd no"
fi
