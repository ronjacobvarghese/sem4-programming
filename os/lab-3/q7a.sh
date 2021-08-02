#!/bin/bash
for r in {5..1}
do
     for i in $(seq 1 $r)
     do
          printf "* "
     done
     printf "\n"
done
