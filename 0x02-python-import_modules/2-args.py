#!/usr/bin/python3
def print_arg(argv):
    n = len(argv) - 1
    if n == 0:
        print("{:a} argument.".format(n))
        return
    else:
        if n == 1:
            print("{:a} argument:".format(n))
        else:
            print("{:a} arguments:".format(n))
        i = 1
        while i <= n:
            print("{:a}: {:c}".format(i, argv[i]))
            i += 1

if __name__ == "__main__":
    import sys
    print_arg(sys.argv)
