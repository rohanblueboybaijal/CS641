#!/bin/bash

python script.py | ssh -i /home/yatharth/Documents/IITK_Courses/Fourth_Sem/CS641/Keys/CS641_rsa student@65.0.124.36 -t 2>/dev/null | grep -A1 "Slowly, a new" | grep -v "Slowly" | sed 's/--//g' | grep -E '[a-z]' | sed 's/^[ \t]*//g' | sed '/^$/d' > outputs.txt
