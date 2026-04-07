# Task 7.4

def common_elements():
    list_3 = set(i for i in range(100) if i % 3 == 0)
    list_5 = set( i for i in range(100) if i % 5 == 0)

    return list_3 & list_5

print(common_elements())