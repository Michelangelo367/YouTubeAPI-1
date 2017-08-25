import requests
import csv
import json
API_KEY = "AIzaSyBe0YoSucvgHHzzqROCXobxvf11wBoYIv4"

ipfilefd = open('videoandchannelidbulk.csv', 'r')
filb = csv.DictReader(ipfilefd)

headings = ('channelId', 'publishedAt','viewCount','subscriberCount','videoCount')
csvfilefd = open('channelStats.csv', 'w')
fileBridge = csv.DictWriter(csvfilefd,headings)
fileBridge.writeheader()

for lolcats in filb:
        base_url = "https://www.googleapis.com/youtube/v3/channels?key="+API_KEY+"&id="+\
                   lolcats['channelId']+"&part=snippet,statistics"
        datadict = {}

        r = requests.get(url=base_url)
        strings = r.json()
        strings.keys()
        #print(strings.keys())
        #exit()
        dataitems = strings["items"]
        #print(dataitems)


        for data in dataitems:
            datadict[headings[0]] = lolcats['channelId']

            if 'publishedAt' in data['snippet'].keys():
                datadict[headings[1]] = data['snippet'][headings[1]]

            if 'viewCount' in data['statistics'].keys():
                datadict[headings[2]] = data['statistics'][headings[2]]
            else:
                datadict[headings[2]] = -1

            if 'subscriberCount' in data['statistics'].keys():
                datadict[headings[3]] = data['statistics'][headings[3]]
            else:
                datadict[headings[3]] = -1

            if 'videoCount' in data['statistics'].keys():
                datadict[headings[4]] = data['statistics'][headings[4]]
            else:
                datadict[headings[4]] = -1

            fileBridge.writerow(datadict)



#print(strings.keys())
#print(data)
exit()
print(base_url)
print("Hello World")