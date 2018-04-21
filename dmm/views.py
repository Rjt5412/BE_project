from django.shortcuts import render, get_object_or_404, redirect
from . import ml,models,services,convert,serializers
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status



# Create your views here.

def index(request):
    twitter_trends = services.get_twitter_trends()
    gplus_trends,tumblr_trends = services.get_tumblr_and_gplus_trends()
    return render(request, 'dmm/index.html',{'twitter_trends': twitter_trends, 'gplus_trends': gplus_trends, 'tumblr_trends': tumblr_trends})

def search(request):
    return render(request, 'dmm/search.html')

def get_params(request):
    '''
    form = forms.Search_form(request.POST)
    print(form.errors)
    if form.is_valid():
        print("is valid")
        keyword = form.cleaned_data["search"]
        twitter = form.cleaned_data["twitter"]
        gplus = form.cleaned_data["gplus"]
        tumblr = form.cleaned_data["tumblr"]
        category = form.cleaned_data["category"]
        sub_category = form.cleaned_data["sub_category"]
        print(keyword)
        return render(request, 'dmm/search.html')
    print("is not valid")
    return render(request, 'dmm/search.html')
'''
    if request.method == "POST":
        keyword = request.POST.get('search')
        twitter = request.POST.get('twitter')
        gplus = request.POST.get('gplus')
        tumblr = request.POST.get('tumblr')
        main_category = request.POST.get('Main_Category')
        sub_category = request.POST.get('Sub_Category')

        ml_out = ml.ml_func(main_category, sub_category)


        if gplus!= None:
            gplus_data = services.g_plus_data(keyword)
            gplus_max = (max(gplus_data['Likes']) + max(gplus_data['Shares']))
            gplus_min = (min(gplus_data['Likes']) + min(gplus_data['Shares']))
            for i in range(0, (len(gplus_data['Likes']))):
                gplus_data['coefficient'][i] = convert.normalize(((gplus_data['Likes'][i])+(gplus_data['Shares'][i])), (int(sub_category) - 9),
                                                                 int(sub_category), gplus_min, gplus_max)

            for i, j, k, l, m, n in zip(gplus_data['Username'], gplus_data['Likes'],
                                  gplus_data['Shares'], gplus_data['coefficient'], gplus_data['url'], gplus_data['user_url']):
                p = models.Posts_data.objects.create(site='Google Plus', username=i, likes=int(j),
                                                     shares=int(k), coefficient=float(l), url=m,
                                                     ml_out=ml_out[0], user_url = n)

                p.save()




        if twitter!= None:
            twitter_data = services.get_twitter_data(keyword)
            twitter_max = (max(twitter_data['Likes']) + max(twitter_data['Shares']))
            twitter_min = (min(twitter_data['Likes']) + min(twitter_data['Shares']))
            for i in range(0, (len(twitter_data['Likes']))):
                twitter_data['coefficient'][i] = convert.normalize((twitter_data['Likes'][i]+(twitter_data['Shares'][i])), (int(sub_category) - 9),
                                                                   int(sub_category), twitter_min, twitter_max)

            for i, j, k, l, m, n in zip(twitter_data['Username'], twitter_data['Likes'],
                                  twitter_data['Shares'], twitter_data['coefficient'], twitter_data['url'], twitter_data['user_url']):
                p = models.Posts_data(site='Twitter', username=i, likes=j, shares=k,
                                      coefficient=l, ml_out=ml_out[0], url=m, user_url=n)
                p.save()


        if tumblr!= None:
            tumblr_data = services.get_tumblr_data(keyword)
            tumblr_max = max(tumblr_data['Likes'])
            tumblr_min = min(tumblr_data['Likes'])
            for i in range(0, (len(tumblr_data['Likes']))):
                tumblr_data['coefficient'][i] = convert.normalize(tumblr_data['Likes'][i], (int(sub_category) - 9),
                                                                  int(sub_category), tumblr_min, tumblr_max)

            for i, j, l, m, n in zip(tumblr_data['Username'], tumblr_data['Likes'],
                               tumblr_data['coefficient'], tumblr_data['url'], tumblr_data['user_url']):
                p = models.Posts_data(site='Tumblr', username=i, likes=j, shares=0,
                                      coefficient=l, ml_out=ml_out[0], url=m, user_url=n)

                p.save()


        posts = models.Posts_data.objects.filter(ml_out= ml_out[0])



        return render(request, 'dmm/results.html',{'post': posts})
    else:
        return render(request, 'dmm/search.html')

def about_us(request):
    return render(request, 'dmm/about_us.html')

'''
# Dropdowns view functions

#for main category
@api_view(['GET'])
@csrf_exempt
def get_main_category(request):
    main_cat_obj = models.Main_Category.objects.all()
    main_cat_serializer = serializers.MainCategorySerializer(main_cat_obj, many=True)
    response = Response(main_cat_serializer.data)
    return Response(response.data, status= status.HTTP_200_OK)

#for sub category
@api_view(['GET'])
@csrf_exempt
def get_sub_category(request,m_id):
    sub_cat_obj = models.Sub_Category.objects.filter(main_category_model=m_id)
    sub_cat_serializer = serializers.MainCategorySerializer(sub_cat_obj, many=True)
    response = Response(sub_cat_serializer.data)
    return Response(response.data, status=status.HTTP_200_OK)
'''