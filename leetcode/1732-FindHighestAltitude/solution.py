class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0] * (len(gain)+1)
        altitudes[1] = gain[0]

        # running sum
        for i in range(1,len(gain)):
            altitudes[i+1] = altitudes[i] + gain[i]
        return max(altitudes)