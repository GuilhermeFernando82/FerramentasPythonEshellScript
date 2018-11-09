#!/bin/bash
if [ $1 == "" ]
then
echo "Exemplo de uso ./script.sh 192.168.1."
else
for host in {1..254};do
ping -c1 $1.$host | grep "64 bytes" 
done
fi
