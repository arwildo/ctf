#!/bin/bash
for i in {0..9}
do
    for j in {0..9}
    do
        for k in {0..9}
        do
            for l in {0..9}
            do
                echo "$i$j$k$l"
                ~/leviathan6 $i$j$k$l
                sleep .1
            done
        done
    done
done
