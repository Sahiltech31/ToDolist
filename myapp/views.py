from django.shortcuts import render, redirect
from .models import TodoList

from django.http import JsonResponse



def home(request):
    tasks = TodoList.objects.all().order_by('-created_at')  # Latest first
    return render(request, 'home.html', {'tasks': tasks})

def store_data(request):
   # created_time = None  

    if request.method == 'POST':
        new_task = ' '.join(request.POST.get('data', '').strip().split()).upper()


        if new_task:
            if not TodoList.objects.filter(add=new_task).exists():
                TodoList.objects.create(add=new_task)#save new_task
                
                
        return redirect('home')

    return render(request, 'home.html')


def toggle_status(request, task_id):
    task = TodoList.objects.get(id=task_id)  # Get the task by its ID
    # Toggle the status
    if task.status == 'Pending':
        task.status = 'Completed'
    else:
        task.status = 'Pending'
    task.save()  # Save the updated task back to the database
    return redirect('home') 

def delete_data(request , tasks_add):
    if request.method == 'POST':
        deltask = TodoList.objects.get(add=tasks_add)

        deltask.delete()
        return redirect('home')
    



def update_task(request):
    if request.method == "POST":
        task_id = request.POST.get("task_id")
        new_text = request.POST.get("task_text")
        try:
            task = TodoList.objects.get(id=task_id)
            task.add = new_text  # Assuming your field is task_text
            task.save()
            return JsonResponse({"success": True})
        except TodoList.DoesNotExist:
            return JsonResponse({"success": False, "error": "Task not found"})
    return JsonResponse({"success": False, "error": "Invalid request"})







    