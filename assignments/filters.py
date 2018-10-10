import django_filters

from vocabs.models import SkosConcept
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
    text_id__participant_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Participant.objects.all(),
        help_text=Text._meta.get_field('participant_id').help_text,
        label=Text._meta.get_field('participant_id').verbose_name
        )
    text_id__grade = django_filters.RangeFilter()
    text_id__medium = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__icontains="text_medium"),
        help_text=Text._meta.get_field('medium').help_text,
        label=Text._meta.get_field('medium').verbose_name
        )
    text_id__mode = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__icontains="text_mode"),
        help_text=Text._meta.get_field('mode').help_text,
        label=Text._meta.get_field('mode').verbose_name
        )
    text_id__text_type = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__icontains="text_type"),
        help_text=Text._meta.get_field('text_type').help_text,
        label=Text._meta.get_field('text_type').verbose_name
        )

    class Meta:
        model = TextVersion
        fields = "__all__"


class LearnerListFilter(django_filters.FilterSet):

    class Meta:
        model = Learner
        fields = "__all__"


class LearnerProfileListFilter(django_filters.FilterSet):

    class Meta:
        model = LearnerProfile
        fields = "__all__"


class CourseGroupListFilter(django_filters.FilterSet):

    class Meta:
        model = CourseGroup
        fields = "__all__"


class ParticipantListFilter(django_filters.FilterSet):

    class Meta:
        model = Participant
        fields = "__all__"
