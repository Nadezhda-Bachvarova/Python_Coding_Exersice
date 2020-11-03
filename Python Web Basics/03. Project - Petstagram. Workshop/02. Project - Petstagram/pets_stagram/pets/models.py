from django.db import models


class Pet(models.Model):
    DOG = 'dog'
    CAT = 'cat'
    PARROT = 'parrot'
    PET_TYPES = (
        (DOG, 'dog'),
        (CAT, 'cat'),
        (PARROT, 'parrot'),
    )
    type = models.CharField(max_length=6, choices=PET_TYPES, default='')
    name = models.CharField(max_length=6, blank=False)
    age = models.IntegerField(blank=False)
    description = models.TextField(blank=False)
    image_url = models.URLField(blank=False)

    def __str__(self):
        return f'Name: {self.name}, type: {self.type}, age: {self.age}'


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    test = models.CharField(max_length=2)


class Test(models.Model):
    test = models.BooleanField(default=True)


class Comment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    text = models.TextField(blank=False)


