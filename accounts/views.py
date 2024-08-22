from django.shortcuts import render, redirect
from .forms import WorkerRegistrationForm
from .models import Worker, WorkerImage
import cv2
import os
import numpy as np
from django.conf import settings
from face_recognition import face_encodings, compare_faces

def register(request):
    if request.method == 'POST':
        form = WorkerRegistrationForm(request.POST)
        if form.is_valid():
            worker = form.save()
            # Capturar video de 15 segundos
            video_capture = cv2.VideoCapture(0)
            frames = []
            for _ in range(int(15 * 30)):  # 15 seconds at 30 fps
                ret, frame = video_capture.read()
                if ret:
                    frames.append(frame)
            video_capture.release()

            # Guardar imágenes extraídas y entrenar el modelo
            face_folder = os.path.join(settings.MEDIA_ROOT, 'worker_images', worker.rut)
            os.makedirs(face_folder, exist_ok=True)
            for i, frame in enumerate(frames):
                image_path = os.path.join(face_folder, f'{worker.rut}_{i}.jpg')
                cv2.imwrite(image_path, frame)
                WorkerImage.objects.create(worker=worker, image=image_path)

            return redirect('login')
    else:
        form = WorkerRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        # Capturar una imagen para comparar
        video_capture = cv2.VideoCapture(0)
        ret, frame = video_capture.read()
        video_capture.release()

        if ret:
            # Procesar y comparar la imagen con la base de datos
            current_face_encoding = face_encodings(frame)[0]
            workers = Worker.objects.all()

            for worker in workers:
                images = WorkerImage.objects.filter(worker=worker)
                for img in images:
                    img_path = img.image.path
                    known_image = face_encodings(cv2.imread(img_path))[0]
                    if compare_faces([known_image], current_face_encoding):
                        return redirect('home')

        return render(request, 'accounts/login.html', {'error': 'No se encontró coincidencia'})
    
    return render(request, 'accounts/login.html')
