def argument_dict(**k):
    dict = {value: key for key, value in k.items()}
    return dict
result = argument_dict(a=1, b='hello', c=[1, 2, 3])
print(result)
