alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
alien_0 = {}
print(alien_0)
alien_0['color'] = 'green'
print(alien_0)
alien_0['points'] = 5
print(alien_0)
alien_0['color'] = 'yellow'
print(alien_0)
del alien_0['points']
print(alien_0)
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

del alien_0["speed"]
print(alien_0)

favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'C++',
    'phll': 'java',
}
print("Edward's favorite language is " + favorite_languages['edward'].title() +
      ".")
for key, value in favorite_languages.items():
    print("\nKey: " + key)
    print("Value: " + value)
    print(key.title() + "'s favorite language is " + value.title() + ".")
for key in favorite_languages.keys():
    print(key.title())
if 'erin' not in favorite_languages.keys():
    print('!')
for key in sorted(favorite_languages.keys()):
    print(key.title())
for value in sorted(favorite_languages.values()):
    print(value.title())
print('\n')
favorite_languages['phll'] = 'python'
for value in set(favorite_languages.values()):
    print(value.title())
