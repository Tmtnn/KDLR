meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL" : "bir şakaya karşılık cevap",
            "SHEESH" : "onaylamamak",
            "CREEPY" : "korkunç",
            "AGGRO" : "agresifleşmek/sinirlenmek",
            "UNCLE" : "Amca",
            "MINECRAFT" : "Oyuncuların blokları kullanarak çeşitli yapılar inşa ettiği, keşif yaptığı ve hayatta kalma mücadelesi verdiği popüler bir video oyunudur.",
            }
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("SOZLUKTE KELIME BULUNAMIYOR.")
    print("  Baska bir kelime dene.")
