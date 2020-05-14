import sys
def permutations(L):
    if len(L)<2: return [L]
    others = permutations(L[1:]) # Everything but the first
    perm_list = []
    for other in others: # for each possible permutation
        # for each slot to place the first item, place it.
            for slot in range(len(others)+1):
                new_list = other[:] # copy of others
                new_list.insert(slot, L[0])
                perm_list.append(new_list)
                # These three lines can also just be perm_list.append(other[:slot]+[L[0]] + other[slot:])
    return perm_list

print (permutations([1,3,4]))
