def compressString(input:str) -> str:
    # problem: compress string by adding count to repeated characters, eg. input=aabcccccaaa output=a2b1c5a3
    # solution: two pointer, left as pivot and right pointer counts number of repeated, then append to result
    # time: O(n), space: O(n)
    left, right = 0, 0
    result = []
    while left < len(input) and right < len(input):
        while right < len(input) and input[left] == input[right]:
            right+=1
        result.append(input[left])
        result.append(str(right-left))
        left = right
    
    return ''.join(result)

def test(input:str, expected:str):
    print(f"Input: {input}, Output: {compressString(input)}, Expected: {expected}")


test("aabcccccaaa", "a2b1c5a3")
test("Jaameees", "J1a2m1e3s1")