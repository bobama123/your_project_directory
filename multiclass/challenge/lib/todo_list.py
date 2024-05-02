
class TodoList:
    def __init__(self):
        self.todo_list = []

    def add(self, todo):
        self.todo_list.append(todo)

    def incomplete(self):
        incomplete_list = []
        for entry in self.todo_list:
            if entry.complete == False:
                incomplete_list.append(entry)       
        return incomplete_list

    def complete(self):
        self.complete_list = []
        for entry in self.todo_list:
            if entry.complete == True:
                self.complete_list.append(entry)       
        return self.complete_list

    def give_up(self):
        for entry in self.todo_list:
            entry.mark_complete()