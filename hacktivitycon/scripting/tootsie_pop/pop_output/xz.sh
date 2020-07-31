#!/bin/bash

mv $1 $1.xz
xz -d $1.xz
