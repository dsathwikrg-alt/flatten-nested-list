# flatten-nested-list
Flatten a Given Nested List

Algorith is ::

A nested list is simply a list that contains other lists as elements.

Example:

nested = [1, [2, 3], [4, [5, 6]], 7]


Here:

1 and 7 are normal elements.

[2, 3] and [4, [5, 6]] are sub-lists (lists inside a list).

🔎 Flattening a nested list

Flattening means converting such a nested list into a single list of all the values, with no sub-lists inside.

Example:

nested = [1, [2, 3], [4, [5, 6]], 7]
flattened = [1, 2, 3, 4, 5, 6, 7]

#########################################################################

for element in input_list:
    if isinstance(element, list):        # only loop if it's a list
        for item in element:
            flat.append(item)
    else:                                # otherwise just add it
        flat.append(element)


If element is a list, go one level deeper and add its contents.

If element is not a list (like an integer), just add it directly.

🔎 What it does

isinstance(object, class_or_tuple)::

Returns True if the object is an instance of the specified class (or a subclass).

Returns False otherwise.

✅ Examples
print(isinstance(5, int))          # True   (5 is an int)
print(isinstance("hello", str))    # True   ("hello" is a str)
print(isinstance([1, 2, 3], list)) # True   (it's a list)
print(isinstance(5.5, int))        # False  (float, not int)

🔎 With multiple types

You can pass a tuple of classes:

print(isinstance(5, (int, float)))   # True  (5 is int, fits)
print(isinstance(5.5, (int, float))) # True  (5.5 is float, fits)
print(isinstance("hi", (int, float)))# False

🧩 Why useful in your flatten function?

In your loop:

if isinstance(element, list):
    ...


This makes sure you only iterate inside a list.
If it’s not a list (e.g., int or str), you just append it directly.


✅ When to use what?

Use type() when you need an exact match (e.g., making sure something is precisely a list, not a subclass).

Use isinstance() when you want to allow subclasses (most common in Python, especially in polymorphism).