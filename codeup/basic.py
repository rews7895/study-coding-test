def evenSum():
    """짝수 합 구하기"""
    n = int(input())
    s = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            s += i
    print(s)
def wantStr():
    """원하는 문자가 입력될 때까지 반복 출력"""
    s = ord('a')
    while s != 'q':
        s = input()
        print(s)
def sumInt():
    """언제까지 더해야 할까?"""
    a = int(input())
    answer = 0
    cnt = 0
    while a != answer:
        answer += 1
        cnt += answer
        if cnt >= a:
            print(answer)
            break

def dice2():
    """주사위 2개 던지기"""
    n, m = input().split()
    n = int(n)
    m = int(m)

    for i in range(1, n+1):
        for j in range(1, m+1):
            print(i,j)

def multiple16():
    """16진수 구구단 출력하기"""
    n = input()
    n = int(n, 16)
    for i in range(1, 16):
        print('%X' % n, '*%X' % i, '=%X' % (n * i), sep='')

def game369():
    """3 6 9 게임의 왕이 되자"""
    n = int(input())
    s = ''
    for i in range(1, n + 1):
        if '3' in str(i) or '6' in str(i) or '9' in str(i):
            s += 'X '
        else:
            s += f"{str(i)} "
    if s.endswith(' '):
        s = s[:-1]
    print(s)

def mixLight():
    """빛 섞어 색 만들기"""
    r, g, b = input().split()
    r, g, b = int(r), int(g), int(b)
    cnt = 0
    for r_i in range(0, r):
        for g_i in range(0, g):
            for b_i in range(0, b):
                print(r_i, g_i, b_i)
                cnt += 1
    print(cnt)

def saveSoundFile():
    h, b, c, s = input().split()
    h, b, c, s = int(h), int(b), int(c), int(s)
    answer = h*b*c*s/8/1024/1024
    print(f"{round(answer, 1)} MB")

def saveImgFile():
    w, h, b = input().split()
    w, h, b = int(w), int(h), int(b)
    answer = w * h * b / 8 / 1024 /1024
    print(f"{round(answer, 2):.2f} MB")

def sumIntStop():

    a = int(input())
    r = 0
    result = 0
    while r < a:
        r += 1
        result += r
        if a <= result:
            print(result)
            break

def multiple3():
    a = int(input())
    s = ''
    for i in range(1, a+1):
        if i % 3 != 0:
            s += f"{str(i)} "
    if s.endswith(' '):
        s = s[:-1]
    print(s)

def arithmetic():
    a, d, n = input().split()
    a, d, n = int(a), int(d), int(n)
    cnt = 0
    re = a
    while cnt != n-1:
        re = re + d
        cnt += 1
        if cnt == n:
            break
    print(re)

def geometric():
    a, r, n = input().split()
    a, r, n = int(a), int(r), int(n)
    cnt = 0
    re = a
    while cnt != n - 1:
        re = re * r
        cnt += 1
        if cnt == n:
            break
    print(re)

def sequences():
    a, m, d, n = input().split()
    a, m, d, n = int(a), int(m), int(d), int(n)
    cnt = 1
    init = a
    while cnt != n:
        init = init * m + d
        cnt += 1
        if cnt == n:
            break
    print(init)

# def together():
#     a, b, c = 3, 7, 9
#     # 같은 날 동시에 가입
#     d = 1
#     while d % a != 0 or d % b != 0 or d % c != 0:
#         d += 1
#     print(d)

def callAttend():
    n = int(input())
    a = input().split()
    a = [int(a[i]) for i in range(n)]
    d = [0 for numb in range(1, 24)]
    for a_id in a:
        d[a_id-1] += 1
    d = [str(d_numb) for d_numb in d]
    print(' '.join(d))

def callAttend2():
    n = int(input())
    a = input().split()
    a = [int(a[i]) for i in range(n)]
    answer = []
    for i in range(n-1, -1, -1):
        answer.append(str(a[i]))
    print(' '.join(answer))

def callAttend3():
    n = int(input())
    a = input().split()
    a = [int(a[i]) for i in range(n)]
    print(min(a))

def white():
    d = []
    for i in range(20):
        d.append([])
        for j in range(20):
            d[i].append(0)
    n = int(input())
    for i in range(n):
        x, y = input().split()
        d[int(x)][int(y)] = 1

    for i in range(1, 20):
        for j in range(1, 20):
            print(d[i][j], end=' ')
        print()

# def convertwhite():
def sugarSnack():
    h, w = input().split()
    h, w = int(h), int(w)
    pan = []
    for h_ in range(h):
        pan.append([])
        for h_d in range(w):
            pan[h_].append(0)
    # print(pan)

    # d: 가로는 0 세로는 1
    n = int(input())
    for i in range(n):
        l, d, x, y = input().split()
        l, d, x, y = int(l), int(d), int(x), int(y)

        if d == 0:



            if l_ > 1:
                for l_ in range(l):
                    pan[x - 1][y - 1] = 1
                    pan[x - 1][y] = 1



            if d == 1:
                pan[x - 1][y - 1] = 1
                pan[x][y - 1] = 1

    # pan
    for p in range(0, len(pan)):
        for p_ in range(0, len(pan)):
            print(pan[p][p_], end=' ')
        print()

if __name__ == '__main__':
    # evenSum()
    # wantStr()
    # sumInt()
    # dice2()
    # multiple16()
    # game369()
    # mixLight()
    # saveSoundFile()
    # saveImgFile()
    # sumIntStop()
    # multiple3()
    # arithmetic()
    # geometric()
    # sequences()
    # callAttend()
    # callAttend3()
    # white()
    # convertwhite()
    sugarSnack()