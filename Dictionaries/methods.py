emp={
    1:45,
    2:65,
    3:87,
    4:25,
    5:78
}

emp2={
    22:67,
    566:90
}

emp.update(emp2);
print(emp)

# emp.clear()
# print(emp)

emp.pop(5);#remove the key 5
emp.popitem();#remove last item
print(emp)

