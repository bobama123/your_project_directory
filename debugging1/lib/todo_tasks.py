class ToDo():
    def __init__(self):
        self.todo_list = []

    def add(self, task):
        self.todo_list.append(task)

    def list_incomplete(self):
        return self.todo_list

    def mark_complete(self, index):
        if index >= len(self.todo_list) or index < 0:
            raise Exception("No tasks given")
        del self.todo_list[index]
        