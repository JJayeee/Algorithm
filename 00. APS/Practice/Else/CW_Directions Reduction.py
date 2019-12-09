# https://www.codewars.com/kata/directions-reduction/python
def dirReduc(arr):
    for i in range(len(arr)-1):
        a = {arr[i], arr[i+1]}
        if a=={"NORTH", "SOUTH"} or a=={"EAST", "WEST"}:
            arr.pop(i)
            arr.pop(i)
            return dirReduc(arr)
    return arr


# Best Practice
opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

def dirReduc2(plan):
    new_plan = []
    for d in plan:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan