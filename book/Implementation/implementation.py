import string
from itertools import combinations


class Implementation:
    def __init__(self):
        pass

    def ex1(self):
        """
        상하좌우
        가장 왼쪽 위 좌표 (1, 1) 가장 오른쪽 아래 좌표 (N, N)
        예시
        5
        R R R U D D
        """
        size = int(input())
        li = input().split()
        x, y = 1, 1  # 좌표의 시작 1, 1 초기화
        for i in li:
            if i == 'R':
                # 기본 이동으로 y는 1씩 증가. 증가 전 최대값 크기 체크. size보다 커진다면 y값 변경되지 않도록
                y += 1 if y + 1 < size else False
            elif i == 'U':
                # 기본 이동으로 x는 1씩 감소. 감소 전 최소값 크기 체크. size보다 작아진다면 x값 변경되지 않도록
                x -= 1 if x - 1 > 0 else False
            elif i == 'D':
                # 기본 이동으로 x는 1씩 증가. 증가 전 최대값 크기 체크. size보다 커진다면 x값 변경되지 않도록
                x += 1 if x + 1 < size else False
            elif i == 'L':
                # 기본 이동으로 y는 1씩 감소. 감소 전 최소값 크기 체크. size보다 작아진다면 y값 변경되지 않도록
                y -= 1 if y - 1 > 0 else False
        start = [x, y]
        print(start)

    def ex1_2(self):
        """
        시각
        정수 N 입력
        00시 00분 00초부터 N시 59분 59초 까지 모든 시각 중 N 포함되는 모든 경우의 수
        """
        n = 5
        h, m, s = 5, 60, 60  # 반복문은 5번돌아야함 0 ~ 4
        s_test = 0
        cnt = 0  # n이 포함되면 올릴 값

        # m과 s는 0부터 59사이 n이 포함될 값이 동일할 것 이므로 cnt 값 구한 후 *2
        # ============테스트시작=============#
        test_cnt = 0
        while s_test <= 59:
            s_test += 1
            print(s_test)
            # str 으로 변경 후 3 포함 된다면 cnt 값 올리기
            if '3' in str(s_test):
                test_cnt += 1
        print(test_cnt)
        # 0시 0분 59초까지 cnt개
        # 0시 59분 59초까지 cnt * cnt
        # 시 경우의 수
        # h_ = int(n / 3) + 1
        # start => 5시 59분 59초 (cnt * cnt)
        # 5시 => 4시 59분 59초 (cnt * cnt)
        # 4시 => 3시 59분 59초 60 * 60
        # 3시 => 2시 59분 59초 cnt * cnt
        # 2시 => 1시 59분 59초 cnt * cnt
        # 1시 => 59분 59초 cnt * cnt
        # ============테스트종료=============#

        for h_ in range(h + 1):
            for m_ in range(m):
                for s_ in range(s):
                    if '3' in str(s_) + str(m_) + str(h_):
                        cnt += 1
        print(cnt)

    def ex2(self):
        """
        왕실의 나이트
        8x8 좌표 평면. 이동할 때 L자 형태로만 이동 가능
        특정 위치에서 2가지 경우로 이동 가능
        1. 수평으로 두 칸 이동 뒤 수직으로 한 칸 이동
        2. 수직으로 두 칸 이동 뒤 수평으로 한 칸 이동
        """
        # focus = input()
        focus = 'h8'
        size = 8
        focus_f = focus[0]
        focus_b = focus[1]
        # 열 소문자 리스트 a ~ h
        alph_li = [i for i in string.ascii_lowercase][:size]

        # 행 숫자 리스트 1 ~ 8
        focus_f_li = [str(i) for i in range(1, size + 1)]
        cnt = 0
        # 오른쪽으로 두 칸 이동, 아래로 한칸 이동
        # 아래로 두 칸 이동, 오른쪽으로 한칸 이동
        # 왼쪽으로 두 칸 이동, 아래로 한칸 이동
        # 위로 두 칸 이동, 오른쪽으로 한칸 이동...
        move_li = [[2, 1], [1, 2], [-2, 1], [1, -2], [-2, -1], [-1, 2], [-1, -2], [2, -1]]

        for i in move_li:
            # a 를 열 소문자 리스트에서 찾아서 인덱스 값 + i[0] 이동
            move_f = alph_li.index(focus_f) + i[0]
            # 1 을 행 숫자 리스트에서 찾아서 인덱스 값 + i[1] 이동
            move_b = focus_f_li.index(focus_b) + i[1]
            print(move_f, move_b)
            # 음수가 아닐 때 이동 성공 cnt + 1
            if 0 < move_f < 8 and 0 < move_b < 8:
                cnt += 1

        print(cnt)

    def ex3(self):
        """
        1 현재 위치에서 현재 방향 기준 => 왼쪽 방향 (반시계 방향으로 90도 회전한 방향)부터 차례대로 - 패턴 O, 육지를 한번 카운트 하면
        0은 북쪽 -> 3 서쪽으로 회전
        2 캐릭터 바로 왼쪽
        - 아직 가보지 않은 칸이 없다면 왼쪽방향으로 회전 2 남쪽 => 왼쪽 한칸 전진
        - 왼쪽방향에 가보지 않은 칸 없다면 왼쪽방향으로 회전 1 동쪽 => 1단계로
        3 네 방향 모두 이미 가본 칸 or 바다 이면
        - 바라본 방향 유지 -> 한칸 뒤로 -> 1다계로
        뒤쪽 방향 바다인 칸이면 뒤로 갈 수 없어 멈춤
        시작점도 횟수에 포함
        """
        n, m = 4, 4
        # 내 위치 북쪽
        x, y, lotate = 1, 1, 0
        li = [
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 1]
        ]
        c = [0, 1, 2, 3]
        position = [x, y]
        count = 1
        limit = 0
        while True:
            # print(x, y)
            # print(lotate)
            if lotate == 0:
                # 북쪽  y -= 1
                if li[x][y - 1] == 0:
                    y -= 1

                    li[x][y] = 1
                    limit = 0
                    count += 1
                    # print(x, y, 0)
                else:
                    limit += 1
            elif lotate == 1:
                # 동쪽 x -= 1
                if li[x - 1][y] == 0:
                    x -= 1
                    li[x][y] = 1
                    limit = 0
                    count += 1
                else:
                    limit += 1
            elif lotate == 2:
                print(x, y + 1, li[x][y + 1], 2)
                # 남쪽
                if li[x][y + 1] == 0:
                    y += 1
                    li[x][y] = 1
                    limit = 0
                    count += 1
                else:
                    limit += 1
            elif lotate == 3:
                # print(li[x + 1][y], 3)
                if li[x + 1][y] == 0:
                    x += 1
                    li[x][y] = 1
                    limit = 0
                    count += 1
                else:
                    limit += 1
                # 서쪽 x += 1
            lotate = c[lotate - 1]
            # 4방향을 체크
            if limit >= 4:
                print(x, y)
                # print(count)
                break



if __name__ == '__main__':
    # Implementation.ex1_2('')
    # Implementation.ex2('')
    Implementation.ex3('')




