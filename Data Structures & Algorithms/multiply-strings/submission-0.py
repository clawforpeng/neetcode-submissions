class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def val(num: str) -> int:
            total = 0
            length = len(num)
            for i in range(length - 1, -1, -1):
                tmp = 0
                n = num[i]
                if n == "1":
                    tmp = 1
                elif n == "2":
                    tmp = 2
                elif n == "3":
                    tmp = 3
                elif n == "4":
                    tmp = 4
                elif n == "5":
                    tmp = 5
                elif n == "6":
                    tmp = 6
                elif n == "7":
                    tmp = 7
                elif n == "8":
                    tmp = 8
                elif n == "9":
                    tmp = 9
                else:
                    tmp = 0
                
                total += tmp * 10 ** (length - i - 1)
            
            return total
        
        mul = val(num1) * val(num2)

        return str(mul)

                