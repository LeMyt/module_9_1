def apply_all_func(int_list, *functions):
    int_list = list(int_list)
    results = {}
    for i in functions:
        results.update({i.__name__: i(int_list)})
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))