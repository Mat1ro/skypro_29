import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import ADS, Categories


class MainView(View):
    def get(self, request):
        try:
            return JsonResponse({"status": "ok"}, status=200)
        except:
            return JsonResponse({"status": "bad"}, status=404)


@method_decorator(csrf_exempt, name="dispatch")
class AdsView(View):
    def get(self, request):
        all_ads = ADS.objects.all()

        response = []
        for ads in all_ads:
            response.append({
                "id": ads.id,
                "name": ads.name,
                "author": ads.author,
                "price": ads.price,
                "description": ads.description,
                "address": ads.address,
                "is_published": ads.is_published
            })

        return JsonResponse(response, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        ads = ADS.objects.create(
            name=data['name'],
            author=data['author'],
            price=data['price'],
            description=data['description'],
            address=data['address'],
            is_published=data['is_published']
        )
        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "author": ads.author,
            "price": ads.price,
            "description": ads.description,
            "address": ads.address,
            "is_published": ads.is_published
        })


class AdsDetailView(DetailView):
    model = ADS

    def get(self, request, *args, **kwargs):
        try:
            ads = self.get_object()
        except:
            return JsonResponse({'error': "not found"}, status=404)

        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "author": ads.author,
            "price": ads.price,
            "description": ads.description,
            "address": ads.address,
            "is_published": ads.is_published
        })


@method_decorator(csrf_exempt, name="dispatch")
class CategoriesView(View):
    def get(self, request):
        all_categories = Categories.objects.all()

        response = []
        for categories in all_categories:
            response.append({
                "id": categories.id,
                "name": categories.name
            })

        return JsonResponse(response, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        categories = Categories.objects.create(
            name=data['name']
        )
        return JsonResponse({
            "id": categories.id,
            "name": categories.name,
        })


class CategoriesDetailView(DetailView):
    model = Categories

    def get(self, request, *args, **kwargs):
        try:
            categories = self.get_object()
        except:
            return JsonResponse({'error': "not found"}, status=404)

        return JsonResponse({
            "id": categories.id,
            "name": categories.name,
        })
