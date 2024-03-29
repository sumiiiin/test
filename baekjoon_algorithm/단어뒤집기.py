# 문제
# 문장이 주어졌을 때, 단어를 모두 뒤집어서 출력하는 프로그램을 작성하시오. 단, 단어의 순서는 바꿀 수 없다. 단어는 영어 알파벳으로만 이루어져 있다.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있으며, 문장이 하나 주어진다. 단어의 길이는 최대 20, 문장의 길이는 최대 1000이다. 단어와 단어 사이에는 공백이 하나 있다.

# 출력
# 각 테스트 케이스에 대해서, 입력으로 주어진 문장의 단어를 모두 뒤집어 출력한다.

# 예제 입력
# 2
# I am happy today
# We want to win the first prize

# 예제 출력
# I ma yppah yadot
# eW tnaw ot niw eht tsrif ezirp

# 문장의 갯수를 입력 받는다

# 각 문장은 각 변수에 담는다? or 하나의 리스트에 담긴다?
# 문장을 띄어쓰기 단위로 쪼갠다 각 조각은 하나의 리스트에 들어간다.
# 리스트 인덱스를 이용하여 하나씩 불러 또 쪼갠다 list를 쓰면 된다.
# 초기화 한 문자열을 두고 거기에 거꾸로 된 순서로 추가한다.
# join으로 한 단어로 만든다. 다시 원 문장의 리스트에 넣는다.

# 각 요소마다 해줘야 하니 for문을 써야할것도 같음 개 복잡한데 이게 초급?

# 정답 돌려보니 한 줄 쓸 때마다 바로바로  나오네 ...문장
#     
# 2
# i am so sad 
# i ma os das
# i am happy
# i ma os das i ma yppah

import sys
N = int(input())

for _ in range(N):
    str = sys.stdin.readline().rstrip()
    words = list(str.split())
    reverse_words = []

    for word in words:
        reverse_words.append(word[::-1])

    answer = " ".join(reverse_words)
    print(answer)