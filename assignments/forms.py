from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,  Layout, Fieldset, Div, MultiField, HTML
from crispy_forms.bootstrap import Accordion, AccordionGroup

from . models import *


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(AssignmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class AssignmentFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(AssignmentFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'title',
                css_id="basic_search_fields"
                ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    'description',
                    css_id="more"
                    ),
                )
            )


class TextForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(TextForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class TextFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(TextFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                'text_type',
                css_id="basic_search_fields"
                ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    'legacy_id',
                    css_id="more"
                    ),
                )
            )


class TextVersionForm(forms.ModelForm):
    class Meta:
        model = TextVersion
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(TextVersionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class TextVersionFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(TextVersionFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Accordion(
                AccordionGroup(
                    'Text',
                    'text_id__medium',
                    'text_id__mode',
                    'text_id__text_type',
                    css_id="basic_search_fields"
                ),
            ),
            Accordion(
                AccordionGroup(
                    'Assignment',
                    'text_id__assignment_id',
                    'text_id__assignment_id__title',                    
                    css_id="assignment_id_title"
                )
            ),
            Accordion(
                AccordionGroup(
                    'Participant',
                    'text_id__participant_id__learner_id__nationality',
                    'text_id__participant_id__learner_id__gender',
                    'text_id__participant_id__institution_level',
                    'text_id__participant_id__clil',
                    css_id="participant_gen"
                    ),
                ),
            Accordion(
                AccordionGroup(
                    'Participant Language',
                    'text_id__participant_id__learner_id__lang_l',
                    'text_id__participant_id__learner_id__lang_mother',
                    'text_id__participant_id__learner_id__lang_father',
                    'text_id__participant_id__learner_id__lang_second',
                    'text_id__participant_id__learner_id__lang_third',
                    css_id="participant_lang"
                    ),
                ),
            Accordion(
                AccordionGroup(
                    'Learner Profile',
                    'text_id__participant_id__learner_profile_id__lang_spoken_home',
                    'text_id__participant_id__learner_profile_id__lang_instruction_primary',
                    'text_id__participant_id__learner_profile_id__proficiency_level',
                    css_id="learner_profile"
                    ),
                ),
            Accordion(
                AccordionGroup(
                    'CLIL',
                    'text_id__clil_text',
                    css_id="clil"
                    ),
                ),
            Accordion(
                AccordionGroup(
                    'internal',
                    'legacy_id',
                    css_id="internal"
                    ),
                )
            )


class LearnerForm(forms.ModelForm):
    class Meta:
        model = Learner
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(LearnerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class LearnerFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(LearnerFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'gender',
                css_id="basic_search_fields"
                ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    'nationality',
                    css_id="more"
                    ),
                )
            )


class LearnerProfileForm(forms.ModelForm):
    class Meta:
        model = LearnerProfile
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(LearnerProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class LearnerProfileFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(LearnerProfileFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'gender',
                css_id="basic_search_fields"
                ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    'nationality',
                    css_id="more"
                    ),
                )
            )


class CourseGroupForm(forms.ModelForm):
    class Meta:
        model = CourseGroup
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CourseGroupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class CourseGroupFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(CourseGroupFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'gender',
                css_id="basic_search_fields"
                ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    'nationality',
                    css_id="more"
                    ),
                )
            )


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ParticipantForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class ParticipantFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(ParticipantFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'gender',
                css_id="basic_search_fields"
                ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    'nationality',
                    css_id="more"
                    ),
                )
            )
