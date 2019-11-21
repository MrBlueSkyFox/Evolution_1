import math
from random import randint, random

from lab4.functions import FUNCTIONS, TERMINALS, FUNCTIONS_WITH_ONE_ARG, MIN_DEPTH
from IPython.display import Image, display
from graphviz import Digraph, Source


class GeneticProgrammingTree:
    def __init__(self, data=None, left=None, right=None):
        self.value = data
        self.left = left
        self.right = right
        self.name_for_debug = self.node_label()

    def naming(self):
        if self.value in FUNCTIONS:
            self.name_for_debug = self.node_label()
        left_b = self.left.naming() if self.left else 0
        right_b = self.right.naming() if self.right else 0

    def size(self):  # tree size in nodes
        if self.value in TERMINALS:
            return 1
        left_branch = self.left.size() if self.left else 0
        right_branch = self.right.size() if self.right else 0
        return 1 + left_branch + right_branch

    def node_label(self):  # string label
        if self.value in FUNCTIONS:
            return self.value.__name__
        else:
            return str(self.value)

    def print_tree_node(self, pr=''):
        print("%s%s" % (pr, self.node_label()))
        if self.left:
            self.left.print_tree_node(pr + "   ")
        if self.right:
            self.right.print_tree_node(pr + "   ")

    # general method for full and grow type init
    def generate_tree(self, full_type, max_depth, depth=0):
        if depth < MIN_DEPTH or (depth < max_depth and not full_type):
            self.value = FUNCTIONS[randint(0, len(FUNCTIONS) - 1)]
        elif depth >= max_depth:
            self.value = TERMINALS[randint(0, len(TERMINALS) - 1)]
        else:  # intermediate depth, full_type
            if random() > 0.5:
                self.value = TERMINALS[randint(0, len(TERMINALS) - 1)]
            else:
                self.value = FUNCTIONS[randint(0, len(FUNCTIONS) - 1)]
        if self.value in FUNCTIONS:
            self.left = GeneticProgrammingTree()
            self.left.generate_tree(full_type, max_depth, depth=depth + 1)
            self.right = GeneticProgrammingTree()
            self.right.generate_tree(full_type, max_depth, depth=depth + 1)

    # generate only full tree
    def generate_full_tree(self, max_depth, depth=0):
        if depth < MIN_DEPTH or depth < max_depth:
            self.value = FUNCTIONS[randint(0, len(FUNCTIONS) - 1)]
        elif depth >= max_depth:
            self.value = TERMINALS[randint(0, len(FUNCTIONS) - 1)]
        if self.value in FUNCTIONS:
            self.left = GeneticProgrammingTree()
            self.left.generate_full_tree(max_depth, depth=depth + 1)
            if self.value not in FUNCTIONS_WITH_ONE_ARG:
                self.right = GeneticProgrammingTree()
                self.right.generate_full_tree(max_depth, depth=depth + 1)

    # generate only grow tree
    def generate_grow_tree(self, max_depth, depth=0):
        if random() > 0.5:
            self.value = TERMINALS[randint(0, len(TERMINALS) - 1)]
        else:
            self.value = FUNCTIONS[randint(0, len(FUNCTIONS) - 1)]
        if self.value in FUNCTIONS:
            self.left = GeneticProgrammingTree()
            self.left.generate_grow_tree(max_depth, depth=depth + 1)
            # print(self.node_label())
            if self.value not in FUNCTIONS_WITH_ONE_ARG:
                self.right = GeneticProgrammingTree()
                self.right.generate_grow_tree(max_depth, depth=depth + 1)
            #     print('Функция с 2 арг')
            # else:
            #     print('Функия с 1 арг')

    def compute_tree(self, x):
        # print("%s" % (self.node_label()))
        if self.value in FUNCTIONS_WITH_ONE_ARG:
            d = 0
            try:
                d = self.value(self.left.compute_tree(x))
                return d
            except Exception as e:
                print(str(e) + '\n')
                return d
        elif self.value in FUNCTIONS:
            d1 = (0)
            try:
                d1 = (self.value(self.left.compute_tree(x), self.right.compute_tree(x)))
                return d1
            except Exception as e:
                print(str(e) + '\n')
                return d1
        elif any(str(self.value) in s for s in TERMINALS):
            return (x)
        else:
            return self.value

    def comp_sec(self, x):
        if self.value in FUNCTIONS_WITH_ONE_ARG:
            d = 0
            try:
                d = self.value(self.left.comp_sec(x))
                return d
            except Exception as e:
                print(str(e) + '\n')
                return d
        elif self.value in FUNCTIONS:
            d1 = (0)
            try:
                d1 = (self.value(self.left.comp_sec(x), self.right.comp_sec(x)))
                return d1
            except Exception as e:
                print(str(e) + '\n')
                return d1
        elif any(str(self.value) in s for s in TERMINALS):
            if self.value == 'x1':
                return x[0]
            if self.value == 'x2':
                return x[1]
            if self.value == 'x3':
                return x[2]
            if self.value == 'x4':
                return x[3]
            if self.value == 'x5':
                return x[4]
            if self.value == 'x6':
                return x[5]
            if self.value == 'x7':
                return x[6]
            if self.value == 'x8':
                return x[7]
            if self.value == 'x9':
                return x[8]
            if self.value == 'x10':
                return x[9]
            return x
        else:
            return self.value

    def build_subtree(self):
        t = GeneticProgrammingTree()
        t.value = self.value
        if self.left:  t.left = self.left.build_subtree()
        if self.right: t.right = self.right.build_subtree()
        return t

    def check_exchangeable(self, node_two, depth):  # depth pass like list for reference
        depth[0] -= 1
        if depth[0] <= 1:
            if not node_two:
                return self.build_subtree()
            else:
                self.value = node_two.value
                self.left = node_two.left
                self.right = node_two.right
        else:
            ret = None
            if self.left and depth[0] > 1:
                ret = self.left.check_exchangeable(node_two, depth)
            if self.right and depth[0] > 1:
                ret = self.right.check_exchangeable(node_two, depth)
            return ret

    def cut_mutation(self):
        tree_size = self.size()
        number_to_cut = [randint(0, tree_size)]
        self._cut_mut(number_to_cut)

    def _cut_mut(self, depth):
        depth[0] -= 1
        if depth[0] <= 1:
            self.value = TERMINALS[randint(0, len(TERMINALS) - 1)]
            self.left = None
            self.right = None
        else:
            if self.left and depth[0] > 1:
                self.left._cut_mut(depth)
            if self.right and depth[0] > 1:
                self.right._cut_mut(depth)

    # Не проверено! Рисование дерева в png
    def draw(self, dot, count):  # dot & count are lists in order to pass "by reference"
        node_name = str(count[0])
        dot[0].node(node_name, self.node_label())
        if self.left:
            count[0] += 1
            dot[0].edge(node_name, str(count[0]))
            self.left.draw(dot, count)
        if self.right:
            count[0] += 1
            dot[0].edge(node_name, str(count[0]))
            self.right.draw(dot, count)

    def draw_tree(self, fname, footer):
        dot = [Digraph()]
        dot[0].attr(kw='graph', label=footer)
        count = [0]
        self.draw(dot, count)
        Source(dot[0], filename=fname + ".gv", format="png").render()
        display(Image(filename=fname + ".gv.png"))
