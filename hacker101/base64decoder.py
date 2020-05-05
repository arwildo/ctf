#!/usr/bin/python3
import base64

strings = ["eyJjbWQiOiJzZXRUZW1wIiwidGVtcCI6Nzd9%0A&",
            "eyJjbWQiOiJnZXRUZW1wIn0%3D%0A&",
            "eyJjbWQiOiJzZXRUZW1wIiwidGVtcCI6Nzd9%0A&",
            "eyJjbWQiOiJzZXRUZW1wIiwidGVtcCI6NzB9%0A&"]


for i in strings:
    print(base64.b64decode(i + '====='))
