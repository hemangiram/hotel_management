from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Room
from .forms import RoomForm






def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'rooms/room_list.html', {'rooms':rooms})





def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    return render(request, 'rooms/room_detail.html', {'room':room})




@login_required
def room_create(request):
    if request.user.role != 'admin':
        return redirect('room_list')

    form = RoomForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('room_list')
    
    return render(request, 'rooms/room_form.html', {'form':form})




@login_required
def room_update(request, pk):
    if request.user.role != 'admin':
        return redirect('room_list')
    

    room = get_object_or_404(Room, pk=pk)
    form = RoomForm(request.POST or None, request.FILES or None, instance=room)


    if form.is_valid():
        form.save()
        return redirect('room_list')
    
    return render(request, 'rooms/room_form.html', {'form':form})



@login_required
def  room_delete(request, pk):
    if request.user.role != 'admin':
        return redirect('room_list')
    

    room = get_object_or_404(Room, pk=pk)

    if request.method == 'POST':
        room.delete()
        return redirect('room_list')
    return render(request, 'rooms/room_confirm_delete.html', {'room':room})





