class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # greedy approach w/ 2 pointers
        # time: O(nlogn + mlogm), space: O(1)
        players.sort()
        trainers.sort()
        result = 0
        trainer_ptr = 0
        for player in players:
            while trainer_ptr < len(trainers) and player > trainers[trainer_ptr]: trainer_ptr+=1 

            if trainer_ptr < len(trainers) and player <= trainers[trainer_ptr]:
                result += 1
                trainer_ptr += 1




        return result