
import sqlite3

def manyTB(name):
    rounds=[]
    f = open('csv/'+name+'.csv','r')
    line = f.readline() #attibute name
    line = f.readline()
    while line:
        line2 = line.split(',')
        
        #line2[0] = line2[0].replace('-','.')
        line2[-1] = line2[-1][:-1]
        rounds.append(line2)
        
        #print(line2)
        line = f.readline()
        
    f.close()
        
    return rounds

def createDB(rounds,assets,property_type,role,special_case,transportation):
    # Establish a connection to the SQLite3 database
    conn = sqlite3.connect('monopoly.db')

    # Create a new table named "weather_data"
    c = conn.cursor()
    """
    c.execute('''
    DROP TABLE rounds
    ''')
    """
    
    #rounds
    c.execute('''CREATE TABLE rounds
                (gameID_roundID varchar(10),
                playerID INTEGER,
                special_case varchar(15),
                transportation varchar(10),
                balance INTEGER,
                positionID INTEGER,
                PRIMARY KEY(gameID_roundID,playerID))''')
    # Insert data
    for i in range(len(rounds)):
        #print(rounds[i])
        c.execute("INSERT INTO rounds (gameID_roundID,playerID,special_case,transportation,balance,positionID) VALUES (?, ?, ?, ?, ?, ?)", (rounds[i][0],rounds[i][1],rounds[i][2],rounds[i][3],rounds[i][4],rounds[i][5]))
        #print(rounds[i])
    
    #assets
    c.execute('''CREATE TABLE assets
                (playerID INTEGER,
                positionID INTEGER
                )''')
    # Insert data
    for i in range(len(assets)):
        c.execute("INSERT INTO assets (playerID, positionID) VALUES (?, ?)", (assets[i][0],assets[i][1]))
        #print(assets[i])
    
    #property_type
    c.execute('''CREATE TABLE property_type
                (
                positionID INTEGER,
                property_type varchar(20),
                price INTEGER,
                PRIMARY KEY(positionID))''')
    # Insert data
    for i in range(len(property_type)):
        #print(property_type[i])
        c.execute("INSERT INTO property_type (positionID, property_type, price) VALUES (?, ?, ?)", (property_type[i][0],property_type[i][1],property_type[i][2]))
        #print(property_type[i])
    
    #role
    c.execute('''CREATE TABLE role
                (
                playerID INTEGER,
                player_name varchar(30),
                role varchar(30),
                PRIMARY KEY(playerID))''')
    # Insert data
    for i in range(len(role)):
        c.execute("INSERT INTO role (playerID,player_name,role) VALUES (?, ?, ?)", (role[i][0],role[i][1],role[i][2]))
        #print(role[i])
    
    #special_case
    c.execute('''CREATE TABLE special_case
                (case_type varchar(20),
                bonus_money INTEGER
                )''')
    # Insert data
    for i in range(len(special_case)):
        c.execute("INSERT INTO special_case (case_type,bonus_money) VALUES (?, ?)", (special_case[i][0],special_case[i][1]))
        #print(special_case[i])
    
    #transportation
    c.execute('''CREATE TABLE transportation
                (transportation varchar(10),
                num_of_dice INTEGER
                )''')
    # Insert data
    for i in range(len(transportation)):
        c.execute("INSERT INTO transportation (transportation, num_of_dice) VALUES (?, ?)", (transportation[i][0],transportation[i][1]))
        #print(transportation[i])
    
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

rounds = manyTB('rounds')
assets = manyTB('assets')
property_type = manyTB('property_type')
role = manyTB('role')
special_case = manyTB('special_case')
transportation = manyTB('transportation')

createDB(rounds,assets,property_type,role,special_case,transportation)