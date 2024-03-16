# Basit barbut oyunu
# bots = ['ahmet','mehmet','ayse'] login olan kullanıcıyıa bu listeden random rakip atanacak
# minimum_bet = 100 yani 50 chip bet yapılamaz
# kullanıcıların kasası olacak. kazanırsa yaptığı bahisin 2 katı kasasına yatırılacak.
# kaybederse yaptığı bahis kasadan eksilecek
# login işlemi olsun
# kullanıcı login olduğunda daily chip hediye edilsin (1000 ile 2000) arası.
from random import choice, randint

bots = ['ahmet', 'mehmet', 'ayse']
minimum_bet = 100
user_dict = {
    '1': {
        'user_name': 'mert',
        'password': '123',
        'safe': '1200'
    },
    '2': {
        'user_name': 'ali',
        'password': '123',
        'safe': '2000'
    }
}


def assign_bot(bot_list : bots):
    return choice(bot_list)

def roll_dice():
    return randint(2, 12)

def gain_daily_reward():
    return randint(1000, 2000)