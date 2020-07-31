#!/usr/bin/python
import re
import time
import socket

s = socket.socket()


with open("numbers.txt") as f:
    numbers = f.read().splitlines()


def sendNumbers():
    s.connect(('jh2i.com', 50012))
    count = 0
    while count < len(numbers):
        time.sleep(1)
        print "R: ", s.recv(1024)
        s.send(numbers[count].encode())
        count += 1


# Main
try:
    sendNumbers()
    s.send(numbers[0].encode())
    time.sleep(1)
    last_response = s.recv(1024)
    print "R: ", last_response
    new_number = re.sub(r"\D", "", last_response)
    print "New number: ", new_number

    with open('numbers.txt', 'a') as outfile:
        outfile.write("%s\n" % new_number)

except Exception as e:
    print(e)
print("Close connection")
s.close()
