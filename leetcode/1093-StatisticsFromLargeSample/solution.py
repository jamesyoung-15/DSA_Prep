from typing import List

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        minimum = 10e9 # minimum number
        maximum = 0 # maximum number
        mode = (0,0) # stored with (number, count)
        running_sum = 0 # for mean calc
        num_nonzeros = 0 # for mean calc
        total_count = 0 # sum the count, for finding median
        samples = [] # create a list of samples that stores (number, count)

        for number, num_count in enumerate(count):
            # if count is 0, skip
            if num_count == 0:
                continue
            # if non-zero count number is smaller than min, update min
            if number<minimum:
                minimum = number
            # if non-zero count number is larger than max, update max
            elif number>maximum:
                maximum = number
            # if the count is greater than current mode, update mode
            if num_count>mode[1]:
                mode = (number,num_count)
            # update total count, sample list, sum, and number of non zero count numbers
            total_count += num_count
            samples.append((number,num_count))
            running_sum += number * num_count
            num_nonzeros += num_count
        
        # calculate mean
        mean = running_sum/num_nonzeros
        
        # calculate median
        # find middle index by taking sum of counts and divide by 2, then go through samples tuple list and subtract middle index by the count until middle index is <=0
        # if middle index is 0, then we take the next number in sample, otherwise we return the number
        median = 0
        middle = total_count//2 # this represents the middle index of the sample
        for i in range(len(samples)):
            middle -= samples[i][1]
            # if subtracting the count so far reached 0, then we know middle is the next number
            if middle==0:
                # if there are even numbers in sample, take average of the two middle
                if total_count%2==0:
                    median = (samples[i][0] + samples[i+1][0])/2
                else:
                    median = samples[i+1][0]
                break
            # if subtracting count so far has given us negative number, we know the number is the middle index
            elif middle<0:
                median = samples[i][0]
                break

        answer = [minimum, maximum, mean, median, mode[0]]
        return answer