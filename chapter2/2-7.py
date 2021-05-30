class Tree:
    def __init__(self, left, right):
        self.left = left
        self.right = right

if __name__ == "__main__":
    t = Tree(Tree("a", "b"), Tree("c", "d"))
    print(t.right.left)