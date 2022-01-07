import sys
# 명령행 인자는 한글 안됨.


def add(*args):
    return sum(args)


file_path = sys.argv[1]


for arg in sys.argv:
    print(arg)

if len(sys.argv) < 2:
    print("insufficient arguments")
    sys.exit()

print(add(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
