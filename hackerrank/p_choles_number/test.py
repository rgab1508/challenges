def check_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    
    return True

def check_threes(n):
    ite = len(n)-2
    for i in range(ite):
        s = sum(list(map(lambda x: int(x) , n[i:i+3])))
        if not check_prime(s):
            return False

    return True


def check_fours(self):
    for i in range(self._len - 4):
        s = self._n[i:i+4]
        if not self.check_prime(int(s)):
            return False

    return True

def check_fives(self):
    for i in range(self._len - 5):
        s = self._n[i:i+5]
        if not self.check_prime(int(s)):
            return False

    return True


print(check_threes('283002'))