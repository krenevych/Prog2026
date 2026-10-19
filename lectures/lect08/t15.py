def func(
        p1,
        p2="Default 2",
        p3="Default 3",
):
    print(f"{p1=}")
    print(f"{p2=}")
    print(f"{p3=}")


##### MAIN

func("Hello 1", p3="Hello 3")  # p1 - позиційний, ключовий параметр для p3, p2 - беремо зі значення за промовчанням

func(p3="Hello 3", p1="Hello 1")  # ключові параметри для p1 та p3, для p2 - типове значення
