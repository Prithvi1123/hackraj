# hackraj
value1,value2=map(int,input().split())
l=list(map(int,input().split()))
result=1
for i in range(0,len(l)):
	for j in range(i+1,len(l)):
		m=l[i]+l[j]
		if m==value2:
			result=0
if result==0:
	print("yes")
else:
	print("no")
