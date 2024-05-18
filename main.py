with open('my_wallets.txt', 'r') as my_wallets, open('initialList.txt', 'r') as wallets_sybils, open('my_bad_wallets.txt', 'w', encoding='utf-8') as my_bad_wallets:

    tuple_sybils = tuple(wallets_sybils.read().split('\n'))
    x = 0

    for line in my_wallets:
        if line.strip() in tuple_sybils:
            print(line, file=my_bad_wallets)
            x =+ 1
    if x == 0:
        print('Я всё проверил, Ваших кошельков нет в списке сибилов', file=my_bad_wallets)