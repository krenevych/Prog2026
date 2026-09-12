# визначити якій координатній чверті належить задана точка площини

x, y = [float(el) for el in input().split()]
if x > 0 and y > 0:
    print("I")
elif x < 0 and y > 0:
    print("II")
elif x < 0 and y < 0:
    print("III")
elif x > 0 and y < 0:
    print("IV")
else:
    print("Точка лежить на коорд. осях")
