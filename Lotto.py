import random

def generate_lotto_numbers():
    # 1부터 45까지의 숫자 중에서 6개를 랜덤으로 추출하여 리스트로 반환합니다.
    lotto_numbers = random.sample(range(1, 46), 6)
    return sorted(lotto_numbers)

# 로또 번호 추천
recommended_numbers = generate_lotto_numbers()
print("로또 추천 번호:", recommended_numbers)
