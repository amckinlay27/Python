# ---------------------------------------------------------------------------- #
#                              Second Sub Project                              #
# ---------------------------------------------------------------------------- #
#
#Author: Adam McKinlay
#Student Number: c0656685
#Program: CSQuery.py
#Description: Uses user input to query a specified database and return the queried results
#

# ---------------------------------------------------------------------------- #
#                                    Imports                                   #
# ---------------------------------------------------------------------------- #
import matplotlib.pyplot as plt
from sqlite3 import Error
import argparse
import sqlite3
import sys
import os

# ---------------------------------------------------------------------------- #
#                                   Main                                       #
# ---------------------------------------------------------------------------- #
def main():
    """ process and execute database statements """
    #Argument Parser
    parser = argparse.ArgumentParser(description="Returns results of a query on a specified database", epilog="Thanks for choosing CSQuery")
    parser.add_argument('-d', '--database', type=str, metavar='database', help="the database to connect to", required=True)
    parser.add_argument('-s', '--statement', type=str, metavar='statement', nargs=argparse.REMAINDER, help="specifies the sql query to execute", required=True)
    parser.add_argument('-q', action="store_true", help="plot frequency of query results", required=False)
    args = parser.parse_args()
    
    #Database Path
    database_path = "C:/Users/McKinlad/OneDrive - Lambton College/Term 4/CSD 3444 Emerging Technologies/Assign/Final/" + args.database
    if(not os.path.isfile(database_path)):
        print('Error: The database does not exist')
        exit()

    #Connect and Query
    if(args.q):
        connection = create_connection(database_path)
        query_s = args.statement[0]
        #print(database_path)
        #print(query_s)
        execute_query(connection, query_s, True)
        connection.close()
    else:
        connection = create_connection(database_path)
        query_s = args.statement[0]
        #print(database_path)
        #print(query_s)
        execute_query(connection, query_s, False)
        connection.close()
#main

# ---------------------------------------------------------------------------- #
#                                   Functions                                  #
# ---------------------------------------------------------------------------- #

# ----------------------------- create_connection ---------------------------- #
def create_connection(db_file):
    """ create a database connection to the SQLite database
        
        Keyword Arguments
        param -> db_file: database file path
        return: connection object
    """
    #Connection
    con = None

    #Attempt Connection
    try:
        con = sqlite3.connect(db_file)
        #print("Connection: Successful")
    except Error as e:
        print("Connection: Failed")
        exit()
 
    return con
#create_connection

# ------------------------------- execute_query ------------------------------ #
def execute_query(con, statement, q):
    """ executes a query on a given database connection and displays results
        
        Keyword Arguments
        param ->      conn: Connection object
        param -> statement: The statement to execute
        param ->         q: Determines to plot
    """
    nums = []

    #Connection
    cur = con.cursor()
    try:
        cur.execute(statement)
    except Error as e:
        print("Error: Query invalid")
        con.close()
        exit()
 
    #Rows
    rows = cur.fetchall()
    if (len(rows) == 0):
        print("Alert: query produced no results")
        con.close()
        exit()

    #Output
    print('-'*47)

    try:
        for row in rows:
            for e in row:
                print(f'{e:15}', end='')
                
                #Append values to list -> needed for final project
                if(row[len(rows[0])-1] == e):
                    nums.append(e)
            print()
    except TypeError as e:
        print("\nError: Query contains empty data")
        con.close()
        exit()

    print('-'*47)

    #If q is present, call plot
    if(q==True):
        plot(nums)
#execute_query

# ----------------------------------- Plot ----------------------------------- #
def plot(nums):
    """ generates and displays frequency histogram
        
        Keyword Arguments
        param -> nums: list of numbers
    """

    #List
    freq = []
    num_pos = []
    
    #Setup List
    pos = 0
    nums.sort()
    num_pos.append(nums[1])
    freq.append(1)
    #print(nums)

    #Frequency Count
    for num in range(1, len(nums)):
        if(num_pos[pos] == nums[num]):
            freq[pos] += 1
        else:
            num_pos.append(nums[num])
            pos += 1
            freq.append(1)
    #print(num_pos)
    #print(freq)

    #Plot Graph
    plt.bar(num_pos,freq, color='#0504aa')
    plt.xticks(num_pos, num_pos)
    plt.suptitle('Frequency of Invoices', color='#0504aa')
    plt.xlabel('Invoice Total($)', color='#0504aa')
    plt.ylabel('Frequency', color='#0504aa')
    plt.show()
#Plot

main()
# ---------------------------------------------------------------------------- #
#                                      EOF                                     #
# ---------------------------------------------------------------------------- #