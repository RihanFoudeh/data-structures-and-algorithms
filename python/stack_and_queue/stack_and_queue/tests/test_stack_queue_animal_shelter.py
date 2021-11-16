from stack_and_queue.stack_queue_animal_shelter import (AnimalShelter,Node,Queue)

def test_enqueue():
    actual = []
    animal = AnimalShelter()
    animal.enqueue('bull', 'dog')
    actual += [animal.dog.peek()]
    animal.enqueue('soker', 'cat')
    actual += [animal.cat.peek()]
    excepted = ['bull', 'soker']
    assert actual == excepted


#####################################################################

def test_enqueue_fail():
    animal = AnimalShelter()
    actual = animal.enqueue('pummy', 'hamster')
    excepted = 'This is not a cat or a dog'
    assert actual == excepted


#####################################################################

def test_dequeue():
    animal = AnimalShelter()
    animal.enqueue('bull', 'dog')
    animal.enqueue('soker', 'cat')
    actual = [animal.dequeue('dog'), animal.dequeue('cat')]
    excepted = ['bull', 'soker']
    assert actual == excepted


#####################################################################

def test_dequeue_fail():
    animal = AnimalShelter()
    actual = animal.dequeue('rabbit')
    excepted = 'This is not a cat or a dog'
    assert actual == excepted
