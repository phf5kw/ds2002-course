#!/bin/bash

clear
echo "Let's build a mad-lib!"

read -p "1. Please give me an adjective: " ADJ1

read -p "2. Please give me a noun: " NOUN1

read -p "3. Please give me a verb: " VERB1

read -p "4. Please give me another noun: " NOUN2

read -p "5. Please give me another adjective: " ADJ2

read -p "6. Please give me another verb: " VERB2

read -p "7. Please give me another noun: " NOUN3

read -p "8. Please give me another adjective: " ADJ3


echo "Once upon a time, there was a $ADJ1 $NOUN1."
echo "The $NOUN1 went to $VERB1 the $ADJ2 $NOUN3, but the $NOUN3 was very $ADJ3."
echo "THE $NOUN3 decided to $VERB2 the $NOUN1."
echo "The end."
