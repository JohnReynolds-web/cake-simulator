from time import sleep
breadcakemultiplier=1
base_cooktime=15
breadupgrade={'cost':150,
              'upgrade':1}
breadupgrade2={'cost':250,
               'upgrade':2}
optionlist=['bakery', 'shop','upgrade']
playermoney=9999
bakeryoptions=['bake dough','make cake']
buyshopcosts={'dough':5}
playerinventory={'dough':1,
                 'bread':0,
                 'cake':0}
ovenupgrade1={'cost':20,
              'cooktime':5,}
sellvalues={'dough':3,
            'bread':8,
            'cake':12,}
sellupgrade1={'cost':50,
              'bread':+2,
              'cake':+3}
sellupgrade2={'cost':150,
              'bread':+5,
              'cake':+5}
sellupgrade3={'cost':250,
              'bread':+10,
              'cake':+15}
ovenupgrade2={'cost':150,
                   'cooktime':5}
sellupgrades=['sellupgrade1','sellupgrade2','sellupgrade3']
sellupgradesba=[sellupgrade1,sellupgrade2,sellupgrade3]
ovenupgradesba=[ovenupgrade1,ovenupgrade2]
ovenupgrades=['ovenupgrade1','ovenupgrade2']
breadupgradesba=[breadupgrade,breadupgrade2]
breadupgrades=['breadupgrade','breadupgrade2']
upgradelist=['sellupgrades','ovenupgrades','goldenbread','breadupgrades']
shopoptions=['purchase','sell',]
shoplist=['dough']
def upgrades():
    while True:
        if upgradeinput=='sellupgrades':
            print(sellupgrades)
            sellupgradeinput=input('Pick your choice and type it here or press q to quit: ')
            if sellupgradeinput=='q':
               break
            elif sellupgradeinput.isdigit()==False or len(sellupgradeinput)!=1:
                print('Thats not an option please pick a number')
            else:
                while True:
                    global playermoney
                    sellupgradeyn=input(f"You're about to purchase {sellupgrades[int(sellupgradeinput)-1]} {sellupgradesba[int(sellupgradeinput)-1]}Y/N?: ").lower()
                    if sellupgradeyn=='n':
                        break
                    elif sellupgradesba[int(sellupgradeinput)-1].get('cost')>playermoney:
                        print('You dont have enough money!')
                        sleep(2)
                        break
                    else:
                        sellvalues['bread']+=sellupgradesba[int(sellupgradeinput)-1].get('bread')
                        sellvalues['cake']+=sellupgradesba[int(sellupgradeinput)-1].get('cake')
                        playermoney-=sellupgradesba[int(sellupgradeinput)-1].get('cost')
                        sellupgrades.pop(int(sellupgradeinput)-1)
                        sellupgradesba.pop(int(sellupgradeinput)-1)
                        break
        elif upgradeinput=='ovenupgrades':
            print(ovenupgrades)
            ovenupgradeinput=input('Pick your choice and type it here or press q to quit: ')
            if ovenupgradeinput=='q':
                break
            elif ovenupgradeinput.isdigit()==False or len(ovenupgradeinput)!=1:
                print('Thats not an option please pick a number')
            else:
                while True:
                    ovenupgradeyn=input(f"You're about to purchase {ovenupgrades[int(ovenupgradeinput)-1]} {ovenupgradesba[int(ovenupgradeinput)-1]}Y/N?: ").lower()
                    if ovenupgradeyn=='n':
                        break
                    elif ovenupgradesba[int(ovenupgradeinput)-1].get('cost')>playermoney:
                        print('You dont have enough money!')
                        sleep(2)
                        break
                    else:
                        global base_cooktime
                        base_cooktime-=ovenupgradesba[int(ovenupgradeinput)-1].get('cooktime')
                        playermoney-=ovenupgradesba[int(ovenupgradeinput)-1].get('cost')
                        ovenupgradesba.pop(int(ovenupgradeinput)-1)
                        ovenupgrades.pop(int(ovenupgradeinput)-1)
                        break
        elif upgradeinput=='breadupgrades':
            print(breadupgrades)
            breadupgradeinput=input('Pick your choice and type it here or press q to quit: ')
            if breadupgradeinput=='q':
                break
            elif breadupgradeinput.isdigit()==False or len(breadupgradeinput)!=1:
                print('Thats not an option please pick a number')
            else:
                while True:
                    breadupgradeyn=input(f"You're about to purchase {breadupgrades[int(breadupgradeinput)-1]} {breadupgradesba[int(breadupgradeinput)-1]}Y/N?: ").lower()
                    if breadupgradeyn=='n':
                        break
                    elif breadupgradesba[int(breadupgradeinput)-1].get('cost')>playermoney:
                        print('You dont have enough money!')
                        sleep(2)
                        break
                    elif breadupgradeyn=='y':
                        global breadcakemultiplier
                        breadcakemultiplier+=breadupgradesba[int(breadupgradeinput)-1].get('upgrade')
                        playermoney-=breadupgradesba[int(breadupgradeinput)-1].get('cost')
                        breadupgradesba.pop(int(breadupgradeinput)-1)
                        breadupgrades.pop(int(breadupgradeinput)-1)
                        break
