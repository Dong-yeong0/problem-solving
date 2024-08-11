def solution(n, slicer, num_list):
    method = {
        1: lambda: num_list[0:slicer[1] + 1],
        2: lambda: num_list[slicer[0]:],
        3: lambda: num_list[slicer[0]:slicer[1] + 1],
        4: lambda: num_list[slicer[0]:slicer[1] + 1:slicer[2]]
    }
    return method.get(n, lambda: False)()