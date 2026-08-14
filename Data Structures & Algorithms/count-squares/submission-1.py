class CountSquares:

    def __init__(self):
        self.xAxis = {}
        self.yAxis = {}
        self.xy = {}

    def add(self, point: List[int]) -> None:
        x, y = point[0], point[1]
        if x in self.xAxis:
            self.xAxis[x].append(y)
        else:
            self.xAxis[x] = [y]
        
        if y in self.yAxis:
            self.yAxis[y].append(x)
        else:
            self.yAxis[y] = [x]

    def count(self, point: List[int]) -> int:
        x, y = point[0], point[1]

        if not x in self.xAxis or not y in self.yAxis:
            return 0
        
        count = 0

        for xx in self.yAxis[y]:
            length = abs(x - xx)
            if length == 0:
                continue

            for yy in self.xAxis[x]:
                if abs(yy - y) == length:
                    for yyy in self.xAxis[xx]:
                        if yyy == yy:
                            count += 1
        
        return count
