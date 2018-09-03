# http://billboardtop100of.com/1989-2/
import requests
import string
from bs4 import BeautifulSoup

printable = set(string.printable)

output_filename = 'music.txt'
print('Writing to {}.'.format(output_filename))
music_names = open(output_filename, 'w')

for year in range(1995, 2017):

    if year == 2013:
        continue

    print('Downloading for {}.'.format(year))
    response = requests.get('http://billboardtop100of.com/{0}-2/'.format(year))
    assert response.status_code == 200
    soup = BeautifulSoup(response.content, 'lxml')
    musics = [str(tr.contents[3].contents[0]) + ' ' + str(tr.contents[5].contents[0]) for tr in
              soup.find('tbody').find_all('tr')]

    for music in musics:
        printable_music = ''.join(list(filter(lambda x: x in printable, music))).strip()
        if len(printable_music) != 0:
            music_names.write(printable_music)
            music_names.write('\n')
            music_names.flush()

music_names.close()
