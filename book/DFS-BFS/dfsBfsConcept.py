from collections import deque
class DfsBfsConcept:
    def __init__():
        pass

    def adjacencyMatrix(self):
        """
        인접 행렬 : 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식
        연결되어 있지 안은 노드끼ㅣ는 무한의 비용
        논리적으로 정답이 될 수 없는 큰 값 999999999
        모든 관계를 저장하므로 노드 개수가 많을수록 메모리 불필요하게 낭비
        """
        # 무한의 비용 선언
        INF = 999999999

        # 2차원 리스트를 이용해 인접 행렬 표현
        graph = [
            [0, 7, 5],
            [7, 0, INF],
            [5, INF, 0]
        ]
        print(graph)
        # print(f"인접 행렬 방식으로 graph[1][7]확인 : {graph[1][7]}")

    def adjacencyList(self):
        """
        인접 리스트 : 모든 노드에 연결된 노드에 대한 정보 차례대로 연결해 저장
        연결된 정보만을 저장하므로 메모리 효율적으로 사용
        특정한 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도 느림 - 연결된 데이터 하나씩 확인
        """
        # 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현
        graph = [[] for _ in range(3)]

        # 노드 0에 연결된 노드 정보 저장(노드, 거리)
        graph[0].append((1, 7))
        graph[0].append((2, 5))

        # 노드 1에 연결된 노드 정보 저장(노드, 거리)
        graph[1].append((0, 7))

        # 노드 2에 연결된 노드 정보 저장(노드, 거리)
        graph[2].append((0, 5))

        return graph

    def dfs_stack(self):
        """
        1. 탐색 시작 노드를 스택에 삽입 후 방문 처리
        2. 스택 최상단 노드에 방문하지 않은 인접 노드 있다면 그 인접노드를 스택에 넣고 방문처리
           방문하지 않은 인접 노드가 없다면 스택에서 최상단 노드를 꺼냄
        2번 과정 더 이상 수행 불가능할 때까지 실행
        1-2 1-3 1-8
        2-1 2-7
        3-1 3-4 3-5
        4-3 4-5
        5-3 5-3
        6-7
        7-2 7-8 7-6
        8-1 8-7
        """
        stack = []
        # 1 최상단노드 '1'에 방문하지 않은 인접 노드 2, 3, 8 중 가장 작은 2
        stack.append(1)
        stack.append(2)
        # 2에 방문하지 않은 인접노드 7
        stack.append(7)
        # 7에 방문하지 않은 인접노드 6, 8 중 가장 작은 6
        stack.append(6)
        # 6에 방문하지 않은 인접노드 없으므로 스택에서 6 꺼냄
        stack.remove(6)
        # 다음 다시 연결할 값 찾기 위해
        point = stack[len(stack) - 1]
        print(point)
        # 7에 방문하지 않은 인접 노드 6은 실행했으니 8
        stack.append(8)
        # 8에 인접한 노드 없어 스택에서 8 꺼냄
        stack.remove(8)
        # 다음 다시 연결할 값 찾기 위해
        point = stack[len(stack) - 1]
        print(point)
        # 7에 인접한 노드 없어 스택에서 7 꺼냄
        stack.remove(point)
        print(stack)
        # 다음 다시 연결할 값 찾기 위해
        point = stack[len(stack) - 1]
        print(point)
        # 2에 인접한 노드 없어 스택에서 2 꺼냄
        stack.remove(point)
        # 다음 다시 연결할 값 찾기 위해
        point = stack[len(stack) - 1]
        # 1에 인접한 노드 다음 3
        stack.append(3)
        # 3에 방문하지 않은 인접 노드 4 , 5 중 4
        stack.append(4)
        # 4에 방문하지 않은 인접 노드 5
        stack.append(5)

    # DFS 메서드 정의
    def dfs(graph, v, visited):
        # 현재 노드를 방문 처리
        visited[v] = True
        print(v, end = ' ')
        # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        for i in graph[v]:
            if not visited[i]:
                DfsBfsConcept.dfs(graph, i, visited)
    def dfs_exec(self):
        # 각 노드가 연결된 정보를 리스트 자료형으로 표현 (2차원 리스트)
        graph = [
            [],
            [2, 3, 8],
            [1, 7],
            [1, 4, 5],
            [3, 5],
            [3, 4],
            [7],
            [2, 6, 8],
            [1, 7]
        ]
        # 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
        visited = [False] * 9
        # 정의된 DFS 함수 호출
        DfsBfsConcept.dfs(graph, 1, visited)

    def bfs_stack(self):
        """
        '너비 우선 탐색' : 가까운 노드부터 탐색하는 알고리즘
        선입선출 방식인 큐 자료구조를 이용하기
        인접한 노드를 반복적으로 큐에 넣어 알고리즘 작성
        1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
        2. 큐에서 노드 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
        """
        queue = deque()
        # 1 시작 노드 1 삽입,
        queue.append(1)
        # 1 꺼내고 인접 노드 2, 3, 8
        queue.remove(queue[0])
        # 방문하지 않은 인접 노드 2, 3, 8 모두 삽입
        queue.append(2)
        queue.append(3)
        queue.append(8)
        print(queue)
        # 먼저들어간 2 꺼내고 방문하지않은 인접노드 7 삽입
        queue.remove(queue[0])
        queue.append(7)
        print(queue)
        # 3 꺼내고 방문하지 않은 인접노드 4, 5 삽입
        queue.remove(queue[0])
        queue.append(4)
        queue.append(5)
        print(queue)
        # 8꺼내고 인접노드 없어 무시
        queue.remove(queue[0])
        print(queue)
        # 7꺼내고 인접노드 6 삽입
        queue.remove(queue[0])
        queue.append(6)
        print(queue)

    # BFS 메서드 정의
    def bfs(graph, start, visited):
        # Queue 구현을 위해 deque 라이브러리 사용
        queue = deque([start])
        # 현재 노드를 방문 처리
        visited[start] = True
        # 큐가 빌 때까지 반복
        while queue:
            # 큐에서 하나의 원소를 뽑아 출력
            v = queue.popleft()
            print(v, end=' ')
            # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
            for i in graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
    def bfs_exec(self):
        # 각 노드가 연결된 정보를 리스트 자료형으로 표현 (2차원 리스트)
        # 각 노드가 연결된 정보를 리스트 자료형으로 표현 (2차원 리스트)
        graph = [
            [],
            [2, 3, 8],
            [1, 7],
            [1, 4, 5],
            [3, 5],
            [3, 4],
            [7],
            [2, 6, 8],
            [1, 7]
        ]
        # 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
        visited = [False] * 9
        # 정의된 DFS 함수 호출
        DfsBfsConcept.bfs(graph, 1, visited)


if __name__ == '__main__':
    # DfsBfsConcept.adjacencyMatrix('')
    # adjacency_list = DfsBfsConcept.adjacencyList('')
    # print(adjacency_list)
    # DfsBfsConcept.dfs_stack()
    # DfsBfsConcept.dfs_exec('')
    DfsBfsConcept.bfs_stack('')

