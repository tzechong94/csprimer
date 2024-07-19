list = ["X", "X", "X", "d", "e", "f", "g", "O", "O"]
print((list[0:3], list[3:6], list[6:9]))
rows = (list[0:3], list[3:6], list[6:9])
# print("|".join(f" {c} " for c in row) for row in (list[0:3], list[3:6], list[6:9]))

print("\n---+---+---\n".join("|".join(f" {c} " for c in row) for row in rows))
# print("\n---------\n".join(str(row) for row in (rows)))
