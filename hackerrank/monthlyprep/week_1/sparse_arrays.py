def matchingStrings(strings, queries):
    hash_map = {}
    output = []
    for string in strings:
        if string in hash_map:
            hash_map[string] += 1
        else:
            hash_map[string] = 1
    
    for query in queries:
        if query in hash_map:
            output.append(hash_map[query])
        else:
            output.append(0)
    return output

if __name__ == '__main__':
    strings = ['ab', 'ab', 'abc']
    queries = ['ab', 'abc', 'ab']
    output = matchingStrings(strings, queries)
    print(output)