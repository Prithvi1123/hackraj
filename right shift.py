b1,a = map(int,input().split())
a = a%b1
l1 = list(map(int,input().split()))
l2 = l1[-a:] + l1[:-a]
print(*l2)
