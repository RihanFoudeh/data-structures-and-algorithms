from linked_list import __version__

from linked_list.linked_list import Linkedlist

def test_version():
    assert __version__ == '0.1.0'

def test_instantiate():
    List = Linkedlist()
    actual = List.head
    expected = None
    assert actual == expected
#########################################################################
def test_insert():
    List = Linkedlist()
    List.insert(6)
    actual=List.head.value
    expected=6
    assert actual == expected
#########################################################################
def test_head():
    List = Linkedlist()
    List.insert(10)
    assert List.head.value == 10
#########################################################################
def test_find_value():
    List = Linkedlist()
    List.insert(1)
    List.append(5)
    List.append(10)
    assert List.includes(10) == True
#########################################################################
def test_find_notExist_value():
    List = Linkedlist()
    List.insert(1)
    List.append(5)
    List.append(10)
    assert List.includes(4) == False
#########################################################################
def test_str():
   List = Linkedlist()
   List.insert(1)
   List.append(2)
   List.append(3)
   assert List.__str__()=='{1}-> {2}-> {3}-> NULL'
#########################################################################
def lists():
    List = Linkedlist()
    List.insert(1)
    List.append(2)
    List.append(3)
    List.append(4)
    List.append(5)
    List.append(6)
    List.append(7)
    List.append(8)
    List.append(9)
    List.append(10)
    return List

#########################################################################

def test_multiple():
    List=lists()
    actual=List.__str__()
    expected='{1}-> {2}-> {3}-> {4}-> {5}-> {6}-> {7}-> {8}-> {9}-> {10}-> NULL'
    assert actual == expected

########################################################################

