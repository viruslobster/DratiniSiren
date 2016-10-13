#! /bin/bash

while true
do
    adb shell screencap -p | sed 's/\r$//' | python siren.py
    if [ $? -eq 0 ]
    then
        sleep 900
    else
        sleep 30
    fi
done
