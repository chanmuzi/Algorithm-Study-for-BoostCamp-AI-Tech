import sys

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    applicants = []
    for j in range(n):
        paper,interview = map(int,sys.stdin.readline().rstrip().split())
        applicants.append([paper,interview])
    
    applicants.sort()
    
    present = applicants[0][1]
    count= 0 
    for j in range(1,n):
        if present > applicants[j][1]:
            count += 1
            present = applicants[j][1]
        
    print(count+1)