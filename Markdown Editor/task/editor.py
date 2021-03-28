# write your code here text = ["# John Lennon", 'or ***John Winston Ono Lennon*** was one of *The Beatles*.',
# 'Here are the songs he wrote I like the most:', '* Imagine', '* Norwegian Wood', '* Come Together', '* In My Life',
# '* ~~Hey Jude~~ (that was *McCartney*)'] text = '\n'.join(text) print(text)
string_compile = []


def help(list_local):
    str1 = " "
    print(f"Available formatters: {str1.join(list_local)}")
    print("Special commands: !help !done")


def error():
    print("Unknown formatting type or command")


def done():
    my_file = open("output.md", "w")
    str3 = ""
    my_file.write(str3.join(string_compile))
    my_file.close()
    exit()


def valid_selection(selection):
    if selection == "plain":
        save_text(plain())
    elif selection == "bold":
        save_text(bold())
    elif selection == "italic":
        save_text(italic())
    elif selection == "link":
        save_text(link())
    elif selection == "inline-code":
        save_text(inline_code())
    elif selection == "header":
        save_text(header())
    elif selection == "line-break":
        save_text(line_break())
    elif selection == "ordered-list":
        save_text(list("1."))
    elif selection == "unordered-list":
        save_text(list("*"))
    elif selection == "new-line":
        save_text(new_line())
    else:
        print("Something went wrong")
        main_code()


def plain():
    user_text = input("Text: ")
    return user_text


def bold():
    user_text = input("Text: ")
    return "**" + user_text + "**"


def italic():
    user_text = input("Text: ")
    return "*" + user_text + "*"


def inline_code():
    user_text = input("Text: ")
    return "`" + user_text + "`"


def new_line():
    nl = '\n'
    return nl


def link():
    label = input("Label: ")
    url = input("URL: ")
    return "[" + label + "](" + url + ")"


def header():
    level = int(input("Level: "))
    if 1 <= level <= 6:
        user_text = input("Text: ")
        return "#" * level + " " + user_text + "\n"
    else:
        print("The level should be within the range of 1 to 6")
        return valid_selection("header")


def list(n):
    # n = "1." (ordered), n = "*" (unordered)
    rows = int(input("Number of rows: "))
    text_local = ""
    if rows > 0:
        for i in range(rows):
            start = "*" if n == "*" else str(i + 1) + "."
            user_text = input(f"Row #{i + 1}")
            text_local += start + " " + user_text + "\n"
        return text_local
    else:
        print("The number of rows should be greater than zero")
        return list(n)


def line_break():
    return "\n"


def save_text(text):
    global string_compile
    string_compile.append(text)
    str2 = ""
    print(str2.join(string_compile))


def main_code():
    valid_options = ["plain", "bold", "italic", "link", "inline-code", "header", "ordered-list", "unordered-list",
                     "line-break", "new-line"]
    usr_select = input("- Choose a formatter:")
    if usr_select == "!help":
        help(valid_options)
    elif usr_select == "!done":
        done()
    elif usr_select in valid_options:
        valid_selection(usr_select)
    else:
        error()


while True:
    main_code()

# formatter = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'ordered-list', 'unordered-list', 'new-line',
#              '!help', '!done']
# user_inputs = []
# nl = '\n'
#
#
# def markdown(user_inputs):
#     print(f"{nl.join(user_inputs)}{nl}")
#
#
# def help():
#     syntax = 'plain bold italic header link inline-code ordered-list unordered-list new-line\nSpecial commands: !help ' \
#              '!done '
#     print(syntax)
#
#
# def plain(text):
#     user_inputs.append(text)
#     print(f"{nl.join(user_inputs)}")
#
#
# def inline_code(text):
#     user_inputs.append(f'`{text}`')
#     print(f"{''.join(user_inputs)}")
#
#
# def bold(text):
#     user_inputs.append(f'**{text}**')
#     print(f"{''.join(user_inputs)}")
#
#
# def link(label, url):
#     user_inputs.append(f'[{label}]({url})')
#     print(f"{''.join(user_inputs)}")
#
#
# def new_line():
#     user_inputs.append('\n')
#     print(f"{''.join(user_inputs)}")
#
#
# def italic(text):
#     user_inputs.append(f'*{text}*')
#     print(f"{''.join(user_inputs)}")
#
#
# def header(level, text):
#     if level == 1:
#         user_inputs.append(f'# {text}')
#         markdown(user_inputs)
#     elif level == 2:
#         user_inputs.append(f'## {text}')
#         markdown(user_inputs)
#     elif level == 3:
#         user_inputs.append(f'### {text}')
#         markdown(user_inputs)
#     elif level == 4:
#         user_inputs.append(f'#### {text}')
#         markdown(user_inputs)
#     elif level == 5:
#         user_inputs.append(f'##### {text}')
#         markdown(user_inputs)
#     elif level == 6:
#         user_inputs.append(f'###### {text}')
#         markdown(user_inputs)
#     else:
#         print('The level should be within the range of 1 to 6')
#
#
# def lsts(rows, list_choice):
#     if list_choice == 'ordered-list':
#         for i in range(int(rows)):
#             text = input(f'- Row #{i + 1}: ')
#             user_inputs.append(f'{i + 1}. {text}')
#         markdown(user_inputs)
#     elif list_choice == 'unordered-list':
#         for i in range(int(rows)):
#             text = input(f'- Row #{i + 1}: ')
#             user_inputs.append(f'* {text}')
#         markdown(user_inputs)
#     return f'{nl}'
#
#
# def done():
#     with open('output.md', 'w') as file:
#         file.write(f"{nl.join(user_inputs)}{nl}")
#         file.close()
#     exit()
#
#
# while True:
#     choice = input('- Choose a formatter: ')
#     if choice not in formatter:
#         print('Unknown formatting type or command. Please try again.')
#     elif choice == '!done':
#         done()
#     elif choice == '!help':
#         help()
#     elif choice == 'header':
#         level = int(input('- Level: '))
#         user_input = input('- Text: ')
#         header(level, user_input)
#     elif choice == 'plain':
#         user_input = input('- Text: ')
#         plain(user_input)
#     elif choice == 'link':
#         label = input('- Label: ')
#         url = input('- URL: ')
#         link(label, url)
#     elif choice == 'bold':
#         user_input = input('- Text: ')
#         bold(user_input)
#     elif choice == 'italic':
#         user_input = input('- Text: ')
#         italic(user_input)
#     elif choice == 'inline-code':
#         user_input = input('- Text: ')
#         inline_code(user_input)
#     elif choice == 'new-line':
#         new_line()
#     elif choice == 'ordered-list' or choice == 'unordered-list':
#         while True:
#             rows = int(input('Number of rows: '))
#             if rows > 0:
#                 lsts(rows, choice)
#                 break
#             else:
#                 print('The number of rows should be greater than zero')
#     else:
#         user_input = input('- Text: ')
#         formatter[choice](user_input)
