#!/bin/bash
logfile=$1.log
echo "$1.log"
while true
 do
    #vm_mem=$(free -m|grep "buffers/cache"|awk '{print $4}')
    vm_mem=$(free -m|grep "Mem"|awk '{print $7}')
    cpu=$(top -bn2|grep "Cpu(s)"|awk '{print $8}'|awk -F'%' '{print $1}'|tail -n1)
    echo "mem $vm_mem" >> $logfile
    echo "cpu $cpu" >> $logfile
    sleep 1m
 done
