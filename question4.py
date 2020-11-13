f=open("question4.txt")
f1=open("delhi.txt","w")
f2=open("shimla.txt","w")
f3=open("other.txt","w")
for data in f:
    if "delhi" in data:
        f1.write(data)
    elif "shimla" in data:
        f2.write(data)
    else:
        f3.write(data)
