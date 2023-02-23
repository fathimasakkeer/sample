import filecmp
a=open("file.txt","r")
s=a.read()
print (s)
b=open("file1.txt","w")
t=b.write(s)
b.close()
c=filecmp.cmp("file.txt","file1.txt")
print(c)
