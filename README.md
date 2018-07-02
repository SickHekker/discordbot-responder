# discordbot-responder
My discord bot for serving data, only needs chat permissions.

https://discordapp.com/api/oauth2/authorize?client_id=446956965130928128&permissions=2048&scope=bot
# Install
execute as root.

apt-get update

apt-get install git python-pip

pip install influxdb

git clone https://github.com/SickHekker/discordbot-responder.git

cd discord-responder

mkdir /opt/responder

mv responder.py /opt/responder

open /opt/responder/responder.py with your favorite editor and change the password, enter your influxdb info.

mv responder.service /etc/systemd/system

systemctl enable  responder

systemctl start responder

portforward port 5102 to the host

you could also use ddns, the bot does also work with dns names instead of ip address

# bot
%setinfo respondername infoname dataname postfix

(postfix is like celsius or % for humidity)

%setresponder respondername responderaddress responderMD5passhash

%removeall

%removeresponders

%removeinfonames

%show infoname
