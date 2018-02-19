filek = open("ziad 0.txt").read()
x=0.0
y=len(filek)
for a in range (0,y):
    if (filek[a]=="C"):
        x=x+1
    elif (filek[a]=="G"):
        x=x+1
z=(x/y)*100
print z




