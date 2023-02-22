def get_input():
    input_string = input(">> ").lower()
    if input_string == "i want to exit from the chat":
        return "i want to exit from the chat"

    find_solution(input_string)


def find_solution(string):

    if string in data["question"]:
        print(">>", data["respond"][data["question"].index(string)])
    else:
        data["question"].append(string)

        answer = input("Sorry I don't know about that. Can you give a any suggestion for the answer: ")
        data["respond"].append(answer)
        # print(data)


if __name__ == "__main__":
    data_file = open("data.csv", 'r')
    data = {"question": [], "respond": []}

    while True:
        if get_input() == "i want to exit from the chat":
            print(">> Okay, see you again...")
            break