def bakedough():
    print(f'You currently have {playerinventory}')
    input('Bake bread?... (press enter to continue)')
    time_left=base_cooktime
    while True:
        print(time_left)
        time_left=time_left-1
        sleep(1)
        if time_left==0:
            input('Take bread out?...')
            time_left=base_cooktime
            playerinventory['dough']=playerinventory.get('dough')-1
            playerinventory['bread']=playerinventory.get('bread')+breadcakemultiplier
            break
def cookcake():
    print(f'You currently have {playerinventory}')
    input('Make cake?... (press enter to continue)')
    global base_cooktime
    time_left=base_cooktime
    while True:
        print(time_left)
        time_left=time_left-1
        sleep(1)
        if time_left==0:
            input('Finish cake?...')
            time_left=base_cooktime
            playerinventory['bread']=playerinventory.get('bread')-1
            playerinventory['cake']=playerinventory.get('cake')+breadcakemultiplier
            break
while True:
    print(f'You have {playermoney} gold')
    print(f'You currently have {playerinventory}')
    playerinput=input(f'What would you like to do? {optionlist}: ').lower()
    if playerinput=='shop':
        while True:
            shopinput=input('Would you like to purchase or sell? (press q to leave) ').lower()
            if shopinput=='q':
                break
            elif shopinput not in shopoptions:
                print('Please type either purchase or sell.')
                sleep(2)
                continue
            elif shopinput=='sell':
                while True:
                    print(f'The prices are {sellvalues}')
                    print(f'You have {playerinventory}')
                    sellinput=input('What would you like to sell? (q to go back) ').lower()
                    if sellinput=='q':
                        break
                    elif sellinput not in playerinventory:
                        print('Thats not an option.')
                    elif playerinventory.get(sellinput)==0:
                        print('You dont have that item.')
                    else:
                        earnings=playerinventory.get(sellinput)*sellvalues.get(sellinput)
                        playerinventory[sellinput]=0
                        print(f'You sold your {sellinput} for {earnings}')
                        playermoney=playermoney+earnings
            elif shopinput=='purchase':
                while True:
                    buyinput=input(f"What do you want to purchase? we have {shoplist} (press q to go back) ").lower()
                    if buyinput=='q':
                        break
                    elif buyinput not in shoplist:
                        print('Thats not an option')
                        sleep(2)
                    else:
                        while True:
                            quantityinput=int(input(f'How much {buyinput} would you like to purchase '))
                            buyamount=buyshopcosts.get(buyinput)*quantityinput
                            missingmoney=buyamount-playermoney
                            if buyamount>playermoney:
                                print(f"You don't have enough money. You're missing {missingmoney} gold")
                            elif buyamount<=playermoney:
                                lastbinput=input(f"You're buying {quantityinput} {buyinput} for {buyamount} Y/N ").lower()
                                if lastbinput=='n':
                                    sleep(2)
                                    break
                                elif lastbinput=='y':
                                    print(f'You bought {quantityinput} {buyinput} for {buyamount}')
                                    playermoney=playermoney-buyamount
                                    playerinventory[buyinput]=playerinventory[buyinput]+quantityinput
                                    sleep(2)
                                    break
    elif playerinput=='bakery':
        while True:
            print(f'You currently have {playerinventory}')
            bakeryinput=input('Welcome to the bakery what would you like to do? (Bake dough, or make cake) press q to go back: ').lower()
            if bakeryinput=='q':
                break
            elif bakeryinput not in bakeryoptions:
                print("Thats not an option.")
                sleep(2)
                continue
            elif bakeryinput=='bake dough':
                if playerinventory.get('dough')==0:
                    print('You dont have dough.')
                    sleep(2)
                    continue
                else:
                    bakedough()
            elif bakeryinput=='make cake':
                if playerinventory.get('bread')==0:
                    print('You need bread to make cake')
                    sleep(2)
                else:
                    cookcake()
    elif playerinput=='upgrade':
        while True:
            print(f'You currently have {playermoney} gold.')
            upgradeinput=input(f'Here are our upgrade options: {upgradelist} which one do you pick? press q to quit. ').lower()
            if upgradeinput=='q':
                break
            elif upgradeinput not in upgradelist:
                print('Thats not a valid option.')
                sleep(2)
            else:
                upgrades()