
def transition(*, tracker, id, enter):
    if (len(id) != 3 ):
        return 901

    floor, room = enter.split("-")

    if floor.isalpha():
        if True:
            return 902

    if floor.isnumeric():
        floor = int(floor)
        if floor < 1:
            return 903

    if floor > 3:
        return 904

    if enter != int:
        return 905

    if room.isaplha():
        if True:
            return 906

    if (enter == 1):
        return 999

    return 0
