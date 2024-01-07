from django.shortcuts import render
from .models import *
import requests


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def news(request):
    def parse():
        url = 'https://api.vk.com/method/wall.get'

        params = {
            'access_token': '7c70b8fa7c70b8fa7c70b8fa0c7f65406877c707c70b8fa195c92061d633e811838ec2c',
            'v': '5.154',
            'domain': 'greensailnn',
            'count': 10
        }

        response = requests.get(url=url, params=params)

        data = response.json()['response']['items']
        _id = []
        post_hash = []
        owner_id = []
        post_id = []
        for item in data:
            _id.append(f'vk_post_{str(item['owner_id'])}_{str(item['id'])}')
            post_hash.append(item['hash'])
            owner_id.append(item['owner_id'])
            post_id.append(item['id'])
        return zip(_id, post_hash, owner_id, post_id)
    context = {'post_params': parse()}
    return render(request, 'main/news.html', context)


def mugs(request):
    all_mugs = Mugs.objects.order_by('teacher')

    about = [f'{curr_mug.description[:250]}...' if len(curr_mug.description) > 250
             else curr_mug.description for curr_mug in all_mugs]

    context = {'mugs': zip(all_mugs, about)}

    return render(request, 'main/mugs.html', context)


def history(request):
    return render(request, 'main/history.html')


def teachers(request):
    all_teachers = Teacher.objects.order_by('bio')

    about = [f'{curr_teacher.about[:250]}...' if len(curr_teacher.about) > 250
             else curr_teacher.about for curr_teacher in all_teachers]

    context = {'teachers': zip(all_teachers, about)}

    return render(request, 'main/teachers.html', context)


def mug(request, mug_id):
    current_mug = Mugs.objects.get(id=mug_id)
    mug_photos = MugsPhotos.objects.filter(mug_id=mug_id)
    context = {'mug': current_mug, 'mug_photos': mug_photos}

    return render(request, 'main/mug.html', context)


def certificate(request):
    return render(request, 'main/certificate.html')


def teacher(request, teacher_id):
    current_teacher = Teacher.objects.get(id=teacher_id)

    context = {'teacher': current_teacher}

    return render(request, 'main/teacher.html', context)


def masterclasses(request):
    all_masterclasses = Masterclasses.objects.order_by('title')

    description = [f'{curr_masterclass.description[:250]}...' if len(curr_masterclass.description) > 250
                   else curr_masterclass.description for curr_masterclass in all_masterclasses]

    context = {'masterclasses': zip(all_masterclasses, description)}

    return render(request, 'main/masterclasses.html', context)


def masterclass(request, masterclass_id):
    current_masterclass = Masterclasses.objects.get(id=masterclass_id)

    context = {'masterclass': current_masterclass}

    return render(request, 'main/masterclass.html', context)


def contests(request):
    all_contests = Contests.objects.order_by('title')

    description = [f'{curr_contest.description[:250]}...' if len(curr_contest.description) > 250
                   else curr_contest.description for curr_contest in all_contests]

    context = {'masterclasses': zip(all_contests, description)}

    return render(request, 'main/contests.html', context)


def contest(request, contest_id):
    current_contest = Contests.objects.get(id=contest_id)

    context = {'contest': current_contest}

    return render(request, 'main/contest.html', context)
