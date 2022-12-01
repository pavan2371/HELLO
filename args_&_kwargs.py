def show_numbers(*args):
    for i in args:
        print(i)



show_numbers(1,2,3,4,5,6)





def show_numbers(**kwargs):
    for i,j in enumerate(kwargs):
     print(kwargs)



show_numbers(one=1,two=2,three=3)