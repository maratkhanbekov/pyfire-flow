import os, path

if __name__ == '__main__':
    path = '../shared-decks/media/city-life/city-file-svg-icons/'
    for i in sorted(os.listdir(path)):
        if not i.startswith('.'):
            print('city-file-svg-icons/' + i)