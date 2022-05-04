from collections import deque
from heapq import heappush, heappop 



def shortest_shortest_path(graph, source):
    d = dict()
    frontier = []
  
    y = (0,0, source)
    heappush(frontier, y)

    return short2_path(d, frontier, graph)

def short2_path(d, frontier, graph):
    l = len(frontier)
    if l !=0 :
        dist, edge , n= heappop(frontier)
        if n not in d:
            d[n] = (dist, edge)
            for neighbor, w in graph[n]:
              dw = dist + w
              x = (dw, edge + 1, neighbor)
              heappush(frontier, x)                
        return short2_path(d, frontier, graph)
      
        if n in d:
            return short2_path(d, frontier, graph)
  
    else:
        return d
      
def test_shortest_shortest_path():

    graph = {
                's': {('a', 1), ('c', 4)},
                'a': {('b', 2)}, # 'a': {'b'},
                'b': {('c', 1), ('d', 4)}, 
                'c': {('d', 3)},
                'd': {},
                'e': {('d', 0)}
            }
    result = shortest_shortest_path(graph, 's')
    # result has both the weight and number of edges in the shortest shortest path
    assert result['s'] == (0,0)
    assert result['a'] == (1,1)
    assert result['b'] == (3,2)
    assert result['c'] == (4,1)
    assert result['d'] == (7,2)
    
    
def bfs_path(graph, source):
    final = dict() 
    frontier = set([source])
    while len(frontier):
      l = len(frontier)
      if l != 0:
        source = frontier.pop()
        for n in graph[source]: 
          if n not in final.keys():
            final[n] = source
            frontier.add(n)
    return final

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }

def test_bfs_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    assert parents['a'] == 's'
    assert parents['b'] == 's'    
    assert parents['c'] == 'b'
    assert parents['d'] == 'c'
    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    ###TODO
    if destination in parents:
        return get_path(parents, parents[destination]) + parents[destination]
    else:
        return ''
    pass

def test_get_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    assert get_path(parents, 'd') == 'sbc'
