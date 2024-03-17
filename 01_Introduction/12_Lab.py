# Basit barbut oyunu
# bots = ['ahmet','mehmet','ayse'] login olan kullanıcıyıa bu listeden random rakip atanacak
# minimum_bet = 100 yani 50 chip bet yapılamaz
# kullanıcıların kasası olacak. kazanırsa yaptığı bahisin 2 katı kasasına yatırılacak.
# kaybederse yaptığı bahis kasadan eksilecek
# login işlemi olsun
# kullanıcı login olduğunda daily chip hediye edilsin (1000 ile 2000) arası.
from random import choice, randint

bots = ['Ahmet', 'Mehmet', 'Ayse']
minimum_bet = 100
user_dict = {
    '1': {
        'user_name': 'mert',
        'password': '123',
        'safe': 1200
    },
    '2': {
        'user_name': 'ali',
        'password': '123',
        'safe': 2000
    }
}


def assign_bot(bot_list : bots):
    return choice(bot_list)

def roll_dice():
    return randint(2, 12)

def gain_daily_reward():
    return randint(1000, 2000)

def is_bet_valid(current_bet:int, safe: int):
    if minimum_bet <= current_bet <= safe:
        return True
    else:
        return False

def login(user_name: str , password: str):
    is_active = False
    user_id = ''
    for i in range(1,len(user_dict)+1):
        if(user_dict.get(str(i)).get('user_name') == user_name and user_dict.get(str(i)).get('password')== password):
            is_active = True
            user_id = str(i)
            break
    if is_active:
        return user_dict.get(user_id)
    else:
        return {}


def update_safe(user:dict, gained_chip: int):
    user.update({
        'safe': user.get('safe') + gained_chip
    })

def main():
    auth_user = login(
        input('Username: '),
        input('Password: ')
    )
    if auth_user != {}:
        daily_chips = gain_daily_reward()
        update_safe(auth_user, daily_chips)

        print(f'Welcome {auth_user.get("user_name")}, you gain {daily_chips} and so your safe is {auth_user.get("safe")}')

        while True:
            if auth_user.get('safe') >= minimum_bet:
                bet = int(input('Please make a bet: '))
                if is_bet_valid(bet,auth_user.get("safe")):
                    player = assign_bot(bots)

                    print(f'Your oppent name is {player}..!\nLets play..!')

                    player_1_roll = roll_dice()
                    player_2_roll = roll_dice()

                    if player_1_roll > player_2_roll:
                        auth_user.update({
                            'safe': auth_user.get('safe') + (bet*2)
                        })
                        print(f'Your dice is {player_1_roll}\n{player} dice is {player_2_roll}')
                        print(f'Congratulations {auth_user.get("user_name")}..!\nYour Current safe is {auth_user.get("safe")}')
                    elif player_2_roll > player_1_roll:
                        auth_user.update({
                            'safe': auth_user.get('safe') - bet
                        })
                        print(f'Your dice is {player_1_roll}\n{player} dice is {player_2_roll}')
                        print(
                            f'Unlucky {auth_user.get("user_name")}..!\nYour Current safe is {auth_user.get("safe")}')

                else:
                    print('Please make a valid bet..!')

            else:
                print(f'Your {auth_user.get("safe")} safe is under the minimum table bet..!\nDo you want to buy any chips?')
                break

    else:
        print('Invalid credantial!..')


main()