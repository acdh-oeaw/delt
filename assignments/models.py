from django.db import models
from django.urls import reverse
from idprovider.models import IdProvider
from vocabs.models import SkosConcept

GENDER_CHOICES = (
    ('male', 'male'),
    ('female', 'female'),
    ('other', 'other'),
)
TEXT_SOURCE = (
    ('born_digital', 'born_digital'),
    ('hw_manuscript', 'hw_manuscript'),
    ('recording_audio', 'recording_audio'),
)

YES_NO_OTHER = (
    ('yes', 'yes'),
    ('no', 'no'),
    ('other', 'other'),
    ('unknown', 'unknown'),
)

SEMESTER = (
    ('W', 'W'),
    ('S', 'S'),
)


class Person(IdProvider):
    name = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Pseudonym",
        help_text="some random name"
    )


class Institution(IdProvider):
    name = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="name",
        help_text="The institution's name"
    )


class Place(IdProvider):
    name = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="name",
        help_text="The place's name"
    )


class AssignmentBaseClass(IdProvider):
    legacy_id = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Legacy ID"
    )
    entered_by = models.ForeignKey(
        Person, null=True, blank=True,
        help_text="Person who entered Assignment",
        related_name="has_entered_assignment",
        on_delete=models.SET_NULL
    )
    entered_date = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True,
        verbose_name="Enter Date",
        help_text="YYYY-MM-DD"
    )
    last_changed = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True,
        verbose_name="last changed",
        help_text="YYYY-MM-DD"
    )
    notes = models.TextField(
        blank=True, null=True, verbose_name="Learners Note",
        help_text="provide some"
    )


class Assignment(AssignmentBaseClass):
    title = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Title of Assignment"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Description of Assignment"
    )
    assignment_desc_link = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="File name of related Binary"
    )

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        ordering = ['id']
        verbose_name = "Assignment"

    @classmethod
    def get_listview_url(self):
        return reverse('assignments:browse_assignments')

    @classmethod
    def get_createview_url(self):
        return reverse('assignments:assignment_create')

    def get_next(self):
        next = Assignment.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = Assignment.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False

    def get_absolute_url(self):
        return reverse(
            'assignments:assignment_detail', kwargs={'pk': self.id}
        )

    def __str__(self):
        if self.title:
            return "{}".format(self.title)
        else:
            return "{}".format(self.id)


