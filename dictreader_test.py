import csv
ipfilefd = open('videoandchannelidbulk.csv', 'r')
filb = csv.reader(ipfilefd)

for videoId in filb:
        print(videoId[0]