# check whether a tree is bst or not
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def is_bst(self,rst):      
        if self.left is not None:
            self.left.is_bst(rst)
        rst.append(self.data)
        if self.right is not None:
            self.right.is_bst(rst)
        return rst

root = TreeNode(31)
root.left = TreeNode(30)
root.right = TreeNode(45)
root.left.left = TreeNode(28)
root.right.left = TreeNode(44)
result=[]
rst= root.is_bst(result)
# rst1=[11,2,3,4,5,6]



for i in range(len(rst)-1):
    flag=0
    if rst[i]<rst[i+1]:
        flag=1
    else:
        break
if flag==1:
    print("bst")
else:
    print("not bst")
