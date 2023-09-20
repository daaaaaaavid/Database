import random
import sqlite3
from flask import Flask, render_template, Response, request, redirect, url_for

from operator import itemgetter
import re
game_num=4
round_num=30
player_num=4
def balance(playerID):
    # input is playerID, output is balance list for this playerID

    # Connect to the database
    conn = sqlite3.connect('monopoly.db')
    c = conn.cursor()

    # Retrieve the balance data from the corresponding table
    c.execute(f"SELECT balance FROM rounds where playerID={playerID}")
    Balance = c.fetchall()

    # Close the database connection
    conn.close()

    # Prepare the data for the balance
    balance = []

    for data in Balance:
        data = list(data)

        balance.append(data[0])

    # print(type(balance))
    # print(balance)                 #look return data

    return balance


def sum_assets_for_each_rounds(playerID):
    # input is playerID, output is sum list for this playerID when getting new asset
    # Connect to the database

    conn = sqlite3.connect('monopoly.db')
    c = conn.cursor()

    # Retrieve the positionID data from the corresponding table
    c.execute(f"SELECT positionID FROM assets where playerID={playerID}")
    Assets = c.fetchall()

    # Retrieve the positionID, price data from the corresponding table
    c.execute(f"SELECT positionID, price FROM property_type ")
    rows = c.fetchall()

    # Close the database connection
    conn.close()

    # Prepare the data for the sum
    sum = []
    property_type = {}
    for row in rows:
        # key:positionID, value:price
        property_type[row[0]] = row[1]
    assets_sum_this_round = 0

    for data in Assets:
        assets_sum_this_round += property_type[data[0]]

        sum.append(assets_sum_this_round)

    l=split_number(round_num,len(Assets))

    temp=[]
    for i in range(len(l)):
        for j in range(l[i][0],l[i][1]):
            temp.append(sum[i])

    return temp


def split_number(number, num_chunks):

    avg_size = number // num_chunks

    sizes = [avg_size] * num_chunks
    total_size = avg_size * num_chunks
    while total_size < number:
        idx = random.randint(0, num_chunks - 1)
        sizes[idx] += 1
        total_size += 1

    chunks = []
    start = 0
    for size in sizes:
        end = start + size
        chunks.append((start, end))
        start = end

    for i in chunks:
        if i[1]==0:
            chunks.append(chunks[len(chunks)-1])
            chunks.remove(i)
    return chunks

def amount_of_each_type_property(playerID):
    # input is playerID, output is the amount of each property type

    # Connect to the database
    conn = sqlite3.connect('monopoly.db')
    c = conn.cursor()

    # Retrieve the balance data from the corresponding table
    c.execute(f"SELECT positionID FROM assets where playerID={playerID}")
    pos = c.fetchall()  # list

    # Mini's House to Mall, Medium-sized House to Mall, Big House to Mall
    type_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(len(pos)):
        positionID = pos[i][0]
        c = conn.cursor()
        c.execute(f"SELECT property_type FROM property_type where positionID={positionID}")
        typ = c.fetchall()
        word_split = typ[0][0].split(" ")

        if word_split[1] == "House":
            list_idx = 0
        if word_split[1] == "Hotel":
            list_idx = 3
        if word_split[1] == "Mall":
            list_idx = 6

        if word_split[0] == "Mini":
            list_idx += 0
        elif word_split[0] == "Medium-sized":
            list_idx += 1
        elif word_split[0] == "Big":
            list_idx += 2


        type_list[list_idx] += 1
        # Close the database connection
    conn.close()

    return type_list

def role_used_number():

    conn = sqlite3.connect('monopoly.db')
    c = conn.cursor()
    c.execute(f"SELECT role FROM role")

    roles = c.fetchall()
    type_list = [0, 0, 0, 0,0]

    for r in range(len(roles)):
        if roles[r][0]=='A Tubo':
            type_list[0] += 1
        elif roles[r][0]=='Madam Qian':
            type_list[1] +=1
        elif roles[r][0]=='Sun Xiaomei':
            type_list[2] +=1
        elif roles[r][0]=='John Joe':
            type_list[3] +=1
        elif roles[r][0]=='Little Danny':
            type_list[4] +=1

    conn.close()

    return type_list

def special_cases_number(playerID):

    conn = sqlite3.connect('monopoly.db')
    c = conn.cursor()
    c.execute(f"SELECT special_case FROM rounds where playerID={playerID}")

    cases = c.fetchall()
    type_list = [0, 0, 0, 0,0]

    for c in cases:
        if c[0]=='Turtle':
            type_list[0] += 1
        elif c[0]=='Dog':
            type_list[1] +=1
        elif c[0] == 'None':
            type_list[2] += 1
        elif c[0] == 'God of luck':
            type_list[3] += 1
        elif c[0] == 'God of wealth':
            type_list[4] += 1

    conn.close()

    return type_list
def get_history_data():

    data=[ [] for i in range(game_num)]
    conn = sqlite3.connect('monopoly.db')
    c = conn.cursor()
    c.execute(f"SELECT gameID_roundID,playerID,balance FROM rounds")
    rows=c.fetchall()

    for row in rows:

        l = re.split(' |-',row[0])
        # print(l[2],str(round_num))
        if l[2] == str(round_num):
            last_round_assets = sum_assets_for_each_rounds(row[1])[len(sum_assets_for_each_rounds(row[1]))-1]

            data[int(l[1])-1].extend([[int(row[1]),int(row[2]),last_round_assets,last_round_assets+int(row[2])]])

    temp=[]
    for d in data:
        temp.append(sorted(d, key=itemgetter(3),reverse=True))

    for d in temp:
        for j in d:
            del j[-1]


    return temp

def get_all_data():
    query=['money','asset','situation','type_num']
    data=[]
    temp=[]
    for i in range(game_num):
        for j in range(player_num):
            id=i*4+j+1
            temp.append(balance(id))
    data.append(temp)

    temp=[]
    for i in range(game_num):
        for j in range(player_num):
            id=i*4+j+1
            temp.append(sum_assets_for_each_rounds(id))
    data.append(temp)

    temp = []
    for i in range(game_num):
        for j in range(player_num):
            id = i * 4 + j + 1
            temp.append(special_cases_number(id))
    data.append(temp)

    temp = []
    for i in range(game_num):
        for j in range(player_num):
            id = i * 4 + j + 1
            temp.append(amount_of_each_type_property(id))
    data.append(temp)

    # for i in range(len(data)):
    #     print(len(data[i]),len(data[i][0]))
    # print(data)
    return data
def balance_history_best():
    return
def get_lucky_guys():
    temp=[]
    for i in range(game_num):
        for j in range(player_num):
            id = i * 4 + j + 1
            cases=special_cases_number(id)
            good=cases[3]*1+cases[4]*3
            temp.append([id,good])
    temp=sorted(temp, key=lambda l: l[1], reverse=True)

    return temp

app = Flask(__name__,static_folder='static',static_url_path='/')
app.config["DEBUG"] = True


@app.route('/')
def index():
    data=get_history_data()
    return render_template("index.html",data=data)

@app.route('/query', methods=['GET', 'POST'])
def query():
    all = get_all_data()
    return render_template('query.html',all=all)

@app.route('/statistic', methods=['GET', 'POST'])
def statistic():
    roles = role_used_number()
    balance = balance_history_best()
    lucky=get_lucky_guys()
    return render_template('statistic.html',data=roles,balance=balance,lucky=lucky)

def main():
    app.run()

if __name__=='__main__':
    main()
