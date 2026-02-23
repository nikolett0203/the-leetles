## Arrays and Strings

### Overview

Some languages (C, Java primitive, etc.) store elements contiguously in memory, but others (Python, JS, etc.) store pointers to elements. Contiguous arrays are more common in performance-first languages where speed and memory efficiency are prioritized. This approach, however, comes at a cost, since it requires all elements to be of the same type and makes resizing computationally expensive. Reference arrays provide the flexibility of mixed-type storage and easy resizing (i.e., just add another pointer to wherever you have free memory!), but are slower, memory-intensive, and cache misses. 

*Cache miss: when you ask for data that is not already in the cache; less common for contiguous arrays because data is loaded in blocks.*

### Fun Facts

+ 