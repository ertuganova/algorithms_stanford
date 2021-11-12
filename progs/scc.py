import sys, threading

def dfs(graph, node, explored, stack):    
    if explored[node] == False:
        explored[node] = True

        if node in graph:
            for v in graph[node]:
                #print(v)
                if explored[v] == False:
                    dfs(graph, v, explored, stack)

            stack.append(node)

        else:
            stack.append(node)

def dfs2(graph, node, explored, rtrn):
    if explored[node] == False:
        explored[node] = True
        rtrn.append(node)
    
        if node in graph:
            for v in graph[node]:
                #print(v)
                if explored[v] == False:
                    dfs2(graph, v, explored, rtrn)    
   # scc_cnt = scc
    return len(rtrn)

def main():
    with open('../extra_files/SCC.txt') as f:
        scc = [x.split(' ') for x in f.read().split('\n')]

    print('File opened')

    scc_dict = {}
    for i in scc:
        if i[0] not in scc_dict:
            scc_dict[i[0]] = [i[1]]
        else:
            scc_dict[i[0]] += [i[1]]

    scc_dict_rev = {}
    for i in scc:
        if i[1] not in scc_dict_rev:
            scc_dict_rev[i[1]] = [i[0]]
        else:
            scc_dict_rev[i[1]] += [i[0]]

    all_vertexes = set(list(scc_dict.keys())+list(scc_dict_rev.keys()))
    all_vert_dict = {}
    for i in all_vertexes:
        all_vert_dict[i] = False

    print('Dicts created')

    stack = []
    for node in scc_dict.keys():
        dfs(scc_dict, node, all_vert_dict, stack)

    print('1st DFS doe')

    stack=stack[::-1]
    all_vert_dict = {}
    for i in all_vertexes:
        all_vert_dict[i] = False
    #scc_count = 0
    exp_global = []
    for node in stack:
        #scc_count = 0
        scc_n = dfs2(scc_dict_rev, node, all_vert_dict, [])
        exp_global.append(scc_n)

    print(sorted(exp_global, reverse=True)[:5])

if __name__ == '__main__':
    sys.setrecursionlimit(800000)
    threading.stack_size(67108864)
    thread = threading.Thread(target=main)  # instantiate thread object
    thread.start()  # run program at target