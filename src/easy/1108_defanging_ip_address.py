"""
1108. Defanging an IP Address
https://leetcode.com/problems/defanging-an-ip-address/
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


solution = Solution()

# Пример 1
test1 = "1.1.1.1"
result1 = solution.defangIPaddr(test1)
print(f"Пример 1: {test1} → {result1}")

# Пример 2
test2 = "255.100.50.0"
result2 = solution.defangIPaddr(test2)
print(f"Пример 2: {test2} → {result2}")
