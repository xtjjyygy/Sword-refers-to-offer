#方法一：
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None


class Solution(object):
    def CreateList(self,nums):
        dummy = ListNode(0)
        head = dummy
        for num in nums:
            head.next = ListNode(num)
            head = head.next
        return dummy.next

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def partition(start, end):
            node = start.next.next
            pivotPrev = start.next
            pivotPrev.next = end
            pivotPost = pivotPrev
            while node != end:
                temp = node.next
                if node.val > pivotPrev.val:
                    node.next = pivotPost.next
                    pivotPost.next = node
                elif node.val < pivotPrev.val:
                    node.next = start.next
                    start.next = node
                else:
                    node.next = pivotPost.next
                    pivotPost.next = node
                    pivotPost = pivotPost.next
                node = temp
            return [pivotPrev, pivotPost]
        def quickSort(start,end):
            if start.next != end:
                prev,post = partition(start,end)
                quickSort(start,prev)
                quickSort(post,end)



        dummy = ListNode(0)
        dummy.next = head
        quickSort(dummy,None)
        return dummy.next
    def outputList(self,head):
        if head is None:
            return []
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res


if __name__ == "__main__":
    nums = [1,5,2,6,3,9,6]
    sol = Solution()
    head = sol.CreateList(nums=nums)
    SortHead = sol.sortList(head)
    print(sol.outputList(SortHead))


#方法二
class Node():
    def __init__(self, item=None):
        self.item = item
        self.next = None

class LinkList():
    def __init__(self):
        self.head = None


    def create(self, item):
        self.head = Node(item[0])
        p = self.head
        for i in item[1:]:
            p.next = Node(i)
            p = p.next


    def print(self):
        p = self.head
        while p != None:
            print(p.item, end=' ')
            p = p.next
        print()

    def getItem(self, index):
        p = self.head
        count = 0
        while count != index:
            p = p.next
            count += 1
        return p.item

    def setItem(self, index, item):
        p = self.head
        count = -1
        while count < index - 1:
            p = p.next
            count += 1
        p.item = item


    def swapItem(self, i, j):
        t = self.getItem(j)
        self.setItem(j, self.getItem(i))
        self.setItem(i, t)

    def quicksortofloop(self, left, right):
        if left < right:
            i = left
            j = i + 1
            start = self.getItem(i)


            while (j <= right):
                while (j <= right and self.getItem(j) >= start):
                    j += 1
                if (j <= right):
                    i += 1
                    self.swapItem(i, j)
                    self.print()
                    j += 1
            self.swapItem(left, i)
            self.quicksortofloop(left, i - 1)
            self.quicksortofloop(i + 1, right)


if __name__ == "__main__":
    L = LinkList()
    L.create([4, 2, 5, 3, 7, 9, 0, 1])
    L.quicksortofloop(0, 7)
    L.print()

#方法三
#方法二
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkList():
    def create(self, item):
        head = ListNode(item[0])
        p = head
        for i in item[1:]:
            p.next = ListNode(i)
            p = p.next
        return head


    def print(self,head):
        p = head
        res = []
        while p != None:
            res.append(p.val)
            p = p.next
        return res


    def quicksortofloop(self,head):
        def partition(start, end):
            node = start.next.next
            pivotPrev = start.next
            pivotPrev.next = end
            pivotPost = pivotPrev
            while node != end:
                temp = node.next
                if node.val > pivotPrev.val:
                    node.next = pivotPost.next
                    pivotPost.next = node
                elif node.val < pivotPrev.val:
                    node.next = start.next
                    start.next = node
                else:
                    node.next = pivotPost.next
                    pivotPost.next = node
                    pivotPost = pivotPost.next
                node = temp
            return [pivotPrev, pivotPost]

        def quicksort(start, end):
            if start.next != end:
                prev, post = partition(start, end)
                quicksort(start, prev)
                quicksort(post, end)

        newHead = ListNode(0)
        newHead.next = head
        quicksort(newHead, None)
        return newHead.next


if __name__ == "__main__":
    L = LinkList()
    root = L.create([4, 2, 5, 3, 7, 9, 0, 1])
    newRoot = L.quicksortofloop(root)
    print(L.print(newRoot))
