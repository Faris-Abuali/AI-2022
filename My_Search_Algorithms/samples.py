graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": ["H", "I"],
    "E": ["J", "K"],
    "F": ["L", "M"],
    "G": ["N", "O"],
    "H": ["P"],
    "I": [],
    "J": [],
    "K": [],
    "L": [],
    "M": [],
    "N": [],
    "O": [],
    "P": [],
}

graph_weighted = {
    'S': [(1, 'A'), (12, 'G')],
    'A': [(1, 'S'), (3, 'B'), (1, 'C')],
    'G': [(12, 'S'), (2, 'C'), (3, 'D')],
    'B': [(3, 'A'), (3, 'D')],
    'C': [(1, 'A'), (1, 'D'), (2, 'G')],
    'D': [(1, 'C'), (3, 'B'), (3, 'G')]
}
# here is the graph_weighted image: https://i.imgur.com/3WDoJ9Z.jpg

weighted_graph_from_slides = {
    "S": [(1, "A"), (5, "B"), (8, "C")],  #each tuple is: (weight, label)
    "A": [(1, "S"), (3, "D"), (7, "E"), (9, "G")],
    "B": [(5, "S"), (4, "G")],
    "C": [(8, "S"), (5, "G")],
    "D": [(3, "A")],
    "E": [(7, "A")],
    "G": [(9, "A"), (4, "B"), (5, "C")],
}


# student_tuples = [
#     ('john', 'A', 15),
#     ('jane', 'Z', 12),
#     ('dave', 'B', 10),
# ]
# l = sorted(student_tuples, key=lambda student: student[2], reverse=True)  

# print(l)


