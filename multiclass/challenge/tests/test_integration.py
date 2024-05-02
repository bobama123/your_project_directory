from lib.todo_list import TodoList
from lib.todo import Todo

"""
Given the task, mark it complete
Tasks are marked complete True
Return the list of complete tasks
"""
def test_for_complete_list():
    todo_list = TodoList()
    todo1 = Todo("Eat food")
    todo_list.add(todo1)
    todo1.mark_complete()
    assert todo_list.complete() == [todo1]

"""
Given the task, if complete is False
Return the list of incompete Tasks
"""
def test_for_incomplete_list():
    todo_list = TodoList()
    todo1 = Todo("Eat food")
    todo_list.add(todo1)
    assert todo_list.incomplete() == [todo1]

"""
Given all tasks, if give up called
All tasks are marked complete True
Return the list of compete Tasks
"""
def test_for_give_up_all_true():
    todo_list = TodoList()
    todo1 = Todo("Eat food")
    todo2 = Todo("Cry")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.give_up()
    assert todo_list.complete() == [todo1, todo2]


