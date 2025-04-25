function countLargestGroup(n: number): number {
    let hashmap = new Map();
    for (let i = 1; i<=n; i++){
        let sumOfDigits = 0;
        let j = i;
        while (j!=0){
            sumOfDigits += j%10;
            j = Math.floor(j/10);
        }
        if (hashmap.has(sumOfDigits))
            hashmap.set(sumOfDigits, hashmap.get(sumOfDigits)+1);
        else
            hashmap.set(sumOfDigits, 1);
    }
    // console.log(hashmap)
    let largestSize = Math.max(...hashmap.values());
    let groupsWithLargestSize = 0;
    
    for (const [sumDigits, size] of hashmap){
        if (size == largestSize)
            groupsWithLargestSize += 1
    }


    return groupsWithLargestSize;
};