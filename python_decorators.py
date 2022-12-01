def fun(f):
    def ing(func):
        res = f(func)
        if isinstance(res, dict):
            print("Checked that the output is a dictionary")
            return res
    return ing

@fun

def give_dictionary(arg):
    return {"program": arg}

print(give_dictionary("python"))