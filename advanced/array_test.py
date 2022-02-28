def find_raza(a):
    for i in a:
        if i == 'raza':
            return True

    return False


people = ['zara', 'braza', 'baba', 'spirit']
found = find_raza(people)
print(found)
