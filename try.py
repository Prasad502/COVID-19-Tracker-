from pymongo import MongoClient # import mongo client to connect  
import pprint  

# Creating instance of mongoclient  
client = MongoClient()  
roll = 221087
prof = "Computer Engineer"
name = "Prasad"
# Creating database  
db = client.javatpoint  
employee = {"id": roll,  
            "name": name,  
            "profession": prof,}  
# Creating document  
employees = db.employees  
# Inserting data  
employees.insert_one(employee)  
# Fetching data  
pprint.pprint(employees.find()) 