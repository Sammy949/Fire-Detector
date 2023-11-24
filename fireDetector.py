import random

# 1 == Moderate
# 2 == Hot
# 3 == Scorching
# 4 == above normal

def check_installed():
    detector = True
    return detector

def default_values():
    global temp
    temp = random.randint(18, 400)
    # temp = random.randint(18, 100)
    print(temp)

def check_moderate_temp():
    if temp in range(18, 27):
        humidity_percent = random.randint(45, 50)
        air_quality_index = random.randint(0, 51)

        print(f"Current temperature is {temp} deg C")
        print(f"Current humidty level is {humidity_percent}%")
        print(f"Current air quality index is {air_quality_index}")
        print("---------------------------------")
        print("It's alright\nStay Safe and cool")


def check_hot_temp():
    if temp in range(28, 37):
        humidity_percent = random.randint(40, 45)
        air_quality_index = random.randint(51, 101)

        print(f"Current temperature is {temp} deg C")
        print(f"Current humidty level is {humidity_percent}%")
        print(f"Current air quality index is {air_quality_index}")
        print("---------------------------------")
        print("It's hot alright!\nIce Cream sounds nice!!! Stay Chill")
def check_scorching_temp():
    if temp in range(38, 61):
        humidity_percent = random.randint(20, 40)
        air_quality_index = random.randint(100, 151)

        print(f"Current temperature is {temp} deg C")
        print(f"Current humidty level is {humidity_percent}%")
        print(f"Current air quality index is {air_quality_index}")
        print("---------------------------------")
        print("It's quite hot, nah It's very hottt.\nStay Safe and cool")
def check_above_norms_temp():
    if temp >= 61:
        humidity_percent = random.randint(0, 20)
        air_quality_index = random.randint(100, 151)

        print(f"Current temperature is {temp} deg C")
        print(f"Current humidty level is {humidity_percent}%")
        print(f"Current air quality index is {air_quality_index}")
        print("---------------------------------")
        print("There's a possible fire...\nJust Stay Safe")

def check_fire():
    if temp >= 300:
        print("There's a possible fire...")
        print("Alerting fire services and resposible caretakers")
        print("Stay alert and Safe")

def check_temp_state():
    default_values()
    check_moderate_temp()
    check_hot_temp()
    check_scorching_temp()
    check_above_norms_temp()
    check_fire()

def main():
    print("Thank You for installing SafeTempGuard\nKeeping you safe from burns")
    print("---------------------------------")
    detector = check_installed()
    if detector:
        print("Setting up detector...")
        print("Setting up detector..")
        print("Setting up detector.")
        print("Done...Ready to keep you safe")
        print("---------------------------------")
        check_temp_state()

    else:
        print("App not properly installed.\nReinstall and Restart app")
        print("...")
        print("..")
        print(".")
        print("You've reached the end of this program.\nIf you want to see it run properly, set the `detector` variable to True...\nThank You.")

main()
