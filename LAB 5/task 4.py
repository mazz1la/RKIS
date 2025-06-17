strings = ["football", "fifa", "abc.basketball", "abc.volleyball"]

for i in range(len(strings)):
    if strings[i].startswith('abc'):
        strings[i] = strings[i].replace('abc', 'www')
    else:
        strings[i] += 'zzz'

print(strings)