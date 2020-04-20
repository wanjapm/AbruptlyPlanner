def add_gamer(gamer,gamers_list):
    if gamer.get("name") and gamer.get("availability"):
        gamers_list.append(gamer)

def build_daily_frequency_table():
    return {"Monday":0, "Tuesday":0 ,"Wednesday":0, "Thursday":0, 
    "Friday":0,"Saturday":0,"Sunday":0}

def calculate_availability(gamers_list,available_frequency):
    for gamer in gamers_list:
        for day in gamer["availability"]:
            available_frequency[day] +=1
    return available_frequency

def find_best_night(availability_table):
    max_num = 0
    best_night = ""
    for day,num in availability_table.items():
        if num > max_num:
            best_night = day
            max_num = num
    return best_night

def gamer_available_on_night(available_days,day):
    if available_days.count(day) > 0 :
        return True
    return False

def available_on_night(gamers_list,day):
    available_list = []
   # print(gamers_list)
    for gamer in gamers_list:
        if gamer_available_on_night(gamer["availability"],day):
                available_list.append(gamer["name"])
    return available_list

def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(form_email.format(name=gamer,game=game,day_of_week=day))

gamers = []
unable_to_attend_best_night = []
# Each gamer should be a dictionary with key being the name and value being a list of available days
# eg gamer = {"name":"Vicky Very","availability":["Monday", "Thursday", "Sunday"]}

add_gamer({'name':'Kimberly Warner','availability': ["Monday", "Tuesday", "Friday"]}, gamers)
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

count_availability = build_daily_frequency_table()

count_availability = calculate_availability(gamers,count_availability)
#print(count_availability)

game_night = find_best_night(count_availability)
#print ("Best game night is: "+game_night)

attending_game_night = available_on_night(gamers,game_night)
#print("Gamers available on {} are:{}".format(game_night,attending_game_night))

form_email = """Dear {name},\n
We wish to inform you that the {game} game will be played every {day_of_week}.
Thank you for noting this. We look forward to seeing you!
"""
#send_email(attending_game_night,game_night,"Abruptly Goblins!")

unable_to_attend_best_night = [gamer for gamer in gamers if attending_game_night.count(gamer["name"])==0]



second_night_availability = build_daily_frequency_table()

second_night_availability = calculate_availability(unable_to_attend_best_night,second_night_availability)
second_night = find_best_night(second_night_availability)


available_second_game_night = available_on_night(gamers,second_night)
send_email(available_second_game_night,second_night,"Abruptly Goblins!")