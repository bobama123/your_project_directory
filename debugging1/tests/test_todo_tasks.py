import pytest
from lib.todo_tasks import ToDo

def test_for_no_tasks():
    todo = ToDo()
    assert todo.list_incomplete() == []

def test_for_single_task_added():
    todo = ToDo()
    todo.add("wash clothes")
    assert todo.list_incomplete() == ["wash clothes"]

def test_for_multiple_tasks_added():
    todo = ToDo()
    todo.add("wash clothes")
    todo.add("eat")
    todo.add("sleep")
    result = todo.list_incomplete() 
    assert result == ["wash clothes", "eat", "sleep"]

def test_for_one_marked_task():
    todo = ToDo()
    todo.add("wash clothes")
    todo.add("eat")
    todo.add("sleep")
    todo.mark_complete(2)
    assert todo.list_incomplete() == ["wash clothes", "eat"]

def test_for_marked_task_not_in_list():
    todo = ToDo()
    todo.add("wash clothes")
    todo.add("eat")
    with pytest.raises(Exception) as e:
        todo.mark_complete(5)
    error = str(e.value)
    assert error == "No tasks given"
    assert todo.list_incomplete() == ["wash clothes", "eat"]


def test_for_marked_task_not_in_list_with_negative_index():
    todo = ToDo()
    todo.add("wash clothes")
    todo.add("eat")
    with pytest.raises(Exception) as e:
        todo.mark_complete(-1)
    error = str(e.value)
    assert error == "No tasks given"
    assert todo.list_incomplete() == ["wash clothes", "eat"]
