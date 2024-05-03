def solution (N, ratings):
    dish_ids = []
    total_ratings = []
    counts =[]

    for rating in ratings:
        dish_id = rating[0]
        rating_value = rating[1]

        if dish_id in dish_ids:
            index = dish_ids.index(dish_id)
            total_ratings[index] += rating_value
            counts[index] += 1
        else:
            dish_ids.append(dish_id)
            total_ratings.append(rating_value)
            counts.append(1)
    
    max_average =0
    best_dish_id = -1
    for i, dish_id in enumerate(dish_ids):
        average = total_ratings[i] / counts[i]

        if average > max_average or (average == max_average and dish_id < best_dish_id):
            max_average = average
            best_dish_id = dish_id
    return best_dish_id

N = int(input())
ratings = [list(map(int, input().split())) for i in range(N)]

out_ = solution(N, ratings)
print (out_)