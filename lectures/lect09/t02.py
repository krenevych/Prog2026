def bar(n):
   if n == 1:
       return 1
   else:
       foo(n-2)


def foo(n):
    if n == 1:
        return 1
    else:
        return bar(n)

# baz

