class TimeMap:

    def __init__(self):
        self.valueMap = {}
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.valueMap:
            val = self.valueMap[key]
            val[timestamp] = value
            self.timeMap[key].append(timestamp)
        else:
            self.valueMap[key] = {timestamp: value}
            self.timeMap[key] = [timestamp]
        

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.timeMap:
            return ""

        timestamps = self.timeMap[key]

        start = 0
        end = len(timestamps) - 1
        targetTimestamp = -1

        while start <= end:
            mid = (start + end) // 2
            cur = timestamps[mid]

            if cur == timestamp:
                targetTimestamp = timestamp
                break
            
            if cur < timestamp:
                targetTimestamp = cur
                start = mid + 1
            else:
                end = mid - 1
        
        if targetTimestamp == -1:
            return ""

        return self.valueMap[key][targetTimestamp]
