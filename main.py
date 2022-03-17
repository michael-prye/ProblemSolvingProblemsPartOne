# problem solving part 1

# 1.

def input_string():
    user_input = input("Please enter a string that you would like reversed: ")
    return user_input
def reverse_string(user_string):
    reverse_string = ''
    for i in range(len(user_string) - 1,-1,-1):
        reverse_string += user_string[i]
    return reverse_string
    # user_list = list(user_string)
    # user_list.reverse()
    # reversed_string = user_string[::-1]
def print_reverse_string():
    print(reverse_string(input_string()))
def run_num1():
    print_reverse_string()
run_num1()

# # 2.

def input_string():
    user_input = input("Please enter a string you want to title: ")
    return user_input
def capitalize_string():
    user_string = input_string()
    title_string = ''
    title_string += user_string[0].upper()
    capitalized_letter = False
    for i in range(1,len(user_string)):
        if user_string[i].isspace() == True:
            title_string += user_string[i]
            i += 1
            title_string += user_string[i].upper()
            capitalized_letter = True
        else:
            if capitalized_letter == True:
                capitalized_letter = False
                continue
            else:
                title_string += user_string[i]
    return title_string
    # return user_string.title()
def print_string():
    print(capitalize_string())
def run_num2():
    print_string()
run_num2()

# 3. 


def input_string():
    user_input = input('Please enter the string you would like to compress: ')
    return user_input
def compress_string(user_string):
    compressed_string = ''
    count = 1
    for i in range(len(user_string)):
        if i == len(user_string)-1:
            compressed_string += str(count)
            compressed_string += user_string[i]
        elif user_string[i] == user_string[i +1]:
            count += 1
        else:
            compressed_string += str(count)
            compressed_string += user_string[i]
            count = 1
    return compressed_string
def run_num3():
    print(compress_string(input_string()))
run_num3()


# 4.
def get_user_input():
    user_input = input("Please enter your Palindrome: ")
    return user_input
def reverse_user_input(user_string):
    reverse_input = user_string[::-1]
    return reverse_input
def test_if_palindrome(user_input, reverse_input):
    if user_input == reverse_input:
        return True
    else:
        return False
def print_test(test_result):
    if test_result == True:
        print("This is a Palindrome")
    else:
        print("This is not a Palindrome")
def run_num4():
    input = get_user_input()
    reverse_string = reverse_user_input(input)
    results = test_if_palindrome(input, reverse_string)
    print_test(results)
run_num4()
