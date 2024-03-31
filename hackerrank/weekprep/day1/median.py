"""
Mock test: Find median of array, will always be odd sized

Ex: [1, 0, 2, 3, 4]

Since sorted array is [0,1,2,3,4], the median is the middle element which is 2.

Return: 2


"""


def median(arr):
    """ Find the median """    
    sorted_array = sorted(arr)
    middle_index = len(arr) - int(len(arr)/2)
    median = sorted_array[middle_index - 1]
    return median

if __name__ == '__main__':
    arr = [1, 0, 2, 3, 4]
    print(median(arr))