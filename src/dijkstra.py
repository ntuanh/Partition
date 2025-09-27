from handle_data import comm_times , layer_times_2 , layer_times_3
from collections import deque
from handle_data import cost , num_points
num_node = 2

""" test bed """
num_nodes = 6

def dijkstra(cost, start=1):
    visited = set()
    node = {"node": start, "prev": -1, "cost": 0}
    heap = deque([node])
    store = deque()

    while len(heap) > 0:
        # pick min-cost node
        # print("heap : " ,  heap)
        min_cost = min(item["cost"] for item in heap)
        for item in list(heap):
            if item["cost"] == min_cost:
                current_node = item
                heap.remove(item)
                break

        # mark visited
        visited.add(current_node["node"])
        store.append(current_node)

        # relax neighbors
        for j, edge_cost in enumerate(cost[current_node["node"]]):
            if edge_cost != -1 and j not in visited:
                new_node = {
                    "node": j,
                    "prev": current_node["node"],
                    "cost": current_node["cost"] + edge_cost
                }

                exist = False
                for item in heap:
                    if item["node"] == new_node["node"]:
                        exist = True
                        if item["cost"] > new_node["cost"]:
                            item["cost"] = new_node["cost"]
                            item["prev"] = new_node["prev"]
                if not exist:
                    heap.append(new_node)

    return list(store)

# print(dijkstra(cost))

if __name__ == "__main__" :
    trace_back = dijkstra(cost)
    end_node = num_points * 2
    start_node = 1
    curr_node = end_node
    lst_nodes = []
    res_cost = 0
    for item in trace_back :
        if item["node"] == end_node:
            res_cost = item["cost"]
    while True :
        lst_nodes.append(curr_node)
        if curr_node == start_node :
            break
        for item in trace_back :
            if item["node"] == curr_node :
                curr_node = item["prev"]
                break

    lst_nodes.reverse()
    for node in lst_nodes :
        print(node , " -> " , end = "")
    print("Result : " , res_cost + layer_times_2[1])

    cut_point = -1
    for i in range(len(lst_nodes)):
        if lst_nodes[i] > num_points:
            cut_point = i
            break


    print("\n=> Layer 1 : " , lst_nodes[:cut_point])
    lst_nodes = [x - num_points for x in lst_nodes]
    print("=> Layer 2 : " , lst_nodes[cut_point :] )
        
