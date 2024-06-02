
```


dig -x 209.90.52.11 | awk '/ANSWER/ {getline;print} PTR'
for i in $(seq 1 5 );do dig -x 10.10.10.1 | awk '/ANSWER/ {getline;print} PTR'.$i ;done


whois 10.90.52.11 | grep -e city -e City -e country -e Country -e address -e Address -e org -e net -e Net

for i in $(seq 1 5 );do ping -c 1 10.10.10.$i |grep "bytes from" |cut -d " "  -f4  ;done

for i in $(cat adds); do nmap -vv -Pn -PS  --top-ports 3000 $i; done

windows
for /L %i in (,1,1,255) do @ping -n 1 10.10.10.%i | find “TTL"
 read file ignoring commented liens
  for /F "eol=; tokens=2,3* delims=," %i in (myfile.txt) do @echo %i %j %k

for i in $(cat temp.txt);do sudo nmap -script=/usr/local/share/nmap/scripts/nbstat.nse $i;done



nmap --script=banner-plus.nse --min-rate=400 --min-parallelism=512 -p80,443 -n -Pn -PS -oA ~/test domain.org
 -PS is SYN discover scan; -sS is a SYN CONNECT scan, slower. 
 -Pn is non ping
 -n do not resolve dns
 -oA output to file all formats


for i in $(seq 1 5 );do ping -c 1 10.142.96.$i | grep "bytes from";done


traceroute -T host  <  tcp syn probes rather than echo
nmap -sn google.com    < host discovery


can ping but can't trace route.. use this ..
nmap --script=firewalk --traceroute 192.168.20.2
hping3 -S 10.10.10.1 -c 100 -p ++1



FIREWALL EVATION
-f 8 byte probes
--mtu 8
-D RND: 10  (decoy option)
-D ip address, ip address  
-sI ipofzombie 
--data-length 25
--randomize-hosts ip-target-range
-sT -PN --spoof-mac 0 target
--bad-sum targetip   sends packets with incorrect checksums

```

