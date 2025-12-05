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

Employee_First_Name=sys.argv[1]
Employee_Last_Name=sys.argv[2]
Employee_Date_Of_Birth=sys.argv[3]
Employee_Adress=sys.argv[4]
Employee_Place=sys.argv[5]
Employee_Postal_Code=sys.argv[6]
Employee_Start_Of_Employment=sys.argv[7]
Employee_Function=sys.argv[8]
Employee_Department=sys.argv[9]
Employee_Location=sys.argv[10]
Employee_Phone_Number=sys.argv[11]
# Querry uitvoeren

#COLUMS OF THE DB SAVING IN A LIST

db_kolommen=[
                     'voornaam',
                     'achternaam',
                     'geboortedatum',
                     'adres',
                     'woonplaats',
                     'postcode',
                     "start_loondienst",
                     "functie_id",
                     "afdeling_id",
                     "locatie_id",
                     "telefoonnummer"
                     ]
# POWERAUTOMATE DESKTOP VARIABLES SAVING IN DICTIONARY
db_data=[
           
            Employee_First_Name,
            Employee_Last_Name,
            Employee_Date_Of_Birth,
            Employee_Adress,
            Employee_Place,
            Employee_Postal_Code,
            Employee_Start_Of_Employment,
            Employee_Function,
            Employee_Department,
            Employee_Location,
            Employee_Phone_Number
        ]

# CONVERTING THE COLUM LIST TO A FORMAT THAT MYSQL ACCEPTS 
kolommen= ", ".join(db_kolommen)

# CONVERTING THE POWERAUTOMATE DATA TO %S PLACEHOLDERS (DYNAMICLY) TO PREVENT SQL INJECTION

Placholders=", ".join(["%s"] * len(db_data))  

Query=f"INSERT INTO `medewerkers` ({kolommen}) VALUES ({Placholders});"   

db_cursor.execute(Query,(db_data))

db_con.commit()

print(f"THE FOLLOWING EMPLOYEE: {Employee_First_Name,Employee_Last_Name} HAS BEING ADDED TO THE HR DB")
