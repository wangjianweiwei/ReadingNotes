class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def is_empty(self):
        return self.__head is None

    def append(self, value):
        node = Node(value)
        if self.is_empty():
            self.__head = node
        else:
            self.__tail.next = node

        self.__tail = node

    def insert(self, pos, value):
        node = Node(value)
        if pos > len(self):
            self.__tail.next = node
            self.__tail = node
        elif pos <= 0:
            node.next = self.__head
            self.__head = node
        else:
            current_pos = 0
            pre = self.__head  # type: Node
            while current_pos != (pos - 1):
                current_pos += 1
                pre = pre.next

            node.next = pre.next
            pre.next = node

    def delete(self, value):
        current = self.__head  # type: Node
        pre = None
        while current:
            if current.data == value:
                if current == self.__head:
                    self.__head = current.next
                else:
                    pre.next = current.next
                break
            else:
                pre = current
                current = current.next

        else:
            raise ValueError

    def __len__(self):
        count = 0
        for _ in self:
            count += 1

        return count

    def __iter__(self):
        current = self.__head  # type: Node
        while current:
            yield current.data
            current = current.next


if __name__ == '__main__':
    link = LinkList()
    link.append(0)
    link.append(2)
    link.append(3)
    link.append(4)
    link.insert(1, 1)
    link.insert(5, 5)
    link.delete(0)
    link.delete(1)
    link.delete(2)
    link.delete(3)
    link.delete(4)
    # link.delete(5)

    if not link.is_empty():
        print("长度: ", len(link))
        for n in link:
            print(n)
    else:
        print("LinkList为空")
