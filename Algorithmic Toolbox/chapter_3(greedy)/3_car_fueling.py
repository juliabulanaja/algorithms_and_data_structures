distance = int(input())
miles_full_tank = int(input())

n_stops = int(input())
stops = [int(num) for num in input().split(' ')]


# def car_fueling(distance: int, miles_full_tank: int, stops: list) -> int:
#     current_position = 0
#     distance_done = 0
#     refills = 0

#     while distance_done + miles_full_tank < distance:

#         last_position = current_position 
 
#         while current_position < len(stops) and stops[current_position] <= distance_done + miles_full_tank: 

#             next_stop = stops[current_position] 
#             current_position += 1 
        
#         if last_position == current_position: 
#              return -1

#         distance_done = stops[current_position-1]
#         refills += 1 

#     return refills


def car_fueling(distance: int, tank: int, stops: list) -> int:
    current_stop = 0
    refills = 0

    for i in range(len(stops)):
        stop = stops[i]

        if stop == stops[-1]:
            next_stop = distance
        else:
            next_stop = stops[i+1]

        if next_stop - current_stop > tank:
            if stop - current_stop > tank or next_stop - stop > tank:
                return -1

            current_stop = stop
            refills += 1

    return refills




# result = car_fueling(distance, miles_full_tank, stops)
# print(result)

####################################################

# tests:

# distance = 950 
# miles_full_tank = 400
# n_stops = 4
# stops =  [200, 375, 550, 750]

# result = car_fueling(distance, miles_full_tank, stops)
# print(result)

# distance = 10 
# miles_full_tank =  3
# n_stops = 4
# stops =  [1, 2, 5, 9]

# result = car_fueling(distance, miles_full_tank, stops)
# print(result)

# distance = 500 
# miles_full_tank =  200
# n_stops = 4
# stops =  [100, 200, 300, 400]

# result = car_fueling(distance, miles_full_tank, stops)
# print(result)

# distance = 200 
# miles_full_tank =  250
# n_stops = 2
# stops =  [100, 150]

# result = car_fueling(distance, miles_full_tank, stops)
# print(result)

# distance = 6 
# miles_full_tank =  2
# n_stops = 2
# stops =  [2, 4]

# result = car_fueling(distance, miles_full_tank, stops)
# print(result)

# distance = 700 
# miles_full_tank =  200
# n_stops = 4
# stops =  [100, 200, 300, 400]

result = car_fueling(distance, miles_full_tank, stops)
print(result)
