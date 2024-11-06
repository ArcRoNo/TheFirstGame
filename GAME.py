
import time
import sys
hp = 2
knifes = 0
smoke = 0
hp_T1=2
mp = 1
eat = 1
water = 1
sword = 0
bandit_cont = 19
egg = 0
team = 0
stels_chos = False
#16 макс итераций 4 дня более 9-12 луз/вин презентация 3 слайда про чара про суть про что нибудь
def slow_print(text): 
    for char in text: 
        print(char, end='', flush=True) 
        time.sleep(0.04)  # Задержка в 0.1 секунды между символами 
    print()
slow_print('ДИСКЛЕЙМЕР\nЯ не успел пофиксить выбор одного и того же варианта несколько раз игра не сломается но в идеале не делать так')
slow_print('Сюжет фикция нужная для подводки к выборам')
slow_print("Вас зовут Фаруст, вы авантюрист и после удачного рейда в подземелье вы весело провели всю ночь в таверне родного маленького городка")
slow_print(f"Вы просыпаетесь в пустой таверне. Вы голодны и испытываете жажду\nУР.Здоровья {hp}\nУР.Воды {water}\nУР.Еды {eat}\nУР.Манны {mp}")
slow_print("Что вы делаете?")
slow_print("(Чтобы выбрать введите соответствующую цифру)")
Taverna_Choose = 0

a = True
his_choos_taverna = []
#tav_cho выбор в таверне
while a == True:
    print('1. Поискать что-нибудь за стойкой')
    print('2. Поискать что-нибудь на столах')
    print('3. Зайти в подсобку')
    print('4. Позвать кого-нибудь')
    print('5. Выйти из таверны')
    tav_cho = input()
    while tav_cho not in ['1','2','3','4','5']:
        print('А если нормально ввести?')
        tav_cho = input()
    match tav_cho:
        case "1":
            #пофиксить абуз одинак вариантов
            slow_print("За стойкой вы находите недопитую бутылку воды")
            slow_print("УР.Воды + 5")
            water += 5
            Taverna_Choose += 1
            his_choos_taverna.append(1)

        case "2":
            slow_print("На столе вы находите недоеденную похлёбку\nУР.Еды +3")
            eat += 3
            Taverna_Choose += 1
            his_choos_taverna.append(2)
            
        case "3":
            slow_print("Вы входите в подсобку")
            his_choos_taverna.append(3)
            a_case3 = True
            while a_case3 == True:
                slow_print("(Выберете что-то одно)")
                print("1. поискать в коробках")
                print("2. выйти")
                print("3. поискать на полках")
                tav_case3 = input()
                while tav_case3 not in ['1','2','3','4','5']:
                    print('А если нормально ввести?')
                    tav_case3 = input()
                match tav_case3:
                    case "1":
                        slow_print("Вы находите зелье маны\nУР.Манны +3\nИ выходите из подсобки т.к мне лень делать большие вложение функции")
                        mp+=3
                        Taverna_Choose += 1
                        a_case3 = False
                        
                    case "2":
                        slow_print("Вы выходите из подсобки")
                        Taverna_Choose += 1
                        a_case3 = False
                        
                    case "3":
                        slow_print("Вы ищите на полках и замечаете старый но добротный меч\nИ выходите из подсобки т.к мне лень делать большие вложение функции")
                        sword = 1
                        Taverna_Choose += 1
                        a_case3 = False
                        
        case "4":
            slow_print("Вы окликаете кого-нибудь и вслушиваетесь\n. . . .\nвдруг вы слышите шаги на улице\n Что вы делаете")
            a_case4 = True
            while a_case4 == True:
                slow_print("(Выберете что-то одно)")
                print("1. Спрятаться")
                print("2. проигнорировать")
                print("3. Выйти к ним")
                tav_case4 = input()
                while tav_case4 not in ['1','2','3','4','5']:
                    print('А если нормально ввести?')
                    tav_case4 = input()
                match tav_case4:
                    case '1':
                        slow_print('Вы прячетесь\nВ таверну заходит несколько креко сбитых, недружелюбно выглядящих человека\nони не замечают вас и уходят\nВы решаете проследить за ними\nОни заходят в здание городского совета, видимо они связаны с пропажей всех и обосновались там')
                        a_case4=False
                        a = False
                        stels_chos = True
                    case '2':
                        slow_print('Вы решаете просто проигнорировать шаги(серьёзно?)')
                        Taverna_Choose += 1
                        a_case4 = False
                    case '3':
                        slow_print('Вы выходите за дверь')
                        a_case4 = False
                        a = False
                        egg = 1
        case "5":
            slow_print('Вы выходите из таверны')
            egg = 1
            a = False
    if Taverna_Choose == 2:
        a = False

