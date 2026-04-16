class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = []

        """
        Using some Python cheat codes, I will match each car with its
        position and speed. Then, I will sort the cars in descending order
        by their position.
        """
        cars = sorted(zip(position, speed), reverse=True)
        print(cars)

        for p, s in cars:
            time = (target - p) / s
            print(time)

            # Only executes on first loop
            if not times:
                times.append(time)
                continue
            
            print(times)
            if time > times[-1]:
                times.append(time)
        print(times)
        return len(times)