dict1 = {
  'name' : 'Fortuna',
  'age': 27,
  'school' : 'Sundsvall VUX',
  'city' : 'Sundsvall'
}

dict2 = {
  'school' : 'Stockholm University',
  'city' : 'Stockholm'
}

merged_dicts = dict1.copy()

for x in dict2:
  merged_dicts[x] = dict2[x]
  

print(merged_dicts)

