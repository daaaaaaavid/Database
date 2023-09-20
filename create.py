import random
import names
import csv
game=5
round=31
player_number=4
initial_money=200000
map_size=50
rounds=[]
role=[]
special_case={'Turtle':-1000,'Dog':-3000,'God of luck':1000,'God of wealth':3000,'None':0}
all_role=['A Tubo','Madam Qian','Sun Xiaomei','John Joe','Little Danny']
assets=[]
property_type=[]
transportation={1:'Walk',2:'Scooter',3:'Car'}
building_type=['House','Hotel','Mall']
building_size=['Mini','Medium-sized','Big']
def main():
    for i in range(1,game):
        players = []
        balance = []
        position = []
        own_asset = []
        roles=random.sample(all_role,player_number)

        for j in range(map_size):
            own_asset.append(-1)

        for j in range(player_number*(i-1)+1,player_number*i+1):
            players.append(j)
            balance.append(initial_money)
            position.append(0)
            name=names.get_full_name()
            role.append([j,name,roles[int((j-1)%player_number)]])

        for j in range(1,round):
            for k in range(player_number):
                temp = []
                trans=random.randint(1,3)
                dice=random.randint(1,trans*6)
                position[k] = (position[k]+dice)%map_size    # 0 ~ map_size-1
                case=get_case(random.randint(1,10))
                balance[k] += special_case[case]
                if own_asset[position[k]] == -1:
                    balance[k] -= property_type[position[k]][2]
                    own_asset[position[k]] = k
                    assets.append([players[k],position[k]+1])
                elif own_asset[position[k]]!=k:
                    balance[own_asset[position[k]]] += property_type[position[k]][2]
                    balance[k] -= property_type[position[k]][2]

                temp.append([' '+str(i)+'-'+str(j),players[k],case,transportation[trans],balance[k],position[k]+1])
                # print(temp)
                rounds.extend(temp)

    with open('rounds.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['gameIDroundID','playerID','special_case','transportation','balance','positionID'])
        for r in rounds:
            writer.writerow(r)

    with open('role.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['playerID','player_name','role'])
        for r in role:
            writer.writerow(r)

    with open('special_case.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['case_type','bonus_money'])
        for key,value in special_case.items():
            writer.writerow([key,value])

    with open('assets.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['playerID','positionID'])
        for a in assets:
            writer.writerow(a)

    with open('property_type.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['positionID','property_type','price'])
        for p in property_type:
            key=p[1]-1
            typ=building_type[int(key/3)]
            size=building_size[key%3]
            writer.writerow([p[0],size+' '+typ,p[2]])

    with open('transportation.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['transportation','num_of_dice'])
        for key,value in transportation.items():
            writer.writerow([value,key])
def get_case(num):
    if num==1:
        return 'Turtle'
    if num==2:
        return 'Dog'
    if num==3:
        return 'God of luck'
    if num==4:
        return 'God of wealth'
    return 'None'


def create_property():
    for i in range(map_size):
        key=random.randint(1,9)
        property_type.append([i+1,key,key*1000])


if __name__=='__main__':
    create_property()
    main()