import sys
# 파이썬 최대 재귀 횟수는 1000번까지 가능하다.
# sys.setrecursionlimit(limit_number)를 통해서 제한을 풀 수 있다.
# Pypy로 실행 시 메모리 초과, Python3로 돌려야 한다.
sys.setrecursionlimit(150000)

# 속도 이슈로 stdin 사용
input = sys.stdin.readline

n = int(input())

# 인접 정보를 저장한다.
connected_node = dict([])
# 특정 노드의 parent를 저장한다.
node_parent = dict([])

# 초기화
for i in range(1, n + 1):
    connected_node[i] = []
    node_parent[i] = []

# Parent 정보가 없기 때문에 상호 연결 해준다.
for _ in range(n - 1):
    node1, node2 = map(int, input().split())
    connected_node[node1].append(node2)
    connected_node[node2].append(node1)

# 재귀로 해결. 시간 복잡도는 O(n log n)..? Global 변수 적극 사용함.
def solution(parent_node):
    try:
        for child_node in connected_node[parent_node]:
            # Parent 정보를 추가해 줌.
            node_parent[child_node] = parent_node
            # Parent는 제외. Remove는 O(n)
            connected_node[child_node].remove(parent_node)
            # 재귀 호출
            solution(child_node)
        return
    except:
        # Child Node가 없는 Leaf일 경우 끝.
        return

# 1은 root를 의미. 답이 node_parent에 저장됨.
solution(1)
for node in list(node_parent.values())[1:]:
    print(node)