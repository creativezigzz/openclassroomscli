import mysql.connector as mc
from mysql.connector import errorcode
import argparse
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# Process to do -> 1. Se connecter a la base de donnée client
#              -> Selectionner le client spécifier dans le parametre du script
#                   ->Si pas de client alors renvoie "Le client n'existe pas dans la bdd"
#                   ->Sinon si plusieurs client demandé lequel exactement.
#                   -Ouvrir une page web de google maps
#                   ->Accepter les cookiess
#                   -> Et ecrire l'adresse du client en question
#                   Done

# def get_cookie():
#     driver = webdriver.Chrome()
#     driver.get("https://books.google.com/")
#     time.sleep(1)
#     pickle.dump(driver.get_cookies(), open("pickle.pkl", "wb"))
#     driver.close()

# def get_googlemaps()
def find_to_db(db_user, db_password, client_name, db_name="test"):
    try:
        cnx = mc.connect(user=db_user,
                         password=db_password,
                         host='127.0.0.1',
                         database=db_name)
        cursor = cnx.cursor()

        fields = "NCLI, NOM, ADRESSE, LOCALITE"
        table = "client"
        conditions = "NOM = %s"
        query = (f"SELECT {fields} "
                 f"FROM {table} "
                 f"WHERE {conditions};")

        cursor.execute(query, client_name)

        myresult = cursor.fetchall()
        cnx.close()
        return myresult
    except mc.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password please "
                  "look for the right credentials")
            exit(2)
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
            exit(2)
        else:
            print(err)
            exit(2)


def many_client(many):
    if len(many) > 1:
        print("There is more than one client with that name \n, please provide your unique client number\n")
        client = ()
        ok = 0
        while ok < 1:
            ncli = input("What is your client number ?\n")
            for x in result:
                if ncli.upper() in x[0].upper():
                    client = x
                    ok = 1
            if not ok:
                print("There is no such client number for the name you provide\n")
                again = 'a'
                while again != 'y' or 'n':
                    again = input("Would you like to retype ? press y for yes or n for no\n")
                    if again == 'n':
                        print("Please search for another name and come back")
                        exit(1)

    else:
        client = result[0]

    return client


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Look for a client in the database and open a browser with "
                    "google maps and show his position base on his address",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    requiredNamed = parser.add_argument_group('required named arguments')
    parser.add_argument("-c", "--client", help="Name of the client")
    requiredNamed.add_argument("-p", "--password", help="Password for access of the database", required=True)
    requiredNamed.add_argument("-u", "--user", help="Username for access of the database", required=True)
    parser.add_argument("-dbn", "--dbname", help="Name of the database you try to access , default is test",
                        default="test")
    args = parser.parse_args(['-h'])

    result = find_to_db(args.user, args.password, [args.client], args.dbname)
    # for x in result:
    #    print(x)
    # Case of many clients with the same name, ask for the client number.
    client_unique = many_client(result)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
