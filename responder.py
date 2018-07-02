import socket
import hashlib
import json
import ssl

from influxdb import InfluxDBClient
from influxdb.client import InfluxDBClientError

class queries:
	def __init__(self, query, db, name):
		self.query = query
		self.db = db
		self.name = name

### enter your influxdb info here server,port,user,password and if you dont use SSL you can change ssl=True to SSL=False
influx = InfluxDBClient('hostname/ipaddr', 8086, 'user', 'pass', ssl=True)
### enter the secret that the bot will use to connect here, in the bot you will need to enter the md5 hash of it in the bot
password = 'password'

KEYFILE = 'key.pem'
CERTFILE = 'cert.pem'

# use a query that only outputs the last value!!
# example:
# SELECT "valuename" FROM "measurement" ORDER BY DESC LIMIT 1
# the values are query,database,dataname
# every thing should have a different dataname so it can be processed properly, you will also need to enter the dataname in the bot later on.
# to add another query simply copy one of the existing queries under this change the number to one that is not used (query3 query4 and etc) and add it to the querylist
# if a query doesnt work or if the query is empty the code will fail
query1 = queries('query', "db", "name")
query2 = queries('query', "db", "name")
query3 = queries('query', "db", "name")
querylist = [query1,query2,query3]

TCP_IP = '0.0.0.0'
TCP_PORT = 5102
BUFFER_SIZE = 1024

m = hashlib.md5()
m.update(password)

data = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
s_ssl = ssl.wrap_socket(s, keyfile=KEYFILE, certfile=CERTFILE, server_side=True)

try:
	while True:
		conn, addr = s_ssl.accept()
		print('Connection address:', addr)
		while 1:
			passhash = conn.recv(BUFFER_SIZE)
			if not passhash:
				break
				print("received passhash:", passhash)
			if m.hexdigest() != passhash:
				print("hash not correct")
				conn.close()
				break
				
			data = {}
			for x in querylist:
				influx.switch_database(x.db)
				querydata = influx.query(x.query)
				result = querydata.raw['series'][0]['values'][0][1]			
				data[x.name] = result
			
			json_data = json.dumps(data)
			print("sending:")	
			print(json_data)	
			conn.send(json_data)
		conn.close()
		
except:
	s.close()
