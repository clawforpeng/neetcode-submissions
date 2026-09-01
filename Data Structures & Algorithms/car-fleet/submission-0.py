class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 1
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        
        cars.sort()

        time = (target - cars[-1][0]) / cars[-1][1]
        goalCar = cars[-1]

        for i in range(len(cars) - 2, -1, -1):
            speed = cars[i][1]
            pos = cars[i][0]
            if speed <= goalCar[1]:
                fleets += 1
                time = (target - pos) / speed
                goalCar = cars[i]
            else:
                distance = goalCar[0] - pos
                speedDif = speed - goalCar[1]

                if distance / speedDif > time:
                    fleets += 1
                    time = (target - pos) / speed
                    goalCar = cars[i]

        return fleets