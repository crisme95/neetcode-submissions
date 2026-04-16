class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        dec = []
        output = [0] * len(temperatures)

        for i in range(len(temperatures)):
            if not dec or temperatures[i] <= temperatures[dec[-1]]:
                dec.append(i)
            else:
                while(dec and temperatures[dec[-1]] < temperatures[i]):
                    output[dec[-1]] = i - dec[-1]
                    dec.pop()
                dec.append(i)
        
        return output
