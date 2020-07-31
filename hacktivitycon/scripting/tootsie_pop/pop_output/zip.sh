#!/bin/bash

mv $1 $1.zip
unzip $1.zip -d room && rm $1.zip
