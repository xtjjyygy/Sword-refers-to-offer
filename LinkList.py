# 定义一个头结点，左边指向队列的开头，
# 右边指向队列的末尾，保证我们插入一个元素和取出一个元素都是O(1)的操作
class Head:
    def __init__(self):
        self.left = None
        self.right = None


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        # 初始化节点
        self.head = Head()

    def enqueue(self, value):
        # 插入元素，先新建一个结点
        newnode = Node(value)
        p = self.head
        if p.right:
            # 如果head结点的右边不为None
            # 说明队列中已经有元素了

            temp = p.right
            p.right = newnode
            temp.next = newnode
        else:
            # 队列为空，插入第一个元素
            p.right = newnode
            p.left = newnode

    def dequeue(self):
        p = self.head
        if p.left and (p.left == p.right):
            # 这说明队列中已经有元素
            # 但是这是最后一个元素
            temp = p.left
            p.left = p.right = None
            return temp.value
        elif p.left and (p.left != p.right):
            # 说明队列中有元素，而且不止一个
            temp = p.left
            p.left = temp.next
            return temp.value

        else:
            # 队列为空，抛出查询错误
            raise LookupError('queue is empty')

    def is_empty(self):
        if self.head.left:
            return False
        else:
            return True

    def top(self):
        # 查询目前队列中最早入队的元素
        if self.head.left:
            return self.head.left.value
        else:
            raise LookupError('queue is empty')


if __name__ == '__main__':
    queue = Queue()
    print(queue.is_empty())
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    print(queue.is_empty())
    print(queue.dequeue())
    print(queue.dequeue())

    print(queue.top())
