print('Want to learn more about the astrological signs?')
print('Use the menu below to pull up information about each of them!')
signs = ['1 for Aries', '2 for Taurus', '3 for Gemini', '4 for Cancer', '5 for Leo', '6 for Virgo', '7 for Libra', '8 for Scorpio', '9 for Sagittarius','10 for Capricorn','11 for Aquarius','12 for Pisces']
index = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
for str in signs:
    print('Enter ' + str)
    
prompt = input('Enter here: ')

def aries():
    print('The cardinal fire sign! Independent and head-strong. Ruled by mars and represented by the ram.')
    print('The sun transits this sign from March 21 to April 20')
def taur():
    print('The fixed earth sign! Stubborn and reliable. Ruled by venus and represented by the bull.')
    print('The sun transits this sign from April 21 to May 20')
def gem():
    print('The mutable air sign! Adaptable and expressive. Ruled by mercury and represented by the twins.')
    print('The sun transits this sign from May 21 to June 20')
def cancer():
    print('The cardinal water sign! Sensitve and caring. Ruled by the moon and represented by the crab.')
    print('The sun transits this sign from June 21 to July 22')
def leo():
    print('The fixed fire sign! Proud and energetic. Ruled by the sun and represented by the lion.')
    print('The sun transits this sign from July 23 to August 22')
def virgo():
    print('The mutable earth sign! Percise and thoughtful. Ruled by mercury and represented as the maiden.')
    print('The sun transits this sign from August 23 to September 22')
def libra():
    print('The cardinal air sign! Empathetic and diplomatic. Ruled by venus and represented as the balancing scale.')
    print('The sun transits this sign from September 23 to October 22')
def scorp():
    print('The fixed water sign! Passionate and determined. Ruled by mars and represented as the scorpion')
    print('The sun transits this sign from October 23 to November 22.')
def sag():
    print('The mutable fire sign! Adventurous and honest. Ruled by jupiter and represented by the archer.')
    print('The sun transits this sign from November 23 to December 21')
def cap():
    print('The cardinal earth sign! Ambitious and loyal. Ruled by saturn and represented by the sea goat.')
    print('The sun transits this sign from December 22 to January 19th')
def aqua():
    print('The fixed air sign! Inventive and individual. Ruled by saturn and represented by the water bearer.')
    print('The sun transits this sign from January 20 to February 19')
def pisces():
    print('The mutable water sign! Idealistic and creative. Ruled by jupiter and represented as the fish.')
    print('The sun transits this sign from February 20 to March 20')
if '1' in prompt:
    print(aries())
elif '2'in prompt:
    print(taur())
elif '3' in prompt:
    print(gem())
elif '4' in prompt:
    print(cancer())
elif '5' in prompt:
    print(leo())
elif '6' in prompt:
    print(virgo())
elif '7' in prompt:
    print(libra())
elif '8' in prompt:
    print(scorp())
elif '9' in prompt:
    print(sag())
elif '10' in prompt:
    print(cap())
elif '11' in prompt:
    print(aqua())
elif '12' in prompt:
    print(pisces())
    
    
