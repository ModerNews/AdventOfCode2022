import copy

from data_fetcher import get_data

data = [list(row) for row in get_data(8, use_cache=False).split('\n')[:-1]]
rows = data.copy()

columns = [[data[i][j] for i in range(len(data))] for j in range(len(data[0]))]
visibilities = copy.deepcopy(rows)
scores = copy.deepcopy(rows)

print(rows)
print(columns)

for i in range(len(rows)):
    row = rows[i]
    for j in range(len(row)):
        tree = row[j]
        # left, right, bottom, top
        visibility = [True, True, True, True]
        score = [0, 0, 0, 0]
        for n in range(j + 1, len(row)):
            score[1] = n - j
            if row[n] >= row[j]:
                visibility[1] = False
                break
        for n in range(j - 1, -1, -1):
            score[0] = j - n
            if row[n] >= row[j]:
                visibility[0] = False
                break
        tree, column = columns[j][i], columns[j]
        for n in range(i + 1, len(column)):
            score[2] = n - i
            if column[n] >= column[i]:
                visibility[2] = False
                break
        for n in range(i - 1, -1, -1):
            score[3] = i - n
            if column[n] >= column[i]:
                visibility[3] = False
                break
        visibilities[i][j] = any(visibility)
        scores[i][j] = score[0] * score[1] * score[2] * score[3]

[print(r) for r in visibilities]
visibilities = sum(visibilities, [])
print(sum(visibilities))
print(max(sum(scores, [])))