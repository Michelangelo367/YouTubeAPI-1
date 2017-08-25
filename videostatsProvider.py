import requests
import csv
import json
API_KEY = "AIzaSyBe0YoSucvgHHzzqROCXobxvf11wBoYIv4"

ipfilefd = open('videoandchannelidbulk.csv', 'r')
filb = csv.DictReader(ipfilefd)

headings = ('videoId', 'publishedAt','viewCount','likeCount','dislikeCount','commentCount')
csvfilefd = open('videoStats.csv', 'w')
fileBridge = csv.DictWriter(csvfilefd,headings)
fileBridge.writeheader()
i = 0
for lolcats in filb:
        base_url = "https://www.googleapis.com/youtube/v3/videos?key=AIzaSyBe0YoSucvgHHzzqROCXobxvf11wBoYIv4&id="+\
                   lolcats['videoId']+"&part=snippet,statistics"
        datadict = {}

        r = requests.get(url=base_url)
        strings = r.json()
        strings.keys()
        #print(strings.keys())
        #exit()
        if "items" in strings.keys():
            dataitems = strings["items"]
        else:
            continue
        #print(dataitems)



        for data in dataitems:
            datadict[headings[0]] = lolcats['videoId']

            if 'publishedAt' in data['snippet'].keys():
                datadict[headings[1]] = data['snippet'][headings[1]]

            if 'viewCount' in data['statistics'].keys():
                datadict[headings[2]] = data['statistics'][headings[2]]
            else:
                datadict[headings[2]] = -1

            if 'likeCount' in data['statistics'].keys():
                datadict[headings[3]] = data['statistics'][headings[3]]
            else:
                datadict[headings[3]] = -1

            if 'dislikeCount' in data['statistics'].keys():
                datadict[headings[4]] = data['statistics'][headings[4]]
            else:
                datadict[headings[4]] = -1

            if 'commentCount' in data['statistics'].keys():
                datadict[headings[5]]=data['statistics'][headings[5]]
            else:
                datadict[headings[5]] = -1
            i = i+1
            print("done",i)
            fileBridge.writerow(datadict)



print(strings.keys())


print(base_url)
print("Hello World")