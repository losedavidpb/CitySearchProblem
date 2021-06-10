# Search methods

import search
import csv

if __name__ == '__main__':
    ways = [
        ('A', 'B'),
        ('L', 'P'),
        ('R', 'H'),
        ('S', 'A'),
        ('C', 'G')
    ]

    with open('bbs_bbes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['BBS vs BBES'])
        writer.writerow(['Start', 'Objective', 'Result', 'Visited BBS', 'Visited BBES', 'Expanded BBS', 'Expanded BBES'])

        for way_case in ways:
            orig_node, goal_node = way_case
            problem = search.GPSProblem(orig_node, goal_node, search.romania)

            print('******************************** Way(', orig_node, ', ', goal_node, ')', sep='')

            # bfs_node, num_bfs = search.breadth_first_graph_search(problem)
            # dfs_node, num_dfs = search.depth_first_graph_search(problem)
            bbs_node, vnum_bbs, num_bbs = search.branch_and_bound_graph_search(problem)
            bbes_node, vnum_bbes, num_bbes = search.branch_and_bound_with_underestimation_graph_search(problem)

            # bfs_node_path = bfs_node.path()
            # dfs_node_path = dfs_node.path()
            bbs_node_path = bbs_node.path()
            bbes_node_path = bbes_node.path()

            # print('BFS: ', bfs_node_path, ', cost = ', bfs_node.path_cost, ', expanded_nodes = ', num_bfs, sep='')
            # print('DFS: ', dfs_node_path, ', cost = ', dfs_node.path_cost, ', expanded_nodes = ', num_dfs, sep='')
            print('BBS: ', bbs_node_path, ', cost = ', bbs_node.path_cost, ', expanded_nodes = ', num_bbs, ', visited_nodes = ', vnum_bbs, sep='')
            print('BBES: ', bbes_node_path, ', cost = ', bbes_node.path_cost, ', expanded_nodes = ', num_bbes, ', visited_nodes = ', vnum_bbes,  sep='')

            if bbs_node_path == bbes_node_path:
                way = [str(node)[-2] for node in bbs_node_path]
                writer.writerow([orig_node, goal_node, way, str(vnum_bbs), str(vnum_bbes), str(num_bbs), str(num_bbes)])
            else:
                print("error: resulted path must be the same for BBS and BBES")
                exit(1)
