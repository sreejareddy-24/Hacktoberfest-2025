"""
Fenwick Tree (Binary Indexed Tree) Implementation in Python
Supports range sum queries and point updates.

Example:
arr = [1, 2, 3, 4, 5]
ft = FenwickTree(len(arr))
for i, val in enumerate(arr):
    ft.update(i, val)
print(ft.range_sum(1, 3))  # Output: 9 (2+3+4)

Author: Your Name
Hacktoberfest 2025 Contribution
"""
class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0]*(size+1)

    def update(self, index, value):
        index += 1
        while index <= self.size:
            self.tree[index] += value
            index += index & -index

    def query(self, index):
        index += 1
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res

    def range_sum(self, l, r):
        return self.query(r) - self.query(l-1)

# Example usage
arr = [1, 2, 3, 4, 5]
ft = FenwickTree(len(arr))
for i, val in enumerate(arr):
    ft.update(i, val)

print(ft.range_sum(1, 3))  # Output: 9 (2+3+4) 
