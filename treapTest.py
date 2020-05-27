from treap import Treap
import pytest

#test that a treap can be initialized
def test_makeEmptyTreap():
    t = Treap()
    assert t 

#test that one node is inserted correctly
def test_insertOne():
    t = Treap()
    assert t.insert("A")

#test that it finds is a key is in the treap
def test_findKeyThere():
    t = Treap()
    t.insert("A")
    assert t.find("A")
    
#test that it comes back false is the key is not in the treap
def test_findKeyNotThere():
    t = Treap()
    t.insert("A")
    assert t.find("B") == False

#test that it keeps track of one occurence of a key
def test_testOccurenceCountOne():
    t = Treap()
    t.insert("A")
    assert t.getOccurenceCount("A") == 1

#test that it keeps track of how many times the key was inserted
def test_testOccurenceCountMany():
    t = Treap()
    t.insert("A")
    t.insert("A")
    t.insert("A")
    assert t.getOccurenceCount("A") == 3

#test that a key is removed properly 
def test_removeWithOneOccurence():
    t = Treap()
    t.insert("A")
    t.remove("A")
    assert t.find("A") == False

#test that it lowers the count of the insertions of one key
def test_removeMoreThanOneOccurence():
    t = Treap()
    t.insert("A")
    t.insert("A")
    t.remove("A")
    assert t.getOccurenceCount("A") == 1

    
pytest.main(["-v", "-s", "treapTest.py"])