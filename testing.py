while True:
    user_input = input("Choice 'Add' or 'Show' or 'Edit' or or 'Remove' or 'Exit':- ")
    user_input = user_input.strip()

    # to avoid extar space in input
    match user_input:
        case 'add':
            word = input("Enter Your Word :") + "\n"
            with open('nefile.txt', 'r') as file:
                words = file.readlines()

            words.append(word)
            # to add something

            with open('nefile.txt', 'w') as file:
                words = file.writelines(words)

        case 'show':
            with open('nefile.txt', 'r') as file:
                words = file.readlines()

            # numerate means to show indexing like 1,2,3,4 or etc
            for index, j in enumerate(words):
                x = f"{index + 1}.{j.strip()}"
                print(x)
        case 'edit':
            with open('nefile.txt', 'r') as file:
                words = file.readlines()

            p = int(input("Enter the number :"))
            p = p - 1
            q = input("Enter the text : ") + "\n"
            words[p] = q
            with open('nefile.txt', 'w') as file:
                file.writelines(words)
        case 'comp':
            with open('nefile.txt', 'r') as file:
                words = file.readlines()
            complete = int(input("Enter Deleted Task :"))
            # pop means to delete or remove something from the list
            remove_count = complete-1
            remove_words = words[remove_count].strip("\n")
            words.pop(remove_count)
            with open('nefile.txt', 'w') as file:
                file.writelines(words)
            show_msg = f"This{remove_words} was removed  !!"
            print(show_msg)
        case 'exit':
            break
print("Say Allah-Akbar")