if (stels_chos == False):
    street_f = 1
    while street_f == 1:
        if egg == 1:
            slow_print('\n\nТолько вы вышли из таверны и осмотрелись на необычно тихой улице у вашего лица пролетает кинжал\nвы замечаете 3 крепких парней идущих к вам с явно не хорошими намерениями\nЧто вы делаете?')
        else:
            slow_print('\n\nВдруг в таверну врываются три креко сбитых, недружелюбно выглядящих человека\nчто вы делаете')
        slow_print(f'УР.Здоровья {hp}\nУР.Воды {water}\nУР.Еды {eat}\nУР.Манны {mp}\nНаличие оружия {sword}')
        print('1. Сражаться')
        print('2. Бежать')
        print('3. Использовать заклинание')
        egg_fight = input()
        while egg_fight not in ['1','2','3']:
            print('А если нормально ввести?')
            egg_fight = input()
        match egg_fight:
            case '1':
                if sword >= 1:
                    slow_print('С мечом вы с легкостью побеждаете каких-то бандитов и осматриваетесь')
                    bandit_cont -=3
                    street_f = 0
                else:
                    slow_print('вы с трудом побеждаете их получив несколько ран УР.Здоровья-1')
                    hp -= 1
                    street_f = 0             
            case '2':
                if water >2:
                    slow_print('Вы убегаете от них и осматриваетесь')
                    street_f = 0
                    water -=2
                else:
                    slow_print('Вы слишком хотите пить чтобы убежать')
            case '3':
                if mp > 2:
                    slow_print('Вы сносите бандитов огненым шаром и оглядываетесь')
                    mp -= 2
                    street_f = 0
                else:
                    slow_print('У вас не хватает манны')

if (stels_chos == True):
    slow_print('Вы возвращаетесь к таверне и оглядываетесь')

slow_print('Город выглядит необычно пустынно и только ветер завывает на пустых улицах\nследует осмотреть город, куда вы идёте?')
city_choose= 1
while city_choose ==1:
    print('1. Сходить домой')
    print('2. Сходить в церковь')
    print('3. Сходить в городской совет')
    print('4. Сходить на площадь')
    print('5. Сходить на рынок')
    
    go_choose = input()
    while go_choose not in ['1','2','3','4','5']:
        print('А если нормально ввести?')
        go_choose = input()
    match go_choose:
        case '1':
            slow_print('Вы идёте домой\nДома вы берёте свой основной меч\nКуда вы идёте дальше')
            sword = 1
        case '2':
            slow_print('Вы идёте в церковь\nНа своё удивление там вы находите своего сокомандника, спящего на лавке\nВы с трудом будите его и обьясняете ситуацию\nКуда вы идёте дальше')
            team +=1
        case '3':
            city_choose = 0
        case '4':
            slow_print('На площади абсолютно пусто только на полу валялась маленькая бутылка маны Ур.Маны +1')
            mp +=1
        case '5':
            slow_print('На рынке вы находите много полезного\nВы едите, пьёте и используете найденую аптечку первой помощи Ур.Здоровья, Ур.Еды, Ур.Воды +1')
            hp +=1
            eat +=2
            water +=2
