 cat input.txt | python text_to_digits.py | tr -d '\r' | awk '{print substr($0,1,1) substr($0,length)}' | awk '{t+=$0} END {print t}'
