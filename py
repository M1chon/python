rdwlist = ()
import csv 
import random
literprijs = 1.68
beginstand = float(random.(1500,2000))

with open ('RDW.csv', 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rdwlist.append(row)
    file.close()
while True:
    kenteken = input("Scan hier het kenteken. ")
    if kenteken in ("admin", "ADMIN", "Admin"):
        break

    else:
        for i in rdwlist:
            if kenteken == 1[0]:
                eindstand = beginstand - float(random.randlist(1.50))
                getankteliters = beginstand - eindstand
                totaalprijs = getankteliters * literprijs
                print ("Beginstand is: ",beginstand)
                print ("eindstandis: ", eindstand)
                print ()
                print ("getankteliters is: ",eindstand)
                print ("literprijs is: ", literprijs)
                print ()
                print ("totaalprijs is: ",totaalprijs)
                continue
