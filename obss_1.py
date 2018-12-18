def IsSorted(A):
    error = 0;
    statement = True;
    
    for i in range(len(A)-1):
        if(A[i] <= A[i+1]):
           continue;
        else:
           error += 1;
    if(error >= 2):
       return 0;
    elif(error == 0):
       statement = True;
       return statement;
    else:
       count = find(A);
       return count;
    
def find(A):
    count = 0;
    for i in range(len(A)-1):
        tmp = [x for x in A if x != A[i]];
        if(IsSorted(tmp) == True):
            count += 1;
    return count;
