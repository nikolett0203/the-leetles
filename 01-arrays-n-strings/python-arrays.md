## Arrays in Python

### Overview

Just kidding! Python doesn't have arrays.

Instead, it has a few different types of collections (a collection being, conceptually, a single "variable" used to store multiple values).

#### Lists

A __list__ is an ordered, mutable collection of items denoted with [ square brackets ].
+ Duplicate items are permitted.
+ Items can be modified, replaced, or removed.
+ The order in which items are added is maintained.
+ Items are accessed via indices.
+ Mixed types can be stored in the same list.

A list can be created using
+ Square brackets: `a = [1, "hello", 3.14, True]`
+ List constructors: `b = list("GFG")`
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