def visible_area(mountains):
    landscape = [0] * (max([rights['right'] for rights in mountains]) + 1)
    for i in mountains:
        if i['height'] > landscape[int((i['right']+i['left'])/2)]:
            landscape[int((i['right']+i['left'])/2)] = i['height']

    for i in enumerate(landscape, start=0):
            for j in enumerate(landscape, start=0):
                if landscape[j[0]] - abs(i[0]-j[0]) > landscape[i[0]]:
                    landscape[i[0]] = landscape[j[0]] - abs(i[0]-j[0])

    sum = 0

    for i in enumerate(landscape[:-1], start=0):
        sum += (landscape[i[0]] + landscape[i[0] + 1])/2
        if landscape[i[0]] == landscape[i[0] + 1]:
            sum -= 0.25
    return sum
