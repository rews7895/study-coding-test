class Greedy:
    def __init__(self):
        pass
        # print('문제번호 입력')
        # part = int(input())
        # self._part = part

    def ex1(self, exchange):
        """
        거스름돈
        500, 100, 50, 10원짜리 동전 무수히 많음
        손님에게 거슬러줘야할 돈 N원일 때,
        거슬러줘야할 동전의 최소 개수
        """
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
        """
        pass

    def ex4(self):
        """
        1이 될 때 까지
        """
        pass

# if __name__ == '__main__':
    # Greedy.ex1('',34230)
    # Greedy.ex2('', )