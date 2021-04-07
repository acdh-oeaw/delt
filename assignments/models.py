from django.db import models
from django.urls import reverse
from idprovider.models import IdProvider
from vocabs.models import SkosConcept
from browsing.browsing_utils import model_to_dict

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
    legacy_id = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Legacy ID"
    )


class Institution(IdProvider):
    name = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="name",
        help_text="The institution's name"
    )
    legacy_id = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Legacy ID"
    )


class Place(IdProvider):
    name = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="name",
        help_text="The place's name"
    )
    legacy_id = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Legacy ID"
    )

    def __str__(self):
        return f"{self.name}"


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

    def field_dict(self):
        return model_to_dict(self)


class Assignment(AssignmentBaseClass):

    """this table allows for the detailed description of specific assignments/tasks
    that were the prompts for the text production
    """

    title = models.CharField(
        max_length=250, blank=True,
        null=True, verbose_name="Title of Assignment",
        help_text="Short description of the assignment"
    )
    description = models.TextField(
        blank=True, null=True,
        verbose_name="Description of Assignment",
        help_text="Detailed description of the assignment"
    )
    assignment_desc_link = models.CharField(
        max_length=250, blank=True, null=True,
        verbose_name="possible PDF/Audio/... files"
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

    """background information about the learner"""

    year_of_birth = models.IntegerField(
        blank=True, null=True, verbose_name="Learner's year of birth",
        help_text="Learner's year of birth"
    )
    gender = models.CharField(
        max_length=250, blank=True, verbose_name="Learner's gender",
        help_text="Learner's gender",
        choices=GENDER_CHOICES
    )
    nationality = models.ForeignKey(
        Place, null=True, blank=True,
        verbose_name="Learner's nationality",
        help_text="Learner's nationality",
        related_name="has_persons",
        on_delete=models.SET_NULL
    )
    lang_l = models.ForeignKey(
        SkosConcept, null=True, blank=True,
        verbose_name="mother tongue",
        help_text="mother tongue",
        related_name="is_lang_l_of",
        on_delete=models.SET_NULL
    )
    lang_mother = models.ForeignKey(
        SkosConcept, null=True, blank=True,
        verbose_name="Mother's L1",
        help_text="Mother's L1",
        related_name="is_mother_lang_of",
        on_delete=models.SET_NULL
    )
    lang_father = models.ForeignKey(
        SkosConcept, null=True, blank=True,
        verbose_name="father's L1",
        help_text="father's L1",
        related_name="is_father_lang_of",
        on_delete=models.SET_NULL
    )
    lang_second = models.ForeignKey(
        SkosConcept, null=True, blank=True,
        verbose_name="second language",
        help_text="second language ≠ foreign language",
        related_name="is_second_lang_of",
        on_delete=models.SET_NULL
    )
    lang_third = models.ForeignKey(
        SkosConcept, null=True, blank=True,
        verbose_name="third language",
        help_text="third language ≠ foreign language",
        related_name="is_third_lang_of",
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return "{}".format(self.id)

    @classmethod
    def get_listview_url(self):
        return reverse('assignments:browse_learners')

    @classmethod
    def get_createview_url(self):
        return reverse('assignments:learner_create')

    def get_absolute_url(self):
        return reverse('assignments:learner_detail', kwargs={'pk': self.id})

    def get_absolute_url(self):
        return reverse('assignments:learner_detail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('assignments:learner_delete', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('assignments:learner_edit', kwargs={'pk': self.id})

    def get_next(self):
        next = self.__class__.objects.filter(id__gt=self.id)
        if next:
            return reverse(
                'assignments:learner_detail',
                kwargs={'pk': next.first().id}
            )
        return False

    def get_prev(self):
        prev = self.__class__.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return reverse(
                'assignments:learner_detail',
                kwargs={'pk': prev.first().id}
            )
        return False


class LearnerProfile(AssignmentBaseClass):

    """Background information about the learner which is subject to change;
    the profile stays unchanged until a new learner profile is filled in;
    to provide for longitudinal data, the profile can be updated."""

    learner_id = models.ManyToManyField(
        Learner, blank=True,
        help_text="learner_id",
        related_name="has_learner_profile"
    )
    year = models.IntegerField(
        blank=True, null=True,
        verbose_name="Year when the profile was filled in",
        help_text="year when the profile was filled in"
    )
    lang_spoken_home = models.CharField(
        null=True, blank=True, max_length=250,
        verbose_name="description of language use at home ",
        help_text="(if more than one language is spoken, provide the % of use of each language)\
        format: Bosnian: 50% Slovenian: 50%"
    )
    lang_instruction_primary = models.ForeignKey(
        SkosConcept, null=True, blank=True,
        verbose_name="Language of instruction in primary school",
        help_text="Language of instruction in primary school",
        related_name="is_lang_instruction_primary",
        on_delete=models.SET_NULL
    )
    lang_instruction_secondary = models.ForeignKey(
        SkosConcept, null=True, blank=True,
        verbose_name="Language of instruction in secondary school",
        help_text="Language of instruction in secondary school",
        related_name="is_lang_instruction_secondary",
        on_delete=models.SET_NULL
    )
    clil_years_learner_profile = models.IntegerField(
        blank=True, null=True,
        verbose_name="Number of years CLIL-classes were attended",
        help_text="Number of years CLIL-classes were attended"
    )
    clil_subjects_learner_profile = models.CharField(
        null=True, blank=True, max_length=250,
        verbose_name="Definition of the CLIL classes attended",
        help_text="format: biology(2) = 2 years of CLIL in biology;"
    )
    english_school = models.IntegerField(
        blank=True, null=True,
        verbose_name="Semesters of English at school",
        help_text="Semesters of English at school"
    )
    english_university = models.IntegerField(
        blank=True, null=True,
        verbose_name="Semesters of English at university",
        help_text="Semesters of English at university"
    )
    english_other = models.IntegerField(
        blank=True, null=True,
        verbose_name="Semesters of English outside school and university",
        help_text="round DOWN/UP --> - 3 months = 0; + 3 months = 1"
    )
    proficiency_level = models.CharField(
        null=True, blank=True, max_length=250,
        verbose_name="Latest CEF score/placement ",
        help_text="A1;A2;B1;B2;C1;C2"
    )
    proficiency_test = models.ForeignKey(
        SkosConcept, null=True, blank=True,
        verbose_name="proficiency test taken",
        help_text="(e.g. QPT; CAE; ...);",
        related_name="is_proficiency_test",
        on_delete=models.SET_NULL
    )
    proficiency_test_year = models.IntegerField(
        blank=True, null=True,
        verbose_name="Year of latest CEF score/placement",
        help_text="year of latest CEF score/placement"
    )
    school_year = models.IntegerField(
        blank=True, null=True,
        verbose_name="Current year of schooling",
        help_text="Only applicable if the participant still attends school"
    )
    studies_semester = models.IntegerField(
        blank=True, null=True,
        verbose_name="Current semester of studies ",
        help_text="Only applicable if the participant attends university/college)"
    )
    abroad_english_total = models.IntegerField(
        blank=True, null=True,
        verbose_name="Total time spent in English speaking countries (weeks); ",
        help_text="DO NOT FILL IN! automatic calculation"
    )
    abroad_english_vacation = models.IntegerField(
        blank=True, null=True,
        verbose_name="Time spent in English speaking countries on vacation ",
        help_text="Weeks! – calculate 1 month = 4 weeks"
    )
    abroad_english_school = models.IntegerField(
        blank=True, null=True,
        verbose_name="Time spent in English speaking countries with school",
        help_text="Including trips with language schools (weeks! – calculate 1 month = 4 weeks)"
    )
    abroad_english_studies = models.IntegerField(
        blank=True, null=True,
        verbose_name="Time spent studying in English speaking countries ",
        help_text="Weeks! – calculate 1 month = 4 weeks"
    )
    abroad_english_work = models.IntegerField(
        blank=True, null=True,
        verbose_name="Time spent working in English speaking countries",
        help_text="Including time spent as an Au-Pair (weeks! – calculate 1 month = 4 weeks)"
    )
    abroad_english_desc = models.TextField(
        null=True, blank=True,
        verbose_name="Description of stays in English-speaking countries",
        help_text="When? How long? Where? What?; format: 2005/2006 - 10 months - London - Au Pair"
    )

    @classmethod
    def get_listview_url(self):
        return reverse('assignments:browse_learnerprofiles')

    @classmethod
    def get_createview_url(self):
        return reverse('assignments:learnerprofile_create')

    def get_absolute_url(self):
        return reverse('assignments:learnerprofile_detail', kwargs={'pk': self.id})

    def get_absolute_url(self):
        return reverse('assignments:learnerprofile_detail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('assignments:learnerprofile_delete', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('assignments:learnerprofile_edit', kwargs={'pk': self.id})

    def get_next(self):
        next = self.__class__.objects.filter(id__gt=self.id)
        if next:
            return reverse(
                'assignments:learnerprofile_detail',
                kwargs={'pk': next.first().id}
            )
        return False

    def get_prev(self):
        prev = self.__class__.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return reverse(
                'assignments:learnerprofile_detail',
                kwargs={'pk': prev.first().id}
            )
        return False


class CourseGroup(AssignmentBaseClass):

    """this table is used either when a text is produced by a group (e.g. classroom discourse)*,
    or when a learner who produces a text by himself can be associated with a group
    (e.g. a particular class/course)"""

    course_type = models.ForeignKey(
        SkosConcept, null=True, blank=True,
        verbose_name="Course type",
        help_text="Course type",
        related_name="is_course_type_of",
        on_delete=models.SET_NULL
    )
    course_name = models.CharField(
        max_length=250, blank=True, null=True,
        verbose_name="group_course_name", help_text="provide some"
    )
    course_description = models.TextField(
        blank=True, null=True,
        verbose_name="Individual 'label' for this group",
        help_text="e.g. 07_Draschestrasse_3A"
    )
    participants_no = models.IntegerField(
        blank=True, null=True,
        verbose_name="Number of participants",
        help_text="Number of participants"
    )
    school_studies_year = models.IntegerField(
        blank=True, null=True,
        verbose_name="Current year of schooling/studies",
        help_text="(approximate?) school: e.g. 5AHS = 9\
        (count school-years 1 through 13)"
    )
    teacher_lecturer = models.CharField(
        max_length=250, blank=True, null=True,
        verbose_name="Name of teacher/lecturer",
        help_text="Name of teacher/lecturer"
    )
    group_notes = models.TextField(
        blank=True, null=True,
        verbose_name="group_notes", help_text="provide some"
    )

    @classmethod
    def get_listview_url(self):
        return reverse('assignments:browse_coursegroups')

    @classmethod
    def get_createview_url(self):
        return reverse('assignments:coursegroup_create')

    def get_absolute_url(self):
        return reverse('assignments:coursegroup_detail', kwargs={'pk': self.id})

    def get_absolute_url(self):
        return reverse('assignments:coursegroup_detail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('assignments:coursegroup_delete', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('assignments:coursegroup_edit', kwargs={'pk': self.id})

    def get_next(self):
        next = self.__class__.objects.filter(id__gt=self.id)
        if next:
            return reverse(
                'assignments:coursegroup_detail',
                kwargs={'pk': next.first().id}
            )
        return False

    def get_prev(self):
        prev = self.__class__.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return reverse(
                'assignments:coursegroup_detail',
                kwargs={'pk': prev.first().id}
            )
        return False

    def __str__(self):
        if self.course_name:
            return "{} (id: {})".format(self.course_name, self.id)
        else:
            return "{}".format(self.id)


INSTITUTION_LEVEL = (
    ('LS', 'LS'),
    ('TU', 'TU'),
    ('US', 'US')
)


class Participant(AssignmentBaseClass):

    """participant (= “virtual” participant); this table provides for the possibility to choose
    between a “group” and a “learner” as being responsible for the text production;
    it also allows for the correlation of a particular learner profile;
    the participant is also linked to the tbl_institution;"""

    learner_id = models.ForeignKey(
        Learner, null=True, blank=True,
        verbose_name="Learner ID",
        help_text="If the text is produced by an individual, LEARNER_ID is filled in\
        and GROUP_ID is optional (e.g. if a student produces a text individually,\
        but is a member of a particular course, both are filled in",
        related_name="has_learner",
        on_delete=models.SET_NULL
    )
    learner_profile_id = models.ForeignKey(
        LearnerProfile, null=True, blank=True,
        verbose_name="Learner Profile ID",
        help_text="If there is more than one profile, choose the one that corresponds to the time\
        the text was produced, i.e. usually the latest one",
        related_name="has_learner",
        on_delete=models.SET_NULL
    )
    group_id = models.ForeignKey(
        CourseGroup, null=True, blank=True,
        verbose_name="Group ID",
        help_text="If the text is produced by a group, only GROUP_ID is filled in; members of a\
        group that produced a text collectively are recorded in tbl_group_members;",
        related_name="has_participant",
        on_delete=models.SET_NULL
    )
    institution_id = models.ForeignKey(
        Institution, null=True, blank=True,
        verbose_name="Institution ID",
        help_text="Institution ID",
        related_name="has_participant",
        on_delete=models.SET_NULL
    )
    institution_level = models.CharField(
        max_length=250, blank=True,
        verbose_name="'Level' of the educational institution currently attended ",
        help_text="primary(PR); lower_secondary(LS); upper_secondary(US); tertiary_university(TU);\
        tertiary_college(TC); further_education(FE)",
        choices=INSTITUTION_LEVEL
    )
    clil = models.CharField(
        max_length=250, blank=True,
        verbose_name="Is this a CLIL-participant",
        help_text="A group or an individual learner currently learning in a CLIL context?",
        choices=YES_NO_OTHER
    )

    @classmethod
    def get_listview_url(self):
        return reverse('assignments:browse_participants')

    @classmethod
    def get_createview_url(self):
        return reverse('assignments:participant_create')

    def get_absolute_url(self):
        return reverse('assignments:participant_detail', kwargs={'pk': self.id})

    def get_absolute_url(self):
        return reverse('assignments:participant_detail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('assignments:participant_delete', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('assignments:participant_edit', kwargs={'pk': self.id})

    def get_next(self):
        next = self.__class__.objects.filter(id__gt=self.id)
        if next:
            return reverse(
                'assignments:participant_detail',
                kwargs={'pk': next.first().id}
            )
        return False

    def get_prev(self):
        prev = self.__class__.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return reverse(
                'assignments:participant_detail',
                kwargs={'pk': prev.first().id}
            )
        return False

    def __str__(self):
        return "{}".format(self.id)


class Text(AssignmentBaseClass):

    """Main table including information about the text"""

    participant_id = models.ForeignKey(
        Participant, null=True, blank=True,
        verbose_name="participant_id",
        help_text="provide some",
        related_name="text_has_participants",
        on_delete=models.SET_NULL
    )
    text_type = models.ForeignKey(
        SkosConcept, null=True, blank=True,
        verbose_name="Text Type",
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
        max_length=250, blank=True, verbose_name="Profile(s) signed?",
        help_text="Profile(s) signed?",
        choices=YES_NO_OTHER
    )
    year = models.IntegerField(
        blank=True, null=True, verbose_name="Year the text was produced",
        help_text="(e.g. 2007 = 2007/2008; W2007 = September 2007-Febuary 2008;\
        S2008 = March 2008 - August 2008)"
    )
    semester = models.CharField(
        max_length=250, blank=True, verbose_name="Semester",
        help_text="w=winter semester (September-February);\
        s=summer semester (March-August);\
        (e.g. 2007 = 2007/2008; W2007 = September 2007-Febuary 2008;\
        S2008 = March 2008 - August 2008)",
        choices=SEMESTER
    )
    lang = models.ForeignKey(
        SkosConcept, null=True, blank=True,
        verbose_name="Language the text is written/spoken in",
        help_text="Language the text is written/spoken in",
        related_name="is_text_lang",
        on_delete=models.SET_NULL
    )
    medium = models.ForeignKey(
        SkosConcept, null=True, blank=True,
        verbose_name="Medium: spoken, written, CMC",
        help_text="CMC (=computer mediated communication)",
        related_name="is_text_medium",
        on_delete=models.SET_NULL
    )
    data_type = models.ForeignKey(
        SkosConcept, null=True, blank=True,
        verbose_name="Type of samples",
        help_text="Type of samples (cf. Ellis & Barkhuizen):\
        naturally occurring, clinically elicited,\
        experimentally elicited",
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
        verbose_name="Recording method used ",
        help_text="audio/video",
        related_name="is_recoding_method",
        on_delete=models.SET_NULL
    )
    mode = models.ForeignKey(
        SkosConcept, null=True, blank=True,
        verbose_name="Mode of writing",
        help_text="argumentative, descriptive, expository, narrative; other",
        related_name="is_text_mode",
        on_delete=models.SET_NULL
    )
    clil_text = models.CharField(
        max_length=250, blank=True, verbose_name="Produced in a CLIL context",
        help_text="E.g. a recording of a biology course taught in English)",
        choices=YES_NO_OTHER
    )
    clil_subject = models.ForeignKey(
        SkosConcept, null=True, blank=True,
        verbose_name="Subject taught through CLIL",
        help_text="Subject taught through CLIL",
        related_name="is_clil_subject",
        on_delete=models.SET_NULL
    )
    timed = models.CharField(
        max_length=250, blank=True,
        verbose_name="Produced in a timed context?",
        help_text="Produced in a timed context?",
        choices=YES_NO_OTHER
    )
    exam = models.CharField(
        max_length=250, blank=True, verbose_name="Produced in an exam?",
        help_text="Produced in an exam?",
        choices=YES_NO_OTHER
    )
    planning_time = models.CharField(
        max_length=250, blank=True, verbose_name="planned; unplanned; unknown",
        help_text="only relevant for spoken texts; written texts: always mark 'unknown';\
        (e.g. Did the speakers have time to think about what they were going to say beforehand?)",
        choices=YES_NO_OTHER
    )
    grade = models.IntegerField(
        blank=True, null=True, verbose_name="Grade, if available",
        help_text="scale 1-5, convert different grading schemes"
    )
    tool = models.CharField(
        max_length=250, blank=True, verbose_name="Were tools used? ",
        help_text="(yes; no; unknown)",
        choices=YES_NO_OTHER
    )
    title = models.CharField(
        max_length=250, blank=True, verbose_name="Text title",
        help_text="If available and different from assignment title\
        (the title is also included in the text itself, where it is tagged as 'head')"
    )
    source = models.CharField(
        max_length=250, blank=True, verbose_name="Text source ",
        help_text="handwritten / born digital / recording_audio / recording_video"
    )
    transcriber = models.ForeignKey(
        Person, null=True, blank=True,
        verbose_name="Transcriber of spoken or handwritten data",
        help_text="Transcriber of spoken or handwritten data",
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
        return "{}".format(self.id)


class TextVersion(AssignmentBaseClass):

    """Various versions of the text can be saved in this table, along with a description of the
    respective version, which is defined in tbl_text_status;
    (the original files are stored in a folder in the server (pool_texts)
    and associated with the database with a link; the texts are copy-pasted into the memo-field)"""

    text_id = models.ManyToManyField(
        Text, blank=True,
        verbose_name="text_id",
        help_text="provide some",
        related_name="has_text_version",
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
