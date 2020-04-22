lines=[line.strip() for line in open("level1_5.in")]

length=lines[1:]
# print('lines being spit here ',length)

timestamps=[]
altitudes=[]
latitudes=[]
longitudes=[]

for line in length:
    newlist=line.split(',')
    timestamps.append(int(newlist[0]))
    latitudes.append(float(newlist[1]))
    longitudes.append(float(newlist[2]))
    altitudes.append(float(newlist[3]))


newalitudes=[int(a) for a in altitudes]
print(longitudes)

f=open('level1_5.out','w+')
print(f"{min(timestamps)} {max(timestamps)}" ,file=f)
print(f"{min(latitudes)} {max(latitudes)}" ,file=f)
print(f"{min(longitudes)} {max(longitudes)}" ,file=f)
print(f"{float(max(newalitudes))}" ,file=f)

mylist=lines[0].split()
i=int(mylist[0])+1
# j=int(mylist[1])+1