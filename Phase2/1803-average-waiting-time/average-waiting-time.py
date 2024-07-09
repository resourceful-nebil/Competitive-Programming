class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_waiting_time = current_time = 0
      
        for arrival_time, service_time in customers:
            current_time = max(current_time, arrival_time)
          
            current_time += service_time
          
            waiting_time = current_time - arrival_time
            total_waiting_time += waiting_time
      
        average_waiting_time = total_waiting_time / len(customers)
      
        return average_waiting_time