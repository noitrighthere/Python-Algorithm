burger = [] # 햄버거
soda = []   # 음료

for _ in range(3):
    temp = int(input())
    burger.append(temp)

for _ in range(2):
    temp = int(input())
    soda.append(temp)

# 세트가격 = (햄버거 + 음료 - 50)
print(min(burger) + min(soda) - 50)
