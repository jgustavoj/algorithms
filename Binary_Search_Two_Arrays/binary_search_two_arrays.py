def countPairs(n,a,m,b,k):
    a.sort()                # sort the first array in ascending order 
    b.sort(reverse=True)    # sort second array in descending order 
    i, j = 0, 0             # initialize pointers at the beginning of the arrays
    count = 0               # initialize count of pairs to 0
    while i < n and j <m:   # Loop until you reach end of array
        if a[i] + b[j] < k: # if sum is less than k
            count += (m-j)  # increase the count by the remaining number in second array
            i += 1          # Move pointer to the next element in first array 
        else:               # Move pointer on second array
            j += 1 
    return count


n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
    
m = int(input())
b = []
for i in range(m):
    b.append(int(input()))

k = int(input())

countPairs(n,a,m,b,k)
# print('Answer:', countPairs(n,a,m,b,k))
# countPairs(a = [1,2,3], b = [1,2], k =  4, n = 3, m = 2)