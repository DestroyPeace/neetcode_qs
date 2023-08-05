class Solution:
    def countBits(self, n: int) -> list[int]:
        final_arr = []


        def num_of_1_bits(den_num):
            num = int(bin(den_num)[2:])
            print(num)

            res = 0

            print("\nnew\n")
            while num:
                res += num % 2 
                print(f"{num} before")
                print("=======================")
                num >>= 1
                print(f"{num} after")

            return res 

        for number in range(1, n + 1):
            final_arr.append(num_of_1_bits(number))

        return final_arr

print(Solution().countBits(12))
            


