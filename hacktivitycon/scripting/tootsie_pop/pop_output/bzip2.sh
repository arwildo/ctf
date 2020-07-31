#!/bin/bash

mv $1 $1.bz2
bzip2 -d $1.bz2
