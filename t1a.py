jumbled_superheroes = ['DocToR_sTRAngE', 'sPidERmaN', 'MoON_KnigHT', 'caPTAIN_aMERIca', 'hULK']

indices = []
decoded_names = []

for index, name in enumerate(jumbled_superheroes):
    indices.append(index)
    decoded_names.append(name.lower().replace("_", " ").title())

length1 = lambda sequence: len(sequence)
map1 = list(map(length1, decoded_names))
indices.sort(key=lambda i: map1[i])

print("Phase 5 kickoff list:")
for i, index in enumerate(indices):
    print(f"{i+1}. {decoded_names[index]}")