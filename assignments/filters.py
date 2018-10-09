import django_filters

from . models import *


class AssignmentListFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Assignment._meta.get_field('title').help_text,
        label=Assignment._meta.get_field('title').verbose_name
        )
    description = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Assignment._meta.get_field('description').help_text,
        label=Assignment._meta.get_field('description').verbose_name
        )

    class Meta:
        model = Assignment
        fields = "__all__"


class TextListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Text._meta.get_field('legacy_id').help_text,
        label=Text._meta.get_field('legacy_id').verbose_name
        )

    class Meta:
        model = Text
        fields = "__all__"


class TextVersionListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=TextVersion._meta.get_field('legacy_id').help_text,
        label=TextVersion._meta.get_field('legacy_id').verbose_name
        )

    class Meta:
        model = TextVersion
        fields = "__all__"


class LearnerListFilter(django_filters.FilterSet):

    class Meta:
        model = Learner
        fields = "__all__"
