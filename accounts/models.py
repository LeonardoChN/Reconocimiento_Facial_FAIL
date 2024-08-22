from django.db import models

class Worker(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class WorkerImage(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='worker_images/')
    created_at = models.DateTimeField(auto_now_add=True)
