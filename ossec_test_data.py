import random

from django.db import transaction

from ossec_api.api import models
from ossec_api.api.db_routers import DJANGO_DB_NAME


with transaction.atomic(using=DJANGO_DB_NAME):
    s = models.Server(last_contact=0, version='v3.3.0', hostname='arm', information='Linux arm - OSSEC HIDS v3.3.0')
    s.save()

    locations = [
        'arm->/var/log/auth.log',
        'arm->/var/log/syslog',
        '(arm2) 192.168.1.1->/var/log/auth.log',
        '(arm2) 192.168.1.1->/var/log/syslog'
    ]

    locations_orm = []

    for i in locations:
        l = models.Location(server_id=s.id, name=i)
        l.save()
        locations_orm.append(l)

    categories = [
        'syslog',
        'firewall',
        'ids',
        'pam',
        'sshd',
        'apache',
        'virus',
        'authentication_failures',
        'rootcheck'
    ]

    categories_orm = []

    for i, name in enumerate(categories):
        c = models.Category(cat_id=i, cat_name=name)
        c.save()
        categories_orm.append(c)

    signatures_categories_orm = []

    for i in range(10):
        r = random.randint(0, len(categories_orm) - 1)
        while True:
            s_c = models.SignatureCategoryMapping(rule_id=i, category=categories_orm[r])
            s_c.save()
            signatures_categories_orm.append(s_c)
            if r <= 1:
                break
            r = random.randint(0, r - 1)

    _rand_users = [
        'root',
        'admin',
        'joe'
    ]

    utime = 1577836800
    for i in range(300):
        rnd_rule = random.randint(
            signatures_categories_orm[0].rule_id, signatures_categories_orm[len(signatures_categories_orm) - 1].rule_id
        )
        rnd_lvl = random.randint(1, 7)
        rnd_loc = random.randint(0, len(locations_orm) - 1)
        rnd_user = _rand_users[random.randint(0, len(_rand_users) - 1)]
        a = models.Alert(
            server_id=s.id,
            rule_id=rnd_rule,
            level=rnd_lvl,
            timestamp=utime,
            location=locations_orm[rnd_loc],
            user=rnd_user,
            full_log='event num {} from {}'.format(i, locations_orm[rnd_loc].name),
            is_hidden=0
        )
        a.save()
        if i % 5 == 0:
            utime += 500
