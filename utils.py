def get_input(task__file__):
    task_file_name = task__file__.split('/')[-1].split('.')[0]
    task_number = int(task_file_name.split('task')[-1])
    with open(f'inputs/input{task_number}.txt', 'r') as f:
        lines = f.readlines()
    if lines[-1] == '':
        lines.pop()
    return [i.strip() for i in lines]
