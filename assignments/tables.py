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
    legacy_id = tables.LinkColumn(
        'assignments:textversion_detail',
        args=[A('pk')], verbose_name='Legacy ID'
    )
    status = tables.LinkColumn(
        'assignments:textversion_detail',
        args=[A('pk')], verbose_name='Status'
    )

    forename = tables.Column()

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
