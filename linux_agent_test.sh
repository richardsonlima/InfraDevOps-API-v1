#!/bin/bash

# Network interface for the IP address
iface="eth0:0"
# network interface for traffic monitoring (RX/TX bytes)
iface2="eth0"
######################
echo -e "\033[40;37;7m [+] Agente de monitoramento em tempo real (TESTE)\033[0m"
echo -e "\033[40;37;7m - API Restful URL- http://x.y.a.f:5000/project/cit/devops/infra/todo/api/v1.0/infra  \033[0m"
echo -e "\033[40;37;7m - Criado por Richardson Lima (contato@richardsonlima.com.br)\033[0m"
######################


#carga=$(uptime | grep -ohe 'load average[s:][: ].*' | awk '{ print $3 }')
carga=$(uptime|awk '{print " [1,5,15 minutos]", $10 $11 $12 }')
#cpu_sys=$()
#cpu_user=$()
cpu=$(top -b -n 1 | sed -ne '/Cpu/ s/.* \([0-9]*\.[0-9]*\)%us.* \([0-9]*\.[0-9]*\)%sy.*/ [+] User: \1%, [+] System: \2%/p')
descricao="Servidor XYZ"
disco_livre=$(df -h --total | awk  ' /total/ { print $4}' )
disco_usado=$(df -h --total | awk  ' /total/ { print $3}' )
total_disco=$(df -h --total | awk  ' /total/ { print $2}' )
done="false"
hostname=$(echo `hostname`)
ip=$(ip -f inet a | grep "$iface" | awk '/inet/{printf $2 }')
ram_livre=$(free -t -m|grep "Total" | awk '{ print $4 }')
ram_usado=$(free -t -m|grep "Total" | awk '{ print $3 }')
total_ram=$(free -t -m|grep "Total" | awk '{ print $2 }')
rede_enviado=$(/sbin/ifconfig $iface2 | awk '{ gsub(/\:/," ") } ; { print  } ' | awk '/RX\ b/ { print $8 }')
rede_recebido=$(/sbin/ifconfig $iface2 | awk '{ gsub(/\:/," ") } ; { print  } ' | awk '/RX\ b/ { print $3 }')
uptime=$(uptime | grep -ohe 'up .*' | sed 's/,//g' | awk '{ print $2" "$3 }')

curl -i -X POST -H "Content-Type: application/json" \
-d '{"carga":"'"$carga"'","cpu":"'"$cpu"'","descricao":"'"$descricao"'","disco_livre":"'"$disco_livre"'","disco_usado":"'"$disco_usado"'","done":"'"$done"'","ip":"'"$ip"'","uptime":"'"$uptime"'","ram_livre":"'"$ram_livre"'","ram_usado":"'"$ram_usado"'","rede_enviado":"'"$rede_enviado"'","rede_recebido":"'"$rede_recebido"'","total_disco":"'"$total_disco"'","total_ram":"'"$total_ram"'","hostname":"'"$hostname"'"}' \
http://x.y.a.f:5000/project/cit/devops/infra/todo/api/v1.0/infra
