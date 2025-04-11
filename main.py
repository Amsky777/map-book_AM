users:list = [
    {"name":"Adrian","location":"Toruń","posts":400},
    {"name":"Krzysztof","location":"Baiłobrzegi","posts":500},
    {"name":"Adrian","location":"Świecie","posts":300},
    {"name":"Zuzia","location":"Radzyń_Podlaski","posts":700},
]



def get_user_info(users_data:list)->None:

    for user in users_data:
        print(f"Twój znajomy {user['name']}! z miejscowości{user["location"]} opublikował {user['posts']} postów")


get_user_info(users)