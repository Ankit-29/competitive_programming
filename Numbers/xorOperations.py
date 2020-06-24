def xorOperation(self, n: int, start: int) -> int:
    res = start
    for i in range(1, n):
        temp = start + 2*i
        res ^= temp
    return res
