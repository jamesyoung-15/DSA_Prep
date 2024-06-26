""" 
Challenge:
Given a list of integers, count and return the number of times each value appears as an array of integers.

Note
For this exercise, always return a frequency array with 100 elements. The example above shows only the first 4 elements, the remainder being zeros. 

Ex:
63 25 73 1 98 73 56 84 86 57 16 83 8 25 81 56 9 53 98 67 99 12 83 89 80 91 39 86 76 85 74 39 25 90 59 10 94 32 44 3 89 30 27 79 46 96 27 32 18 21 92 69 81 40 40 34 68 78 24 87 42 69 23 41 78 22 6 90 99 89 50 30 20 1 43 3 70 95 33 46 44 9 69 48 33 60 65 16 82 67 61 32 21 79 75 75 13 87 70 33  

Return:
0 2 0 2 0 0 1 0 1 2 1 0 1 1 0 0 2 0 1 0 1 2 1 1 1 3 0 2 0 0 2 0 3 3 1 0 0 0 0 2 2 1 1 1 2 0 2 0 1 0 1 0 0 1 0 0 2 1 0 1 1 1 0 1 0 1 0 2 1 3 2 0 0 2 1 2 1 0 2 2 1 2 1 2 1 1 2 2 0 3 2 1 1 0 1 1 1 0 2 2 

"""

def countingSort(arr):
    # Write your code here
    
    # first create frequency array, populate with 100 0s as specified in challenge notes
    freq_arr = [0 for i in range(100)]
    # update frequency array, should just be able to increment by index
    for i in arr:
        if i<100:
            freq_arr[i] += 1
    

    return freq_arr

if __name__ == "__main__":
    arr= [63,25,73,1,98,73,56,84,86,57,16,83,8,25,81,56,9,53,98,67,99,12,83,89,80,91,39,86,76,85,74,39,25,90,59,10,94,32,44,3,89,30,27,79,46,96,27,32,18,21,92,69,81,40,40,34,68,78,24,87,42,69,23,41,78,22,6,90,99,89,50,30,20,1,43,3,70,95,33,46,44,9,69,48,33,60,65,16,82,67,61,32,21,79,75,75,13,87,70,33]
    print(countingSort(arr))
    # print(len(arr))
    # result = [0,2,0,2,0,0,1,0,1,2,1,0,1,1,0,0,2,0,1,0,1,2,1,1,1,3,0,2,0,0,2,0,3,3,1,0,0,0,0,2,2,1,1,1,2,0,2,0,1,0,1,0,0,1,0,0,2,1,0,1,1,1,0,1,0,1,0,2,1,3,2,0,0,2,1,2,1,0,2,2,1,2,1,2,1,1,2,2,0,3,2,1,1,0,1,1,1,0,2,2]
    # print(len(result))
