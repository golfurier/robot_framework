for i in range(30):
    j = str(i + 1)
    if len(j) == 1:
        date = '0' + j
    else:
        date = j

    file = open("C:\\Users\\root\\PycharmProjects\\robot_framework\CB1906"+date, 'w')
