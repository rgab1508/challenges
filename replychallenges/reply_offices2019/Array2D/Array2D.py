
class Array2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self.arr = []
        for i in range(x):
            __ = [0 for j in range(y)]
            self.arr.append(__)


        
    def pprint(self):
        for i in range(self.x):
            for j in range(self.y):
                print(self.arr[i][j], end="")
            print("\n", end="")

    
    def steps_from(self,a: list, b: list):
        """
            a-> array of [x, y] where (x,y) are coords
            b-> array of [x1, y1] where (x1,y1) are coords

            return a string of steps to take from a to get to b
            UP    -> U
            DOWN  -> D
            RIGHT -> R
            LEFT  -> L
        """
        steps = ""
        if a[0] > b[0]:
            while a[0] != b[0]:
                a[0] -= 1
                steps += "L"
        if a[0] < b[0]:
            while a[0] != b[0]:
                a[0] += 1
                steps += "R"
        if a[1] > b[1]:
            while a[1] != b[1]:
                a[1] -= 1
                steps += "U"
        if a[1] < b[1]:
            while a[1] != b[1]:
                a[1] += 1
                steps += "D"

        return steps

    @staticmethod
    def no_of_steps_from(a: list, b: list):
        steps = 0
        if a[0] > b[0]:
            while a[0] != b[0]:
                a[0] -= 1
                steps += 1
        if a[0] < b[0]:
            while a[0] != b[0]:
                a[0] += 1
                steps += 1
        if a[1] > b[1]:
            while a[1] != b[1]:
                a[1] -= 1
                steps += 1
        if a[1] < b[1]:
            while a[1] != b[1]:
                a[1] += 1
                steps += 1

        return steps




def _test():
    m = Array2D(4, 4)
    steps = m.steps_from([0, 0], [3, 2])
    nsteps = Array2D.no_of_steps_from([0,0], [3,2])
    print(steps)
    print(nsteps)

if __name__ == "__main__":
    _test()