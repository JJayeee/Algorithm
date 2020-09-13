def solution(boxes):
    answer = -1
    # items = [0]*1000001
    items = [0]*10
    box_len = len(boxes)
    box_cnt = 0
    for a, b in boxes:
        print(a, b)
        if a == b:
            box_cnt += 1
        else:
            if items[a]:
                box_cnt += 1
                items[a] = 0
            else:
                items[a] = 1
            if items[b]:
                box_cnt += 1
                items[b] = 0
            else:
                items[b] = 1
        # print(items)
        # print()

    left_items = sum(items)
    # print(items)
    # print('len', box_len, 'cnt', box_cnt)
    # print(left_items)
    left_boxes = box_len - box_cnt
    if left_items >= left_boxes:
        answer = left_boxes
    else:
        answer = (left_boxes - left_items) * 2 + left_items

    return answer


boxes = [[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]
boxes = [[1, 2], [3, 4], [5, 6]]
boxes = [[1, 2], [2, 3], [3, 1]]
print(solution(boxes))

