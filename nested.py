import ast

def flatten_nested_list(input_list: list) -> list:
    flat = []
    nested_list = input_list
    for sublist in nested_list:
        if isinstance(sublist, list):
            for item in sublist:
                flat.append(item)

        else:
            flat.append(sublist)        

    return flat

def main():

    # Accepts the list items as string
    user_input = input("Enter the Nested List items (e.g. [[1,2],[3,4]]) ::")

    # Safely parse through the user_input string and convert to list
    nested_list = ast.literal_eval(user_input)

    # Function call
    flatten_list = flatten_nested_list(nested_list)

    print(f"Flatten list is {flatten_list}")

if __name__ == '__main__':
    main()
    



