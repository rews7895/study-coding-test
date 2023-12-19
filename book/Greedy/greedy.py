import time
class Greedy:
    def __init__(self):
        self.count = 4
        pass
        # print('문제번호 입력')
        # part = int(input())
        # self._part = part

    def ex1(self):
        """
        거스름돈
        500, 100, 50, 10원짜리 동전 무수히 많음
        손님에게 거슬러줘야할 돈 N원일 때,
        거슬러줘야할 동전의 최소 개수
        """
        exchange = int(input())
        exchange_coin = [500, 100, 50, 10]
        cnt = 0
        coin_r = exchange
        for coin in exchange_coin:
            coin_cnt = coin_r // coin
            cnt += coin_cnt
            coin_r = coin_r - (coin_cnt * coin)
        return f"결과 : {cnt}"

    def ex2(self):
        """
        큰 수 법칙
        다양한 수로 이루어지니 배열 => 주어진 수들을 M번 더해 가장 큰 수 만들기
        특정 인덱스에 해당하는 수가 연속해서 K번 초과해 더해질 수 없는 것이 특징
        첫째줄 N(2<=N<=1000), K(1<=K<=10000)
        둘째줄 N개 자연수
        입력예시)
        5 8 3
        2 4 5 4 6
        """
        i, m, k = input().split()
        i, m, k = int(i), int(m), int(k)
        input_list = input().split()
        input_list = [int(a) for a in input_list]
        result = 0
        max_fir = max(input_list)
        input_list.remove(max_fir)
        max_sec = max(input_list)
        for i in range(1, m+1):
            if i % k == 0:
                result += max_sec
            else:
                result += max_fir
        return f"결과 : {result}"

    def ex3(self):
        """
        숫자 카드 게임
        여러개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장
        n은 행의 개수 m은 열의 개수. 뽑고자 하는 카드 포함
        행에 포함된 카드 중 가장 낮은 카드 뽑기
        3 3
        3 1 2
        4 1 4
        2 2 2

        2 4
        7 3 1 8
        3 3 3 4
        """
        n, m = input().split()
        n, m = int(n), int(m)
        li = []
        for a in range(n):
            li_ = list(map(int, input().split()))
            li.append(li_)
        result = 0
        for (idx, i) in enumerate(li):
            if m-1 > idx:
                result = min(i)
            else:
                if result < min(i):
                    result = min(i)
        print(result)


    def ex4(self):
        """
        1이 될 때 까지
        어떤 수 N이 1이 될 때까지 반복 수행
        N에서 1을 빼고 N을 K로 나눔
        """

        cnt = 0
        n, k = map(int, input().split())
        start_time = time.time()
        while n != 1:
            if k % 2 == 0:  # 짝수일 때
                if n % 2 != 0:
                    n -= 1
                    cnt += 1
                else:
                    n = int(n / k)
                    cnt += 1
            else: # 홀수일 때
                if n % 2 != 0:
                    n = int(n / k)
                    cnt += 1
                else:
                    n -= 1
                    cnt += 1
        print(cnt)
        end_time = time.time()
        print(f"실행시간 : {round(end_time - start_time, 4)}")

if __name__ == '__main__':
    pass
    # Greedy.ex1('',34230)
    # Greedy.ex2('', )
    # Greedy.ex3('')
    # Greedy.ex4('')
    # test()