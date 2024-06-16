"""  



Ex: a = [2,3,5,1,4]

Permuted array is [1,4,5,3,2]

"""


"""  
[1,2,3,4,5] -> [1,2,3,5,4]

"""
def findZigZagSequence(a, n):
    a.sort()
    mid = int((n - 1)/2) # change from n + 1 to n-1, n+1 is not mid
    a[mid], a[n-1] = a[n-1], a[mid]
    print(a)

    st = mid + 1
    ed = n - 2 # change from n-1 to n-2 so that change is correct
    while(st <= ed):
        print(st, ed)
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1 # change from ed + 1 to ed - 1 to fix out of bound error

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = [1, 2, 3, 4, 5, 6, 7]
n = len(test_cases)
findZigZagSequence(test_cases, n)

