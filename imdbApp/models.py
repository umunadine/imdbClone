from django.db import models
import datetime as dt

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length =50)
     
    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self, update):
        self.name = update
        self.save()

    @classmethod
    def get_category_id(cls, id):
        category = Category.objects.get(pk = id)
        return category
    
    

class Language(models.Model):
    name = models.CharField(max_length =50)

    def __str__(self):
        return self.name

    @classmethod
    def tag_articles(cls):
        tags = cls.objects.all()
        return tags

    def save_language(self):
        self.save()

    def delete_language(self):
        self.delete()

    def update_language(self, update):
        self.name = update
        self.save()

    @classmethod
    def get_language_id(cls, id):
        locate = Language.objects.get(pk = id)
        return locate


class Status(models.Model):
    name = models.CharField(max_length =50)

    def __str__(self):
        return self.name

    @classmethod
    def tag_status(cls):
        stats = cls.objects.all()
        return stats

    def save_status(self):
        self.save()

    def delete_status(self):
        self.delete()

    def update_status(self, update):
        self.name = update
        self.save()

    @classmethod
    def get_status_id(cls, id):
        stat = Status.objects.get(pk = id)
        return stat 


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='movies/')
    movie_category = models.ForeignKey('Category',on_delete=models.CASCADE,)
    movie_language = models.ForeignKey('Language',on_delete=models.CASCADE,)
    movie_status = models.ForeignKey('Status',on_delete=models.CASCADE, )
    cast = models.CharField(max_length=100)
    year_of_production = models.DateField()
    views_count = models.IntegerField(default=0)
    trailer = models.URLField(max_length=250)

    def __str__(self):
        return self.title
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    @classmethod
    def update_image(cls, id ,title, description , movie_language, movie_category,movie_status):
        update = cls.objects.filter(id = id).update(title = title, description = description ,movie_language = movie_language,movie_category = movie_category,movie_status=movie_status)

    @classmethod
    def get_image_by_id(id):
        image = cls.objects.filter(id=id)
        return image

    @classmethod
    def search_by_title(cls,search_term):
        search = Movie.objects.filter(title__icontains=search_term)
        return search

    @classmethod
    def filter_by_category(cls,category):
        movies = cls.objects.filter(movie_category=category)
        return movies 

    @classmethod
    def filter_by_language(cls,language):
        movies = cls.objects.filter(movie_language=language)
        return movies 

    @classmethod
    def filter_by_status(cls,status):
        movies = cls.objects.filter(movie_status=status)
        return movies 

    class Meta:
        ordering = ['title']
