import sys


def which_player():
    name = input("С кем я говорю?\n- ")
    player_number_count = 0
    for player in players:
        if name == player[0]:
            find = True
            break
        else:
            find = False
        player_number_count += 1
    if not find:
        print("Данного игрока не существует.")
    return player_number_count


diesel = ["1", "diesel", 500, 150, 300, 600]
boss = ["2", "boss", 700, 200, 350, 700]
wrangler = ["3", "wrangler", 900, 250, 400, 800]
light_industrial = [diesel, boss, wrangler]

utel = ["4", "utel", 1000, 250, 500, 1000]
kyivstar = ["5", "kyivstar", 1200, 250, 500, 1100]
beeline = ["6", "beeline", 1500, 300, 600, 1200]
mobile_operators = [utel, kyivstar, beeline]

samsung = ["7", "samsung", 1800, 350, 700, 1400]
sony = ["8", "sony", 2000, 350, 700, 1400]
nokia = ["9", "nokia", 2300, 400, 800, 1600]
phone_manufacturers = [samsung, sony, nokia]

audi = ["10", "audi", 2500, 400, 800, 1600]
porshe = ["11", "porshe", 2800, 450, 900, 1800]
ferrari = ["12", "ferrari", 3100, 450, 900, 1800]
automaker = [audi, porshe, ferrari]

spurs = ["13", "spurs", 3300, 500, 1000, 2000]
chicago_bulls = ["14", "chicago_bulls", 3500, 500, 1000, 2000]
lakers = ["15", "lakers", 3700, 550, 1100, 2200]
nba = [spurs, chicago_bulls, lakers]

bayern = ["16", "bayern", 4000, 550, 1100, 2200]
liverpool = ["17", "liverpool", 4200, 600, 1200, 2400]
barselona = ["18", "barselona", 4300, 650, 1300, 2600]
fifa = [bayern, liverpool, barselona]

southwest = ["19", "southwest", 4500, 700, 1400, 2800]
american_airlines = ["20", "american_airlines", 4700, 750, 1500, 3000]
aero_svit = ["21", "aero_svit", 4800, 750, 1500, 3000]
aircompany = [southwest, american_airlines, aero_svit]

tatneft = ["22", "tatneft", 5000, 800, 1600, 3200]
rosneft = ["23", "rosneft", 5500, 850, 1600, 3200]
lukoil = ["24", "lukoil", 6000, 850, 1700, 3400]
neftcompany = [tatneft, rosneft, lukoil]

businesses = [
    light_industrial,
    mobile_operators,
    phone_manufacturers,
    automaker,
    nba,
    fifa,
    aircompany,
    neftcompany,
]

end = False

""" НАЧАЛО """
number_of_players = int(input("Сколько игроков?\n- "))
if number_of_players >= 2 and number_of_players <= 4:
    player1 = [input("Как зовут первого игрока?\n- "), 15000]
    player2 = [input("Как зовут второго игрока?\n- "), 15000]
    players = [player1, player2]
    if number_of_players >= 3:
        player3 = [input("Как зовут третьего игрока?\n- "), 15000]
        players = [player1, player2, player3]
    if number_of_players == 4:
        player4 = [input("Как зовут четвёртого игрока?\n- "), 15000]
        players = [player1, player2, player3, player4]
else:
    print(
        "Невозможное количество игроков для данной игры. Игра рассчитана на 2-4 игрока."
    )
    end = True

while not end:
    question = input("Чем могу помочь?\n- ").lower()

    """ БАЗОВЫЕ КОМАНДЫ """
    if question == "помощь" or question == "help":
        pass

    if question == "правила" or question == "rules":
        pass

    if question == "игроки" or question == "players":
        print(players)

    if question == "баланс" or question == "balance":
        player_number = which_player()
        if player_number < len(players):
            player = players[player_number]
            print(player[1])

    if question == "филиалы" or question == "branches":
        for enterprice in businesses:
            for branch in enterprice:
                print(branch[0], branch[1])

    if question == "мои филиалы" or question == "my branches":
        pass

    if question == "конец" or question == "qq":
        sys.exit("Спасибо за игру!")

    """ КОМАНДЫ С ФИЛИАЛАМИ """
    if question == "купить" or question == "buy":
        player_number = which_player()
        if player_number < len(players):
            player = players[player_number]
            which_branch = input(
                "Какой бизнес вы хотите приобрести? (название/номер)\n- "
            )
            for enterprice in businesses:
                for branch in enterprice:
                    if which_branch == branch[0] or which_branch == branch[1]:
                        if player[1] >= branch[2]:
                            player.append(branch)
                            player[1] -= branch[2]
                            enterprice.remove(branch)
                            find = True
                            print(
                                f"Поздравляю! Вы купили филиал <<{branch[1]}>> за {branch[2]} евриков."
                            )
                        else:
                            print("У вас недостаточно денег.")
            if not find:
                print("Филиала с таким названием/номером не существует.")

    if question == "продать" or question == "sell":
        player_number = which_player()
        if player_number < len(players):
            player = players[player_number]
            buyer = input("Кому вы хотите продать филиал?\n-")
            for player1 in players:
                if buyer == player1[0]:
                    find = True
                    break
                else:
                    find = False
            if not find:
                print("Данного игрока не существует.")
            else:
                which_branch = input(
                    "Какой бизнес вы хотите приобрести? (название/номер)\n- "
                )
                for branch in player[2:]:
                    if which_branch == branch[0] or which_branch == branch[1]:
                        find_brunch = True
                        sales_amount = int(
                            input(
                                f"По какой цене вы хотите продать <<{branch[1]}>> игроку {buyer[0]}?\n- "
                            )
                        )
                        if buyer[1] >= sales_amount:
                            buyer.append(branch)
                            buyer[1] -= sales_amount
                            player.remove(branch)
                            player[1] += sales_amount
                        else:
                            print("У вас недостаточно денег.")
                    else:
                        find_brunch = False
                if not find_brunch:
                    print(f"Филиала <<{branch[1]}>> у игрока {player[0]} нет.")

    """ ОПЛАТА """
    if question == "оплатить" or question == "to pay":
        player_number = which_player()
        if player_number < len(players):
            player = players[player_number]
            which_branch_come = input("Куда вы наступили? (название/номер)\n- ")
            for owner_player in players:
                for branch in owner_player[2:]:
                    if branch[0] == which_branch_come or branch[1] == which_branch_come:
                        pass

    """ НАЛОГОВАЯ """
    if question == "налог" or question == "налоговая" or question == "tax":
        pass

    """ БОНУСЫ """
    if question == "приз" or question == "prize":
        player_number = which_player()
        if player_number < len(players):
            player = players[player_number]
            player[1] += 1500
            print(f"Ваш баланс пополнен на 1500 и равен {player[1]}.")

    if question == "доход 2000" or question == "income 2000":
        player_number = which_player()
        if player_number < len(players):
            player = players[player_number]
            player[1] += 2000
            print(f"Ваш баланс пополнен на 2000 и равен {player[1]}.")

    if question == "доход 5000" or question == "income 5000":
        player_number = which_player()
        if player_number < len(players):
            player = players[player_number]
            player[1] += 5000
            print(f"Ваш баланс пополнен на 5000 и равен {player[1]}.")

    """ СЕКТОР ШАНС """
    if question == "шанс" or question == "chance":
        pass
