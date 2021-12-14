
from hashtable.hashtable import HashTable

def left_join(hash1 , hash2):
    output = []
    for i in hash1.map:
        if i:
            output.append(i)
    for i in range(len(output)):
        hashed = hash2.hash(output[i][0])
        if hash2.contains(output[i][0]):
            output[i].append(hash2.map[hashed][1])
        else:
            output[i].append("None")
    return output

if __name__ == "__main__":
    ht1 = HashTable()
    ht1.add('fond', 'enamored')
    ht1.add('wrath', 'anger')
    ht1.add('diligent', 'employed')
    ht1.add('outifit', 'grap')
    ht1.add('guide', 'usher')
    ht2 = HashTable()
    ht2.add('fond', 'averse')
    ht2.add('wrath', 'delight')
    ht2.add('diligent', 'idle')
    ht2.add('guide', 'follow')
    ht2.add('flow', 'jam')

    print(left_join(ht1,ht2))
