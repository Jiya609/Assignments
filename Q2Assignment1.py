
marks = [78, 35, 92, 40, 61]

marks_tuple = tuple(marks)

print("List:", marks)
print("Type of list:", type(marks))

print("Tuple:", marks_tuple)
print("Type of tuple:", type(marks_tuple))

print("Highest marks:", max(marks))
print("Lowest marks:", min(marks))

print("Students scoring at least 40:", (marks[0] >= 40) + (marks[1] >= 40) + (marks[2] >= 40) + (marks[3] >= 40) + (marks[4] >= 40))

print("All marks are valid:", all(0 <= mark <= 100 for mark in marks))

marks[0] = 80
print("List after changing an element:", marks)

