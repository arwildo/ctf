#!/bin/bash

mv $1 $1.gz
gunzip $1.gz
