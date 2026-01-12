N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]
white_cnt = 0
blue_cnt = 0

def is_same_color(x, y, size):
    color = paper[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if paper[i][j] != color:
                return False
    return True

def divide(x, y, size):
    global white_cnt, blue_cnt
    if is_same_color(x, y, size):
        if paper[x][y] == 0:
            white_cnt +=1
        else:
            blue_cnt +=1
        return

    half = size // 2
    divide(x, y, half)             
    divide(x, y + half, half)       
    divide(x + half, y, half)       
    divide(x + half, y + half, half)  


divide(0,0, N)
print(white_cnt)
print(blue_cnt)