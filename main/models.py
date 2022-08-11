from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Expenses(models.Model):
    MONTH_CHOICES = (
        ("1", "January"),
        ("2", "February"),
        ("3", "March"),
        ("4", "April"),
        ("5", "May"),
        ("6", "June"),
        ("7", "July"),
        ("8", "August"),
        ("9", "September"),
        ("10", "October"),
        ("11", "November"),
        ("12", "December"),

    )

    title = models.CharField(max_length=150)
    amount = models.IntegerField()
    detail = models.TextField(null=True, blank=True)
    month = models.CharField(max_length=2, choices = MONTH_CHOICES)
    year = models.CharField(max_length=4)
    category = models.ManyToManyField(Category)

    def category_to_str(self):
        return ", ".join([category.title for category in self.category.all()])

    def __str__(self):
        return self.title