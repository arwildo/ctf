#!/usr/bin/python3

p = {}
p[0] = 52037 
p[6] = 52081 
p[5] = 52063 
p[1] = 52077 
p[9] = 52077 
p[10] = 52080
p[4] = 52046 
p[3] = 52066 
p[8] = 52085 
p[7] = 52081 
p[2] = 52077 
p[11] = 52066

ret = ""
for key, value in sorted(p.items()):
    ret += str(str(value)+" ")

print(ret)
