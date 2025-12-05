from dotenv import load_dotenv
import os
import mysql.connector
import sys

#env bestand laden 

load_dotenv()

try:

    #db gegevens defineren a.d.h.v een .env bestand
    db_con=mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")

    )

    db_cursor=db_con.cursor()

except:

     print("Kan geen verbinding maken met de database\n"
    "Controleer je credentials en zorg ervoor dat de software verbinding maakt met de juiste database." )
     
# PowerAutomate Desktop variabalen ophalen en opslaan 

Employee_ID=sys.argv[1]
Employee_Name=sys.argv[2]
# Querry uitvoeren

Query="DELETE FROM medewerkers WHERE medewerker_id= %s;"   

db_cursor.execute(Query,(Employee_ID,))

db_con.commit()

print(f"THE FOLLOWING EMPLOYEE: {Employee_Name} HAS BEING DELETED FROM THE DB")










