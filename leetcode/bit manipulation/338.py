class Solution:
    def countBits(self, n: int) -> list[int]:
        final_arr = []


        def num_of_1_bits(den_num):
            num = int(bin(den_num)[2:])

            res = 0

            while num:
                res += num % 2 

                print(bin(num), den_num)
                num >>= 1

            return res 

        for number in range(0, n):
            final_arr.append(num_of_1_bits(number))

        return final_arr


# print(Solution().countBits(5))

def num_of_1_bits(den_num):
            num = int(bin(den_num)[2:])

            res = 0

            while num:
                print(num, den_num, num % 2)
                res += num % 2 

                num >>= 1

            return res 

print(num_of_1_bits(2))