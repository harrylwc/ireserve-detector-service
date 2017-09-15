import urllib, json, array, datetime, time, sys
from datetime import datetime, timedelta

url = "https://reserve-prime.apple.com/HK/zh_HK/reserve/iPhone/availability.json"

output = ""

def readDataFromURL(url):
	"read json from apple"
	response = urllib.urlopen(url)
	return json.loads(response.read());
	
def createLink(model, shop):
   "create direct ireserve buying link"
   return "https://reserve-prime.apple.com/HK/en_HK/reserve/iPhone?partNumber="+model+"&channel=1&rv=0&sourceID=&iPP=false&appleCare=N&iUID=&iuToken=&carrier=&store="+shop;
data = ""

for x in range(1, 10):
	try:
		data = readDataFromURL(url)
		break
	except IOError:
		time.sleep(3)

#with open('stores.json') as data_file:    
#    data = json.load(data_file)

if data == "" or not data.has_key("stores"):
	sys.exit()

shopList = ["R409","R499","R485","R428","R610","R673"]
shopListNameMap = {"R409":"CWB","R499":"TST","R485":"FW","R428":"IFC","R610":"NTP","R673":"APM"}

modelList8 = ["MQ6K2ZP/A","MQ6L2ZP/A","MQ6M2ZP/A","MQ7F2ZP/A","MQ7G2ZP/A","MQ7H2ZP/A"]
modelList8Plus = ["MQ8D2ZP/A","MQ8E2ZP/A","MQ8F2ZP/A","MQ8G2ZP/A","MQ8H2ZP/A","MQ8J2ZP/A"]
modelListX = ["MQA52ZP/A","MQA62ZP/A","MQA82ZP/A","MQA92ZP/A"]
modelListShortColourMap8 = {"MQ6K2ZP/A":"B","MQ6L2ZP/A":"S","MQ6M2ZP/A":"G","MQ7F2ZP/A":"B","MQ7G2ZP/A":"S","MQ7H2ZP/A":"G"}
modelListShortColourMap8Plus = {"MQ8D2ZP/A":"B","MQ8E2ZP/A":"S","MQ8F2ZP/A":"G","MQ8G2ZP/A":"B","MQ8H2ZP/A":"S","MQ8J2ZP/A":"G"}
modelListShortColourMapX = {"MQA52ZP/A":"B","MQA62ZP/A":"S","MQA82ZP/A":"B","MQA92ZP/A":"S"}


#for model in modelListX:
#	output += "<th>" + modelListShortColourMapX[model] + "</th>"
for model in modelList8Plus:
	output += "<th>" + modelListShortColourMap8Plus[model] + "</th>"
for model in modelList8:
	output += "<th>" + modelListShortColourMap8[model] + "</th>"
output += "</tr>"
for shop in shopList:
	output += "<tr><td>"+shopListNameMap[shop]+"</td>"
#	for model in modelListX:
#		if data["stores"][shop][model]["availability"]["unlocked"] == True:
#			output += "<td class='available'><a href='"+createLink(model, shop)+"'>A</a></td>"
#		else:
#			output += "<td><a href='"+createLink(model, shop)+"'>X</a></td>"
	for model in modelList8Plus:
		if data['stores'][shop][model]['availability']['unlocked'] == True:
			output += "<td class='available'><a href='"+createLink(model, shop)+"'>A</a></td>"
		else:
			output += "<td><a href='"+createLink(model, shop)+"'>X</a></td>"
	for model in modelList8:
		if data['stores'][shop][model]['availability']['unlocked'] == True:
			output += "<td class='available'><a href='"+createLink(model, shop)+"'>A</a></td>"
		else:
			output += "<td><a href='"+createLink(model, shop)+"'>X</a></td>"
	output += "</tr>"
output += "</table>"


#current_datetime = datetime.now() + timedelta(hours=15);
current_datetime = datetime.now();

output += "Last updated:" + current_datetime.strftime("%Y-%m-%d %H:%M:%S") 

header = open('./header.txt', 'r').read()
footer = open('./footer.txt', 'r').read()
#print header
#print output
#print footer

f = open('./index.html', 'w')
f.write(header)
f.write(output)
f.write(footer)
f.close()
