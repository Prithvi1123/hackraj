# hackraj
x=int(input())
arr=[]
for i in range(0,x):  
    y=input()
    arr.append(y)
l=[]
for i in zip(*arr):
    if i.count(i[0])==len(i): 
        l.append(i[0])
    else:
        break
print(''.join(l))
