def solution(genres, plays):
    answer = []
    genre_play = {}
    genre_sum = {}

    for i in range(len(genres)):
        genre_play.setdefault(genres[i], [])
        genre_play[genres[i]].append((plays[i], i))
        genre_sum[genres[i]] = genre_sum.get(genres[i], 0) + plays[i]

    order_list = sorted(list(genre_sum.items()), key=lambda x: x[1], reverse=True)

    for k, v in order_list:
        if len(genre_play[k]) > 1:
            genre_play[k].sort(key=lambda x: (x[0], -x[1]))
            print(k, genre_play[k])
            answer.extend((genre_play[k][-1][1], genre_play[k][-2][1]))
        else:
            answer.append(genre_play[k][0][1])

    return answer


genres = ['classic', 'pop', 'classic', 'classic', 'pop', 'pop']
plays = [500, 600, 150, 800, 2500, 2500]
print(solution(genres, plays))

"""
pop [(600, 1), (2500, 5), (2500, 4)]
classic [(150, 2), (500, 0), (800, 3)]
[4, 5, 3, 0]
"""