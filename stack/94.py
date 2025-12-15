from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)
        return res


def build_tree(level_order: List[Optional[int]]) -> Optional[TreeNode]:
    if not level_order:
        return None
    nodes = [None if v is None else TreeNode(v) for v in level_order]
    kid = 1
    for i, node in enumerate(nodes):
        if node is None:
            continue
        if kid < len(nodes):
            node.left = nodes[kid]
            kid += 1
        if kid < len(nodes):
            node.right = nodes[kid]
            kid += 1
    return nodes[0]


if __name__ == "__main__":
    sol = Solution()

    # 例子1：root = [1, null, 2, 3] -> [1, 3, 2]
    root1 = build_tree([1, None, 2, 3])
    print(sol.inorderTraversal(root1))  # [1, 3, 2]

    # 例子2：root = [] -> []
    root2 = build_tree([])
    print(sol.inorderTraversal(root2))  # []

    # 例子3：root = [1] -> [1]
    root3 = build_tree([1])
    print(sol.inorderTraversal(root3))  # [1]

    # 例子4：root = [2, 1, 3] -> [1, 2, 3]
    root4 = build_tree([2, 1, 3])
    print(sol.inorderTraversal(root4))  # [1, 2, 3]

    # 例子5：root = [4, 2, 6, 1, 3, 5, 7] -> [1,2,3,4,5,6,7]
    root5 = build_tree([4, 2, 6, 1, 3, 5, 7])
    print(sol.inorderTraversal(root5))  # [1, 2, 3, 4, 5, 6, 7]