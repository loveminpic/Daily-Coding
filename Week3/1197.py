import sys 
input = sys.stdin.readline

class nodes :
    def __init__(self,first,end,value) :
        self.first = first
        self.end = end
        self.value = value

node,line = map(int, input().split())
node_table = []
for i in range(0,line) :
    a,b,c = map(int, input().split())
    node_table.append(nodes(a,b,c))
    

cycle_table = [[] for i in range(node+1)]

for i in range(1, node+1) :
    cycle_table[i] = i
    
node_table = sorted(node_table, key=lambda node: node.value)
mx = 0

def check_parent(cycle_table, index):
    if cycle_table[index] == index:
        return index

    cycle_table[index] = check_parent(cycle_table, cycle_table[index])
    return cycle_table[index]
    
for i in range(0, line):
    a_parent = check_parent(cycle_table, node_table[i].first)
    b_parent = check_parent(cycle_table, node_table[i].end)

    if a_parent != b_parent:
        if a_parent > b_parent:
            cycle_table[a_parent] = b_parent
        else:
            cycle_table[b_parent] = a_parent
        mx += node_table[i].value
print(mx)
