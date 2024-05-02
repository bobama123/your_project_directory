from lib.todo import Todo


"""
Initially
Tasks are complete False
"""
def test_for_task_is_False():
    todo = Todo("Eat food")
    assert todo.complete == False



