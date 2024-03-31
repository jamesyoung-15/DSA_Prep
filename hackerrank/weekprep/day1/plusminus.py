import math

""" 
Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with digits after the decimal. The function should not return a value. 

"""

def plusMinus(arr):
    # Write your code here
    zero_sum = 0
    positive_sum = 0
    negative_sum = 0
    # loop through array, sum up number of zeros, pos, neg
    for i in arr:
        if i == 0:
            zero_sum+=1
        elif i>0:
            positive_sum += 1
        elif i<0:
            negative_sum += 1
        else:
            raise Exception("Invalid number for some reason")
    
    # demoninator
    arr_length = len(arr)
    # if array is empty, print 0s
    if arr_length == 0:
        print("0")
        print("0")
        print("0")
    # otherwise print ratios
    else:
        print(positive_sum/arr_length)
        print(negative_sum/arr_length)
        print(zero_sum/arr_length)
    # print(element_dic)


if __name__ == '__main__':
    arr = [1,1,0,-1,-1]
    result = plusMinus(arr)