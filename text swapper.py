a=open("text1.txt","r")
data2=a.read()
    



b=open("text2.txt","r")
data1=b.read()
    
with open("text1.txt","w") as y:
    y.write(data1)


with open("text2.txt","w") as z:
    z.write(data2)
