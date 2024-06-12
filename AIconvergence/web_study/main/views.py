from django.shortcuts import render
from .models import AdminInfo
from django.shortcuts import render, redirect
from .camera import VideoCamera  # Import the updated camera class
from .forms import VideoUploadForm
from .models import Video
import logging
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.conf import settings
import os
# Create your views here.
def index(request):
    return render(request,'main/index.html')

def Database(request):
    video_dir = os.path.join(settings.MEDIA_ROOT, 'videos')  # Ensure your videos are stored in media/videos
    video_files = [f for f in os.listdir(video_dir) if f.endswith('.mp4')]
    
    # video_paths = [os.path.join(settings.MEDIA_URL, 'videos', video) for video in video_files]
    video_paths = [{'path': f"{settings.MEDIA_URL}videos/{video}", 'name': video} for video in video_files]
    
    return render(request, 'main/Database.html', {'video_paths': video_paths})
    # return render(request, 'main/Database.html', {'video_files': video_files, 'video_dir': video_dir})
    # return render(request, 'main/Database.html', {'current_page': 'Database'})

def Admin_page(request):
    admins = AdminInfo.objects.all()
    return render(request, 'main/Admin_page.html', {'current_page': 'Admin_page', 'admins': admins})

from django.http import StreamingHttpResponse
import cv2

def monitoring(request):
    return render(request, 'main/monitoring.html', {'current_page': 'monitoring'})

# Instantiate the camera object globally to maintain the same instance
camera = VideoCamera()
def start_recording(request):
    if request.method == 'POST':
        camera.start_recording("recorded_video.avi")
        return redirect('monitoring')  # Adjust to your desired redirect page

def stop_recording(request):
    if request.method == 'POST':
        camera.stop_recording()
        return redirect('monitoring')  # Adjust to your desired redirect page

def video_feed(request):
    return StreamingHttpResponse(gen(camera), content_type='multipart/x-mixed-replace; boundary=frame')

def gen(camera_instance):
    while True:
        frame = camera_instance.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    
def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_videos')  # Adjust to your desired page
    else:
        form = VideoUploadForm()
    return render(request, 'upload_video.html', {'form': form})

def list_videos(request):
    videos = Video.objects.all()
    return render(request, 'list_videos.html', {'videos': videos})
    






def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        print(form)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'main/index.html', {'form': form, 'error': 'Invalid login credentials'})
    else:
        form = AuthenticationForm()
    return render(request, 'main/index.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required
def some_protected_view(request):
    # Your view logic here
    return render(request, 'protected.html')


# from django.contrib.auth.models import User
# User.objects.create_user('Jaehyun Yoon', 'jhyoon964@jnu.ac.kr', '123')
