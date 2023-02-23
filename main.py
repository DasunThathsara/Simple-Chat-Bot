# Get the user input
def get_input():
    input_string = input(">> ").lower()
    if input_string == "i want to exit from the chat":
        return "i want to exit from the chat"

    find_solution(input_string)


# Find the better solution for the given question using dataset
def find_solution(string):
    if string in data["question"]:
        print(">>", data["respond"][data["question"].index(string)])
    else:
        data["question"].append(string)

        answer = input("Sorry I don't know about that. Can you give a any suggestion for the answer: ")
        data["respond"].append(answer)


# Store the current values
def store_data():
    data_file = open("data.csv", 'w')
    for i in range(len(data["question"])):
        data_file.write(data["question"][i] + ", " + data["respond"][i])
        data_file.write("\n")


if __name__ == "__main__":
    data = {"question": [], "respond": []}

    # for items in data_file:

    while True:
        text = get_input()
        store_data()
        if text == "i want to exit from the chat":
            print(">> Okay, see you again...")

            break
