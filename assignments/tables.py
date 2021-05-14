import django_tables2 as tables
from django_tables2.utils import A
from assignments.models import *


class AssignmentTable(tables.Table):
    title = tables.LinkColumn(
        'assignments:assignment_detail',
        args=[A('pk')], verbose_name='Title'
    )
    description = tables.LinkColumn(
        'assignments:assignment_detail',
        args=[A('pk')], verbose_name='Description'
    )
    forename = tables.Column()

    class Meta:
        model = Assignment
        sequence = (
            'id',
            'title',
            'description',
        )
        attrs = {"class": "table table-responsive table-hover"}


class TextTable(tables.Table):
    legacy_id = tables.LinkColumn(
        'assignments:text_detail',
        args=[A('pk')], verbose_name='Legacy ID'
    )
    text_type = tables.LinkColumn(
        'assignments:text_detail',
        args=[A('pk')], verbose_name='Text Type'
    )

    forename = tables.Column()

    class Meta:
        model = Text
        sequence = (
            'legacy_id',
            'text_type',
        )
        attrs = {"class": "table table-responsive table-hover"}


class TextVersionTable(tables.Table):
    text_id = tables.ManyToManyColumn()
    legacy_id = tables.LinkColumn(
        'assignments:textversion_detail',
        args=[A('pk')], verbose_name='ID'
    )
    status = tables.LinkColumn(
        'assignments:textversion_detail',
        args=[A('pk')], verbose_name='Status'
    )
    text_id__grade = tables.TemplateColumn(
        template_name='assignments/tables/text_id__grade.html',
    )
    text_id__medium = tables.TemplateColumn(
        template_name='assignments/tables/text_id__medium.html',
        verbose_name=Text._meta.get_field('medium').verbose_name
    )
    text_id__mode = tables.TemplateColumn(
        template_name='assignments/tables/text_id__mode.html',
        verbose_name=Text._meta.get_field('mode').verbose_name
    )
    text_id__text_type = tables.TemplateColumn(
        template_name='assignments/tables/text_id__text_type.html',
        verbose_name=Text._meta.get_field('text_type').verbose_name
    )
    content_plain = tables.TemplateColumn(
        template_name='assignments/tables/plaintext.html',
        verbose_name="Text ohne Markup"
    )
    Assignment = tables.TemplateColumn(
        template_name='assignments/tables/text_id__assignment.html',
        verbose_name=Assignment._meta.get_field('title').verbose_name
    )

    class Meta:
        model = TextVersion
        sequence = (
            'legacy_id',
            'status',
        )
        attrs = {"class": "table table-responsive table-hover"}


class LearnerTable(tables.Table):
    id = tables.LinkColumn()

    class Meta:
        model = Learner
        sequence = (
            'id',
            'year_of_birth',
            'gender',
        )
        attrs = {"class": "table table-responsive table-hover"}


class LearnerProfileTable(tables.Table):
    id = tables.LinkColumn()

    class Meta:
        model = LearnerProfile
        sequence = (
            'id',
        )
        attrs = {"class": "table table-responsive table-hover"}


class CourseGroupTable(tables.Table):
    id = tables.LinkColumn()

    class Meta:
        model = CourseGroup
        sequence = (
            'id',
        )
        attrs = {"class": "table table-responsive table-hover"}


class ParticipantTable(tables.Table):
    id = tables.LinkColumn()

    class Meta:
        model = Participant
        sequence = (
            'id',
        )
        attrs = {"class": "table table-responsive table-hover"}
