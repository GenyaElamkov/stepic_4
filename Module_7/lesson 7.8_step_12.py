from typing import OrderedDict


class Queue:
    def __init__(self, pairs=[]) -> None:
        self.pairs = OrderedDict(pairs)

    def add(self, n):
        self.pairs[n[0]] = n[1]
        if n[0] in self.pairs:
            self.pairs.move_to_end(n[0])

    def pop(self):
        if not self.pairs:
            raise KeyError("Очередь пуста")
        return self.pairs.popitem(last=False)

    def __repr__(self) -> str:
        return f"{__class__.__name__}({list(self.pairs.items())})"

    def __len__(self):
        return len(self.pairs)


# INPUT DATA:

# # TEST_1:
# queue = Queue()

# queue.add(('one', 1))
# queue.add(('two', 2))
# print(queue)

# # TEST_2:
# queue = Queue([('one', 1)])

# queue.add(('two', 2))
# print(queue.pop())
# print(queue.pop())
# print(queue)

# # TEST_3:
# queue = Queue({'one': 1, 'two': 2})

# print(len(queue))
# queue.add(('three', 1))
# print(len(queue))

# TEST_4:
queue = Queue()

queue.add(("one", 1))
queue.add(("two", 2))
print(queue)
queue.add(("one", 10))
print(queue)

# # TEST_5:
# queue = Queue()

# try:
#     queue.pop()
# except KeyError as error:
#     print(error)

# # TEST_6:
# data = [
#     ("Kerry Martinez", 36),
#     ("Todd Watson", 47),
#     ("Andrew Elliott", 56),
#     ("Jamie Collins", 44),
#     ("Kelli Aguilar", 35),
#     ("Sara Guerrero", 20),
#     ("Michelle Allen", 29),
#     ("Elizabeth George", 17),
#     ("Suzanne Rodriguez", 42),
#     ("Timothy Smith", 46),
#     ("Dr. Olivia Thomas", 59),
#     ("Kevin Johnson", 59),
#     ("Jennifer Padilla", 54),
#     ("Ariel Saunders", 26),
#     ("Jason Haley", 28),
#     ("David Howard", 20),
#     ("Duane Dixon", 57),
#     ("Sierra Graves", 30),
#     ("Todd Watson", 46),
#     ("Amanda Wilson", 45),
#     ("Nicole Johnson", 24),
#     ("Lauren Lopez", 25),
#     ("Amanda Miranda", 30),
#     ("Sharon Russell", 29),
#     ("Robert Richardson", 40),
#     ("Kristen Thompson", 32),
#     ("Adam Bush", 33),
#     ("Mackenzie Hanson", 50),
#     ("David Ortega", 48),
#     ("Tim Williams", 29),
#     ("Angela Johnson", 41),
#     ("Duane Watson", 31),
#     ("Tamara Wood", 13),
#     ("Julie Morris", 40),
#     ("Michele Blake", 52),
#     ("Kevin Hill", 28),
#     ("Wesley Roberts", 14),
#     ("Autumn Ryan", 15),
#     ("Jeff Cline", 36),
#     ("Timothy Taylor", 34),
#     ("Yolanda Morris", 34),
#     ("Christina Johnson", 43),
#     ("Shaun Johnson", 48),
#     ("Elizabeth Lopez", 31),
#     ("Angela Ramos", 47),
#     ("Andrea Roberts", 20),
#     ("Carrie Santiago", 16),
#     ("Valerie Hunt", 18),
#     ("Jasmin May", 31),
#     ("Ethan Smith", 57),
#     ("Cynthia Miles", 32),
#     ("Thomas Johnson", 19),
#     ("Brenda Ochoa", 39),
#     ("Tammy Shields", 16),
#     ("Jodi Combs", 17),
#     ("Edward Evans", 50),
#     ("Susan Maldonado", 49),
#     ("Kelly Harris", 43),
#     ("Dawn Graham", 32),
#     ("Cynthia Simpson", 35),
#     ("James Norris", 58),
#     ("Jeanne Blevins", 26),
#     ("Bradley Hall", 39),
#     ("Bridget Holland", 22),
#     ("Paul Henderson", 47),
#     ("James Stein", 24),
#     ("Joshua Moore", 44),
#     ("Aaron Chandler", 48),
#     ("Jason Vance", 18),
#     ("David Williams", 48),
#     ("Donna Johnson", 45),
#     ("Shelby Schmidt", 25),
#     ("Cody Ford", 35),
#     ("William Hampton", 41),
#     ("Michael Cooper", 20),
#     ("Megan Snyder", 34),
#     ("Wendy Baxter", 47),
#     ("Nicole Walker", 16),
#     ("Kelly Harris", 57),
#     ("Maurice Brady", 58),
#     ("Jennifer Mayo", 26),
#     ("Cynthia Miles", 43),
#     ("Michelle Conley", 38),
#     ("Andrew Gonzalez", 10),
#     ("Christina Grant", 53),
#     ("Jessica Pena", 22),
#     ("Jerry Carroll", 16),
#     ("Candace Aguirre", 49),
#     ("Curtis Hall", 20),
#     ("Adam Bush", 46),
#     ("Carrie Williams", 26),
#     ("Lisa Barker", 27),
#     ("Thomas Smith", 36),
#     ("Sheila Marsh PhD", 55),
#     ("Tracy Potts", 23),
#     ("Christopher Brown", 46),
#     ("Michael Thompson", 47),
#     ("Jennifer Peterson MD", 15),
#     ("Paul Henderson", 24),
#     ("Julie Gibson", 48),
# ]

# queue = Queue([("Allison Finley", 14), ("Bryan Bradshaw", 48)])

# for item in data:
#     queue.add(item)

# print(len(queue))
# for _ in range(97):
#     print(queue.pop())

# try:
#     queue.pop()
# except KeyError as e:
#     print(e)

# print(len(queue))
