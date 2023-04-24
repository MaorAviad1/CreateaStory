'''
Mad Libs Generator
'''

# Questions for the user to answer
noun = input('Choose a noun: ')

p_noun = input('Choose a plural noun: ')

verb = input('Choose a verb (present tense): ')

noun2 = input('Choose a noun: ')

place = input('Name a place: ')

adjective = input('Choose an adjective (Describing word): ')

noun3 = input('Choose a noun: ')

color = input('Choose a color: ')

verb2 = input('Choose a verb (past tense): ')

# Print a story from the user input
print('------------------------------------------')

print('Once upon a time, there was a', color, noun, 'who loved to', verb, 'around the town.')

print('One day, the', noun, 'met a group of', p_noun, 'who were', verb2, 'nearby.')

print('The', p_noun, 'invited the', noun, 'to join them on an adventure to find the legendary', noun2, 'in', place)

print('The', noun, 'was', adjective, 'and decided to join the', p_noun, 'on their adventure.')

print('After many hours of', verb + 'ing', 'through', place, 'the group finally found the', noun2, '.')

print('But to their surprise, the', noun2, 'was guarded by a giant', noun3, '.')

print('The', p_noun, 'fought bravely and eventually defeated the', noun3, '.')

print('The', noun, 'was forever grateful to the', p_noun, 'and together they', verb2, 'back to their home.')

print('The end.')

print('------------------------------------------')
