from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import FAQ
from .serializers import FAQSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    @action(detail=True, methods=['get'])
    def translate(self, request, pk=None):
        faq = self.get_object()
        lang = request.GET.get('lang', 'en')
        translated_question = faq.get_translated_question(lang)
        return Response({"translated_question": translated_question, "answer": faq.answer})
