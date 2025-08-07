def urlify(url:str) -> str:
    # problem: given string replace spaces between characters with "%20", use fixed array
    # my solution: count number of spaces we need to replace (eg. between characters), 
    # use that and length of input to create resulting array and replace spaces
    # time: O(n), space: O(n)
    num_space_between_char = 0
    i = len(url) - 1
    j = 0
    # trim front and back spaces
    while i >= 0 and url[i] == " ":
        i -= 1
    while j < len(url) and url[j] == " ":
        j+=1

    # count number of spaces
    while i >= 0:
        if i <= j:
            break
        if url[i] == " ":
            num_space_between_char += 1
        i-=1

    if num_space_between_char == 0:
        return url
    
    # add spaces to new char array, join char array to result string
    total_length = (num_space_between_char)*2 + len(url)
    new_url = [""] * total_length
    index = 0
    num_space_seen = 0
    for idx, char in enumerate(url):
        if char!= " ":
            new_url[index] = char
            index+=1
        elif char == " " and num_space_seen < num_space_between_char and idx!=0:
            num_space_seen += 1
            new_url[index] = "%"
            index+=1
            new_url[index] = "2"
            index+=1
            new_url[index] = "0"
            index+=1

    return ''.join(new_url)



def testCase(url:str, expected:str):
    print(f"Input: {url}, Got {urlify(url)}, expected: {expected}")


test_str1 = "Mr John Smith   "
expected1 = "Mr%20John%20Smith"
test_str2 = " James Young "
expected2 = "James%20Young"
test_str3 = "asd  asdf"
expected3 = "asd%20%20asdf"

testCase(test_str1, expected1)
testCase(test_str2, expected2)
testCase(test_str3, expected3)