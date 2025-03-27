class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        def dfs(tiles_cnt:Counter):
            result = 0
            for character, count in tiles_cnt.items():
                if count>0:
                    result+=1
                    tiles_cnt[character] -= 1
                    result+=dfs(tiles_cnt)
                    tiles_cnt[character] += 1
            return result


        tiles_cnt = Counter(tiles)
        return dfs(tiles_cnt)