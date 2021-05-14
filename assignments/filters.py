import django_filters
from django import forms


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
    text_id__participant_id__learner_id__gender = django_filters.ChoiceFilter(
        choices=GENDER_CHOICES,
        help_text="Gender",
        label="Gender"
        )
    text_id__participant_id__institution_level = django_filters.ChoiceFilter(
        choices=[(x[0], x[0]) for x in list(set(Participant.objects.all().values_list('institution_level')))],
        help_text="Institution Level",
        label="Institution Level"
        )
    text_id__participant_id__clil = django_filters.ChoiceFilter(
        choices=YES_NO_OTHER,
        help_text="clil",
        label="clil"
        )

    text_id__participant_id__learner_id__nationality = django_filters.ModelMultipleChoiceFilter(
        queryset=Place.objects.all(),
        help_text="Nationality",
        label="Nationality"
        )
    text_id__participant_id__learner_id__lang_l = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.exclude(is_lang_l_of=None),
        help_text="mother tongue",
        label="mother tongue"
        )
    text_id__participant_id__learner_id__lang_mother = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.exclude(is_mother_lang_of=None),
        help_text="lang mother",
        label="lang mother"
        )
    text_id__participant_id__learner_id__lang_father = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.exclude(is_father_lang_of=None),
        help_text="lang father",
        label="lang father"
        )
    text_id__participant_id__learner_id__lang_second = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.exclude(is_second_lang_of=None),
        help_text="second language",
        label="second language ≠ foreign language"
        )
    text_id__participant_id__learner_id__lang_third = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.exclude(is_third_lang_of=None),
        help_text="third language",
        label="third language ≠ foreign language"
        )

    text_id__participant_id__learner_profile_id__lang_spoken_home = django_filters.ChoiceFilter(
        choices=[(x[0], x[0]) for x in list(set(LearnerProfile.objects.all().values_list('lang_spoken_home')))],
        help_text="(if more than one language is spoken, provide the % of use of each language)\
        format: Bosnian: 50% Slovenian: 50%",
        label="description of language use at home"
        )
    text_id__participant_id__learner_profile_id__lang_instruction_primary = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.exclude(is_lang_instruction_primary=None),
        help_text="Language of instruction in primary school",
        label="Language of instruction in primary school"
        )
    text_id__participant_id__learner_profile_id__proficiency_level = django_filters.ChoiceFilter(
        choices=[(x[0], x[0]) for x in list(set(LearnerProfile.objects.all().values_list('proficiency_level')))],
        help_text="A1;A2;B1;B2;C1;C2",
        label="Latest CEF score/placement"
        )

    text_id__grade = django_filters.RangeFilter()
    text_id__medium = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__icontains="text_medium"),
        help_text=Text._meta.get_field('medium').help_text,
        label=Text._meta.get_field('medium').verbose_name,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'chbx-select-multi'})
        )
    text_id__mode = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__icontains="text_mode"),
        help_text=Text._meta.get_field('mode').help_text,
        label=Text._meta.get_field('mode').verbose_name,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'chbx-select-multi'})
        )
    text_id__text_type = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__icontains="text_type"),
        help_text=Text._meta.get_field('text_type').help_text,
        label=Text._meta.get_field('text_type').verbose_name,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'chbx-select-multi'})
        )
    text_id__clil_text = django_filters.ChoiceFilter(
        choices=[(x[0], x[0]) for x in list(set(Text.objects.all().values_list('clil_text')))],
        help_text="(if more than one language is spoken, provide the % of use of each language)\
        format: Bosnian: 50% Slovenian: 50%",
        label="description of language use at home"
        )
    text_id__assignment_id__title = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Assignment._meta.get_field('title').help_text,
        label=Assignment._meta.get_field('title').verbose_name
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
