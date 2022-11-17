import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'level_two_project.settings')

import django
# Import settings
django.setup()

# import random
from second_app.models import User
from faker import Faker
def populate_data(N=5):
    for _ in range(N):

        u = User(first_name=first_name,last_name=last_name,email_id=email_id)
        u.save()
    print('completed')

# fakegen = Faker()
# topics = ['Search','Social','Marketplace','News','Games']

# def add_topic():
#     t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
#     t.save()
#     return t
def populate(N):
    pass
fakegen = Faker()
# userdata = User()

first_name = fakegen.first_name()
last_name = fakegen.last_name()
email_id = fakegen.email()

def populate_data(N=5):
    for _ in range(N):

        uii = User.objects.get_or_create(first_name=fakegen.first_name(),last_name=fakegen.last_name(),email_id=fakegen.email())[0]
    print('completed')




# def populate(N=5):
#     '''
#     Create N Entries of Dates Accessed
#     '''

#     for entry in range(N):

#         # Get Topic for Entry
#         top = add_topic()

#         # Create Fake Data for entry
#         fake_url = fakegen.url()
#         fake_date = fakegen.date()
#         fake_name = fakegen.company()

#         # Create new Webpage Entry
#         webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

#         # Create Fake Access Record for that page
#         # Could add more of these if you wanted...
#         accRec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate_data(20)
    print('Populating Complete')