
"""
As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.
"""


class ToDo():
    def add(self, task):
        #Parameters:
        #   task: a string, task for todo list
        pass
    def list_incomplete(self):
        #Returns:
        #   A list of incomplete tasks
        pass
    def mark_complete(self, index):
        #Parameters:
        #   index: an integer, an integer representing the task to complete
        #Side effect:
        #   Removes the task at index from list of tasks
        pass
"""
Inititally, there are tasks
"""
todo = ToDo()
todo.list_incomplete() # > []

"""
When add a task
Task is in the list
"""
todo = ToDo()
todo.add("wash clothes")
todo.list_incomplete() # > ["wash clothes"]

"""
When add 3 tasks
All tasks are in the list
"""
todo = ToDo()
todo.add("wash clothes")
todo.add("eat")
todo.add("sleep")
todo.list_incomplete() # > ["wash clothes", "eat", "sleep"]

"""
When we add multiple tasks
Mark one as complete
It is removed from the list
"""
todo = ToDo()
todo.add("wash clothes")
todo.add("eat")
todo.add("sleep")
todo.mark_complete(2)
todo.list_incomplete() # > ["wash clothes", "eat"]

"""
We try to mark a class not in task list (too high)
Raises Error
"""
todo = ToDo()
todo.add("wash clothes")
todo.add("eat")
todo.mark_complete(5) # > Raises an Error > "No task found"
todo.list_incomplete() # > ["wash clothes", "eat"]

"""
We try to mark a class not in task list (too low)
Raises Error
"""
todo = ToDo()
todo.add("wash clothes")
todo.add("eat")
todo.mark_complete(-1) # > Raises an Error > "No task found"
todo.list_incomplete() # > ["wash clothes", "eat"]





