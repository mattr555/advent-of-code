players = 468
last_marble = 71843 * 100

special_multiple = 23

scores = [0] * players
# circle = [0, 2, 1]
# current_ind = 1

# for marble in range(3, last_marble+1):
#     player_ind = (marble - 1) % players
#     if marble % special_multiple == 0:
#         scores[player_ind] += marble
#         current_ind -= 7
#         current_ind %= len(circle)
#         scores[player_ind] += circle.pop(current_ind)
#     else:
#         current_ind += 2
#         if current_ind > len(circle):
#             current_ind = 1
#         circle.insert(current_ind, marble)

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def insert_before(node, linked):
    new_before = linked.prev
    new_before.next = node
    node.prev = new_before
    linked.prev = node
    node.next = linked
    return node

def remove(node):
    p = node.prev
    n = node.next
    p.next = n
    n.prev = p
    return n

zero = Node(0)
zero.prev = zero
zero.next = zero

ptr = zero
for marble in range(1, last_marble+1):
    player_ind = (marble - 1) % players
    if marble % special_multiple == 0:
        scores[player_ind] += marble
        for _ in range(7):
            ptr = ptr.prev
        scores[player_ind] += ptr.val
        ptr = remove(ptr)
    else:
        for _ in range(2):
            ptr = ptr.next
        ptr = insert_before(Node(marble), ptr)

print(max(scores))

