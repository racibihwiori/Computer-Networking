import heapq

def dijkstra_algorithm(graph, start_node):
    num_nodes = len(graph)
    distances = [float('infinity')] * num_nodes
    predecessors = [None] * num_nodes
    distances[start_node] = 0
    pq = [(0, start_node)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in enumerate(graph[current_node]):
            if weight == float('infinity'):
                continue
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return distances, predecessors

def format_output(distances, predecessors):
    formatted_output = []
    for node in range(len(distances)):
        predecessor = 'none' if predecessors[node] is None else chr(predecessors[node] + ord('a'))
        distance = 'inf' if distances[node] == float('infinity') else str(distances[node])
        formatted_output.append(f"{predecessor},{distance}")
    return formatted_output

graph_str = '''
a	0	1		3	5								17		
b	1	0	11	16											
c		11	0	18	6		9		15			20			12
d	3	16	18	0	15		15								
e	5		6	15	0	15								10	
f					15	0			9		12				
g			9	15			0	4				3			
h							4	0	16	13					
i			15			9		16	0						
j								13		0		1			12
k						12					0		2	7	5
l			20				3			1		0	10		
m	17										2	10	0	13	
n					10						7		13	0	
o			12							12	5				0
'''

# Convert the graph string to a list of lists
graph = [list(map(lambda x: float('infinity') if x == '' else int(x), row.split('\t')[1:])) for row in graph_str.strip().split('\n')]

# Replace 12 with the index of the start node (Node 'm') assuming 'a' is 0, 'b' is 1, and so on.
start_node_index = 12
distances, predecessors = dijkstra_algorithm(graph, start_node_index)
output = format_output(distances, predecessors)

# Output formatting
output_str = ','.join(output)
semicolon_index = output_str.index(',none')
formatted_output = f"{output_str[:semicolon_index]}; {output_str[semicolon_index + 1:]}"
print(formatted_output)
