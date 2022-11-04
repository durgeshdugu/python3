list=[1,0,3,0,12]   #list=[1,3,12,0,0] output want
#next=0
pre=0
for i in range(0,len(list)): 
	if list[i]!=0:
		hold=list[pre]
		list[pre]=list[i]
		list[i]=hold
		pre=pre+1
	print(list)
