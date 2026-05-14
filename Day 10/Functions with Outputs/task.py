def format_name(f_name: str, l_name: str):
    return f"{f_name.title()} {l_name.title()}"

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

print(format_name(first_name, last_name))