import random
import sys
from itertools import product

class Rules(dict):
    def __init__(self, dimentions):
        super().__init__(self)
        combinations = product(['0','1'], repeat=dimentions)
        for x in combinations:
            self[''.join(x)] = random.randint(0,1)

class RBN:
    def __init__(self, n: int = 20, m: int = 3, seed: int = None):
        self.nodes = [self.Node(x,random.randint(0,1)) for x in range(0, n)]
        self.rules = Rules(m)
        self.seed = seed or random.randrange(sys.maxsize)
        random.seed(self.seed)
        for node in self.nodes:
            node.connect(random.choices(population=self.nodes, k=m))

    def iterate(self):
        current_states = {}
        for node in self.nodes:
            current_states[node.id] = node.current_state
        for node in self.nodes:
            node.state = self.rules[current_states[node.id]]
        del(current_states)
        

    class Node:
        def __init__(self, id: int = None, initial_state: bin = None):
            self.id = id
            self.state = initial_state or random.randint(0,1)
            self.neighbours = []
            self.mutation_rate = random.random()
        
        def connect(self, neighbours):
            for x in neighbours:
                self.neighbours.append(x)
        
        @property
        def current_state(self):
            if (random.random() <= self.mutation_rate):
                return ''.join([str((n.state + 1) % 2) for n in self.neighbours])
            return ''.join([str(n.state) for n in self.neighbours])
        
        def __str__(self):
            return self.state

        
    