class Robot:
    def __init__(self, width: int, height: int):
        self.width = width  # Initialize the width of the grid
        self.height = height  # Initialize the height of the grid
        self.direction = "East"  # Initialize the direction of the robot to "East"
        self.position = [0, 0]  # Initialize the starting position of the robot to [0, 0]

    def step(self, num: int) -> None:
        calculation = (2 * self.width) + (2 * self.height) - 4  # Calculate the total steps for a full loop around the grid
        num = num % calculation  # Adjust num to be within a single loop around the grid

        for i in range(num):  # Iterate 'num' times
            # Check the current position of the robot and update the direction accordingly
            if self.position == [0, 0]:
                self.direction = "East"
            elif self.position == [self.width - 1, 0]:
                self.direction = "North"
            elif self.position == [self.width - 1, self.height - 1]:
                self.direction = "West"
            elif self.position == [0, self.height - 1]:
                self.direction = "South"

            # Update the position of the robot based on the current direction
            if self.direction == "East":
                self.position[0] += 1
            elif self.direction == "West":
                self.position[0] -= 1
            elif self.direction == "North":
                self.position[1] += 1
            elif self.direction == "South":
                self.position[1] -= 1

        if self.position == [0, 0]:
            self.direction = "South"  # Special case: when the robot reaches the starting position, change the direction to "South"

    def getPos(self) -> List[int]:
        return self.position  # Return the current position of the robot as a list of two integers

    def getDir(self) -> str:
        return self.direction  # Return the current direction of the robot as a string
    

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()