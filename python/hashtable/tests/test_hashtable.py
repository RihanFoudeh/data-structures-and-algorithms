from hashtable import __version__
from hashtable.hashtable import HashTable


def test_version():
    assert __version__ == '0.1.0'


# #########################################################################

def test_add():
    hashtable = HashTable()
    actual=hashtable.add('ahmad', 30)
    expected=['ahmad', 30]
    assert actual==expected

# #########################################################################

def test_get():
    hashtable = HashTable()
    hashtable.add('Rami', 24)
    actual=hashtable.get('Rami')
    expected=24
    assert actual==expected

# #########################################################################

def test_contain():
    hashtable = HashTable()
    hashtable.add('Yaser', 24)
    actual=hashtable.contains('Yaser')
    expected=True
    assert actual==expected

# #########################################################################

def test_get_None_contain():
    hashtable = HashTable()
    hashtable.add('Rihan', 24)
    actual=hashtable.get('Bab')
    expected=None
    assert actual==expected

# #########################################################################

def test_None_contain():
    hashtable = HashTable()
    hashtable.add('Rihan', 24)
    actual=hashtable.contains('Bab')
    expected=False
    assert actual==expected

# #########################################################################

def test_hashtable_collision_get():
    new_hashtable = HashTable()
    new_hashtable.add('Yazan', 20)
    new_hashtable.add('Ayman', 30)

    actual = new_hashtable.get('Yazan')
    expected = 20
    assert actual == expected

# #########################################################################

def test_hashtable_collision_contain():
    hashtable = HashTable()
    hashtable.add('Yazan', 20)
    hashtable.add('Ayman', 30)

    actual = hashtable.contains('Yazan')
    expected =True
    assert actual == expected

# #########################################################################

def test_the_hash_size():
    hashtable = HashTable()

    assert 0<=hashtable.hash("Rihaan")<=1024
