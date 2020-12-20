temp = []
answer = False

for _ in range(9):
    temp.append(int(input()))

result = sum(temp)
temp.sort()

for i in range(9):

    if answer:
        break
    
    for j in range(i+1, 9):

        if result - temp[i] - temp[j] == 100:
            temp.pop(i)
            temp.pop(j-1)

            for k in temp:
                print(k)
                
            answer = True
            break
        
