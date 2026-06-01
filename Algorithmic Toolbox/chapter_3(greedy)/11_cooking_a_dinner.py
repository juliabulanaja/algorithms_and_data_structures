
def cook(cook_times: list, fresh_times: list):
    dishes = sorted(zip(cook_times, fresh_times), key=lambda x: x[0] + x[1], reverse=True)
    total_cooking_time = sum(cook_times)
    # dishes_total = [c + f for c, f in zip(cook_times, fresh_times)]

    print(dishes, "total_cooking_time", total_cooking_time)

    remaining_time = dishes[0][1]

    for i in range(1, len(dishes)):
        remaining_time -= dishes[i][0]

        if dishes[i][1] < remaining_time:
            remaining_time = dishes[i][1]
        # print(f"cook_times: {dishes[i][0]}, remaining_time: {remaining_time}")

    return remaining_time 




# cook_times = [5, 3, 2]     
# fresh_times = [10, 4, 6]
# result = cook(cook_times, fresh_times)
# print(result)

# c = [3, 2, 5]   # cooking times
# f = [2, 1, 4]   # freshness times
# result = cook(c, f)
# print(result) # impossible

# c = [1, 2, 3]   # cooking times
# f = [5, 4, 6]   # freshness times
# result = cook(c, f)
# print(result)

# c = [4, 3, 2]   # cooking times
# f = [2, 1, 3]   # freshness times
# result = cook(c, f)
# print(result) # impossible

# c = [2, 3, 1]   # cooking times
# f = [4, 5, 3]   # freshness times
# result = cook(c, f)
# print(result)

# c = [10, 1]     # cooking times
# f = [2, 5]      # freshness times
# result = cook(c, f)
# print(result)

# c = [5, 1, 5]     # cooking times
# f = [2, 5, 3]      # freshness times
# result = cook(c, f)
# print(result)

# c = [3, 1, 1]
# f = [3, 2, 2]
# result = cook(c, f)
# print(result)

c = [1, 17, 2]
f = [15, 4, 14]
result = cook(c, f)
print(result)

# c = [5, 8, 2]
# f = [10, 4, 4]
# result = cook(c, f)
# print(result)