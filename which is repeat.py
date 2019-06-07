# hackraj
y1=[]
y2=[]
b=0
n=int(input())
item=input().split()
for i in item:
  y1.append(int(i))
for i in range(0,n-1):
  b=0
  for j in range(i+1,n):
    if y1[i]==y1[j]:
      b=b+1
      break
  if b>=1 and y1[i] not in y2:
    y2.append(y1[i])
z=len(y2)
if z==0:
  print("unique")
else:
  for i in y2:
    print(i,end=" ")
