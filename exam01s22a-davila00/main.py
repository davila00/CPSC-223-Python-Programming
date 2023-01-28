
tracker = [[[],['f3e'],['a9b','c6e'],[]],[[],['d2d','f6a','c8c'],[],[]],[[],[],['e8c','d1e'],['a0a']]]

while True:

    print("")
    print("************ TUFFY TITAN BUILDING ACCESS TRACKER ************")
    print("|--------(F1)-------|--------(F2)-------|--------(F3)-------|")
    print("|                   |                   |                   |")
    print(f'{"|(R1) *":7}{len(tracker[0][0]):1}{"*":2}{"|(R2) *":7}{len(tracker[0][1]):1}{"*":2}',end="")
    print(f'{"|(R1) *":7}{len(tracker[1][0]):1}{"*":2}{"|(R2) *":7}{len(tracker[1][1]):1}{"*":2}',end="")
    print(f'{"|(R1) *":7}{len(tracker[2][0]):1}{"*":2}{"|(R2) *":7}{len(tracker[2][1]):1}{"*":2}',end="")
    print("|")
    for ct in range(3):
        print("|",end="")
        for fl in range(3):
            for rm in range(2):
                x = ""
                if len(tracker[fl][rm]) > ct:
                    x = tracker[fl][rm][ct]
                print(f'{"":3}{x:3}{"   |":4}',end='')
        print('')
    print("|---------|---------|---------|---------|---------|---------|")
    print(f'{"|(R3) *":7}{len(tracker[0][2]):1}{"*":2}{"|(R4) *":7}{len(tracker[0][3]):1}{"*":2}',end="")
    print(f'{"|(R3) *":7}{len(tracker[1][2]):1}{"*":2}{"|(R4) *":7}{len(tracker[1][3]):1}{"*":2}',end="")
    print(f'{"|(R3) *":7}{len(tracker[2][2]):1}{"*":2}{"|(R4) *":7}{len(tracker[2][3]):1}{"*":2}',end="")
    print("|")
    for ct in range(3):
        print("|",end="")
        for fl in range(3):
            for rm in range(2,4):
                x = ""
                if len(tracker[fl][rm]) > ct:
                    x = tracker[fl][rm][ct]
                print(f'{"":3}{x:3}{"   |":4}',end='')
        print('')
    print("|-----------------------------------------------------------|")
    print()


    id = input("Identity (0 to exit): ")
    if id == '0':
        break
    e = input("Enter (Floor-Room)  : ")

    print("<** REPLACE THIS LINE WITH TRANSITION FUNCTION CALL **>")
    #replace following line with function call
    r = 0
    if r > 900:
        print("ERROR:",r)

