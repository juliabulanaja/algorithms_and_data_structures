class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None
        self.height = 1
        self.num = 0

    def __str__(self):
        return f"{self.value}"


    def __repr__(self):
        return f"{self.value}"


class BinaryTree:
    def __init__(self):
        self.root = None
        self.mod = 1_000_000_001
        self.x = 0


    def find_closest(self, value: int, root=None) -> TreeNode:
        """ Find the exact node with value == value or some the parent node where the new node with value can be placed. """

        if root is None:
            root = self.root

        current_node = root
        while current_node:
            if value == current_node.value: # found the exact node with value
                break

            elif value < current_node.value:        # left child
                if not current_node.left_child:
                    break
                else:
                    current_node = current_node.left_child
            else:                                   # right child
                if not current_node.right_child:
                    break
                else:
                    current_node = current_node.right_child

        return current_node


    def add(self, value: int) -> None:
        """ Add the value on the tree if such value does not exist. Make rebalance. """

        value = self.define_value(value)
        new_node = TreeNode(value)

        if not self.root:
            self.root = new_node
            return

        nearest = self.find_closest(value)

        if nearest.value == value:
            return
        
        elif nearest.value > value:
            nearest.left_child = new_node
        else:
            nearest.right_child = new_node
        new_node.parent = nearest

        self.rebalance(new_node)


    def define_value(self, value: int) -> int:
        """Recalculate the value by the formula ((i + x) mod M)."""

        return (value + self.x) % self.mod


    def find(self, value: int) -> None:
        """Print 'Found' is node exists and 'Not found' if doesn't. """

        value = self.define_value(value)

        nearest = self.find_closest(value)
        if nearest and nearest.value == value:
            print('Found')
        else:
            print('Not found')
    

    def delete(self, value: int) -> None:
        """Delete the node from the tree. Make rebalance. """

        value = self.define_value(value)
        node_to_delete = self.find_closest(value)
        if not node_to_delete or node_to_delete.value != value:
            return
        
        parent = node_to_delete.parent

        # node_to_delete has only left child
        if node_to_delete.left_child and not node_to_delete.right_child:

            node_to_move = node_to_delete.left_child
            rebalance_start_point = parent

            if not parent:
                self.root = node_to_move
                self.root.parent = None

            elif parent.left_child == node_to_delete:
                parent.left_child = node_to_move
                node_to_move.parent = parent
            else:
                parent.right_child = node_to_move
                node_to_move.parent = parent


        # node_to_delete has a right child
        elif node_to_delete.right_child:   


            node_to_move = self.find_next(node_to_delete)       # exists for sure
            node_to_move_parent = node_to_move.parent           # exists for sure
            node_to_move_right_child = node_to_move.right_child # may exist or not

            if node_to_move_parent != node_to_delete:
                rebalance_start_point = node_to_move_parent
            else:
                rebalance_start_point = node_to_move

            # replacing the node_to_move with it's right_child if exists
            if node_to_move_parent != node_to_delete:
        
                if node_to_move_parent.left_child == node_to_move:
                    node_to_move_parent.left_child = node_to_move_right_child
                else:
                    node_to_move_parent.right_child = node_to_move_right_child
                if node_to_move_right_child:
                    node_to_move_right_child.parent = node_to_move_parent
            
                
            # replacing node_to_delete with node_to_move
            if node_to_delete == self.root:
                self.root = node_to_move
                node_to_move.parent = None
            else:
                if parent.left_child == node_to_delete:
                    parent.left_child = node_to_move
                else:
                    parent.right_child = node_to_move
                node_to_move.parent = parent

            # replacing left and right child of node_to_move
            node_to_move.left_child = node_to_delete.left_child     # may exist ot not
            if node_to_move.left_child:
                node_to_move.left_child.parent = node_to_move

            if node_to_move_parent != node_to_delete:
                node_to_move.right_child = node_to_delete.right_child
                if node_to_move.right_child:
                    node_to_move.right_child.parent = node_to_move

        # no childs
        else:                                   
            if not parent:
                self.root = None
            elif parent.left_child == node_to_delete:
                parent.left_child = None
            else:
                parent.right_child = None

            rebalance_start_point = parent

        self.rebalance(rebalance_start_point)


    def initialize(self, commands: list) -> None:
        """Execute all commands. """
        
        for op, *args in commands:
            # print(f'Starting: {op} with arg {args}')
            if op == '+':
                self.add(*args)
            elif op == '-':
                self.delete(*args)
            elif op == '?':
                self.find(*args)
            elif op == 's':
                self.find_range_sum(*args)


    def find_next(self, node: TreeNode) -> TreeNode:
        """Find the next node ascending by value."""

        if node.right_child:
            return self.left_descendant(node.right_child)
        else:
            return self.right_ancestor(node)


    def left_descendant(self, node: TreeNode) -> TreeNode:
        if not node.left_child:
            return node
        else:
            return self.left_descendant(node.left_child)


    def right_ancestor(self, node: TreeNode) -> TreeNode:
        while node.parent:
            if node.value < node.parent.value:
                return node.parent
            node = node.parent
        return None
        

    def get_sum_less_then(self, value: int) -> int:
        """Find the sum of nodes less then value."""

        node = self.root
        total = 0

        while node: 
            if node.value <= value:
                left_child_num = node.left_child.num if node.left_child else 0
                total += node.value + left_child_num
                node = node.right_child
            else:
                node = node.left_child

        return total


    def find_range_sum(self, x: int, y: int) -> int:
        """Find the sum in range x <= value <= y."""

        x = self.define_value(x)
        y = self.define_value(y)

        if x > y:
            return 0

        total = self.get_sum_less_then(y) - self.get_sum_less_then(x-1)
        self.x = total
        print(total)


    def get_balance_factor(self, node: TreeNode) -> int:
        """Fint the balance factor."""

        if not node: 
            return 0
        left = node.left_child.height if node.left_child else 0
        right = node.right_child.height if node.right_child else 0
        return left - right


    def update_node_stats(self, node: TreeNode) -> None:
        """Update the node heights and number."""
        if not node:
            return

        left_height = node.left_child.height if node.left_child else 0
        right_height = node.right_child.height if node.right_child else 0
        node.height = 1 + max(left_height, right_height)

        left_num = node.left_child.num if node.left_child else 0
        right_num = node.right_child.num if node.right_child else 0
        node.num = node.value + left_num + right_num        


    def rebalance_left_left(self, node: TreeNode) -> None:
        parent = node.parent
        y = node.left_child
        x = y.left_child

        t3 = y.right_child

        y.parent = parent
        if parent is None:
            self.root = y
        else:
            if parent.left_child == node:
                parent.left_child = y
            else:
                parent.right_child = y

        y.left_child, x.parent = x, y
        y.right_child, node.parent = node, y

        node.left_child = t3
        if t3:
            t3.parent = node

        self.update_node_stats(node) # New right child
        self.update_node_stats(x)    # New left child
        self.update_node_stats(y)    # The new root of this subtree


    def rebalance_right_right(self, node: TreeNode) -> None:
        parent = node.parent
        y = node.right_child
        x = y.right_child

        t2 = y.left_child

        y.parent = parent
        if parent is None:
            self.root = y
        else:
            if parent.left_child == node:
                parent.left_child = y
            else:
                parent.right_child = y

        y.left_child, node.parent = node, y
        y.right_child, x.parent = x, y

        node.right_child = t2
        if t2:
            t2.parent = node

        self.update_node_stats(node)    # New left child
        self.update_node_stats(x)       # New right child
        self.update_node_stats(y)       # The new root of this subtree

    
    def rebalance_left_right(self, node: TreeNode) -> None:
        parent = node.parent
        y = node.left_child
        x = y.right_child

        t2 = x.left_child
        t3 = x.right_child

        x.parent = parent
        if parent is None:
            self.root = x
        else:
            if parent.left_child == node:
                parent.left_child = x
            else:
                parent.right_child = x

        x.left_child, y.parent = y, x
        x.right_child, node.parent = node, x

        y.right_child = t2
        if t2:
            t2.parent = y
        
        node.left_child = t3
        if t3:
            t3.parent = node

        self.update_node_stats(y)       # New right child
        self.update_node_stats(node)    # New left child
        self.update_node_stats(x)       # The new root of this subtree


    def rebalance_right_left(self, node: TreeNode) -> None:
        parent = node.parent
        y = node.right_child
        x = y.left_child

        t2 = x.left_child
        t3 = x.right_child

        x.parent = parent
        if parent is None:
            self.root = x
        else:
            if parent.left_child == node:
                parent.left_child = x
            else:
                parent.right_child = x

        x.left_child, node.parent = node, x  
        x.right_child, y.parent = y, x
        
        node.right_child = t2
        if t2:
            t2.parent = node

        y.left_child = t3
        if t3:
            t3.parent = y

        self.update_node_stats(node) # New right child
        self.update_node_stats(y)    # New left child
        self.update_node_stats(x)    # The new root of this subtree
     

    def rebalance(self, node: TreeNode) -> None:
        """Rebalance the tree checking every node if it has unbalance factor."""

        while node:

            self.update_node_stats(node)
            bf = self.get_balance_factor(node)
            next_node = node.parent

            if bf > 1:
                if self.get_balance_factor(node.left_child) >= 0:
                    self.rebalance_left_left(node)
                else:
                    self.rebalance_left_right(node)

            elif bf < -1:
                if self.get_balance_factor(node.right_child) <= 0:
                    self.rebalance_right_right(node)
                else:
                    self.rebalance_right_left(node)
    
            node = next_node
            
        

if __name__ == "__main__":
    n = int(input())

    commands = []
    for _ in range(n):
        operation, *args = input().split(' ')
        commands.append((operation, *list(map(int, args))))

    tree = BinaryTree()
    tree.initialize(commands)
