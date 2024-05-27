def calculate_structure_sum(*args):
    total_sum = 0
    for arg in args:
        if isinstance(arg, int):
            total_sum += arg
        elif isinstance(arg, (list, tuple, set)):
            sub_structure_sum = calculate_structure_sum(*arg)
            total_sum += sub_structure_sum
        elif isinstance(arg, dict):
            for key, value in arg.items():
                total_sum += calculate_structure_sum(key, value)
        elif isinstance(arg, str):
            total_sum += len(arg)
        elif isinstance(arg, tuple):
            sub_structure_sum = calculate_structure_sum(*arg)
            total_sum += sub_structure_sum

    return total_sum


data_structure = [[1, 2, 3],
                  {'a': 4, 'b': 5},
                  (6, {'cube': 7, 'drum': 8}),
                  "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])
                  ]

result = calculate_structure_sum(*data_structure)
print(result)
