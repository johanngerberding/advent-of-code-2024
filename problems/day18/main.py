from heapq import heapify, heappop, heappush

example = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""

example = [[int(el) for el in line.split(",")] for line in example.split("\n")[:12]]
print(example)

with open("input.txt", "r") as fp:
    data = [[int(el) for el in line.strip().split(",")] for line in fp]

data = data[:1024]

start = (0, 0)
end = (max([el[0] for el in data]), max([el[1] for el in data]))


graph = {}

for row in range(end[0] + 1):
    for col in range(end[1] + 1):
        if [row, col] in data:
            continue
        adjs = []
        if row - 1 >= 0 and [row - 1, col] not in data:
            adjs.append((row - 1, col))
        if row + 1 <= end[0] and [row + 1, col] not in data:
            adjs.append((row + 1, col))
        if col + 1 <= end[1] and [row, col + 1] not in data:
            adjs.append((row, col + 1))
        if col - 1 >= 0 and [row, col - 1] not in data:
            adjs.append((row, col - 1))
        graph[(row, col)] = adjs

distances = {node: float("inf") for node in graph.keys()}
distances[start] = 0

pq = [(0, start)]
heapify(pq)
visited = set()

while pq:
    distance, node = heappop(pq)
    if node in visited:
        continue
    visited.add(node)

    for adj in graph[node]:
        temp_distance = distance + 1
        if temp_distance < distances[adj]:
            distances[adj] = temp_distance
            heappush(pq, (temp_distance, adj))

print(distances[end])


# X,Y
# X => distance from left edge
# Y => distance from top

start = (0, 0)
end = (70, 70)