class Learner(AssignmentBaseClass):
    year_of_birth = models.IntegerField(
        blank=True, null=True, verbose_name="Year of Birth",
        help_text="provide some"
    )
    gender = models.CharField(
        max_length=250, blank=True, verbose_name="gender",
        help_text="provide some",
        choices=GENDER_CHOICES
    )
    nationality = models.ForeignKey(
        Place, null=True, blank=True,
        help_text="nationality",
        related_name="has_persons",
        on_delete=models.SET_NULL
    )
    lang_l = models.ForeignKey(
        SkosConcept, null=True, blank=True,
        verbose_name="lang_L1",
        help_text="provide some",
        related_name="is_lang_l_of",
        on_delete=models.SET_NULL
    )
    lang_mother = models.ForeignKey(
        SkosConcept, null=True, blank=True,
        verbose_name="lang_mother",
        help_text="provide some",
        related_name="is_mother_lang_of",
        on_delete=models.SET_NULL
    )
    lang_father = models.ForeignKey(
        SkosConcept, null=True, blank=True,
        verbose_name="lang_father",
        help_text="provide some",
        related_name="is_father_lang_of",
        on_delete=models.SET_NULL
    )
    lang_second = models.ForeignKey(
        SkosConcept, null=True, blank=True,
        verbose_name="lang_second",
        help_text="provide some",
        related_name="is_second_lang_of",
        on_delete=models.SET_NULL
    )
    lang_third = models.ForeignKey(
        SkosConcept, null=True, blank=True,
        verbose_name="lang_third",
        help_text="provide some",
        related_name="is_third_lang_of",
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return "{}".format(self.id)


class LearnerProfile(AssignmentBaseClass):
    learner_id = models.ForeignKey(
        Learner, null=True, blank=True,
        help_text="learner_id",
        related_name="has_learner_profile",
        on_delete=models.SET_NULL
    )
    year = models.IntegerField(
        blank=True, null=True,
        verbose_name="Year of Learner Profile",
        help_text="provide some"
    )
    lang_spoken_home = models.CharField(
        null=True, blank=True, max_length=250,
        verbose_name="lang_spoken@home",
        help_text="provide some"
    )
    lang_instruction_primary = models.ForeignKey(
        SkosConcept, null=True, blank=True,
        verbose_name="lang_instruction_primary",
        help_text="provide some",
        related_name="is_lang_instruction_primary",
        on_delete=models.SET_NULL
    )
    lang_instruction_secondary = models.ForeignKey(
        SkosConcept, null=True, blank=True,
        verbose_name="lang_instruction_secondary",
        help_text="provide some",
        related_name="is_lang_instruction_secondary",
        on_delete=models.SET_NULL
    )
    clil_years_learner_profile = models.IntegerField(
        blank=True, null=True,
        verbose_name="clil_years_learner_profile",
        help_text="provide some"
    )
    clil_subjects_learner_profile = models.CharField(
        null=True, blank=True, max_length=250,
        verbose_name="clil_subjects_learner_profile",
        help_text="provide some"
    )
    english_school = models.IntegerField(
        blank=True, null=True,
        verbose_name="english_school",
        help_text="provide some"
    )
    english_university = models.IntegerField(
        blank=True, null=True,
        verbose_name="english_university",
        help_text="provide some"
    )
    english_other = models.IntegerField(
        blank=True, null=True,
        verbose_name="english_other",
        help_text="provide some"
    )


class CourseGroup(AssignmentBaseClass):
    course_type = models.ForeignKey(
        SkosConcept, null=True, blank=True,
        verbose_name="course type ('COURSE_ID')",
        help_text="provide some",
        related_name="is_course_type_of",
        on_delete=models.SET_NULL
    )
    course_name = models.CharField(
        max_length=250, blank=True, null=True,
        verbose_name="group_course_name", help_text="provide some"
    )
    course_description = models.TextField(
        blank=True, null=True,
        verbose_name="group_course_desc", help_text="provide some"
    )
    participants_no = models.IntegerField(
        blank=True, null=True,
        verbose_name="participants_no",
        help_text="provide some"
    )
    school_studies_year = models.IntegerField(
        blank=True, null=True,
        verbose_name="school_studies_year",
        help_text="provide some"
    )
    teacher_lecturer = models.ManyToManyField(
        Person, blank=True, verbose_name="teacher_lecturer",
        help_text="provide some",
        related_name="has_group"
    )
    group_notes = models.TextField(
        blank=True, null=True,
        verbose_name="group_notes", help_text="provide some"
    )


INSTITUTION_LEVEL = (
    ('LS', 'LS'),
    ('TU', 'TU'),
    ('US', 'US')
)


class Participant(AssignmentBaseClass):
    learner_id = models.ForeignKey(
        Learner, null=True, blank=True,
        verbose_name="learner_id",
        help_text="provide some",
        related_name="has_learner",
        on_delete=models.SET_NULL
    )
    learner_profile_id = models.ForeignKey(
        LearnerProfile, null=True, blank=True,
        verbose_name="learner_profile_id",
        help_text="provide some",
        related_name="has_learner",
        on_delete=models.SET_NULL
    )
    group_id = models.ForeignKey(
        CourseGroup, null=True, blank=True,
        verbose_name="GROUP_ID",
        help_text="provide some",
        related_name="has_participant",
        on_delete=models.SET_NULL
    )
    institution_id = models.ForeignKey(
        Institution, null=True, blank=True,
        verbose_name="Institution",
        help_text="provide some",
        related_name="has_participant",
        on_delete=models.SET_NULL
    )
    institution_level = models.CharField(
        max_length=250, blank=True, verbose_name="institution_level",
        help_text="provide some",
        choices=INSTITUTION_LEVEL
    )
    clil = models.CharField(
        max_length=250, blank=True, verbose_name="clil",
        help_text="provide some",
        choices=YES_NO_OTHER
    )

    def __str__(self):
        return "{}".format(self.learner_id)


class Text(AssignmentBaseClass):
    participant_id = models.ForeignKey(
        Participant, null=True, blank=True,
        verbose_name="participant_id",
        help_text="provide some",
        related_name="text_has_participants",
        on_delete=models.SET_NULL
    )
    text_type = models.ForeignKey(
        SkosConcept, null=True, blank=True,
        verbose_name="TEXT_TYPE_ID",
        help_text="provide some",
        related_name="is_text_type_of",
        on_delete=models.SET_NULL
    )
    assignment_id = models.ForeignKey(
        Assignment, null=True, blank=True,
        verbose_name="assignment_id",
        help_text="provide some",
        related_name="has_text",
        on_delete=models.SET_NULL
    )
    availability = models.CharField(
        max_length=250, blank=True, verbose_name="availability",
        help_text="provide some",
        choices=YES_NO_OTHER
    )
    year = models.IntegerField(
        blank=True, null=True, verbose_name="Year of Text",
        help_text="provide some"
    )
    semester = models.CharField(
        max_length=250, blank=True, verbose_name="text_semester",
        help_text="provide some",
        choices=SEMESTER
    )
    lang = models.ForeignKey(
        SkosConcept, null=True, blank=True,
        verbose_name="text_lang",
        help_text="provide some",
        related_name="is_text_lang",
        on_delete=models.SET_NULL
    )
    medium = models.ForeignKey(
        SkosConcept, null=True, blank=True,
        verbose_name="text_medium",
        help_text="provide some",
        related_name="is_text_medium",
        on_delete=models.SET_NULL
    )
    data_type = models.ForeignKey(
        SkosConcept, null=True, blank=True,
        verbose_name="data_type",
        help_text="provide some",
        related_name="is_data_type",
        on_delete=models.SET_NULL
    )
    recording = models.ForeignKey(
        SkosConcept, null=True, blank=True,
        verbose_name="recording",
        help_text="provide some",
        related_name="is_recording",
        on_delete=models.SET_NULL
    )
    recoding_method = models.ForeignKey(
        SkosConcept, null=True, blank=True,
        verbose_name="recoding_method",
        help_text="provide some",
        related_name="is_recoding_method",
        on_delete=models.SET_NULL
    )
    mode = models.ForeignKey(
        SkosConcept, null=True, blank=True,
        verbose_name="text_mode",
        help_text="provide some",
        related_name="is_text_mode",
        on_delete=models.SET_NULL
    )
    clil_text = models.CharField(
        max_length=250, blank=True, verbose_name="clil_text",
        help_text="provide some",
        choices=YES_NO_OTHER
    )
    clil_subject = models.ForeignKey(
        SkosConcept, null=True, blank=True,
        verbose_name="clil_subject",
        help_text="provide some",
        related_name="is_clil_subject",
        on_delete=models.SET_NULL
    )
    timed = models.CharField(
        max_length=250, blank=True, verbose_name="timed",
        help_text="provide some",
        choices=YES_NO_OTHER
    )
    exam = models.CharField(
        max_length=250, blank=True, verbose_name="exam",
        help_text="provide some",
        choices=YES_NO_OTHER
    )
    planning_time = models.CharField(
        max_length=250, blank=True, verbose_name="planning_time",
        help_text="provide some",
        choices=YES_NO_OTHER
    )
    tool = models.CharField(
        max_length=250, blank=True, verbose_name="tool",
        help_text="provide some",
        choices=YES_NO_OTHER
    )
    grade = models.IntegerField(
        blank=True, null=True, verbose_name="text_grade",
        help_text="provide some"
    )
    title = models.CharField(
        max_length=250, blank=True, verbose_name="text_title",
        help_text="provide some"
    )
    source = models.CharField(
        max_length=250, blank=True, verbose_name="text_source",
        help_text="provide some"
    )
    transcriber = models.ForeignKey(
        Person, null=True, blank=True,
        help_text="transcriber",
        related_name="has_transcribed_text",
        on_delete=models.SET_NULL
    )

    class Meta:
        ordering = ['id']
        verbose_name = "Text"

    @classmethod
    def get_listview_url(self):
        return reverse('assignments:browse_texts')

    @classmethod
    def get_createview_url(self):
        return reverse('assignments:text_create')

    def get_next(self):
        next = Text.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = Text.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False

    def get_absolute_url(self):
        return reverse(
            'assignments:text_detail', kwargs={'pk': self.id}
        )

    def __str__(self):
        if self.text_type:
            return "{}".format(self.text_type)
        else:
            return "{}".format(self.id)


class TextVersion(AssignmentBaseClass):
    text_id = models.ForeignKey(
        Text, null=True, blank=True,
        verbose_name="text_id",
        help_text="provide some",
        related_name="has_text_version",
        on_delete=models.SET_NULL
    )
    status = models.ForeignKey(
        SkosConcept, null=True, blank=True,
        verbose_name="text_version_status",
        help_text="provide some",
        related_name="is_text_version_status",
        on_delete=models.SET_NULL
    )
    link = models.CharField(
        max_length=250, blank=True, verbose_name="text_version_link",
        help_text="provide some"
    )
    content = models.TextField(
        blank=True, null=True, verbose_name="text_content",
        help_text="provide some"
    )

    class Meta:
        ordering = ['id']
        verbose_name = "TextVersion"

    @classmethod
    def get_listview_url(self):
        return reverse('assignments:browse_textversions')

    @classmethod
    def get_createview_url(self):
        return reverse('assignments:textversion_create')

    def get_next(self):
        next = TextVersion.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = TextVersion.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False

    def get_absolute_url(self):
        return reverse(
            'assignments:textversion_detail', kwargs={'pk': self.id}
        )

    def __str__(self):
        if self.status:
            return "{}".format(self.status)
        else:
            return "{}".format(self.id)
