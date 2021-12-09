from itertools import combinations
from collections import deque
import json

test = False
if test:
    start = {
                'e': 1, 'h_m': 1, 'l_m': 1,
                'h_g': 2, 
                'l_g': 3
            }

    pairs = {
                'h_g': 'h_m',
                'l_g': 'l_m'
            }
else:
    start = { 
                'e': 1, 'th_g': 1, 'th_m': 1, 'pl_g': 1, 'st_g': 1,
                'pl_m': 2, 'st_m': 2,
                'pr_g': 3, 'pr_m': 3, 'ru_g': 3, 'ru_m': 3,
            }

    pairs = { 
                'th_g': 'th_m', 
                'pl_g': 'pl_m',
                'st_g': 'st_m',
                'pr_g': 'pr_m',
                'ru_g': 'ru_m',
            }

new_start = { 'el_g': 1, 'el_m': 1, 'di_g': 1, 'di_m': 1 }
start = { **start, **new_start }
new_pairs = { 'el_g': 'el_m', 'di_g': 'di_m' }
pairs = { **pairs, **new_pairs }


def isValid(config):
    for g, m in pairs.items():
        if config[g] == config[m]:
            continue

        for gg in pairs.keys():
            if config[m] == config[gg]:
                return False

    return True

def permute(config):
    floor = config.pop('e')
    items = [item for item in config.keys() if config[item] == floor]

    ret = []

    for dest in [floor + 1, floor - 1]:
        if dest <= 0 or dest > 4:
            continue
        
        for item in items:
            perm = config.copy()
            perm[item] = dest
            perm['e'] = dest

            if isValid(perm):
                ret.append(perm)

        for combo in combinations(items, 2):
            i1, i2 = combo
            perm = config.copy()
            perm[i1] = dest
            perm[i2] = dest
            perm['e'] = dest

            if isValid(perm):
                ret.append(perm)

    return ret

q = deque([start])
acc = set(json.dumps(start, sort_keys=True))

level = 0
while q:
    for _ in range(len(q)):
        config = q.popleft()
        if (all(v == 4 for v in config.values())):
            print(level)
            exit()

        for perm in permute(config):
            h = []
            for g, m in pairs.items():
                h.append([perm[g], perm[m]])
            h.sort()
            h.append(perm['e'])

            hashed = json.dumps(h, sort_keys=True)
            if hashed not in acc:
                q.append(perm)
                acc.add(hashed)

    level += 1

