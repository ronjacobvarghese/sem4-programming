#!/bin/bash
cat >numericdata << eof
Karunagappally 34567 7864 6785
Kollam 56754 6754 7654
Vallikkavu 54328 7548 45675
Trivandrum 16423 6654 6754
Ernakulam 28796 8549 9875
Kayamkulam 35589 75892 3451
kottayam 45557 6773 6547
tirukulum 45675 56476 7896
eof
cat numericdata|cut -d" " -f1|grep -i ^T
cat numericdata|cut -d" " -f1,4|grep -i ^K|cut -d" " -f2|sort -n
cat numericdata|cut -d" " -f3|grep ^6|grep 4$
cat numericdata|cut -d" " -f3|grep -E '6'+
cat numericdata|cut -d" " -f2|grep -E '5'+

