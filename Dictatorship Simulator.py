day=1
publicorder=50
fear=0
military=100
population=1000
money=1000
lowpublicorder=['A fierce storm is growing in the east.', 'The people stay sheltered in their homes.', 'You feel an air of unease among your subjects', 'The economy is failing.', 'The people grow restless', 'Rumours spread about a terrorist group.', 'Hurried whispers spread amongst the people.']
highpublicorder=['The sun is shining on your growing empire.', 'The people are smiling.', 'Your country is growing', 'The people are happy.', 'The economy is strong.', 'Your subjects congratulate you on your strong rule.']
normalpublicorder=['The rain splashes down on tin rooves.', 'The people hurry to work as usual.', 'The cars hustle in the streets.']
import random
import time
rebels=0

while publicorder>0:
    rebeltotalchance=random.randint(0, 100+fear)
    if rebeltotalchance>publicorder+fear-1:
        rebelchance=random.randint(0,1)
        if rebelchance==1:
            rebels=1
        elif rebelchance==0:
            rebels=rebels
    elif rebeltotalchance<publicorder+fear:
        rebels=rebels

    print('Day ', day)
    time.sleep(.1)
    if publicorder<30:
        print(random.choice(lowpublicorder))
    elif publicorder>90:
        print(random.choice(highpublicorder))
    else:
        print(random.choice(normalpublicorder))
    print('')

    time.sleep(2)
    print('Public order: ', publicorder, '%', sep='')
    time.sleep(.1)
    print('Fear: ', fear, '%', sep='')
    time.sleep(.1)
    print('Military power:', military)
    time.sleep(.1)
    print('Money: $', money, sep='')
    time.sleep(.1)
    print('Population:', population)
    time.sleep(.1)
    print('')

    time.sleep(2)
    print('Your advisor comes to your side and asks what the day\'s action will be.')
    time.sleep(.1)
    print(' - Recruit members for the great army (press 1)')
    time.sleep(.1)
    print(' - Expand your empire (press 2)')
    time.sleep(.1)
    print(' - Print money (press 3)')
    time.sleep(.1)
    print(' - Do a public parade (press 4)')
    time.sleep(.1)
    print(' - Demonstrate your military power (press 5)')
    time.sleep(.1)
    print(' - Search for rebelions (press 6)')

    while True:
        action=int(input())
        if action<1:
            print('That is not an option. Please try again.')
            continue
        elif action>7:
            print('That is not an option. Please try again.')
            continue
        elif 0<action<8:
            break

    if action==1:
        willingrecruits=(publicorder*population)//100-random.randint(0, 0.1*(population-military))
        recruitcosts=10-round(((publicorder/20)+0.1*random.randint(0, 10)),2)
        print('Radio announcers around the country round up people to enlist in the Great Army.')
        time.sleep(.1)
        print('There are ', willingrecruits, ' people willing to enlist in the great army. Recruitments cost $', recruitcosts, ' each.')
        time.sleep(.1)
        print('How many people would you like to recruit? Type a negative number to remove people. If you remove people from the Great Army, you will not gain the recruitment fee back, but you will no longer have to pay their daily fee.')
        while True:
            recruits=int(input())
            if recruits>willingrecruits:
                print('You do not have enough people willing to enlist.')
                continue
            elif recruits*recruitcosts>money:
                print('You do not have enough money to enlist', recruits, 'people.')
                continue
            elif recruits<0-military:
                print('You cannot remove more than', military, 'people from the army.')
                continue
            elif 0>recruits>(0-military)-1:
                publicorderaction=100*(1/(20*military))*random.randint(recruits, recruits//5)
                print('You removed ', 0-recruits, ' people from the Great Army. The people did not like to see their families lose their jobs and you lost ', 0-publicorderaction, '% of your public order.', sep='')
                military=military+recruits
                publicorder=publicorder+publicorderaction
                break
            elif 0<recruits<military+1:
                print('You recruited', recruits, 'people for the Great Army.')
                military=military+recruits
                money=money-(recruits*recruitcosts)
                break
            elif recruits==0:
                print('You did nothing')
                break

    elif action==2:
        militarymodifier=population//military
        opposingmilitary=random.randint((military//5)+militarymodifier, (military//2)+10*militarymodifier)
        opposingpopulation=random.randint(opposingmilitary*2, opposingmilitary*20)
        if publicorder<10:
            print('The Great Army refuses to fight for you.')
        elif publicorder>90:
            opposingmilitary=opposingmilitary//2
        if publicorder>10:
            if military>opposingmilitary:
                militarydeaths=random.randint(0.02*military, 0.2*military)
                population=population+opposingpopulation
                print('Your conquest was succesful. You gained control over', opposingpopulation, 'people, unfortunately, you lost', militarydeaths, 'people in the fight.')
                population=population-militarydeaths
                military=military-militarydeaths
            elif military<opposingmilitary:
                militarydeaths=random.randint(0.5*military, 0.9*military)
                militarycosts=random.randint(((((1000*military)//population)/1000)*money)/2, (((1000*military)//population)/1000)*money*2)
                print('Your Great Army was overpowered by the opposition. Many people died, however, ', military-militarydeaths, ' people managed to retreat in time. You also had to pay a fee of $', militarycosts, ' to cover the costs for the opposition.')
                population=population-militarydeaths
                military=military-militarydeaths
                money=money-militarycosts
            elif military==opposingmilitary:
                militarydeaths=random.randint(0.2*military, 0.5*military)
                print('Your invasion came to a stalemate. Both sides agrees to retreat. You lost', militarydeaths, 'people in the onslaught.')
                population=population-militarydeaths
                military=military-militarydeaths

    elif action==3:
        printable=random.randint(money//5, (money*2)//1)
        print('The money printers whir to life for another round of printing. Small amounts of ink slosh out of their containers.')
        time.sleep(.1)
        print('You can print up to $', printable, '.', sep='')
        time.sleep(.1)
        print('How much money would you like to print?')
        while True:
            printedmoney=int(input())
            if printedmoney<0:
                print('You can\'t burn money.')
                continue
            elif printedmoney>printable:
                print('You don\'t have enough ink to print this much money.')
                continue
            elif 0<printedmoney<printable+1:
                publicorderaction=round((printedmoney/money)*random.randint(20,50), 2)
                print('You printed $', printedmoney, '. This damages the economy, pushing the people further into poverty. You lost ', publicorderaction, '% public order.', sep='')
                money=money+printedmoney
                publicorder=publicorder-publicorderaction
                break
            elif printedmoney==0:
                print('You did nothing.')
                break

    elif action==4:
        if publicorder<10:
            attendees=((population*(publicorder/100))//1)+random.randint(0, population//50)
        elif publicorder>90:
            attendees=round((population*(publicorder/100))-random.randint(0, population//50), 2)
        else:
            attendees=round((population*(publicorder/100))+random.randint(0-population//50, population//50), 2)
        print('There will be', attendees, 'people attending your parade.')
        time.sleep(.1)
        print('How much money would you like to spend on the parade?')
        while True:
            parademoney=int(input())
            if parademoney>money:
                print('You don\'t have this much money.')
                continue
            elif parademoney<0:
                print('You can\'t spend negative money.')
                continue
            elif parademoney==0:
                print('You called off the parade.')
                break
            elif 0<parademoney<money+1:
                publicorderaction=round(((attendees*parademoney)/(population**2))/0.01, 2)
                print('You held an extravagant parade, hoping to win over the peoples\' hearts with your display. You gained ', publicorderaction, '% public order.', sep='')
                publicorder=publicorder+publicorderaction
                money=money-parademoney
                break

    elif action==5:
        fearaction=round(random.randint(((50*military)//population), ((100*military)//population)), 2)
        publicorderaction=round(random.randint(fearaction//5, fearaction), 2)
        print('You sent your troops marching down the streets to strike fear into the hearts of those who oppose you. You gained ', fearaction, '% fear, but lost ', publicorderaction, '% public order.', sep='')
        fear=fear+fearaction
        publicorder=publicorder-publicorderaction

    elif action==6:
        if rebels==0:
            publicorderaction=random.randint(1,5)
            print('You searched every home and establishment for signs of rebelion, but found none. The people did not like this disruption. You lost ', publicorderaction, '% public order.', sep='')
            publicorder=publicorder-publicorderaction
        elif rebels==1:
            findchance=random.randint(1, 2+(fear//50))
            if findchance==1:
                fearaction=random.randint(5,15)
                print('You found some rebels hidding in a derelict warehouse. You made a public show of their execution to discourage any of their followers. You gained ', fearaction, '% fear.', sep='')
                rebels=0
                fear=fear+fearaction
            elif findchance>1:
                publicorderaction=random.randint(1+(fear//50),5+(fear//50))
                print('You searched every home and establishment for signs of rebelion, but found none. The people did not like this disruption. You lost ', publicorderaction, '% public order.', sep='')
                publicorder=publicorder-publicorderaction 

    if publicorder>100:
        publicorder=100
    if fear>100:
        fear=100
    if fear<0:
        fear=0
    if publicorder<0:
        publicorder=0
    if population<0:
        population=0
    if military<0:
        military=0
    if money<0:
        money=0
    if military>population:
        military=population
    publicorder=round(publicorder, 2)
    money=rount(money, 2)
        
    taxes=round(population*(publicorder/500), 2)
    militarytaxes=round(military*0.05, 2)
    if rebels==1:
        publicorderend=random.randint(1,10)
    elif rebels==0:
        publicorderend=random.randint(1,5)
    if fear>10:
        fearend=random.randint(1,5)
    elif fear<11:
        fearend=0
    print('')
    time.sleep(2)
    print('The day ends')
    if fearend==0:
        print('You gained $', taxes, ' from taxes.')
        time.sleep(.1)
        print('You lost ', publicorderend, '% public order.', sep='')
        money=money+taxes
        publicorder=publicorder-publicorderend
    elif fearend>0:
        print('You gained $', taxes, ' from taxes.')
        time.sleep(.1)
        print('You lost ', publicorderend, '% publicorder and ', fearend, '% fear.', sep='')
        money=money+taxes
        publicorder=publicorder-publicorderend
        fear=fear-fearend
    if militarytaxes>0:
        time.sleep(.1)
        print('You also had to pay $', militarytaxes, ' to cover the costs of the military.', sep='')
        money=money-militarytaxes
    day=day+1
    if population==0:
        publicorder=0
    print('')
    time.sleep(3)
    
    if publicorder>100:
        publicorder=100
    if fear>100:
        fear=100
    if fear<0:
        fear=0
    if publicorder<0:
        publicorder=0
    if population<0:
        population=0
    if military<0:
        military=0
    if money<0:
        money=0
    if military>population:
        military=population
    publicorder=round(publicorder, 2)
    money=rount(money, 2)

endtext=['The streets run red with blood.', 'Your empire descends into chaos.', 'There is no one left alive to rule.', 'The empire erupts into civil war.']
print(random.choice(endtext))
time.sleep(1)
print('...')
time.sleep(1)
print('You lose.')
time.sleep(1)
