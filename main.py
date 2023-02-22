data_file = open("data.txt", 'r')

data = {"question": ["hey"], "respond": ["hey!"]}
while True:
    input_string = input()
    if input_string.lower() in data["question"]:
        print(data["respond"][data["question"].index(input_string.lower())])
    else:
        data["question"].append(input_string.lower())

        answer = input("Sorry I don't know about that. Can you give a any suggestion for the answer: ")
        data["respond"].append(answer)
        # print(data)
