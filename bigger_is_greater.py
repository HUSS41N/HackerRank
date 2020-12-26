from itertools import permutations
a = 'zedawdvyyfumwpupuinbdbfndyehircmylbaowuptgmw'
b = 'abdc'
arr = []
for i in permutations('zedawdvyyfumwpupuinbdbfndyehircmylbaowuptgmw'):
    if ''.join(i) > a:
        arr.append(''.join(i))
print(min(arr))
