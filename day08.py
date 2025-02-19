class TreeNode:
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None




del_group = '에이핑크'

if __name__ == "__main__":
    groups = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']
    root = None

    node = TreeNode()
    node.data = groups[0]
    root = node

    for group in groups[1:]:
        node = TreeNode()
        node.data = group
        current = root
        while True:
            if group < current.data:
                if current.left is None:
                    current.left = node
                    break
                current = current.left          # move
            else:
                if group > current.data:
                    if current.right is None:
                        current.right = node
                        break
                current = current.right         # move
    print("BST 구성 완료")

    find_group = input()

    current =root
    while True:
        if find_group == current.data:
            print(f"{find_group}을(를) 찾았습니다.")
            break
        elif find_group < current.data:
            if current.left is None:
                print(f"{find_group}가 존재하지 않습니다.")
                break
            current = current.left
        else:
            if current.right is None:
                print(f"{find_group}가 존재하지 않습니다.")
                break
            current = current.right



# 자식이 둘 있고 재귀..
#             블랙핑크(current)
#     레드벨벳           에이핑크
# 걸스데이    마마무             트와이스

while True:
    if del_group == current.data:
        # 지우려는 노드가 현재 노드일 경우(뿌리에서 내려가기)
        # 근데 뿌리가 지우려는 코드면 어카지?

        # 1. 지우려는 노드가 리프 노드일 경우
        if current.left == None and current.right == None:
            # 부모 노드가 나를 왼쪽으로 품은 경우
            if root.left == current:
                root.left = None
            # 부모 노드가 나를 오른쪽으로 품은 경우
            else:
                root.right = None

            del(current)

        # 2. 지우려는 노드가 자식 노드를 한 개 보유할 경우(left)
        elif current.left != None and current.right == None:
            # 2-1 부모 노드가 나를 왼쪽으로 품은 경우
            if root.left == current:
                root.left = current.left
            # 2-2 부모 노드가 나를 오른쪽으로 품은 경우
            else:
                root.right = current.left

            del(current)

        # 3. 지우려는 노드가 자식 노드를 한 개 보유할 경우(right)
        elif current.left == None and current.right != None:
            # 3-1 부모 노드가 나를 왼쪽으로 품은 경우
            if root.left == current:
                root.left = current.right
            # 3-2 부모 노드가 나를 오른쪽으로 품은 경우
            else:
                root.right = current.right

            del(current)

        # 4. 지우려는 노드가 자식 노드를 두 개 보유할 경우
        # 오른쪽 자식 노드를 부모 노드랑 연결, 왼쪽 자식 노드는
        else:
            # 4-1 부모 노드가 나를 왼쪽으로 품은 경우
            if root.left == current:
            pass



