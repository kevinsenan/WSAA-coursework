#
#
#

import requests
import csv
from xml.dom.minidom import parseString

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)
#to check it works, outputs to console, delete or comment it out  when you know it works
#print (doc.toprettyxml())

#to store the details in a file, comment out later if you want
#with open("traindetails.xml","w") as xmlfp:
#       doc.writexml(xmlfp)

retrieveTags=['TrainStatus', 'TrainLatitude', 'TrainLongitude', 'TrainCode', 'TrainDate', 'PublicMessage', 'Direction']

#Modify the program to print out each of the trainscodes. I.e. find the listings and 
# iterate through them to print each traincode out
objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
for objTrainPositionsNode in objTrainPositionsNodes:
    traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
    traincode = traincodenode.firstChild.nodeValue.strip()
    trainlatitudenode = objTrainPositionsNode.getElementsByTagName("TrainLatitude").item(0)
    trainlatitudecode = trainlatitudenode.firstChild.nodeValue.strip()
    #print (traincode, trainlatitudecode)


dataList = []
for retrieveTag in retrieveTags:
    datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
    dataList.append(datanode.firstChild.nodeValue.strip())



with open("week03_train.csv", mode='w', newline='') as train_file:
        train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        train_writer.writerow(dataList)

        objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
        for objTrainPositionsNode in objTrainPositionsNodes:
                traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
                traincode = traincodenode.firstChild.nodeValue.strip()