slow_print('Вы идёте в городской совет\nзайдя в здание вы сразу натыкаетесь на группу из 4 вооружённых бандитов и они сразу бросаются на вас\nчто вы делаете')
mary_fight = 1
print(f'УР.Здоровья {hp}\nУР.Воды {water}\nУР.Еды {eat}\nУР.Манны {mp}\nНаличие оружия {sword}\nКоличество сокомандников {team}')
while mary_fight ==1:
    print('1. Сражаться')
    print('2. Использовать магию')
    print('3. Бежать')
    mary_fight_choose = input()
    while  mary_fight_choose not in ['1','2','3']:
        print('А если нормально ввести?')
        mary_fight_choose = input()
    match mary_fight_choose:
        case '3':
            slow_print('только вы развернулись дверь захлопнулась бежать не выйдет')
        case '2':
            if mp>2:
                slow_print('Вы сносите бандитов огненым шаром и идёте дальше')
                mary_fight = 0
                bandit_cont -=4
                mp -= 2
            else:
                slow_print('У вас не хватает манны')
                if team >0:
                    slow_print('у вашего сокомандника тоже')
        case '1':
            if sword == 0 and team == 0:
                   slow_print('У вас нет ни меча ни команды по этому Вы проиграли драку\nGAME OVER')
                   time.sleep(3)
                   sys.exit() 
                   
            if sword == 1 and team == 1:
                   slow_print('Вы вдвоём с лёгкостью побеждаете бандитов и идёье дальше')
                   bandit_cont -=4
                   mary_fight = 0
            if sword == 0 and team == 1:
                slow_print('ваш сокомандник с трудом справляется в бандитами с вашей помощью Ур.Здоровья.Сокомандника-1')
                hp_T1 -= 1
                bandit_cont -=4
                mary_fight = 0
            if sword == 1 and team == 0:
                slow_print('Вы с трудом побеждаете 4 бандитов но получаете ранения')
                hp -=1
                bandit_cont -=4
                mary_fight = 0
                if hp == 0:
                    print('Вы получили слишком много ран и умерли')
                    time.sleep(3)
                    sys.exit() 
                    
eat -= 1
slow_print('Поднявшись на второй этаж вы ходите по пустым кабинетам и в кабинете главы находите карту с обозначенным на ней лагерем в лесу, видимо все там\nВы видвинулись туда')
if eat < 2:
    slow_print('Из за голода вам не очень хорошо Ур.Здоровья-1')
    hp -=1
if eat == 0:
    slow_print('Поздравляю вы умудрились умереть от голода')
    time.sleep(3)
    sys.exit()
slow_print('Вы подошли лагерю бандитов и осматриватесь из кустов\nВыдимо это просто перевалочный пункт тут стоит только 1 телега с жителями вашей деревни, остальные видимо уже кудато отправлены\nтут только 3 противника что вы делаете')
print(f'УР.Здоровья {hp}\nУР.Воды {water}\nУР.Еды {eat}\nУР.Манны {mp}\nНаличие оружия {sword}\nКоличество сокомандников {team}')
if team == 1:
    print(f'здоровье сокомандника {hp_T1}')
forest_fight = 1
while forest_fight == 1:
    print('1. Выйти и сразиться с ними')
    print('2. Дождаться ночи и напасть')
    print('3. использовать заклинание из кустов')
    forest_fight_choose = input()
    while forest_fight_choose not in ['1','2','3']:
        print('А если нормально ввести?')
        forest_fight_choose = input()
    match forest_fight_choose:
        case '1':
            if sword == 0 and team == 0:
                   slow_print('У вас нет ни меча ни команды по этому Вы проиграли драку\nGAME OVER')
                   sys.exit() 
            if sword == 1 and team == 1:
                   slow_print('Вы вдвоём с лёгкостью побеждаете бандитов')
                   bandit_cont -=3
                   forest_fight = 0
            if sword == 0 and team == 1:
                slow_print('ваш сокомандник с трудом справляется в бандитами с вашей помощью Ур.Здоровья.Сокомандника-1')
                hp_T1 -= 1
                bandit_cont -=3
                forest_fight = 0
                if hp_T1 == 0:
                    slow_print('ваш сокомандник в очень тяжёлом состоянии по этому вы оказываете ему первую помощь и оставляете его отдыхать')
                    team -=1
            if sword == 1 and team == 0:
                slow_print('С мечом Вы без проблем побеждаете 3 бандитов')
                bandit_cont -=3
                forest_fight = 0
        case '2':
            slow_print('Времени мало не следует отлагать')
        case '3':
            if mp>2:
                slow_print('Вы сносите бандитов огненым шаром')
                forest_fight = 0
                bandit_cont -=3
                mp -= 2
            else:
                slow_print('У вас не хватает манны')
                if team >0:
                    slow_print('у вашего сокомандника тоже')

