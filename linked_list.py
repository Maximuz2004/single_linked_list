import random as rnd

rnd.seed()


class Node:

    def __init__(self, data):
        self.item = data
        self.ref = None


class Linked_list:

    def __init__(self):
        self.start_node = None
        self.count_items = 0

    def traverse_list(self):
        if self.start_node is None:
            print('List has no element')
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.ref

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node
        self.count_items += 1

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            self.count_items += 1
            return

        n = self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node
        self.count_items += 1

    def insert_after_item(self, x, data):
        n = self.start_node
        # print(n.ref)
        while n is not None:
            if n.item == x:
                break
            n = n.ref
        if n is None:
            print('item not in the list')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
            self.count_items += 1

    def insert_before_item(self, x, data):
        if self.start_node is None:
            print('List has no element')
            return

        if x == self.start_node:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
            self.count_items += 1
            return

        n = self.start_node
        # print(n.ref)
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n.ref is None:
            print('item not in the list')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
            self.count_items += 1

    def insert_at_index(self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
            self.count_items += 1

        i = 1
        n = self.start_node
        while i < index - 1 and n is not None:
            n = n.ref
            i += 1

        if n is None:
            print('Index out of bound')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
            self.count_items += 1

    def get_count(self):
        if self.start_node is None:
            return 0
        n = self.start_node
        count = 0
        while n is not None:
            count += 1
            n = n.ref
        return count

    def search_item(self, x):
        if self.start_node is None:
            print('List has no elements')
            return
        n = self.start_node
        while n is not None:
            if n.item == x:
                print('Item found')
                return True
            n = n.ref
        print('Item not found')
        return False

    def make_new_list(self, nums=None):
        if nums is None:
            nums = int(input('How many nodes? : '))
        if nums == 0:
            return
        for _ in range(nums):
            value = rnd.randrange(0, 101)
            self.insert_at_end(value)

    def delete_at_start(self):
        if self.start_node is None:
            print('The list has no elements to delete')
            return
        self.start_node = self.start_node.ref
        self.count_items -= 1

    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return

        n = self.start_node
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None
        self.count_items -= 1

    def delete_element_by_value(self, value):
        if self.start_node is None:
            print('The list has no elements to delete')
            return

        if self.start_node.item == value:
            self.start_node = self.start_node.ref
            return

        n = self.start_node
        while n.ref is not None:
            if n.ref.item == value:
                break
            n = n.ref

        if n.ref is None:
            print('Item not found in the list')
        else:
            n.ref = n.ref.ref
            self.count_items -= 1

    def reverse(self):
        prev = None
        n = self.start_node
        while n is not None:
            nxt = n.ref
            n.ref = prev
            prev = n
            n = nxt
        self.start_node = prev

    def bulb_sort_data_change(self):
        """ Сортировка списка пусзырьковым методом заменой данных """
        end = None
        while end != self.start_node:
            curr = self.start_node
            while curr.ref != end:
                nxt = curr.ref
                if curr.item > nxt.item:
                    curr.item, nxt.item = nxt.item, curr.item
                curr = curr.ref
            end = curr

    def bulb_sort_link_change(self):
        """ Сортировка сиска пузырьковым методом заменой ссылок """
        end = None
        while end != self.start_node:
            prev = curr = self.start_node
            while curr.ref != end:
                nxt = curr.ref
                if curr.item > nxt.item:
                    curr.ref = nxt.ref
                    nxt.ref = curr
                    if curr != self.start_node:
                        prev.ref = nxt
                    else:
                        self.start_node = nxt
                    curr, nxt = nxt, curr
                prev = curr
                curr = curr.ref
            end = curr

    def merge_lists1(self, list2):
        """ Функция объединения текущего (отсортированного)
        списка с новым"""
        merged_list = Linked_list()
        merged_list.start_node = self.__merge_by_newlist(self.start_node, list2.start_node)
        return merged_list

    @staticmethod
    def __merge_by_newlist(p: Node, q: Node) -> Node:
        """Функция объединяет два связанных списка,
        создавая новый связанный список, и возвращает
        начальный узел нового связанного списка."""
        if p.item <= q.item:
            start_node = Node(p.item)
            p = p.ref
        else:
            start_node = Node(q.item)
            q = q.ref

        em = start_node

        while p is not None and q is not None:
            if p.item <= q.item:
                em.ref = Node(p.item)
                p = p.ref
            else:
                em.ref = Node(q.item)
                q = q.ref
            em = em.ref

        while p is not None:
            em.ref = Node(p.item)
            p = p.ref
            em = em.ref

        while q is not None:
            em.ref = Node(q.item)
            q = q.ref
            em = em.ref
        return start_node

    def merge_lists2(self, list2):
        """ Функция объединяет два списка изменением ссылок"""
        merged_list = Linked_list()
        merged_list.start_node = self.__merge_by_linkChange(self.start_node, list2.start_node)
        return merged_list

    @staticmethod
    def __merge_by_linkChange(p, q):
        """Функция объединяет два связанных списка,
        создавая новый связанный список, и возвращает
        начальный узел нового связанного списка."""
        if p.item <= q.item:
            start_node = Node(p.item)
            p = p.ref
        else:
            start_node = Node(q.item)
            q = q.ref

        em = start_node

        while p is not None and q is not None:
            if p.item <= q.item:
                em.ref = Node(p.item)
                em = em.ref
                p = p.ref
            else:
                em.ref = Node(q.item)
                em = em.ref
                q = q.ref

        if p is None:
            em.ref = q
        else:
            em.ref = p

        return start_node


if __name__ == '__main__':
    # new_linked_list = Linked_list()

    # new_linked_list.insert_at_end(10)
    # new_linked_list.insert_at_end(20)
    # new_linked_list.insert_at_end(30)
    # new_linked_list.insert_at_end(40)
    # new_linked_list.insert_at_end(60)
    #
    # new_linked_list.traverse_list()
    # print(new_linked_list.get_count())
    # print(new_linked_list.count_items)
    # print('=' * 20)
    #
    # new_linked_list.reverse()
    # new_linked_list.traverse_list()
    #
    # print(new_linked_list.get_count())
    # print(new_linked_list.count_items)

    new_linked_list2 = Linked_list()
    new_linked_list2.make_new_list(4)
    new_linked_list2.traverse_list()
    print('=' * 20)
    new_linked_list3 = Linked_list()
    new_linked_list3.make_new_list(6)
    new_linked_list3.traverse_list()
    print('=' * 20)

    new_linked_list2.bulb_sort_link_change()
    new_linked_list3.bulb_sort_link_change()

    new_linked_list2.traverse_list()
    print('=' * 20)
    new_linked_list3.traverse_list()
    print('=' * 20)

    merge_list = new_linked_list2.merge_lists2(new_linked_list3)
    merge_list.traverse_list()