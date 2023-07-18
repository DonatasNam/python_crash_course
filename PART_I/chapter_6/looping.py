favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'Tristan': 'python',
 }

friends = {'Connie':1,
            'Sally':2,
            'Brett':3,
            'Sarah':4,
            'Tristan':5}

for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")