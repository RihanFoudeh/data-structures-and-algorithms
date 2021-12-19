from hashtable.hashtable import HashTable
from hashtable.hashmap_left_join import left_join

#########################################################################

def test_left_join_solution_one():
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

    actual = left_join(ht1, ht2)

    expected = [['fond', 'enamored', 'averse'], ['guide', 'usher', 'follow'], ['diligent', 'employed', 'idle'], ['outifit', 'grap', 'None'], ['wrath', 'anger', 'delight']]

    assert expected == actual

#########################################################################


def test_left_join_solution_one_right_hashtable_empty():

    hashtable1 = HashTable()

    ht2 = HashTable()
    ht2.add('fond', 'averse')
    ht2.add('wrath', 'delight')
    ht2.add('diligent', 'idle')
    ht2.add('guide', 'follow')
    ht2.add('flow', 'jam')

    actual = left_join(hashtable1, ht2)

    expected = []

    assert expected == actual

#########################################################################

def test_left_join_solution_one_left_hashtable_empty():

    ht1 = HashTable()
    ht1.add('fond', 'enamored')
    ht1.add('wrath', 'anger')
    ht1.add('diligent', 'employed')
    ht1.add('outifit', 'grap')
    ht1.add('guide', 'usher')

    hashtable2 = HashTable()

    actual = left_join(ht1, hashtable2)

    expected = [['fond', 'enamored', 'None'], ['guide', 'usher', 'None'], ['diligent', 'employed', 'None'], ['outifit', 'grap', 'None'], ['wrath', 'anger', 'None']]

    assert expected == actual

#########################################################################

def test_left_join_solution_two_right_hashtable_empty():
    hashtable1 = HashTable()

    hashtable2 = HashTable()
    hashtable2.add('fond', 'averse')
    hashtable2.add('wrath', 'delight')
    hashtable2.add('diligent', 'idle')
    hashtable2.add('guide', 'follow')
    hashtable2.add('flow', 'jam')

    actual = left_join(hashtable1, hashtable2)

    expected = []

    assert expected == actual

# #########################################################################


