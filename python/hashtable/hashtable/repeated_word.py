from hashtable.hashtable import HashTable

def repeated_word(string):
    """
    Write a function called repeated word that finds the first word to occur more than once in a string
    Arguments:
        string: a string
    Returns: string
    """
    if not string  :
        return "String Is Empty"

    string = string.replace(".", "")
    string = string.replace(",", "")
    string = string.replace("-", "")
    string = string.lower()

    list_words = string.split()

    new_hashtable = HashTable()

    for word in list_words:

        if new_hashtable.contains(word):
            return word

        else:
            new_hashtable.add(word, word)

    return "No Duplicate"


#########################################################################
if __name__ == "__main__":
    string1 = "Once upon a time, there was a brave princess who..."
    print(f"{string1} >>> {repeated_word(string1)}\n")

    string2 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    print(f"{string2} >>> {repeated_word(string2)}\n")

    string3 = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    print(f"{string3} >>> {repeated_word(string3)}\n")
