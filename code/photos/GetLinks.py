from bs4 import BeautifulSoup
import requests
import os

# You need to have directoris in imagesT like in dictionary

baseName = "images/"
myDict = {'Skandinavskiy': 'https://www.houzz.ru/photos/foto-gostinaya-komnata-v-skandinavskom-stile-phbr1-bp~t_13807~s_22925',
          'Sovremenniy': 'https://www.houzz.ru/photos/foto-gostinaya-komnata-v-sovremennom-stile-phbr1-bp~t_13807~s_14086',
          'Klassicheskiy': 'https://www.houzz.ru/photos/foto-gostinaya-komnata-v-klassicheskom-stile-phbr1-bp~t_13807~s_14089',
          'Loft': 'https://www.houzz.ru/photos/foto-gostinaya-komnata-v-stile-loft-phbr1-bp~t_13807~s_14094',
          'Fyyushn': 'https://www.houzz.ru/photos/foto-gostinaya-komnata-v-stile-fyyuzhn-phbr1-bp~t_13807~s_14087',
          'Modernizm': 'https://www.houzz.ru/photos/foto-gostinaya-komnata-v-stile-modernizm-phbr1-bp~t_13807~s_14088',
          'Vostochniy': 'https://www.houzz.ru/photos/foto-gostinaya-komnata-v-vostochnom-stile-phbr1-bp~t_13807~s_14090',
          'Morskoiy': 'https://www.houzz.ru/photos/foto-gostinaya-komnata-v-morskom-stile-phbr1-bp~t_13807~s_14091',
          'Kantri': 'https://www.houzz.ru/photos/foto-gostinaya-komnata-v-stile-kantri-phbr1-bp~t_13807~s_14093',
          'ShebbiShink': 'https://www.houzz.ru/photos/foto-gostinaya-komnata-v-stile-shebbi-shik-phbr1-bp~t_13807~s_24688',
          'Sredizemnomorskiy': 'https://www.houzz.ru/photos/foto-gostinaya-komnata-v-sredizemnomorskom-stile-phbr1-bp~t_13807~s_14095',
          'Retro': 'https://www.houzz.ru/photos/foto-gostinaya-komnata-v-stile-retro-phbr1-bp~t_13807~s_14096',
          'Rustika': 'https://www.houzz.ru/photos/foto-gostinaya-komnata-v-stile-rustika-phbr1-bp~t_13807~s_14097',
          'SovremennayaKlassika': 'https://www.houzz.ru/photos/foto-gostinaya-komnata-v-stile-sovremennaya-klassika-phbr1-bp~t_13807~s_14098',
          'Viktorianskom': 'https://www.houzz.ru/photos/foto-gostinaya-komnata-v-viktorianskom-stile-phbr1-bp~t_13807~s_22926'
          }

for (type, url) in myDict.items():
    os.makedirs(baseName + type)
    out = open(baseName + type + "/links.txt", "w")
    counter = 1000
    baseUrl = url + "?fi="
    while counter < 1200:
        curentUrl = baseUrl + str(counter)
        page = requests.get(curentUrl)
        soup = BeautifulSoup(page.text, features="html.parser")
        myimages = soup.select("picture", {"class": "hz-image-container"})
        curCount = 0
        for img in myimages:
            if "hz-image-placeholder" in img["class"]:
                continue
            curCount += 1
            imgUrl = img.contents[1]["src"]
            myImage = imgUrl[27:48]
            out.write(myImage + "\n")
            print(myImage + " " + type)
        counter += curCount
        print("---------------" + str(counter) + "----------------------")

    out.close()
