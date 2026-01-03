def calculate_sums(max_num):
    print(f"--- 1부터 {max_num}까지 분석을 시작합니다 ---")
    
    even_total = 0  # 짝수 합을 담을 변수
    odd_total = 0   # 홀수 합을 담을 변수

    # 1부터 max_num까지 반복
    for i in range(1, max_num + 1):
        
        # [연습 포인트 1] 여기서 i 값이 1, 2, 3... 변하는 걸 지켜보세요.
        if i % 2 == 0:
            print(f"{i} -> 짝수 발견!")
            even_total += i  # 짝수면 여기에 더하기
        else:
            print(f"{i} -> 홀수 발견!")
            odd_total += i   # 홀수면 저기에 더하기
            
        # [연습 포인트 2] 여기 올 때마다 total 변수들이 어떻게 늘어나는지 보세요.
        
    return even_total, odd_total

# --- 메인 실행 ---
target_number = 5
result_even, result_odd = calculate_sums(target_number)

print(f"최종 결과: 짝수합={result_even}, 홀수합={result_odd}")