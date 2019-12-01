all_recipes = 509671 
recipes_to_create = 509671 * 50

class Recipe(object):
    def __init__(self, n):
        self.n = n
        self.next = None

elf1 = Recipe(3)
elf2 = Recipe(7)
front = elf1
back = elf2

elf1.next = elf2
elf2.next = elf1

while recipes_to_create + 10 > 0:
    next_recipes = elf1.n + elf2.n
    if next_recipes >= 10:
        back.next = Recipe(next_recipes // 10)
        back = back.next
        next_recipes %= 10
        recipes_to_create -= 1
    back.next = Recipe(next_recipes)
    recipes_to_create -= 1
    back = back.next
    back.next = front

    for _ in range(elf1.n + 1):
        elf1 = elf1.next
    for _ in range(elf2.n + 1):
        elf2 = elf2.next

s = str(front.n)
i = front.next
while i != front:
    s += str(i.n)
    i = i.next
print(s[all_recipes:all_recipes+10])
print(s.find(str(all_recipes)))
