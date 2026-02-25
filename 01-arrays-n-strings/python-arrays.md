# Arrays in Python

## Overview

Just kidding! Python doesn't have arrays.

Instead, it has a few different types of collections (a collection being, conceptually, a single "variable" used to store multiple values).

## Lists

A __list__ is an ordered, mutable collection of items denoted with [ square brackets ].
+ Duplicate items are permitted.
+ Items can be modified, replaced, or removed.
+ The order in which items are added is maintained.
+ Items are accessed via indices.
+ Mixed types can be stored in the same list.

A list can be created using
+ Square brackets: `a = [1, "hello", 3.14, True]`
+ List constructors: `b = list("GFG")` or `d = list(("apple", "banana", "orange"))`
+ Multiplication operators: `c = [0] * 7`

Elements are accessed with 
+ Singular indices: `print(c[1])` yields `0`
+ Ranges of indices: `print(a[0:3])` yields `[1, "hello", 3.14]`
+ Step indices: `b[::2]` yields every other element, `b[::-1]` yields the list in reverse

Elements are updated using
+ `append` to add to the list end: `a.append(10)`
+ `extend` to add multiple elements to the end of the list: `a.extend([15, 20, 25])`
+ `insert` to add to a specific position: `a.insert(0,5)`
+ `clear` to remove all items: `a.clear()`
+ `remove` to remove the first occurence of an element: `a.remove("hello")`
+ `pop` to remove an element at a specific index, or the last index if unspecified: `a.pop(1)`
+ `del` statement to delete an element at a specific index: `del a[0]`
+ `list[index] = value` to change an element: `a[1] = 25`

2D lists can be created by nesting 1D lists:
```
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

__List comprehension__ is a concise way to create lists by applying an expression to each item in an existing iterable.
```
a = [1, 2, 3, 4, 5]
b = [val * 2 for val in a if val % 2 == 0]
```

Lists are most useful in circumstances where
+ The sequence of data carries meaning (e.g. timelines of events, undo/redo stacks, rankings).
+ If you expect to add, remove, or change elements frequently.
+ If you have duplicate items (e.g. items purchased by a customer)

Other useful methods include
+ `len()` to count the list

A list doesn't store items directly. Instead, it stores references to objects in memory.
+ For immutable objects (integers, strings, booleans, tuples), when you 'change' the object in a list, you aren't actually modifying the object. Python creates a new object at a different memory address and updates the list pointer to the new object. This means that changing one variable won't change another.
+ For mutable objects (nested lists, dictionaries, etc.) within lists, it stores a pointer to that object's specific location. If you modify the nested object, you are changing the data at the existing address. For example: `A = [1, 2]`, `my_list = [A]`, `A.append(3)` will modify the original list to become `A = [1, 2, 3]`. This can lead to ghost updates where changing one variable affects others that reference the same object.
An example of where this could go wrong:
```
grid = [[0] * 3] * 3
```
This doesn't create three separate rows. It creates one list and creates a list of three pointers all looking at the same row.

Another example:
```
def add_item(my_data):
    my_data.append("Surprise!")

items = [1, 2, 3]
add_item(items)
print(items) # Output: [1, 2, 3, "Surprise!"]
```
Lists passed to function will be changed outside of the function as well. 

## Tuple

## Set

Good for "have I seen this element before?" fast lookup or membership checks

## Dictionary

Counting or mapping relationships

