"""
Repetitions
 
You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.
Input
The only input line contains a string of n characters.
Output
Print one integer: the length of the longest repetition.
Constraints

1 <= n <= 10^6

Example
Input:
ATTCGGGA

Output:
3

"""



def find_repetition(input_string: str):
    # find longest repetition
    prev_char = ''
    curr_count = 0
    max_count = 0
    for char in input_string:
        if char == prev_char:
            curr_count += 1
        else:
            curr_count = 1
            prev_char = char
        if curr_count > max_count:
            max_count = curr_count    
        
    print(max_count)


if __name__ == '__main__':
    input_string = input()
    find_repetition(input_string)