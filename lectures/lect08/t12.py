def func(
        p1,
        p2="Default 2",
        p3="Default 3",
):
    print(f"{p1=}")
    print(f"{p2=}")
    print(f"{p3=}")



#### MAIN ####

# func("Hello1", "Hello2", "Hello3")
# func("Hello1", "Hello2") # p3 = "Default 3"
# func("Hello1") # p2="Default 2", p3 = "Default 3"

# Якщо ми хочемо лише для p2 скористатися типовим значенням,
# а для p3 використати кастомне значення, то так НЕ ВИЙДЕ!!  треба задати всі значення!!!
# func("Hello1",  "My custom for p3") # p2 = "My custom for p3"
func("Hello1", "Default 2", "My custom for p3")