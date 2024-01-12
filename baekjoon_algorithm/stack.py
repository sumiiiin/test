l = []
import sys

# inputt = int(sys.stdin.readline())

# from six.moves import input as raw_input
def stack():
    n = int(sys.stdin.readline())
    for _ in range(n):
        a = str(n)
        ab = a.split(" ")
        
        if len(ab) > 1:
            c = int(ab[1])
            l.append(c)
            
        if len(ab) == 1:
            if ab[0] == "pop":
                if len(l) == 0:
                    print(-1)
                else:
                    l.pop()
       
        if len(ab) == 1:        
            if ab[0] == "size":
                print(len(l))
                
        if len(ab) == 1:      
            if ab[0] == "empty":
                if len(l) == 0:
                    print(1)
                else:
                    print(0)
        if len(ab) == 1:         
            if ab[0] == "top":
                if len(l) == 0:
                    print(-1)
                else:
                    print(l[0])
# print("hw")
stack()
