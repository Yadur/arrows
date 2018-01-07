# countdown module
import time

def countdown(n):
    print 'Ready???'
    while n > 0:
        print n
        time.sleep(1)
        n = n - 1
        if n == 0:
            print 'GO!!!!!'

"""
useful to use the module
in command line to test
ex : python 'module' 'arg'
"""

if __name__=="__main__":
    import sys
    countdown(int(sys.argv[1]))
