```bash
#!/bin/bash

#Update apt and install necessary packages
apt update --allow-releaseinfo-change
apt install -y ufw
apt install -y netcat
apt install -y curl
apt install -y unzip
apt install -y git
apt install -y python-pip
apt install -y build-essential
apt install -y default-jre
#Setup Firewall
ufw allow 21
ufw allow 22
ufw allow 53
ufw allow 80
ufw allow 443
ufw allow 8080
ufw allow 50050
echo y | ufw enable
#Make Folders
mkdir ~/exfil/
mkdir -p ~/tools/netcat/
mkdir -p ~/tools/curl/
mkdir -p ~/tools/chisel/
#Setup External IP resolver
printf '#!/bin/bash\ncurl https://ifconfig.co/ip\n' > /usr/local/bin/exip
chmod +x /usr/local/bin/exip
#Download and extract netcat
cd ~/tools/netcat/
wget https://eternallybored.org/misc/netcat/netcat-win32-1.12.zip
unzip netcat-win32-1.12.zip
#Download and extract curl
cd ~/tools/curl/
wget https://curl.se/download/curl-7.75.0.tar.gz
tar zxf curl-7.75.0.tar.gz
#Dowanload and extract chisel
cd ~/tools/chisel/
wget https://github.com/jpillora/chisel/releases/download/v1.7.4/chisel_1.7.4_windows_amd64.gz
wget https://github.com/jpillora/chisel/releases/download/v1.7.4/chisel_1.7.4_linux_amd64.gz
gunzip -d chisel_1.7.4_windows_amd64.gz
gunzip -d chisel_1.7.4_linux_amd64.gz
mv chisel_1.7.4_linux_amd64 chisel
mv chisel_1.7.4_windows_amd64 chisel.exe
chmod +x chisel
#Download and install Impacket
cd ~/tools/
git clone https://github.com/SecureAuthCorp/impacket.git
cd impacket
pip install .
#Download and install go
cd ~/
wget https://golang.org/dl/go1.15.6.linux-amd64.tar.gz
tar zxf go1.15.6.linux-amd64.tar.gz
mv go /usr/local/
rm go1.15.6.linux-amd64.tar.gz
export PATH=$PATH:/usr/local/go/bin
export GOPATH=/root/go_projects
### my additions
apt -y install powershell

```

