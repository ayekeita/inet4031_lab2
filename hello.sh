#!/bin/bash

a=2
b=2
c=$((a + b))
echo "Bash says: Hello, World!"
echo "$a + $b = $c"

users=("User1" "User2" "User3")

for user in "${users[@]}"; do
    echo "$user"
done
