f=open("file-question3.txt","a")
f=open("file-question3.txt","r")
print(f.read())
banks_list=["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
i=0
while i <len(banks_list):
    print(banks_list[i])
    i=i+1
f.close()