slow_print('Вы освобождаете жителей и находите 5 серебряных')
gold = 5
smoke = 0
if team == 1:
    slow_print('Ваш сокомандник подзывает вас и показывает карту найденую у одного из трупов она указывает на подпольный рынок соседнего города')
else:
    slow_print('Вы находите карту у одного из трупов она указывает на подпольный рынок соседнего города')
slow_print('Вы спешите туда, лишнего времени нет, но надо решить как освободить остальных, Вы можете успеть добежать только до 2 лавок')
print(f'УР.Здоровья {hp}\nУР.Воды {water}\nУР.Еды {eat}\nУР.Манны {mp}\nНаличие оружия {sword}\nКоличество сокомандников {team}')
if team == 1:
    print(f'здоровье сокомандника {hp_T1}')
prefinal_choose = 1
prefinal_choose_count = 2

while prefinal_choose_count !=0:

    print('1. купить зелье маны 1 серебряный')
    print('2. купить метательные ножи 2 серебряных')
    print('3. нанять союзника в гильдии 4 серебряных')
    print('4. купить дымовую шашку 1 серебряный')
    print('5. купить аптечку 1 серебряный ')
    print('6. купить меч 3 серебряных')
    prefinal_choose = input()
    while prefinal_choose not in ['1','2','3','4','5','6']:
        print('А если нормально ввести?')
        prefinal_choose = input()
    match prefinal_choose:
        case '1':
            if gold >0:
                prefinal_choose_count -=1
                slow_print('Вы купили зелье маны Ур.Маны +3')
                mp += 3
                gold -=1
            else:
                slow_print('денег нет')
        case '2':
            if gold >1:
                slow_print('Вы купили 2 метательных ножа')
                knifes = 2
                prefinal_choose_count -=1
                gold -=2
            else:
                slow_print('денег нет')
        case '3':
            if gold >3:
                team +=1
                prefinal_choose_count -=1
                hp_T2 = 2
                gold -=4
                slow_print(f'Вы наняли союзника теперь вас {team+1}')
            else:
                slow_print('денег нет')
        case '4':
            if gold >0:
                prefinal_choose_count -=1
                smoke += 1
                gold -=1
                slow_print('Вы купили дымовую шашку')
            else:
                slow_print('денег нет')
        case '5':
            if gold > 0:
                slow_print('Вы купили аптечку Ур. Здоровья + 2')
                hp +=2
                gold -=1
                prefinal_choose_count -=1
            else:
                slow_print('денег нет')
        case '6':
            if gold > 2:
                slow_print('Вы купили новый меч')
                gold -=3
                sword += 1
                prefinal_choose_count -=1
                if sword == 2:
                    slow_print('теперь у вас 2 меча')
            else:
                slow_print('денег нет')
    if prefinal_choose_count ==0:
        prefinal_choose = 0
#9
slow_print('Вы подходите к двери подпольного рынка')
print(f'УР.Здоровья {hp}\nУР.Воды {water}\nУР.Еды {eat}\nУР.Манны {mp}\nНаличие оружия {sword}\nКоличество сокомандников {team}')
if team == 1:
    print(f'здоровье сокомандника {hp_T1}')
if team >1:
    print(f'здоровье сокомандника 1 {hp_T1}\nздоровье сокомандника 2 {hp_T2}')
print(f'ножей {knifes}\nдымовых шашек {smoke}')
slow_print('Начать с дымовой шашки?')
print('1 Да\n2 Нет')
final_f1 = input()
while final_f1 not in ['1','2']:
        print('А если нормально ввести?')
        final_f1 = input()
match final_f1:
    case '1':
        if smoke == 0:
            slow_print('так нет её')
            slow_print(f'вы просто врываетесь в дверь и видите {bandit_cont} противников')
        else:
            slow_print('Вы кидаете дымовую шашку и врываетесь в дверь')
    case '2':
        slow_print(f'вы врываетесь в дверь и видите {bandit_cont} противников')
if sword == 2:
    bandit_cont -=1
    #8
    slow_print('Вы кидаете 1 из мечей, всё же с 1 привычнее,')
    sword -= 1
    if smoke != 0:
        slow_print('В дыму вы слышите хрипение, видимо повезло')
    else:
        slow_print('и попадаете в врага')
