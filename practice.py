def todo_list(new_task, base_list=['wake up']):
    base_list.append(new_task)
    return base_list

todo_list("check the mail")



print(todo_list("begin orbital transfer"))