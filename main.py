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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Look for a client in the database and open a browser with "
                    "google maps and show his position base on his address",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("-c", "--client", help="Name of the client")
    parser.add_argument("-p", "--password", help="Password for access of the database")
    parser.add_argument("-u", "--user", help="Username for access of the database")
    parser.add_argument("-dbn", "--dbname", help="Name of the database you try to access , default is test",
                        default="test")
    args = parser.parse_args()

    result = find_to_db(args.user, args.password, [args.client], args.dbname)

    webdriver.Chrome
    for x in result:
        print(x)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
