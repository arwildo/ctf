#!/bin/bash

nc -N jh2i.com 50012

while read s; 
  do echo "$s" | ;
done < numbers.txt
