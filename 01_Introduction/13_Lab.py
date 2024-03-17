burak_account = {
    'account_no': '12345',
    'full_name': 'Burak Yılmaz',
    'user_name': 'beast',
    'password': '123',
    'balance': 3000,
    'additional_balance': 1000,
}

hakan_account = {
    'account_no': '98765',
    'full_name': 'Hakan Yılmaz',
    'user_name': 'bear',
    'password': '123',
    'balance': 5000,
    'additional_balance': 1000,
}
ipek_account = {
    'account_no': '56478',
    'full_name': 'İpek Yılmaz',
    'user_name': 'keko',
    'password': '123',
    'balance': 8000,
    'additional_balance': 1000,
}

users = [burak_account, hakan_account, ipek_account]

#region withdraw money
#Çekilmek istenilen para bakiye tarafından karşılanmalı
#miktar bakiyeden fazla ise ek hesap kullanılsın mı diye müşteriye soralım
#müşteri evet derse ek hesap devreye girsin ve para çekilsin
#hayır derse işlem iptal
#adamın balance ve additional balance'si çekilmek istenilen tutarı karşılamıyorsa feedback verip işlemi iptal edilsin


def menu(account: dict):
    print(f"""
    Welcome, {account.get('full_name')}
    ===================================
    Withdraw Money                 => 1
    Deposit Money                  => 2
    Account Info                   => 3
    EFT                            => 4
    Exit                           => 5
    """)

def login(account_no: str, password: str) -> dict:
    account = {}
    for user in users:
        if user["account_no"] == account_no and user["password"] == password:
            account = user
            break
    return account

def balance_result(account: dict) -> None:
    print(f'You have {account["balance"]} TL. Account No: {account["account_no"]}\n'
          f'Additional balance has {account["additional_balance"]}')
def withdraw_money(amount: int, account: dict)-> None:
    if account['balance'] >= amount:
        account['balance'] -= amount
        print("Do not forget to take money..!")
        balance_result(account)
    else:
        total_balance = account['balance'] + account['additional_balance']

        if total_balance >= amount:
            use_additional_balance = input('Insufficient balance.Do you want to use additional balance? ("yes" or "no")').lower()

            match use_additional_balance:
                case 'yes':
                    amount_used_additional_ballance = amount - account['balance']
                    account['balance'] = 0
                    account['additional_balance'] -= amount_used_additional_ballance
                    balance_result(account)
                case 'no':
                    print("Transaction has been canceled")
                    balance_result(account)
        else:
            print('Insufficient total balance. Transaction has been canceled')

def deposit_money(account: dict, amount: int):
    account['balance'] += amount
    if account['additional_balance'] < 1000:
        transfered_amount = 1000 - account['additional_balance']
        account['balance'] -= transfered_amount
        account['additional_balance'] += transfered_amount
    balance_result(account)

def show_account_info(account: dict) -> None:
    print(f'Account Information\n'
          f'==================='
          f'Full Name: {account['full_name']}'
          f'Account No: {account['account_no']}'
          f'Password: {account['password']}'
          f'Balance: {account['ballance']}'
          f'Additional Balance: {account['additional_balance']}')

def eft_transaction(sender_account: dict, receiver_account_no: str, amount: int) -> None:
    for user in users:
        if user['account_no'] == receiver_account_no:
            withdraw_money(amount, sender_account)
            deposit_money(user, amount)

def main():
    user_account = login(
        input('Account No: ').lower(), input('Password: ')
    )
    if user_account != {}:

        menu(user_account)
        while True:
            process = input('Please choose a process: ')

            match process:
                case '1':
                    amount = int(input('Amount: '))
                    withdraw_money(amount,user_account)
                case '2':
                    amount = int(input('Amount: '))
                    deposit_money(user_account,amount)
                case '3':
                    show_account_info(user_account)
                case '4':
                    amount = int(input('Amount: '))
                    receiver_no = input("Receiver No: ")
                    eft_transaction(user_account, receiver_no, amount)
                case '5':
                    print('Application has been closing..!')
                    break
                case  _:
                    print('Invalid type')
    else:
        print('Authentication failed. Please check your credentials..!')

main()
