from itertools import groupby

x = [(k, len(list(g))) for k, g in groupby('heeelloooooee')]

print(x)


print(any(len(list(g)) >= 3 for k, g in groupby('heeelloooooee')))
