# -*- coding: UTF-8 -*-

from os import environ
from peewee import MySQLDatabase, Model, IntegerField, CharField, TextField
from peewee import DateTimeField, SmallIntegerField, FixedCharField
from peewee import ForeignKeyField, FloatField

db = MySQLDatabase("infop7db", user="root",
        password=environ["INFOP7_MYSQL_PASSWORD"])

class BaseModel(Model):
    class Meta:
        database = db

class Cursus(BaseModel):
    short_name = FixedCharField(max_length=2)
    name = CharField(max_length=16)
    description = TextField()
    responsable_id = IntegerField(null=True)

class Course(BaseModel):
    class Meta:
        table_name = "courses"

    cursus = ForeignKeyField(Cursus, null=True)
    semester = SmallIntegerField(default=0)
    name = CharField(max_length=64)
    short_name = CharField(max_length=16)
    ECTS = FloatField(default=3)
    description = TextField()
    use_latex = SmallIntegerField(default=0)
    use_sourcecode = SmallIntegerField(default=1)
    deleted = SmallIntegerField(default=0)

class ContentType(BaseModel):
    class Meta:
        table_name = "content_types"

    name = CharField(max_length=32)
    short_name = CharField(max_length=16)
    access_rights = SmallIntegerField(default=0)

class Content(BaseModel):
    class Meta:
        table_name = "contents"

    author_id = IntegerField(null=True)
    content_type = ForeignKeyField(ContentType, null=True)
    access_rights = SmallIntegerField(default=0)
    validated = SmallIntegerField(default=0)
    title = CharField(max_length=255, null=True)
    text = TextField()
    cursus = ForeignKeyField(Cursus, null=True)
    course = ForeignKeyField(Course, null=True)
    year = IntegerField(null=True)
    deleted = SmallIntegerField(default=0)
    created_at = DateTimeField(null=True)
    updated_at = DateTimeField(null=True)

class File(BaseModel):
    class Meta:
        table_name = "files"

    author_id = IntegerField(null=True)
    title = CharField(max_length=128)
    date = DateTimeField()
    description = CharField(max_length=255, null=True)
    file_type = SmallIntegerField()
    path = CharField(max_length=255)
    access_rights = SmallIntegerField(default=0)
    downloads_count = SmallIntegerField(default=0)
    deleted = SmallIntegerField(default=0)

class ContentFile(BaseModel):
    class Meta:
        table_name = "contents_files"
        primary_key = False

    content = ForeignKeyField(Content, backref="files")
    file = ForeignKeyField(File, backref="contents")


def assert_schema_ok():
    for table in (
        Cursus, Course, Content, File, ContentFile,
    ):
        table.get()

assert_schema_ok()
