from django.db import models
from django.utils.text import slugify

class Car(models.Model):
    CATEGORY_CHOICES = (
        ('RENT', 'Rental'),
        ('SALE', 'Sale'),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    category = models.CharField(max_length=4, choices=CATEGORY_CHOICES, default='RENT')
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Prezzo al mese (RENT) or Prezzo di vendita (SALE)")
    image = models.ImageField(upload_to='cars/')
    specs = models.TextField(help_text="JSON or simple text. e.g., '0-100: 3.5s, Engine: V8'")
    is_featured = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"
