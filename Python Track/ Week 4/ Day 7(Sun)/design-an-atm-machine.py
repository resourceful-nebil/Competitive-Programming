class ATM:
    def __init__(self):
        # Initialize available banknote denominations and their count
        self.banknotes = [20, 50, 100, 200, 500]
        self.bank = [0] * 5  # Initially, no banknotes are available

    def deposit(self, banknotesCount: List[int]) -> None:
        # Increment the count of each banknote denomination by the specified count
        for i in range(5):
            self.bank[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        withdrew = [0] * 5  # List to track withdrawn banknotes of each denomination

        # Loop through banknote denominations from largest to smallest
        for i in reversed(range(5)):
            # Determine the maximum number of banknotes that can be withdrawn
            withdrew[i] = min(self.bank[i], amount // self.banknotes[i])
            amount -= withdrew[i] * self.banknotes[i]  # Update the remaining amount

        # If there's remaining amount, the withdrawal is not possible
        if amount:
            return [-1]

        # Update the count of banknotes after successful withdrawal
        for i in range(5):
            self.bank[i] -= withdrew[i]

        return withdrew  # Return the withdrawn banknotes

        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)