lines=[line.strip() for line in open("level2_example.in")]

length=lines[1:int(lines[0])]
# print('lines being spit here ',length)

timestamps=[]
altitudes=[]
latitudes=[]
longitudes=[]
flightpoints=[]

for line in length:
    newlist=line.split(',')
    timestamps.append(int(newlist[0]))
    latitudes.append(float(newlist[1]))
    longitudes.append(float(newlist[2]))
    altitudes.append(float(newlist[3]))
    flightpoints.append(newlist[4:])


newalitudes=[int(a) for a in altitudes]

L=[]
for point in flightpoints:
    L.append(point[:2])


newoccuredlist=[]
print('printing L',L)
for occurence in L:
    a=L.count(occurence)
    newoccuredlist.append([*occurence,str(a)])

print('printing new occurence',newoccuredlist)

unique_occurence=[]

for item in newoccuredlist:
    if (item  not in unique_occurence):
         unique_occurence.append(item)

destructured_list=[]
for item in unique_occurence:
    # for a in item:
        destructured_list.append(' '.join(item))
    


print(len(destructured_list))
sortedclients=sorted(destructured_list)



     

f=open('level1_5.out','w+')


for item in sortedclients:
    print(item,file=f)


