from django.db import models



class Tag(models.Model):
    name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return f"{self.name}"
    


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE,blank=True)
    views = models.BigIntegerField(default=0)
    video = models.FileField(upload_to='videos/')
    published_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return f"{self.title}"
