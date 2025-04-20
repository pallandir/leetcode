from collections import defaultdict


def journey_to_the_moon(astronaut_number: int, astronaut_ids: list[tuple]):
    # build graph
    graph = defaultdict(list)
    for index in range(astronaut_number):
        graph[index] = []
    for id_1, id_2 in astronaut_ids:
        graph[id_1].append(id_2)
        graph[id_2].append(id_1)
    visited = [False] * astronaut_number
    country_sizes = []

    def dfs(node):
        stack = [node]
        country_size = 0

        while stack:
            current_node = stack.pop()
            if not visited[current_node]:
                visited[current_node] = True
                country_size += 1
                stack.extend(graph[current_node])
        return country_size

    for index in range(astronaut_number):
        if not visited[index]:
            country_sizes.append(dfs(index))
    total_pairs = 0
    current_total_pair = 0
    for size in country_sizes:
        total_pairs += size * current_total_pair
        current_total_pair += size
    return total_pairs


if __name__ == "__main__":
    print(journey_to_the_moon(5, [(0, 1), (2, 3)]))
