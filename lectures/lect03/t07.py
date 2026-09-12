# визначити якій координатній чверті належить задана точка площини

x, y = [float(el) for el in input().split()]
if x > 0 and y > 0:
    print("I")
else:
    if x < 0 and y > 0:
        print("II")
    else:
        if x < 0 and y < 0:
            print("III")
        else:
            if x > 0 and y < 0:
                print("IV")
            else:
                print("Точка лежить на коорд. осях")
