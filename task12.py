from utils import get_input


def get_test_input():
    a = '''fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW'''
    return [i.strip() for i in a.split('\n') if i.strip() != '']


def get_next_nodes(cur_node, path, graph_node_to_nodes):
    return set(node for node in graph_node_to_nodes[cur_node] if node.isupper() or node not in path and node != 'start')


def main0(input_lines: list):
    graph_node_to_nodes = {}
    for line in input_lines:
        n1, n2 = line.split('-')
        graph_node_to_nodes[n1] = graph_node_to_nodes.get(n1, set()) | set([n2])
        graph_node_to_nodes[n2] = graph_node_to_nodes.get(n2, set()) | set([n1])

    ready_paths = []
    to_handle_paths = [['start']]
    while to_handle_paths:
        new_to_handle_paths = []
        for path in to_handle_paths:
            next_nodes = get_next_nodes(path[-1], path, graph_node_to_nodes)
            for next_node in next_nodes:
                if next_node == 'end':
                    ready_paths.append(path + ['end'])
                else:
                    new_to_handle_paths.append(path + [next_node])
        to_handle_paths = new_to_handle_paths
    return len(ready_paths)


def get_next_nodes1(cur_node, path, graph_node_to_nodes):
    small_nodes = [k for k in graph_node_to_nodes.keys() if k.islower()]
    double_permitted = True
    for s in small_nodes:
        if path.count(s) > 1:
            double_permitted = False
            break
    r = set()
    for node in graph_node_to_nodes[cur_node]:
        if node == 'start':
            pass
        elif node.isupper():
            r.add(node)
        elif node not in path:
            r.add(node)
        elif path.count(node) == 1 and double_permitted:
            r.add(node)
    return r


def main1(input_lines: list):
    graph_node_to_nodes = {}
    for line in input_lines:
        n1, n2 = line.split('-')
        graph_node_to_nodes[n1] = graph_node_to_nodes.get(n1, set()) | set([n2])
        graph_node_to_nodes[n2] = graph_node_to_nodes.get(n2, set()) | set([n1])

    ready_paths = []
    to_handle_paths = [['start']]
    while to_handle_paths:
        new_to_handle_paths = []
        for path in to_handle_paths:
            next_nodes = get_next_nodes1(path[-1], path, graph_node_to_nodes)
            for next_node in next_nodes:
                if next_node == 'end':
                    ready_paths.append(path + ['end'])
                else:
                    new_to_handle_paths.append(path + [next_node])
        to_handle_paths = new_to_handle_paths
    return len(ready_paths)


if __name__ == '__main__':
    test_input_lines = get_test_input()
    print('Answer 0, test:', main0(test_input_lines))
    print('Answer 1, test:', main1(test_input_lines))

    real_input = get_input(__file__)
    print('Answer 0, real:', main0(real_input))
    print('Answer 1, real:', main1(real_input))
