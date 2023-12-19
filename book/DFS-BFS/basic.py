from collections import deque
class Basic:
    def __init__(self):
        pass

    def stack_ex(self):
        """
        선입후출 or 후입선출
        python에서는 stack 관련 별도 라이브러리 사용할 필요 없음
        append() pop() 메서드 사용
        """
        stack = []
        # 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
        stack.append(5)
        stack.append(2)
        stack.append(3)
        stack.append(7)
        stack.pop()
        stack.append(1)
        stack.append(4)
        stack.pop()
        print(stack)  # 최하단 원소부터 출력
        print(stack[::-1])  # 최상단 원소부터 출력

    def queue_ex(self):
        """
        선입선출 구조
        """
        # Queue 구현을 위해 deque 라이브러리 사용
        queue = deque()

        # 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
        queue.append(5)
        queue.append(2)
        queue.append(3)
        queue.append(7)
        queue.popleft()
        queue.append(1)
        queue.append(4)
        queue.pop()
        print(queue)  # 먼저 들어온 순서대로 출력
        queue.reverse()  # 다음 출력을 위해 역순으로 바꾸기
        print(queue)  # 나중에 들어온 원소부터 출력

    def recursive(self):
        """
        재귀함수 - 자기자신을 다시 호출하는 함수
        계속 호출하면 재귀의 최대 깊이 초과 - 파이썬 인터프리터 호출 횟수 제한
        종료 조건 필수 명시

        연속해서 호출하는 함수는 메인 메모리 스택 공간에 적재
        = 재귀함수는 내부적으로 스택 자료구조와 동일
        """
        def recursive_function(i):
            # 10번째 출력했을 때 종료되도록 종료 조건 명시
            if i == 100:
                return
            print(i, '번째 재귀함수에서 ', i+1, '번째 재귀 함수를 호출합니다.')
            recursive_function(i + 1)
            print(i, '번째 재귀함수를 종료합니다')
        recursive_function(1)

    def recursive_ex(self):
        # 반복적으로 구현한 n!
        def factorial_iterative(n):
            result = 1
            # 1부터 n까지의 수를 차례대로 곱하기
            for i in range(1, n + 1):
                result *= i
            return result

        # 재귀적으로 구현한 n!
        def factorial_recursive(n):
            if n <= 1:  # n이 1이하인 경우 1을 반환
                return 1
            # n! = n * (n-1)!을 그대로 코드로 작성
            return n * factorial_recursive(n - 1)
        # 각각 방식으로 구현한 n! 출력(n = 5)
        print("반복적으로 구현:", factorial_iterative(5))
        print("재귀적으로 구현:", factorial_recursive(5))