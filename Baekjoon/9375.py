T = int(input())

for _ in range(T):
    n = int(input())
    wears = {}
    for i in range(n):
        cloth_name, type = input().split()
        
        if type in wears:
            wears[type].append(cloth_name)
        else:
            wears[type] = [cloth_name]
        # 딕셔너리 key : type, value : 옷 이름을 리스트로 저장
    
    cnt = 1
    for x in wears:
        cnt *= (len(wears[x]) +1)
    
    cnt -= 1 # 알몸 제외
    print(cnt)

# 배운 점 : 딕셔너리에서 string : list[] 매칭이된다