import csv
import json

# Accessing The Passwords CSV & Adding Compromised Users To The List
compromised_users = []

with open("passwords.csv") as password_file:
  password_csv = csv.DictReader(password_file)
  for row in password_csv:
    compromised_users.append(row["Username"])
    
# Writing Compromised Users To The TXT File
with open("compromised_user.txt", "w") as compromised_user_file:
  for user in compromised_users:
    compromised_user_file.write(user)

# Using JSON To Send A Message To Notify The Boss
with open("boss_message.json", "w") as boss_message:
  boss_message_dict = {"recipient":"The Boss", "message":"Mission Success"}
  json.dump(boss_message_dict, boss_message)

# Scrambling The Passwords CSV & Adding Attackers Signature
with open("new_passwords.csv", "w") as new_passwords_obj:
  slash_null_sig = """
   _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""
  new_passwords_obj.write(slash_null_sig)
