"""
Given an array of integers, where all elements but one occur twice, find the unique element. 

Ex: 
a = [1,2,3,4,3,2,1]

Unique element is 4.

"""



def lonelyinteger(a):
    # Write your code here

    # Overall approach is to store elements in dictionary, then if dictionary value is 1, then it is unique
      
    # hashmap variable
    element_hashmap = {}

    # loop through array, populate hashmap
    for number in a:
        # if it already exists in hashmap, increment occurence
        if number in element_hashmap:
            element_hashmap[number] += 1
        # otherwise add it to dictionary
        else:
            element_hashmap[number] = 1
    
    # check
    # print(element_hashmap)

    # go through hashmap, check for unique element
    for key, value in element_hashmap.items():
        if value == 1:
            return key
    # shouldn't reach here
    return 0


if __name__=="__main__":
    arr = [1,2,3,4,3,2,1]
    print(lonelyinteger(arr))
