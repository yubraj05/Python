#---------------------------- Unpacking Function Arguments -------------------------
def foo(a, b, c):
    print(a, b, c)

args = (1, 2, 3)
foo(*args)  # Equivalent to foo(1, 2, 3)

kwargs = {'a': 1, 'b': 2, 'c': 3}
foo(**kwargs)  # Equivalent to foo(a=1, b=2, c=3)


#------------------------ Variable-Length Argument Lists ------------------------
def foo(*args, **kwargs):
    print(args)
    print(kwargs)

foo(1, 2, 3, a=4, b=5)  # args=(1, 2, 3), kwargs={'a': 4, 'b': 5}


#------------------------- Keyword-Only Arguments -----------------------------
def foo(a, b, *, c):
    print(a, b, c)

foo(1, 2, c=3)  # Valid
# foo(1, 2, 3)    # Error, c must be a keyword argument (after declarig * all the argumnt after that must be a keyword argument)