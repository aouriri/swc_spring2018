#!/bin/bash

#this script finds what country had the highest "LifeExp" in 2002 in gapminder.txt
#usage: ./MyFirstScript.sh
echo "cut -f1,3,4 Data/gapminder.txt | grep 2002 | sort -n -k3 |tail -n 1 > CountryHighestLifeExp.txt"
