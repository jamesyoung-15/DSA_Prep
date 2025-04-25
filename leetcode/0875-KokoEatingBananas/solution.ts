function minEatingSpeed(piles: number[], h: number): number {
    let min_k = 1, max_k = Math.max(...piles);
    let result = 0;
    
    while (min_k <= max_k){
        let candidate_k = min_k + Math.floor((max_k-min_k)/2)
        let time_taken = 0;
        for (let pile of piles){
            time_taken += Math.ceil(pile/candidate_k);
        }
        if (time_taken>h){
            min_k = candidate_k + 1
        }
        else{
            max_k = candidate_k - 1
            result = candidate_k
        }

    }


    return result
};t