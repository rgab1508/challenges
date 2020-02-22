
class ChloesNumber:
    def __init__(self, number):
        self._n = str(number)
        self._len = len(self._n)

    def check_threes(self):
        print("CHECKIGN 3S")
        for i in range(self._len - 2):
            print(self._n[i:i+3], end="")
            s = sum(list(map(lambda x: int(x) , self._n[i:i+3])))
            print(f" {s}")
            if not self.check_prime(int(s)):
                return False

        return True


    def check_fours(self):
        print("CHECKING 4s")
        for i in range(self._len - 3):
            print(self._n[i:i+4],end="")
            s = sum(list(map(lambda x: int(x) , self._n[i:i+4])))
            print(f" {s}")
            if not self.check_prime(s):
                return False

        return True

    def check_fives(self):
        print("CHECKING 5s")
        for i in range(self._len - 4):
            print(self._n[i:i+5],end="")
            s = sum(list(map(lambda x: int(x) , self._n[i:i+5])))
            print(f" {s}")
            if not self.check_prime(s):
                return False
    
        return True

    def check_prime(self, n):
        for i in range(2, n):
            if (n % i) == 0:
                return False
        
        return True

    def is_choles_number(self):
        if(self.check_threes() and self.check_fours() and self.check_fives()):
            return True
        return False

c = ChloesNumber(101100)
print(c.is_choles_number())