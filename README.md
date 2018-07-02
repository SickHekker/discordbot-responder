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

add your responder

%setresponder respondername responderaddress responderMD5passhash	

set a bind for the dataname, dataname is the name you gave the data in the responder.py, showname is what you will put after %show to get the data (postfix is like celsius or % for humidity)

%setshowbind respondername showname dataname postfix		
	
remove ALL info stored in the bot

%removeall	

remove your responders stored in the bot

%removeresponders	

remove your showbinds stored in the bot

%removeshowbinds	
	
display data

%show showname


example:

%setresponder homeresponder hostname.com d0763edaa9d9bd2a9516280e9044d885

%setshowbind homeresponder outdoortemperature outtemp Celsius

%show outdoortemperature
