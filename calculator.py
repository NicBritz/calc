while True:

    user_input = input('>>> ')

    if user_input.lower() == 'q':
        break
    else:

        current = 0
        l = user_input.split()
        ll = [int(i) for i in l if i.isnumeric()]

        for i in l:
            if i == '+':
                print(sum(ll))

