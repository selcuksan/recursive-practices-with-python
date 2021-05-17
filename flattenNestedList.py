def flatten(my_list):
    result = []
    for i in my_list:
        if isinstance(i, list):
            result += flatten(i)
        else:
            result.append(i)
    return result


planets = ['mercury', 'venus', ['earth'], 'mars', [
    ['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]
print(planets)
print(flatten(planets))
