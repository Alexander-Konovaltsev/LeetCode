class Solution:
    roman_num = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
    }
    
    def romanToInt(self, s: str) -> int:       
        sum = 0
        idx = 0

        while idx < len(s):
            union_flag = False

            current_roman_num = s[idx]
            next_roman_num = s[idx + 1] if (idx + 1) < len(s) else None
            
            current_num = self.roman_num[current_roman_num]
            next_num = self.roman_num[next_roman_num] if next_roman_num is not None else -1

            if next_roman_num is None:
                sum += current_num
                break

            if ((current_roman_num == 'I' and next_roman_num in ('V', 'X')) or 
            (current_roman_num == 'X' and next_roman_num in ('L', 'C')) or
            (current_roman_num == 'C' and next_roman_num in ('D', 'M'))):
                current_num = next_num - current_num
                union_flag = True

            sum += current_num

            idx += 1 if not union_flag else 2

        return sum

    
sol = Solution()

test_cases = ["III", "LVIII", "MCMXCIV"]

for case in test_cases:
    print(sol.romanToInt(case))
