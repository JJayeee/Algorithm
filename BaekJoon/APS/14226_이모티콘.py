target_num = int(input())
total_visited = [[0] * 2020 for _ in range(2020)]
num_visited = [0] * 2020
time = 0
queue = [(1, 0)]
total_visited[1][0] = 1
while queue:
    new_queue = []
    for screen, clipboard in queue:
        num_visited[screen] = 1
        # 화면에 있는 이모티콘 클립보드에 저장
        if screen != clipboard and not total_visited[screen][screen]:
            new_queue.append((screen, screen))
            total_visited[screen][screen] = 1
        # 클립보드에 있는 이모티콘 화면에 붙여넣기
        if screen+clipboard < 2020 and not total_visited[screen+clipboard][clipboard]:
            new_queue.append((screen+clipboard, clipboard))
            total_visited[screen+clipboard][clipboard] = 1
        # 화면에 있는 이모티콘 하나 삭제
        if 0 < screen - 1 and not total_visited[screen-1][clipboard]:
            new_queue.append((screen-1, clipboard))
            total_visited[screen-1][clipboard] = 1

    if not num_visited[target_num]:
        time += 1
        queue = new_queue
    else:
        break

print(time)



"""
화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
화면에 있는 이모티콘 중 하나를 삭제한다.

클립보드가 비어있는 상태에는 붙여넣기를 할 수 없으며, 일부만 클립보드에 복사할 수는 없다.

영선이는 이미 화면에 이모티콘 1개를 입력했다.
"""