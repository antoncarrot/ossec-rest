# python3 manage.py inspectdb > models.py

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.postgres.fields import ArrayField


class Agent(models.Model):
    server_id = models.BigIntegerField()
    last_contact = models.BigIntegerField()
    ip_address = models.CharField(max_length=46)
    version = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    information = models.CharField(max_length=128)

    class Meta:
        app_label = 'ossec_data'
        managed = False
        db_table = 'agent'
        unique_together = (('id', 'server_id'),)


class Alert(models.Model):
    id = models.BigAutoField(primary_key=True)
    server_id = models.IntegerField()
    rule_id = models.BigIntegerField()
    level = models.SmallIntegerField(blank=True, null=True)
    timestamp = models.BigIntegerField()
    # location_id = models.IntegerField()
    location = models.ForeignKey(
        'Location', to_field='id', db_column='location_id', null=True, on_delete=models.SET_NULL, db_constraint=False
    )
    src_ip = models.CharField(max_length=46, blank=True, null=True)
    dst_ip = models.CharField(max_length=46, blank=True, null=True)
    src_port = models.IntegerField(blank=True, null=True)
    dst_port = models.IntegerField(blank=True, null=True)
    alertid = models.TextField(blank=True, null=True)
    user = models.TextField(blank=True, null=True)
    full_log = models.TextField()
    is_hidden = models.SmallIntegerField()
    tld = models.CharField(max_length=32)

    class Meta:
        app_label = 'ossec_data'
        managed = False
        db_table = 'alert'
        unique_together = (('id', 'server_id'),)


class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(unique=True, max_length=32)

    class Meta:
        app_label = 'ossec_data'
        managed = False
        db_table = 'category'


class Data(models.Model):
    id = models.BigIntegerField(primary_key=True)
    server_id = models.IntegerField()
    user = models.TextField()
    full_log = models.TextField()

    class Meta:
        app_label = 'ossec_data'
        managed = False
        db_table = 'data'
        unique_together = (('id', 'server_id'),)


class Location(models.Model):
    server_id = models.BigIntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        app_label = 'ossec_data'
        managed = False
        db_table = 'location'
        unique_together = (('id', 'server_id'),)


class Server(models.Model):
    last_contact = models.BigIntegerField()
    version = models.CharField(max_length=32)
    hostname = models.CharField(unique=True, max_length=64)
    information = models.TextField()

    class Meta:
        app_label = 'ossec_data'
        managed = False
        db_table = 'server'


class Signature(models.Model):
    rule_id = models.BigIntegerField(unique=True)
    level = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=255)

    class Meta:
        app_label = 'ossec_data'
        managed = False
        db_table = 'signature'


class SignatureCategoryMapping(models.Model):
    rule_id = models.BigIntegerField()
    # cat_id = models.IntegerField()
    category = models.ForeignKey(
        Category, to_field='cat_id', db_column='cat_id', null=True, on_delete=models.SET_NULL, db_constraint=False
    )

    class Meta:
        app_label = 'ossec_data'
        managed = False
        db_table = 'signature_category_mapping'
        # unique_together = (('id', 'rule_id', 'cat_id'),)
        unique_together = (('id', 'rule_id', 'category'),)


# Custom views from ossec_ext.sql


class RuleView(models.Model):
    rule_id = models.AutoField(primary_key=True)
    categories = ArrayField(models.CharField(max_length=32))

    class Meta:
        app_label = 'ossec_data'
        managed = False
        db_table = 'rule_view'


class CategoryView(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(unique=True, max_length=32)
    rules = ArrayField(models.BigIntegerField())

    class Meta:
        app_label = 'ossec_data'
        managed = False
        db_table = 'category_view'
