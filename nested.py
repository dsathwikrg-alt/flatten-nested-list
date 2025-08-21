import ast
from typing import Any, List, Iterable, Iterator


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

def flatten_recursive(input_list: List[Any]) -> List[Any]:
    flat: List[Any] = []
    for sublist in input_list:
        if isinstance(sublist, list):          # if it's a list, flatten it further
            flat.extend(flatten_recursive(sublist))
        else:                                  # otherwise, append the value
            flat.append(sublist)
    return flat


def flatten_generative(input_list: Iterable[Any]) -> Iterator[Any]:
    for sublist in input_list:
        if isinstance(sublist, list):
            # yield each item from the recursive generator
            yield from flatten_generative(sublist)
        else:
            yield sublist


def main():

    # Accepts the list items as string
    user_input = input("Enter the Nested List items (e.g. [[1,2],[3,4]]) ::")

    # Safely parse through the user_input string and convert to list
    nested_list = ast.literal_eval(user_input)

    # Function call
    flatten_list = flatten_nested_list(nested_list)
    flatten_list_recursive = flatten_recursive(nested_list)
    flatten_list_gen = list(flatten_generative(nested_list))

    print(f"Flatten list is {flatten_list}")
    print(f"Flatten list is {flatten_list_recursive}")
    print(f"Flatten list is {flatten_list_gen}")

if __name__ == '__main__':
    main()
    



