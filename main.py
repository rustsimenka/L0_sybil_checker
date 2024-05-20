with open('my_wallets.txt', 'r') as my_wallets, \
        open('l0_black_list.txt', 'r') as wallets_sibyls, \
        open('my_bad_wallets.txt', 'w', encoding='utf-8') as my_bad_wallets:

    set_sibyls = set(wallets_sibyls.read().split('\n'))
    count_bad_wallets = 0

    for line in my_wallets:
        if line.strip():
            if line.strip().lower() in set_sibyls:
                print(f'{count_bad_wallets + 1}. {line}', file=my_bad_wallets)
                count_bad_wallets += 1
    if count_bad_wallets == 0:
        print("Я всё проверил, Ваших кошельков нет в списке сибилов", file=my_bad_wallets)
