#!/bin/bash

Ip_Lst="ip_adrslst.txt"

if [ ! -f "$Ip_Lst" ]; then
    echo "File $Ip_Lst not found!"
    exit 1
fi

while IFS= read -r ip; do

    echo "Pinging $ip..."
    ping -n 4 "$ip"


    if [ $? -eq 0 ]; then
        echo "$ip is reachable."
    else
        echo "$ip is not reachable."
    fi
    echo "--------------------------"
done < "$Ip_Lst"

