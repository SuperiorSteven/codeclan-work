# 1. Create an empty list called `task_list`

# 2. Add a few `str` elements, representing some everyday tasks e.g. 'Make Dinner'

# 3. Print out `task_list`

# 4. Remove the last task

# 5. Print out `task_list`

# 6. Print out the number of elements in `task_list`

task_list = []
task_list.append("cook dinner")
task_list.append("feed cat")
task_list.append("eat")
task_list.append ("washing")
task_list.insert(0, "buy food")
task_list.extend(["play with cat", "get cuddles from cat"])
task_list.pop(2)
print(task_list)