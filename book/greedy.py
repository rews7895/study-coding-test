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
        return cnt

    def ex2(self):
        """
        큰 수 법칙
        첫째줄 N(2<=N<=1000), K(1<=K<=10000)
        둘째줄 N개 자연수
        입력예시)
        5 8 3
        2 4 5 4 6
        """
        pass

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
#     Greedy.ex1('',34230)