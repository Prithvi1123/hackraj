# hackraj
y1=[]
z=int(input())
r=0
num=input().split()
for i in num:
  if r<z:
    y1.append(int(i))
    r+=1
y1.sort(reverse=True)
z1=0
for i in y1:
  z1=(z1*10)+i
print(z1)
