import requests
import os.path

# You need to have directoris in imagesT like in dictionary and file that was generatied by GetLinks.py

baseName = "images/"
myDict = {'Skandinavskiy':          'https://www.houzz.ru/photos/foto-gostinaya-komnata-v-skandinavskom-stile-phbr1-bp~t_13807~s_22925',
          'Sovremenniy':            'https://www.houzz.ru/photos/foto-gostinaya-komnata-v-sovremennom-stile-phbr1-bp~t_13807~s_14086',
          'Klassicheskiy':          'https://www.houzz.ru/photos/foto-gostinaya-komnata-v-klassicheskom-stile-phbr1-bp~t_13807~s_14089',
          'Loft':                   'https://www.houzz.ru/photos/foto-gostinaya-komnata-v-stile-loft-phbr1-bp~t_13807~s_14094',
          'Fyyushn':                'https://www.houzz.ru/photos/foto-gostinaya-komnata-v-stile-fyyuzhn-phbr1-bp~t_13807~s_14087',
          'Modernizm':              'https://www.houzz.ru/photos/foto-gostinaya-komnata-v-stile-modernizm-phbr1-bp~t_13807~s_14088',
          'Vostochniy':             'https://www.houzz.ru/photos/foto-gostinaya-komnata-v-vostochnom-stile-phbr1-bp~t_13807~s_14090',
          'Morskoiy':               'https://www.houzz.ru/photos/foto-gostinaya-komnata-v-morskom-stile-phbr1-bp~t_13807~s_14091',
          'Kantri':                 'https://www.houzz.ru/photos/foto-gostinaya-komnata-v-stile-kantri-phbr1-bp~t_13807~s_14093',
          'ShebbiShink':            'https://www.houzz.ru/photos/foto-gostinaya-komnata-v-stile-shebbi-shik-phbr1-bp~t_13807~s_24688',
          'Sredizemnomorskiy':      'https://www.houzz.ru/photos/foto-gostinaya-komnata-v-sredizemnomorskom-stile-phbr1-bp~t_13807~s_14095',
          'Retro':                  'https://www.houzz.ru/photos/foto-gostinaya-komnata-v-stile-retro-phbr1-bp~t_13807~s_14096',
          'Rustika':                'https://www.houzz.ru/photos/foto-gostinaya-komnata-v-stile-rustika-phbr1-bp~t_13807~s_14097',
          'SovremennayaKlassika':   'https://www.houzz.ru/photos/foto-gostinaya-komnata-v-stile-sovremennaya-klassika-phbr1-bp~t_13807~s_14098',
          'Viktorianskom':          'https://www.houzz.ru/photos/foto-gostinaya-komnata-v-viktorianskom-stile-phbr1-bp~t_13807~s_22926'}

counter1 = 0
counter2 = 0
w = 300
h = 300
begin = "https://st.hzcdn.com/"
dir1 = "fimgs/"
dir2 = "simgs/"
endFormat = "-w{0}-h{1}-b0-p0--.jpg"
res = [14, 9]

for (type, url) in myDict.items():
    print("--------------------------" + type + "----------------------------")
    myLinks = open(baseName + type + "/links.txt", "r")
    for link in myLinks:
        link = link.strip()
        parts = link.split("_")
        url1 = begin + dir1 + link + endFormat.format(h, h)
        url2 = begin + dir2 + parts[0] + "_" + str(res[0]) + "-" + parts[1] + ".jpg"

        #Загрузить эту ссылку
        #print(url1)

        p = requests.get(url2)

        if (p.status_code == 404):
            counter2 += 1
            print("Уменьшили")
            url2 = begin + dir2 + parts[0] + "_" + str(res[1]) + "-" + parts[1] + ".jpg"
            p = requests.get(url2)

        if (p.status_code == 404):
            counter1 += 1
            print("Не могу закачать")
            continue

        print(url2)
        if os.path.exists(baseName + type + "/" + url2[27:]):
            continue
        p = requests.get(url2)
        out = open(baseName + type + "/" + url2[27:], "wb")
        out.write(p.content)
        out.close()
print(counter1, counter2)

