def clustering(graph, nodes, k):
    """Needs some refactoring - tests are successful, but the results look odd
    """
    visited = set()
    cluster = list(range(1, nodes + 1))
    cluster = [(i,) for i in cluster]

    while len(cluster) > k:

        first_node, second_node, weight = graph.pop(0)

        if first_node not in visited and second_node not in visited:

            visited.add(first_node)
            visited.add(second_node)

            cluster.remove((first_node,))
            cluster.remove((second_node,))

            cluster.append(tuple((first_node, second_node)))

        elif first_node not in visited:

            visited.add(first_node)
            cluster.remove((first_node,))

            for i, subcluster in enumerate(cluster):
                if second_node in subcluster:
                    cluster[i] = subcluster + (first_node,)

        elif second_node not in visited:

            visited.add(second_node)
            cluster.remove((second_node,))

            for i, subcluster in enumerate(cluster):
                if first_node in subcluster:
                    cluster[i] = subcluster + (second_node,)

        else:
            temp_1 = [item for item in cluster if first_node in item][0]
            temp_2 = [item for item in cluster if second_node in item][0]

            if temp_1 == temp_2:
                continue

            else:
                cluster.append(tuple(set(temp_1 + temp_2)))
                cluster.remove(temp_1)
                cluster.remove(temp_2)

    return cluster


def find_shortest(graph, cluster):
    seeking = True

    while seeking:

        first_node, second_node, weight = graph.pop(0)

        temp_1 = [item for item in cluster if first_node in item][0]
        temp_2 = [item for item in cluster if second_node in item][0]

        if temp_1 == temp_2:
            continue

        else:
            seeking = False

        return weight
