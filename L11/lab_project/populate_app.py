import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lab_project.settings")
import django
django.setup()
from app.models import Topic, WebPage, AccessRecord
from faker import Faker
import random


fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top = add_topic()

        fake_url = fakegen.url()
        fake_name = fakegen.company()
        fake_date = fakegen.date()

        webpg = WebPage.objects.get_or_create(
            topic=top, name=fake_name, URL=fake_url)[0]
        webpg.save()

        acc_rec = AccessRecord.objects.get_or_create(
            name=webpg, date=fake_date)[0]
        acc_rec.save()

if __name__ == '__main__':
    print("Populating script!")
    populate(10)
    print("Populating complete!")
