def uppercase(input_function):
    def processed_text(input_text):
        return input_function(input_text.upper())

    return processed_text


@uppercase
def print_text(input_text):
    print(input_text)


def floating_point_check(input_function):
    def check_safety(first, second):
        if (type(first) is float) or (type(second) is float):
            print("The result might not be correctly calculated, due to floating point inaccuracies")
            return input_function(first, second)
        else:
            return input_function(first, second)

    return check_safety


@floating_point_check
def addition(first, second):
    return first + second


if __name__ == '__main__':

    print_text("This string will be uppercase")

    print(addition(3, 6))
    print(addition(3, 6.6))






