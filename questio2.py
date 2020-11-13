# f=open("data.text")
# count=0
# while count<=len(f):
#     count+=1
# print(count)
# f.close()


f=open("data.text")
count=0
for i in f:
    count+=1
print(count)
f.close()