if sword == 0:
    slow_print('Без меча сражаться возможно, но тяжело. Вы продвигаетесь убив 2 противников но получаете раны ')
    bandit_cont -=2
    hp -= 1
    if hp == 0:
        time.sleep(3)
        sys.exit()
    slow_print('вдруг у 1 из побеждённых противников вы находите подходящий меч и решаете продолжить с ним')
    sword = 1
else:
    slow_print('С мечом Вы продвигаетесь без особых трудностей убив 2 противников')
    bandit_cont -=2
    #6
if team !=0:
    if team == 1:
        slow_print('Вы слышите падающие тела с стороны видимо сокомандник справляется')
        bandit_cont -=2
    else:
        slow_print('Вы слышите падающие тела с стороны видимо сокомандники справляется')
        bandit_cont -=4
if smoke == 1:
    slow_print(f'Вы оглядываетесь противников осталось всего {bandit_cont}')
if smoke == 0 and sword != 0:
    slow_print('При встрече с очередным противником вас внезапно ударяют со спины и выбивают меч Ур. здоровья -1')
    hp -= 1
    if hp == 0:
        time.sleep(3)
        sys.exit()

slow_print('что делать')
print('1 продолжить сражение руками')
print('2 попробовать добежать до своего меча')
print('3 продолжить сражение метательным ножом')
print('4 раскинуть всех огненым шаром и прорваться к мечу')
final_f2 =1
while final_f2 == 1:
    final_f2_c = input()
    while final_f2_c not in ['1','2','3','4']:
        print('А если нормально ввести?')
        final_f2_c = input()
    match final_f2_c:
        case '1':
            slow_print('руками сражаться тяжело но возможно, вы побеждаете 2 противников и возвращаете свой меч Ур.здоровья -1')
            hp -=1
            bandit_cont -=2
            final_f2 =0
        case '2':
            if water <=2:
                slow_print('Вы слишком хотите пить, чтобы добежать до него')
            else:
                slow_print('Резким рывком вы добегаете до меча и распавляетесь с противниками')
                bandit_cont -=2
                final_f2 =0
        case '3':
            if knifes == 0:
                slow_print('Так у вас их нет')
            else:
                slow_print('Вы выхватываете метательный нож, побеждаете противников и подбераете свой меч обратно')
                bandit_cont -= 2
                final_f2 =0
        case '4':
            if mp <= 2:
                slow_print('У вас не хватит маны')
            else:
                slow_print('Вы используете огненый шар и раскидываете противников')
                bandit_cont -= 2
                final_f2 =0
                if team != 0:
                    slow_print('Но серьёзно задеваете союзника и он отходит')
                    team -=1
if bandit_cont == 0:
    slow_print('Оглядываясь вы видите, чтот противники закончились, Вы победили, Поздравляем')
    time.sleep(3)
    sys.exit()
if smoke != 0:
    slow_print(f'Дым уже рассеивается и вы видите {bandit_cont} противников')
else:
    slow_print(f'вы оглядываетесь и видите {bandit_cont} противников')
if bandit_cont >= 6 and team != 2:
    slow_print('противников осталось слишком много и они окружили вас, вы не спавились Game Over')
    time.sleep(3)
    sys.exit()
else:
    if team == 0:
        if bandit_cont > 4:
            if hp <= 2 and mp <=2:
                slow_print('Противников осталось слишком много и они окружили вас вы не спавились Game Over')
                time.sleep(3)
                sys.exit()
            elif hp > 2 and mp <=2:
                slow_print('Вы с трудом  и ранениями справляетесь с остальными противниками и побеждаете, конец Поздравляем')
                time.sleep(3)
                sys.exit()
            elif mp >2:
                slow_print('противников много но у вас осталась мана и вы применили огненый шар добив оставшихся и побеждаете, конец Поздравляем')
                time.sleep(3)
                sys.exit()
        elif bandit_cont <=4:
            slow_print('Вы с трудом  и ранениями справляетесь с остальными противниками и побеждаете, конец Поздравляем')
            time.sleep(3)
            sys.exit()
    if team != 0:
        slow_print('В команде вы без проблем справляетесь с остальными противниками и побеждаете, конец Поздравляем')
        time.sleep(3)
        sys.exit()
#сделать вариации и выход при кончании бандитов смертб и вариант при плохом старте
