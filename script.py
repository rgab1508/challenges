import os
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("--name", "-n", type=str, required=True, help="Name of the folder")
parser.add_argument("--path", "-p", type=str, default=".", help="Path of the folder(default current)")
parser.add_argument("--sub", "-s", type=int, default=5, help="No. of problems")
parser.add_argument("--inputs", "-i", type=int, default=0, help="No. of input files")


def main(args):
    os.chdir(args.path)
    os.mkdir(args.name)
    os.chdir(args.name)

    al = 65
    for i in range(args.sub):
        os.mkdir(chr(al))
        os.chdir(chr(al))
        f = open("soln.py", "w")
        _al = 97
        if args.inputs > 0:
            os.mkdir("inputs")
            os.chdir("inputs")
            for i in range(args.inputs):
                _f = open(f"{chr(_al)}.in", "w")
                _f.close()
                _al+= 1
            os.chdir("..")
        else:
            f1 = open("a.in", "w")
            f1.close()
        f.close()
        os.chdir("..")
        al += 1


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)