def explode_chains(sublists):
    result = []
    for sublist in sublists:
        new_sublist = []
        i = 0
        while i < len(sublist):
            if i + 2 < len(sublist) and sublist[i] + 1 == sublist[i+1] and sublist[i] + 2 == sublist[i+2]:
                i += 3 
            else:
                new_sublist.append(sublist[i])
                i += 1
        result.append(new_sublist)
    return result

encoded_lists = [
    [1, 2, 3, 4, 6],
    [5, 7, 8, 9, 15],
    [12, 14, 16, 18],
    [10, 11, 12, 13, 16, 17, 18, 20]]

result = explode_chains(encoded_lists)
print(result)