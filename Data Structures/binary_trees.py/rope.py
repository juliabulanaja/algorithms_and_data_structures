class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None
        self.weight = 1  
        self.height = 1

    def __str__(self):
        return f"Value: {self.value}"
  

class Rope:
    def __init__(self, string, queries):
        self.string = string
        self.queries = queries
        self.root = self.build_avl(self.string)
        self.execute_queries()

    
    def update_weight_height(self, node):
        if not node:
            return
        
        left_weight = node.left_child.weight if node.left_child else 0
        right_weight = node.right_child.weight if node.right_child else 0
        node.weight = left_weight + right_weight + 1

        left = node.left_child.height if node.left_child else 0
        right = node.right_child.height if node.right_child else 0
        node.height = max(left, right) + 1
        

    def balance_factor(self, node):
        if not node: 
            return 0
        left = node.left_child.height if node.left_child else 0
        right = node.right_child.height if node.right_child else 0
        return left - right


    def rebalance_left_left(self, node):
        parent = node.parent
        y = node.left_child
        x = y.left_child

        t3 = y.right_child

        y.parent = parent
        # if parent is None:
        #     self.root = y

        if parent:
            if parent.left_child == node:
                parent.left_child = y
            else:
                parent.right_child = y

        y.left_child, x.parent = x, y
        y.right_child, node.parent = node, y

        node.left_child = t3
        if t3:
            t3.parent = node

        self.update_weight_height(node) # New right child
        self.update_weight_height(x)    # New left child
        self.update_weight_height(y)    # The new root of this subtree

        return y


    def rebalance_left_right(self, node):
        parent = node.parent
        y = node.left_child
        x = y.right_child

        t2 = x.left_child
        t3 = x.right_child

        x.parent = parent
        # if parent is None:
        #     self.root = x
        if parent:
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

        self.update_weight_height(y)       # New right child
        self.update_weight_height(node)    # New left child
        self.update_weight_height(x)       # The new root of this subtree

        return x


    def rebalance_right_right(self, node):
        parent = node.parent
        y = node.right_child
        x = y.right_child

        t2 = y.left_child

        y.parent = parent
        # if parent is None:
        #     self.root = y
        if parent:
            if parent.left_child == node:
                parent.left_child = y
            else:
                parent.right_child = y

        y.left_child, node.parent = node, y
        y.right_child, x.parent = x, y

        node.right_child = t2
        if t2:
            t2.parent = node

        self.update_weight_height(node)    # New left child
        self.update_weight_height(x)       # New right child
        self.update_weight_height(y)       # The new root of this subtree

        return y


    def rebalance_right_left(self, node):
        parent = node.parent
        y = node.right_child
        x = y.left_child

        t2 = x.left_child
        t3 = x.right_child

        x.parent = parent
        # if parent is None:
        #     self.root = x
        if parent:
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

        self.update_weight_height(node) # New right child
        self.update_weight_height(y)    # New left child
        self.update_weight_height(x)    # The new root of this subtree

        return x


    def rebalance(self, node):
        root = node
        
        while node:
            root = node
            
            self.update_weight_height(node)
            bf = self.balance_factor(node)
            next_node = node.parent
            
            if bf > 1:
                if self.balance_factor(node.left_child) >= 0:
                    root = self.rebalance_left_left(node)
                else:
                    root = self.rebalance_left_right(node)

            elif bf < -1:
                if self.balance_factor(node.right_child) <= 0:
                    root = self.rebalance_right_right(node)
                else:
                    root = self.rebalance_right_left(node)

            node = next_node

        self.root = root
        return root
    

    def build_avl(self, chars):
        if not chars:
                return None

        mid = len(chars) // 2

        root = Node(chars[mid])
        root.left_child = self.build_avl(chars[:mid])
        root.right_child = self.build_avl(chars[mid+1:])

        if root.left_child:
            root.left_child.parent = root
        if root.right_child:
            root.right_child.parent = root

        self.update_weight_height(root)
        return root


    def print_structured_tree(self, node=None, tab=0):

        if tab == 0 and node == None:
            print('The tree is empty')
            return 

        if node == None:
            return

        T = '\t'
        
        self.print_structured_tree(node.right_child, tab=tab+1)
        print()
        print(f"{T * tab} {node.value}")
        print()
        self.print_structured_tree(node.left_child, tab=tab+1)
        
       
    def print_string(self, node=None, root=True):
        if root == True:
            node = self.root

        if node is None:
            return ""
        
        self.print_string(node.left_child, False)
        print(node.value, end="")
        self.print_string(node.right_child, False)
            

    def find_largest_node(self, root):
        if not root:
            return None
        if root.right_child:
            return self.find_largest_node(root.right_child) 
        else:   
            return root


    def find_smallest_node(self, root):
        if not root:
            return None
        if root.left_child:
            return self.find_smallest_node(root.left_child) 
        else:
            return root

    
    def delete_biggest_node(self, root): # delete the biggest node in the tree
        if not root:
            return None, None

        node_to_delete = self.find_largest_node(root)
        parent = node_to_delete.parent
        left_child = node_to_delete.left_child

        node_to_delete.left_child = None
        node_to_delete.right_child = None
        node_to_delete.parent = None

        if parent:
            parent.right_child = left_child
            if left_child:
                left_child.parent = parent

            new_root = self.rebalance(parent)
            
            return node_to_delete, new_root
        else:
            return node_to_delete, left_child
        

    def delete_smallest_node(self, root): # delete the smallest node in the tree
        if not root:
            return None, None

        node_to_delete = self.find_smallest_node(root)
        parent = node_to_delete.parent
        right_child = node_to_delete.right_child

        node_to_delete.left_child = None
        node_to_delete.right_child = None
        node_to_delete.parent = None

        if parent:
            parent.left_child = right_child
            if right_child:
                right_child.parent = parent

            new_root = self.rebalance(parent)
        
            return node_to_delete, new_root
        else:
            return node_to_delete, right_child


    def merge_with_root(self, r1, r2, root):
        if not root:
            return None
        root.left_child = r1
        root.right_child = r2
        if r1:
            r1.parent = root

        if r2:
            r2.parent = root

        self.update_weight_height(root)
        return root


    def merge(self, root1, root2):
        if not root1: 
            return root2
        if not root2: 
            return root1

        if root1.height >= root2.height:
            deleted_node, root1 = self.delete_biggest_node(root1)
        
        else:
            deleted_node, root2 = self.delete_smallest_node(root2)

        new_root = self.merge_with_root(root1, root2, deleted_node)
        new_root = self.rebalance(new_root)
           
        return new_root


    def split(self, root, k):

        if root == None:
            return None, None

        left_weight = root.left_child.weight if root.left_child else 0

        if k <= left_weight: 
            r1, r2 = self.split(root.left_child, k) 
            if r1: 
                r1.parent = None 

            self.update_weight_height(r1)
            self.update_weight_height(r2)
            
            root.left_child = None 

            r3 = self.merge_with_root(r2, root.right_child, root) 
            if r3: 
                r3.parent = None 

            r3 = self.rebalance(r3) 

            return r1, r3


        else:
            new_k = k - left_weight - 1 
            r1, r2 = self.split(root.right_child, new_k) 
            if r2: 
                r2.parent = None 

            self.update_weight_height(r1)
            self.update_weight_height(r2)
            
            root.right_child = None 
            
            r3 = self.merge_with_root(root.left_child, r1, root) 
            if r3: 
                r3.parent = None 

            r3 = self.rebalance(r3) 
            return r3, r2


    def execute_queries(self):

        for i, j, k  in self.queries:
            
            left_chunk, remaining_chunk = self.split(self.root, i) 

            if left_chunk:
                j = j - left_chunk.weight + 1
            else:
                j += 1

            extracted_substring, right_chunk = self.split(remaining_chunk, j)
            tree_without_substring = self.merge(left_chunk, right_chunk)


            before_insert, after_insert = self.split(tree_without_substring, k)
            merged_with_substring = self.merge(before_insert, extracted_substring)

            self.root = self.merge(merged_with_substring, after_insert)

      
if __name__ == "__main__":

    string = input()
    n = int(input())
    queries = [list(map(int, input().split())) for _ in range(n)]

    rope = Rope(string, queries)
    rope.print_string()
    print()

