# I am not going to write the whole main.py
# This generator script will do that for me

main_ = """
a = int(input('Enter first number : '))
b = input('Enter the operator (+, -, *, /) :')
c = int(input('Enter the second number : '))

#Here's how it works:
"""

main_ += """\nif a==0 and b=='+' and b==0:\n\tprint('0 + 0 = 0')"""

with open('main.py', 'w') as f:
    for first_number in range(101):
        for second_number in range(101):
            for operator in ['+', '-', '*', '/']:
                try:
                    if operator == "+":
                        app_str = f"\nelif a == {first_number} and b == '{operator}' and c == {second_number}:\n\tprint('{first_number} {operator} {second_number} = {first_number + second_number}')"
                    elif operator == "-":
                        app_str = f"\nelif a == {first_number} and b == '{operator}' and c == {second_number}:\n\tprint('{first_number} {operator} {second_number} = {first_number - second_number}')"
                    elif operator == '*':
                        app_str = f"\nelif a == {first_number} and b == '{operator}' and c == {second_number}:\n\tprint('{first_number} {operator} {second_number} = {first_number * second_number}')"
                    else:
                        app_str = f"\nelif a == {first_number} and b == '{operator}' and c == {second_number}:\n\tprint('{first_number} {operator} {second_number} = {first_number / second_number}')"
                    main_ += app_str
                except Exception as e:
                    print(e)

    main_ += """\nelse :\n\tprint(f'Are you kidding me {a} and {c} ? why ?')"""
    f.write(main_)
