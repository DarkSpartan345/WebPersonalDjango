from django.db import models

class Project(models.Model):
    title=models.CharField(max_length=200,verbose_name="Titulo")
    description=models.TextField(verbose_name="Descripcion")
    imagen=models.ImageField(verbose_name="Imagen",upload_to="projects")
    update=models.DateTimeField(auto_now=True,verbose_name="Fecha de actualizacion")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    URL=models.URLField(null=True,blank=True)
    class Meta:
        verbose_name="Projecto"
        verbose_name_plural="Projectos"
        ordering=["-created"]
    def __str__(self):
        return self.title