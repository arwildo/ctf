#!/usr/bin/python3
a = "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"

with open("wordlist", 'w') as file:
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    file.write("{} {}{}{}{}\n".format(a, i, j, k, l))
