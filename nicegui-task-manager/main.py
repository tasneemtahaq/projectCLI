from nicegui import ui

tasks = []

def refresh_tasks():
    task_container.clear()
    if not tasks:
        with task_container:
            ui.label('🎉 No tasks yet. Add one above!').classes('text-gray-500 italic')
    else:
        with task_container:
            for i, task in enumerate(tasks):
                with ui.row().classes('items-center gap-2'):
                    checkbox = ui.checkbox('', value=task['done'])
                    label_text = f"{task['text']} (📅 {task['date']})" if task['date'] else task['text']
                    label = ui.label(label_text).classes('text-lg')

                    def update_status(e=None, i=i):
                        tasks[i]['done'] = checkbox.value
                        label.classes('line-through' if checkbox.value else '')

                    checkbox.on('update:modelValue', update_status)
                    update_status()

def add_task():
    text = task_input.value.strip()
    date = date_input.value
    if text:
        tasks.append({'text': text, 'done': False, 'date': str(date) if date else ''})
        task_input.value = ''
        date_input.value = None
        refresh_tasks()

# Main container
with ui.column().classes('w-full min-h-screen justify-center items-center bg-gray-100 p-10'):

    # Header
    ui.label('📝 Task Manager').classes('text-3xl font-bold text-blue-800 mb-6')

    # Task input and date
    with ui.column().classes('gap-2 mb-4 items-center'):
        task_input = ui.input('Enter your task...').props('outlined').classes('w-72')
        date_input = ui.date().classes('w-60')
        ui.button('Add Task', on_click=add_task).classes('bg-blue-600 text-white w-36')

    # Task list heading
    ui.label('📝 Your Tasks').classes('text-2xl font-semibold text-blue-700 mb-2')

    # Task list container
    task_container = ui.column().classes('bg-white p-6 rounded-lg shadow-md w-[420px] min-h-[200px]')

    # Footer / Signature
    ui.label('Developed by TasneemTaha').classes('text-xs text-gray-400 text-center mt-10')

# Run the app
if __name__ in {"__main__", "__mp_main__"}:
    ui.run()
