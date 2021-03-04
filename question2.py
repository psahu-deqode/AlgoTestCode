"""Function for maximum connected node identification """


# function to identify router with maximum connections
def identify_router(node_list):
    node_count_dict = {}
    for i in range(len(node_list)):
        count = 0
        # check if the node is in extreme end and calculate the adjacent node counts accordingly
        if i == 0 or i + 1 == len(node_list):
            count += 1
        else:
            count += 2
        # check if the node already has any other connections
        if node_list[i] not in node_count_dict.keys():
            node_count_dict[node_list[i]] = count
        else:
            node_count_dict[node_list[i]] += count
    # calculates maximum number of connection available
    max_conn = max(node_count_dict.values())
    # returns the node with maximum connection
    node = [key for key, value in node_count_dict.items() if value == max_conn]
    return node


node_list = input(
    'Please enter the router input graph of nodes separated by "->" '
).split("->")
print(identify_router(node_list))
