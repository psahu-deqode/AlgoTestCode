"""Function for maximum connected node identification """


# function to identify router with maximum connections
def identify_router(list1):
    # Initialization of lists used
    node_list = []
    conn_count_list = []
    identified_nodes = []
    for i in range(len(list1)):
        count = 0
        # algo to find if an element is first or last node so their adjacent 1 node is counted otherwise 2 nodes
        if i == 0 or i + 1 == len(list1):
            count += 1
        else:
            count += 2
        # for adding the count if multiple connections of the same node are present
        if list1[i] not in node_list:
            node_list.append(list1[i])
            conn_count_list.append(count)
        else:
            x = node_list.index(list1[i])
            conn_count_list[x] += count
    # find the max number of connection with any node
    max_conn = max(conn_count_list)
    # find the list of the nodes with max number of connections
    for i in range(len(conn_count_list)):
        if conn_count_list[i] == max_conn:
            identified_nodes.append(node_list[i])
    return f" The nodes with maximum number of connections are " + str(identified_nodes)


list1 = input('Please enter the router input graph of nodes separated by "->" ').split('->')
print(identify_router(list1))
