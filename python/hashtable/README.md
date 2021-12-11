# Hashtables
<!-- Short summary or background information -->
### Hashing is a technique that is used to uniquely identify a specific object from a group of similar objects.

## PR Description Section :

| Table Of Content                               | Links                                       |
| ---------------------------------------------- | ------------------------------------------- |
| PR '1' > Implement Hashtable                   | [PR '1' > Hashtable](https://github.com/RihanFoudeh/data-structures-and-algorithms/pull/29)|


# Challenge
<!-- Description of the challenge -->
### Implement a Hashtable Class.

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
* add: 
    - time `O(1)`
    - space `O(1)`
* get:
    - time `O(1)` 
    - space `O(1)`
* contains: 
    - time `O(1)` 
    - space `O(1)`
* hash: 
    - time `O(n)` 
    - space `O(1)`

## API
<!-- Description of each method publicly available in each of your hashtable -->
* add
    - Arguments: key, value
    - Returns: nothing
    - This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
* get
    - Arguments: key
    - Returns: Value associated with that key in the table
* contains
    - Arguments: key
    - Returns: Boolean, indicating if the key exists in the table already.
* hash
    - Arguments: key
    - Returns: Index in the collection for that key

