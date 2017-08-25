import requests
import csv
import json
API_KEY = "AIzaSyBe0YoSucvgHHzzqROCXobxvf11wBoYIv4"

nextPageToken = " "
#base_url = "https://www.googleapis.com/youtube/v3/search?key="+API_KEY+"&part=snippet&maxResults=50&q=shakira&type=video"

ipfilefd = open('query_string.csv', 'r')
filb = csv.reader(ipfilefd)

headings = ('videoId', 'channelId')
csvfilefd = open('videoandchannelidbulk.csv', 'w')
fileBridge = csv.DictWriter(csvfilefd,headings)
fileBridge.writeheader()

j = 0
for searchquery in filb:
    nextPageToken = " "
    for i in range(5):

        base_url = "https://www.googleapis.com/youtube/v3/search?key="+API_KEY+"&part=snippet&maxResults=50&" \
                                                        "q="+searchquery[0]+"&type=video&pageToken="+nextPageToken
        datadict = {}

        r = requests.get(url=base_url)
        strings = r.json()
        strings.keys()
        print(strings.keys())
        dataitems = strings["items"]

        #exit()

        for data in dataitems:
            if 'videoId' in data['id'].keys():
                datadict[headings[0]] = data['id'][headings[0]]
                print(data['id']['videoId'])
                j = j+1
            else:
                datadict[headings[0]] = "lolcats"
                print("Lolcats")

            if 'channelId' in data['snippet'].keys():
                datadict[headings[1]] = data['snippet'][headings[1]]
                print(data['snippet']['channelId'])
            else:
                datadict[headings[0]] = "lolcats"
                print("Lolcats")
            fileBridge.writerow(datadict)
        if "nextPageToken" in strings.keys():
            nextPageToken = strings["nextPageToken"]
        else:
            break


#print(strings.keys())
#print(data)
print(base_url)
print("The number of videos is ", j)
print("Hello World")