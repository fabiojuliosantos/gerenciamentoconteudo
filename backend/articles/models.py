from django.db import models
from users.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30, blank=False)
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    tag_name = models.CharField(max_length=30, blank=False)
    
    def __str__(self):
        return self.tag_name

class Article(models.Model):
    title = models.CharField(max_length=90, blank=False)
    text = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    liked_by = models.ManyToManyField(User, related_name='liked_articles')
    #tags = models.ManyToManyField(Tag, related_name='article_tags')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.title
    
    """ def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.tags:
            tag_names = [tag.strip() for tag in self.tags.split(",") if tag.strip()]
            tags = []
            for tag_name in tag_names:
                tag, _ = Tag.objects.get_or_create(tag_name=tag_name)
                tags.append(tag)
            
            self.tags.set(tags)
 """
class Reply(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, blank=False)
    text = models.CharField(max_length=500, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
