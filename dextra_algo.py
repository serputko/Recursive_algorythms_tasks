class DextraAlgo:
    graph = {'start': {'A': 2, 'B': 5}, 'A': {'C': 7, 'B': 8}, 'B': {'C': 2, 'D': 4}, 'C': {'end': 1},
             'D': {'C': 6, 'end': 3}, 'end': {}}
    costs = {'A': graph['start']['A'], 'B': graph['start']['B'], 'C': float('inf'), 'D': float('inf'),
             'end': float('inf')}
    parents = {'A': 'start', 'B': 'start', 'C': None, 'D': None, 'end': None}
    processed_nodes = []

    def find_lowest_cost(self, cost):
        lowest_cost_node = None
        lowest_cost = float('inf')
        for n in cost:
            if cost[n] < lowest_cost and n not in self.processed_nodes:
                lowest_cost = cost[n]
                lowest_cost_node = n
        return lowest_cost_node

    def dextra_algo(self):
        node = self.find_lowest_cost(self.costs)
        while node is not None:
            cost = self.costs[node]
            neighbors = self.graph[node]
            for n in neighbors:
                new_cost = cost + neighbors[n]
                if self.costs[n] > new_cost:
                    self.costs[n] = new_cost
                    self.parents[n] = node
            self.processed_nodes.append(node)
            node = self.find_lowest_cost(self.costs)
        self.get_chain()

    def get_chain(self):
        parents = self.parents
        chain = []
        start_node = 'end'
        while start_node != 'start':
            chain.append(start_node)
            start_node = parents[start_node]
        chain.append('start')
        print('The fastest route:')
        print(chain[::-1])



dex = DextraAlgo()
dex.dextra_algo()
