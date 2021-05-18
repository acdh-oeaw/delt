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
        args=[A('pk')], verbose_name='Column ID'
    )
    status = tables.LinkColumn(
        'assignments:textversion_detail',
        args=[A('pk')], verbose_name='Status'
    )
    Grade = tables.TemplateColumn(
        template_name='assignments/tables/text_id__grade.html',
        verbose_name="Grade"
    )
    Medium = tables.TemplateColumn(
        template_name='assignments/tables/text_id__medium.html',
        verbose_name=Text._meta.get_field('medium').verbose_name
    )
    content = tables.TemplateColumn(
        template_name='assignments/tables/content.html',
        verbose_name=TextVersion._meta.get_field('content').verbose_name
    )
    text_id__mode = tables.TemplateColumn(
        template_name='assignments/tables/text_id__mode.html',
        verbose_name=Text._meta.get_field('mode').verbose_name
    )
    text_id__text_type = tables.TemplateColumn(
        template_name='assignments/tables/text_id__text_type.html',
        verbose_name=Text._meta.get_field('text_type').verbose_name
    )
    Text = tables.TemplateColumn(
        template_name='assignments/tables/plaintext.html',
        verbose_name="Text without Markup",
    )
    Assignment = tables.TemplateColumn(
        template_name='assignments/tables/text_id__assignment.html',
        verbose_name=Assignment._meta.get_field('title').verbose_name
    )
    Participant_Institution_Level= tables.TemplateColumn(
        template_name='assignments/tables/text_id__participant_institution_level.html',
        verbose_name=Participant._meta.get_field('institution_level').verbose_name
    )
    Participant_clil= tables.TemplateColumn(
        template_name='assignments/tables/text_id__participant_clil.html',
        verbose_name=Participant._meta.get_field('clil').verbose_name
    )
    Learner_Gender = tables.TemplateColumn(
        template_name='assignments/tables/text_id__learner_gender.html',
        verbose_name=Learner._meta.get_field('gender').verbose_name
    )
    Learner_Nationality = tables.TemplateColumn(
        template_name='assignments/tables/text_id__learner_nationality.html',
        verbose_name=Learner._meta.get_field('nationality').verbose_name
    )
    Learner_Mother_Tongue = tables.TemplateColumn(
        template_name='assignments/tables/text_id__learner_lang_l.html',
        verbose_name=Learner._meta.get_field('lang_l').verbose_name
    )
    Learner_Mother = tables.TemplateColumn(
        template_name='assignments/tables/text_id__learner_lang_mother.html',
        verbose_name=Learner._meta.get_field('lang_mother').verbose_name
    )
    Learner_Father = tables.TemplateColumn(
        template_name='assignments/tables/text_id__learner_lang_father.html',
        verbose_name=Learner._meta.get_field('lang_father').verbose_name
    )
    Learner_Second_Language= tables.TemplateColumn(
        template_name='assignments/tables/text_id__learner_lang_second.html',
        verbose_name=Learner._meta.get_field('lang_second').verbose_name
    )
    Learner_Third_Language= tables.TemplateColumn(
        template_name='assignments/tables/text_id__learner_lang_third.html',
        verbose_name=Learner._meta.get_field('lang_third').verbose_name
    )
    Learner_Profile_Language_Spoken_Home= tables.TemplateColumn(
        template_name='assignments/tables/text_id__learner_profile_lang_spoken_home.html',
        verbose_name=LearnerProfile._meta.get_field('lang_spoken_home').verbose_name
    )
    Learner_Profile_Language_Instruction_Primary= tables.TemplateColumn(
        template_name='assignments/tables/text_id__learner_profile_lang_instruction_primary.html',
        verbose_name=LearnerProfile._meta.get_field('lang_instruction_primary').verbose_name
    )
    Learner_Profile_Proficiency_Level= tables.TemplateColumn(
        template_name='assignments/tables/text_id__learner_profile_proficiency_level.html',
        verbose_name=LearnerProfile._meta.get_field('proficiency_level').verbose_name
    )
    Plain_Text = tables.TemplateColumn(
        template_name='assignments/tables/text_id__plain_text.html',
        verbose_name='Plain Text'
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
