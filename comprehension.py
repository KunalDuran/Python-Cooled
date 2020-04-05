

##================= List Comprehension ============================

# TASK IS TO CONVERT THE GIVEN LIST TO LOWERCASE
sampleText = ['This', 'is', 'the', 'sample', 'text', 'AND', 'WE',
          'want', 'TO', 'lowerCase', 'All', 'the', 'letters']


# simple method
lower_text = []
for word in sampleText:
    l = word.lower()
    lower_text.append(l)


# with list comprehension
lower_text = [i.lower() for i in sampleText]



##================= Dictionary Comprehension =========================

# TASK IS TO CONVERT THE GIVEN LIST TO DICTIONARY
list_with_tuples = [('Batsman1', 100), ('Batsman2', 34),('Batsman3', 62),('Batsman4', 50)]


# simple method
new_dict = {}
for k,v in list_with_tuples:
    new_dict[k] = v


# with dict comprehension
new_dict = {k:v for k,v in list_with_tuples}
