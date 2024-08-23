class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.spaces = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.spaces[0] > 0:
                self.spaces[0] = self.spaces[0] - 1
                return True
            
        elif carType == 2:
            if self.spaces[1] > 0:
                self.spaces[1] = self.spaces[1] - 1
                return True
        elif carType == 3:
            if self.spaces[2] > 0:
                self.spaces[2] = self.spaces[2] - 1
                return True
        else:
            return False

        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

if __name__ == "__main__":
    # Initialize the parking system with 1 big, 1 medium, and 1 small space
    obj = ParkingSystem(1, 1, 1)
    
    # Try to park cars of different types
    print(obj.addCar(1))  # True, as there is 1 big space available
    print(obj.addCar(1))  # False, as the big space is now occupied
    print(obj.addCar(2))  # True, as there is 1 medium space available
    print(obj.addCar(3))  # True, as there is 1 small space available
    print(obj.addCar(3))  # False, as the small space is now occupied