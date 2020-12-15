import json

good_mutations = []

def mutation_is_good(mutation, mutations):
     if 'starting_trait' not in mutation:
         return False
     if mutation['points'] < 0:
         return False
     if 'valid' not in mutation or mutation['valid'] != False:
         return False
     if 'category' in mutation:
         return False
     return True

with open ('mutations.json', encoding='utf-8') as muts_file:
    mutations = json.load(muts_file)
    for mutation in mutations:
        if mutation_is_good(mutation, mutations):
            good_mutations.append(mutation)
for mutation in good_mutations:
    print(mutation['id'])
