class FrequencyTracker:

    def __init__(self):
        # to store data and there frequency
        self.freq = defaultdict(int)
        # to store frequecy and there occurance
        self.freq_of_freq = defaultdict(int)

    def add(self, number: int) -> None:
        # to reduce the previous occurance by one 
        self.freq_of_freq[self.freq[number]] -= 1
        # add the number's frequency
        self.freq[number]+=1
        # to change it's occurance
        self.freq_of_freq[self.freq[number]] += 1

        

    def deleteOne(self, number: int) -> None:
        # to delete if the frequecy is > 0 , to reduce it's previous occurance, redce that number from freq hashmap and change it's occurance 
        if self.freq[number] >0:
            self.freq_of_freq[self.freq[number]]-=1
            self.freq[number]-=1
            self.freq_of_freq[self.freq[number]]+=1

        

    def hasFrequency(self, frequency: int) -> bool:
        # check if the frequecy is in the freq hashmap and occurance > 0
        if frequency in self.freq_of_freq and self.freq_of_freq[frequency]>0:
            return True
        return False
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)