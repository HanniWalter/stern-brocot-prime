import numpy as np
MAXSEQ =1000000

stern_brocot_sequenz = np.empty((MAXSEQ),dtype = int)
stern_brocot_sequenz[0]=0
stern_brocot_sequenz[1]=1
nonedivList = np.zeros((MAXSEQ),dtype = int)

for i in range(2,MAXSEQ):
	if i % 2 ==0:
		stern_brocot_sequenz[i] = stern_brocot_sequenz[int(i/2)]
	else:
		stern_brocot_sequenz[i] = stern_brocot_sequenz[int((i-1)/2)]+stern_brocot_sequenz[int((i+1)/2)]
	if stern_brocot_sequenz[i]<stern_brocot_sequenz[i-1]:
		nonedivList[stern_brocot_sequenz[i-1]] +=1

for i in range(int(MAXSEQ/10)):
	if i<2:
		continue
	if i == nonedivList[i]+1:
		print (i)
