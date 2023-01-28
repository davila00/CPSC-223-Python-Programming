
def sum(*, list):
    sum = 0
    for i in range(len(list)):
        sum = sum + list[i]
    return sum

def average(*, list):
    sum = 0
    for i in range(len(list)):
        sum = sum + list[i]
    average = 0
    average = sum / len(list)
    return average
