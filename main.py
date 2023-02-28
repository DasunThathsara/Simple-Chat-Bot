import time
import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim


# # function for get current geolocation
# def get_location():
#     geoLoc = Nominatim(user_agent="GetLoc")
#     locname = geoLoc.reverse("39.2138905, -79.6371124")
#     print(locname.address)
#
# def f ():
#     geolocator = Nominatim(user_agent="geoapiExercises")
#     location = geolocator.geocode("my location")
#     print(location.latitude, location.longitude)
#     get_location()
# f()


# find the weather of the given city
def weather(city):
    url = "https://www.google.com/search?q=" + "weather" + city
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    str1 = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    data = str1.split('\n')
    time1 = data[0]
    sky = data[1]
    str_d = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})[5].text
    pos = str_d.find('Wind')
    other_data = str_d[pos:]

    # printing all the data
    print(">> City           :", temp)
    print(">> Temperature    :", temp)
    print(">> Time           :", time1)
    print(">> Sky Description: ", sky)


# Get the user input
def get_input():
    input_string = input(">> ").lower()
    if input_string == "i want to exit from the chat":
        return "i want to exit from the chat"

    find_solution(input_string)


# Find the better solution for the given question using dataset
def find_solution(string):

    # Telling the time
    if "time now" in string:
        print(">> Time is", time.strftime("%H:%M:%S", time.localtime()))
        return

    # Telling the date
    if "date today" in string or "the date" in string:
        print(">> Date is", time.strftime("%d/%m/%Y", time.localtime()))
        return

    # Telling the whether
    if "whether of" in string or "whether in" in string or "whether" in string:
        weather(string.split()[-1])
        return

    for element in data["question"]:
        if string in element or element in string:
            print(">>", data["respond"][data["question"].index(element)])
            return

    try:
        # Name of the user
        if "my name is" in string:
            data["personal_details"][0] = string.split()[-1]
            print(">> Hello", data["personal_details"][0] + "!")
            return
        elif "what is my name" in string:
            print(">> Your name is", data["personal_details"][0])
            return

        # Age of the user
        if "my age is" in string:
            data["personal_details"][1] = string.split()[-1]
            print(">> Your age is", data["personal_details"][1])
            return
        if "what is my age" in string:
            print(">> Your age is", data["personal_details"][1])
            return

        # Location of the user
        if "my location is" in string or "I am from" in string or "live in" in string:
            data["personal_details"][2] = string.split()[-1]
            print(">> Your location is", data["personal_details"][2])
            return
        if "what is my location" in string or "where do I live" in string:
            print(">> Your location is", data["personal_details"][2])
            return

    except IndexError:
        print(">> Sorry.. I don't know it :/")
        return

    if string in data["question"]:
        print(">>", data["respond"][data["question"].index(string)])
    else:
        data["question"].append(string)

        answer = input("Sorry I don't know about that. Can you give a any suggestion for the answer: ")
        data["respond"].append(answer)


# Store the current values
def store_data():
    data_file3 = open("questions.csv", 'w')
    data_file4 = open("responds.csv", 'w')
    data_file5 = open("personal.csv", 'w')
    for i in range(len(data["question"])):
        data_file3.write(data["question"][i] + "\n")
        data_file4.write(data["respond"][i] + "\n")

    for i in range(len(data["personal_details"])):
        data_file5.write(data["personal_details"][i] + "\n")


# Load the current values
def load_data():
    data_file1 = open("questions.csv", 'r')
    data_file2 = open("responds.csv", 'r')
    data_file6 = open("personal.csv", 'r')
    for i in data_file1:
        data["question"].append(i.strip())

    for i in data_file2:
        data["respond"].append(i.strip())

    count = 0
    for i in data_file6:
        data["personal_details"][count] = i.strip()


if __name__ == "__main__":
    data = {"question": [], "respond": [], "personal_details": ["", "", ""]}
    try:
        load_data()
    except IndexError:
        pass

    if int(time.strftime("%H", time.localtime())) < 12:
        print(">> Good Morning! How can I help you?")
    elif int(time.strftime("%H", time.localtime())) < 16:
        print(">> Good Afternoon! How can I help you?")
    elif int(time.strftime("%H", time.localtime())) < 20:
        print(">> Good Evening! How can I help you?")
    else:
        print(">> Good Night! How can I help you?")

    while True:
        text = get_input()
        store_data()
        if text == "i want to exit from the chat":
            print(">> Okay, see you again...")
            break
