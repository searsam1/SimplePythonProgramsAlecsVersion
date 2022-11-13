favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python'
}

print("The following people have participated in the poll:")
for language in favorite_languages.keys():
    print(language.title())

print("\nThe following languages have been mentioned by them, respectively:")
for people in favorite_languages.values():
    print(people.title())