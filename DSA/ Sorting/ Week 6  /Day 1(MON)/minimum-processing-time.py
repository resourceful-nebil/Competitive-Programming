class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        ans = 0

        # Sort the processorTime list in ascending order
        processorTime.sort()
        
        # Sort the tasks list in descending order
        tasks.sort(reverse=True)
        
        # Iterate over each processor
        for i in range(len(processorTime)):
            # Calculate the processing time by adding the current processor time with the largest assigned task
            processing_time = processorTime[i] + tasks[i * 4]
            
            # Update the maximum processing time
            ans = max(ans, processing_time)

        # Return the maximum processing time
        return ans