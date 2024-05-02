from lib.todo_list import TodoList


"""
Initially
There are no tasks
"""
def test_for_no_tasks():
    todo = TodoList()
    assert todo.todo_list == []

