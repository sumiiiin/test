# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 다섯 가지이다.

# - push X: 정수 X를 스택에 넣는 연산이다.
# - pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# - size: 스택에 들어있는 정수의 개수를 출력한다.
# - empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# - top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

import sys

def stack():
    l = []
    n = int(sys.stdin.readline())
    
    for _ in range(n):
        ab = sys.stdin.readline().rstrip().split() # 문자열 그대로 가져오는데 엔터키(개행문자)도 그대로 가져와서 제거해줌

        # ab = x.split(" ")
        
        if ab[0] == "push":
            c = int(ab[1])
            l.append(c)
            
        elif ab[0] == "pop":
                if len(l) == 0:
                    print(-1)
                else:
                    print(l.pop())
       
        elif ab[0] == "size":
                print(len(l))
                
        elif ab[0] == "empty":
                if len(l) == 0:
                    print(1)
                else:
                    print(0)
        elif ab[0] == "top":
                if len(l) == 0:
                    print(-1)
                else:
                    print(l[-1])
stack()
# 다른 답 보면 각 기능을 함수화 했던데 그렇게도 해봐야겠다.
# input 말고 raw_input이랑 sys.stdin.readline이 처리속도가 더 빠르다는데 난 왜 안될까? 무한 로딩임 ipynb라 그런가?
# 남의 답도 내 컴퓨터에선 무한 로딩이다.
