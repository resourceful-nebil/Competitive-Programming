class UndergroundSystem:

    def __init__(self):
        # maps id -> (starting_station,time) 
        self.check_ins = {}
        # maps key = (start_station,end_station) -> time  
        self.travel_times = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # appends values to check_ins hashmap
        self.check_ins[id] = (stationName,t)


    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # takes details from check_ins and calculates time and gives key to travel_times hashmap
        start_station , start_time = self.check_ins[id]
        time = t - start_time
        key = (start_station,stationName)

        # adds an empty list to the key if not found 
        if key not in self.travel_times:
            self.travel_times[key] = []

        # adds time to travels time hash map
        self.travel_times[key].append(time)


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # takes key of travels_time ,gets the time and calculate its avaerage 
        key = (startStation,endStation)
        time = self.travel_times[key]
        return sum(time)/len(time)



# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)