import time

# Get the user input
def get_input():
    input_string = input(">> ").lower()
    if input_string == "i want to exit from the chat":
        return "i want to exit from the chat"

    find_solution(input_string)


# Find the better solution for the given question using dataset
def find_solution(string):
    for element in data["question"]:
        if string in element or element in string:
            print(">>", data["respond"][data["question"].index(element)])
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
    for i in range(len(data["question"])):
        data_file3.write(data["question"][i] + "\n")
        data_file4.write(data["respond"][i] + "\n")


# Load the current values
def load_data():
    data_file1 = open("questions.csv", 'r')
    data_file2 = open("responds.csv", 'r')
    for i in data_file1:
        data["question"].append(i.strip())

    for i in data_file2:
        data["respond"].append(i.strip())


if __name__ == "__main__":
    data = {"question": [], "respond": []}
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
