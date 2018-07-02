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

mv cert.pem /opt/responder

mv key.pem /opt/responder

i recommend creating your own self signed certificates.


open /opt/responder/responder.py with your favorite editor and change the password, enter your influxdb info.

mv responder.service /etc/systemd/system

systemctl enable  responder

systemctl start responder

portforward port 5102 to the host

you could also use ddns, the bot does also work with dns names instead of ip address

# bot
In discord, send %help, you will get a list of commands in your pm, info for each command can be found by sending %help commandname

descriptions on commands is still work in progress
