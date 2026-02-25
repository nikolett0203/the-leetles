## Arrays and Strings

### Overview

An __array__ is a linear data structure that stores items of the same type at contiguous locations.

Arrays allow __random access__, meaning all elements can be accessed in equal time via indexing, regardless of the array size. To do this, the system calculates the physical memory address using

```address = base + index * element_size```

Or, in the case of multi-dimensional arrays,

```address = base + (row_index * num_columns + column_index) * element_size```

*Cache miss: when you ask for data that is not already in the cache; less common for contiguous arrays because data is loaded in blocks.*

### Time and Space Complexity



### Fun Facts

+ Some languages (C, Java primitive, etc.) store elements contiguously in memory, but others (Python, JS, etc.) store pointers to elements. Contiguous arrays are more common in performance-first languages where speed and memory efficiency are prioritized. This approach, however, comes at a cost, since it requires all elements to be of the same type and makes resizing computationally expensive. Reference arrays provide the flexibility of mixed-type storage and easy resizing (i.e., just add another pointer to wherever you have free memory!), but are slower, memory-intensive, and encounter more cache misses. 

+ 0-based indexing is typical to C-family languages like C/C++, Java, Python, Javascript, Go, and Rust. It was implemented to make array indexing easier: ```address = base + index * element_size```. 1-based indexing is common in math and science-heavy languages like MATLAB, R, Fortran, etc. 

+ Elements at the end of arrays can be accessed via negative indices. For example, in Python, it is acceptable to use ```array[-1]``` to access the last element, ```array[-2]``` to access the second-to-last element, etc.