from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
from googletrans import Translator

translator = Translator()

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    
    question_hi = models.TextField(blank=True, null=True)  
    question_bn = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.question_hi:
            self.question_hi = translator.translate(self.question, dest='hi').text
        if not self.question_bn:
            self.question_bn = translator.translate(self.question, dest='bn').text
        super().save(*args, **kwargs)

    def get_translated_question(self, lang="en"):
        cache_key = f"faq_{self.id}_{lang}"
        translated_question = cache.get(cache_key)

        if not translated_question:
            if lang == "hi":
                translated_question = self.question_hi or self.question
            elif lang == "bn":
                translated_question = self.question_bn or self.question
            else:
                translated_question = self.question

            cache.set(cache_key, translated_question, timeout=3600)  # Store in memory

        return translated_question

    def __str__(self):
        return self.question
