class GreedySolution:
    def __init__(self):
        pass
    def ex1_solution1(self):
        n = 1260
        count = 0

        # 큰 단위의 화폐부터 차례대로 확인
        coint_types = [500, 100, 50, 10]

        for coin in coint_types:
            count += n // coin  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
            n %= coin
        print(count)

    def ex2_solution1(self):
        # N, M, K를 공백으로 구분해 입력받기
        n, m, k = map(int, input().split())
        # N개의 수를 공백으로 구분하여 입력받기
        data = list(map(int, input().split()))

        data.sort()  # 입력받은 수들 정렬하기
        first = data[n - 1]  # 가장 큰 수
        second = data[n - 2]  # 두 번째로 큰 수
        result = 0
        while True:
            for i in range(k):  # 가장 큰 수를 K번 더하기
                if m == 0:  # m이 0이라면 반복문 탈출
                    break
                result += first
                m -= 1  # 더할 때마다 1씩 빼기
            if m == 0:  # m이 0이라면 반복문 탈출
                break
            result += second  # 두 번째로 큰 수를 한 번 더하기
            m -= 1  # 더할 때마다 1씩 빼기
        print(result)  # 최종 답안 출력

    def ex2_solution2(self):
        # N, M, K를 공백으로 구분해 입력받기
        n, m, k = map(int, input().split())
        # N개의 수를 공백으로 구분하여 입력받기
        data = list(map(int, input().split()))

        data.sort()  # 입력받은 수들 정렬하기
        first = data[n - 1]  # 가장 큰 수
        second = data[n - 2]  # 두 번째로 큰 수

        # 가장 큰 수가 더해지는 횟수 계산
        count = int(m / (k + 1)) * k
        count += m % (k + 1)

        result = 0
        result += (count) * first  # 가장 큰 수 더하기
        result += (m - count) * second  # 두 번째로 큰 수 더하기
        print(result)  # 최종 답안 출력

    def ex3_solution1(self):
        # n, m을 공백으로 구분하여 입력받기
        n, m = map(int, input().split())

        result = 0
        # 한 줄씩 입력받아 확인
        for i in range(n):
            data = list(map(int, input().split()))
            # 현재 줄에서 '가장 작은 수' 찾기
            min_value = min(data)
            # '가장 작은 수'들 중에서 가장 큰 수 찾기
            result = max(result, min_value)
        print(result)  # 최종 답안 출력


    def ex3_solution2(self):
        # n, m을 공백으로 구분하여 입력받기
        n, m = map(int, input().split())

        result = 0
        # 한 줄씩 입력받아 확인
        for i in range(n):
            data = list(map(int, input().split()))
            # 현재 줄에서 '가장 작은 수' 찾기
            min_value = 10001
            for a in data:
                min_value = min(min_value, a)
            # '가장 작은 수'들 중에서 가장 큰 수 찾기
            result = max(result, min_value)
        print(result)  # 최종 답안 출력

    def ex4_solution1(self):
        n, k = map(int, input().split())
        result = 0

        # n이 k 이상이라면 k로 계속 나누기
        while n >= k:
            # n이 k로 나누어 떨어지지 않는다면 n에서 1씩 빼기
            while n % k != 0:
                n -= 1
                result += 1
            # k로 나누기
            n //= k
            result += 1
        # 마지막으로 남은 수에 대하여 1씩 빼기
        while n > 1:
            n -= 1
            result += 1
        print(result)

    def ex4_solution2(self):
        n, k = map(int, input().split())
        result = 0

        while True:
            # (N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
            target = (n // k) * k
            result += (n - target)
            n = target
            # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
            if n < k:
                break
            # K 로 나누기
            result += 1
            n //= k
        # 마지막으로 남은 수에 대하여 1씩 빼기
        result += (n - 1)
        print(result)


if __name__ == '__main__':
    GreedySolution.ex1_solution1('')