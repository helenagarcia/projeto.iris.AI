from connection import list_all_users
from os import listdir

users_directories = listdir('C:\\Users\\helen\\Downloads\\Projeto.Iris\\Projeto.Iris\\Images')
users_database = list_all_users()

users_analyse = []

for UserId, Name in users_database:
    if str(UserId) in users_directories:
        users_analyse.append(Name)


#print(users_analyse)

#print(users_directories)

print(users_database)