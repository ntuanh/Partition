from handle_data import comm_times , layer_times_2 , layer_times_3
from collections import deque
num_node = 2

""" test bed """
num_nodes = 6
cost = [[-1 for _ in range(num_nodes + 1)] for _ in range(num_nodes + 1)]
cost[1][2] = cost[2][1] = 4       # A - B
cost[1][3] = cost[3][1] = 5       # A - C
cost[2][3] = cost[3][2] = 11      # B - C
cost[2][4] = cost[4][2] = 9       # B - D
cost[3][5] = cost[5][3] = 3       # C - E
cost[4][5] = cost[5][4] = 13      # D - E
cost[4][6] = cost[6][4] = 2       # D - F
cost[5][6] = cost[6][5] = 6       # E - F
cost[2][5] = cost[5][2] = 7       # B - E

def dijkstra(cost ):
    visited = []
    node = {"node": 1 , "prev" : -1 , "cost": 0 }
    current_node = 0
    heap = deque([node])
    store = deque()
    while len(heap) != 0 :
        print("heap : " , heap)
        min_cost = 100000
        for item in list(heap):
            min_cost = min(min_cost , item["cost"])
        for item in list(heap):
            if item["cost"] == min_cost :
                current_node = item
                heap.remove(item)
                visited.append(current_node["node"])
                store.append(current_node)
            for j in range(len(cost[current_node["node"]])) :
                if j not in visited and cost[current_node["node"]][j] != -1:
                    new_node = {"node": j , "prev" : current_node["node"] , "cost" : current_node["cost"] + cost[current_node["node"]][j]}
                    exist = False
                    if len(heap) > 0 :
                        for item in heap :
                            if item["node"] == new_node["node"] :
                                exist = True
                                if item["cost"] > new_node["cost"]  :
                                    print("new node " , new_node)
                                    item["prev"] = new_node["prev"]
                                    item["cost"] = new_node["cost"]
                    if exist == False:
                        heap.append(new_node)

    return store


if __name__ == "__main__" :
    trace_back = dijkstra(cost)
    end_node = 6
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

    print(res_cost)
    lst_nodes.reverse()
    for node in lst_nodes :
        print(node , " -> " , end = "")
        
