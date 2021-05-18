import datetime
import time
from io import BytesIO
from zipfile import ZipFile

from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponse


from django_tables2 import RequestConfig

from browsing.browsing_utils import GenericListView, BaseCreateView, BaseUpdateView
from webpage.utils import access_for_shib_and_loggedin

from . models import *
from . tables import *
from . filters import *
from . forms import *


class AssignmentListView(UserPassesTestMixin, GenericListView):
    model = Assignment
    table_class = AssignmentTable
    filter_class = AssignmentListFilter
    formhelper_class = AssignmentFilterFormHelper
    init_columns = [
        'id',
        'title',
    ]

    def test_func(self):
        access = access_for_shib_and_loggedin(self)
        print(access)
        return access

    def get_all_cols(self):
        all_cols = list(self.table_class.base_columns.keys())
        return all_cols

    def get_context_data(self, **kwargs):
        context = super(AssignmentListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        togglable_colums = [x for x in self.get_all_cols() if x not in self.init_columns]
        context['togglable_colums'] = togglable_colums
        return context

    def get_table(self, **kwargs):
        table = super(GenericListView, self).get_table()
        RequestConfig(self.request, paginate={
            'page': 1, 'per_page': self.paginate_by
        }).configure(table)
        default_cols = self.init_columns
        all_cols = self.get_all_cols()
        selected_cols = self.request.GET.getlist("columns") + default_cols
        exclude_vals = [x for x in all_cols if x not in selected_cols]
        table.exclude = exclude_vals
        return table


class AssignmentDetailView(UserPassesTestMixin, DetailView):
    model = Assignment
    template_name = 'assignments/assignment_detail.html'

    def test_func(self):
        access = access_for_shib_and_loggedin(self)
        return access


class AssignmentCreate(BaseCreateView):

    model = Assignment
    form_class = AssignmentForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AssignmentCreate, self).dispatch(*args, **kwargs)


class AssignmentUpdate(BaseUpdateView):

    model = Assignment
    form_class = AssignmentForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AssignmentUpdate, self).dispatch(*args, **kwargs)


class AssignmentDelete(DeleteView):
    model = Assignment
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('assignments:browse_assignments')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AssignmentDelete, self).dispatch(*args, **kwargs)


class TextListView(UserPassesTestMixin, GenericListView):
    model = Text
    table_class = TextTable
    filter_class = TextListFilter
    formhelper_class = TextFilterFormHelper
    init_columns = [
        'legacy_id',
        'type',
    ]

    def test_func(self):
        access = access_for_shib_and_loggedin(self)
        return access

    def get_all_cols(self):
        all_cols = list(self.table_class.base_columns.keys())
        return all_cols

    def get_context_data(self, **kwargs):
        context = super(TextListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        togglable_colums = [x for x in self.get_all_cols() if x not in self.init_columns]
        context['togglable_colums'] = togglable_colums
        return context

    def get_table(self, **kwargs):
        table = super(GenericListView, self).get_table()
        RequestConfig(self.request, paginate={
            'page': 1, 'per_page': self.paginate_by
        }).configure(table)
        default_cols = self.init_columns
        all_cols = self.get_all_cols()
        selected_cols = self.request.GET.getlist("columns") + default_cols
        exclude_vals = [x for x in all_cols if x not in selected_cols]
        table.exclude = exclude_vals
        return table


class TextDetailView(UserPassesTestMixin, DetailView):
    model = Text
    template_name = 'assignments/text_detail.html'

    def test_func(self):
        access = access_for_shib_and_loggedin(self)
        return access


class TextCreate(BaseCreateView):

    model = Text
    form_class = TextForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TextCreate, self).dispatch(*args, **kwargs)


class TextUpdate(BaseUpdateView):

    model = Text
    form_class = TextForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TextUpdate, self).dispatch(*args, **kwargs)


class TextDelete(DeleteView):
    model = Text
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('assignments:browse_texts')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TextDelete, self).dispatch(*args, **kwargs)


class TextVersionListView(UserPassesTestMixin, GenericListView):
    model = TextVersion
    table_class = TextVersionTable
    filter_class = TextVersionListFilter
    formhelper_class = TextVersionFilterFormHelper
    init_columns = [
        'legacy_id',
        'Plain_Text',
        'text_id__mode',
        'text_id__text_type',
    ]
    template_name = 'assignments/text_list.html'

    def test_func(self):
        access = access_for_shib_and_loggedin(self)
        return access

    def get_all_cols(self):
        all_cols = list(self.table_class.base_columns.keys())
        return all_cols

    def get_context_data(self, **kwargs):
        context = super(TextVersionListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        togglable_colums = [x for x in self.get_all_cols() if x not in self.init_columns]
        context['togglable_colums'] = togglable_colums
        return context

    def get_table(self, **kwargs):
        table = super(GenericListView, self).get_table()
        RequestConfig(self.request, paginate={
            'page': 1, 'per_page': self.paginate_by
        }).configure(table)
        default_cols = self.init_columns
        all_cols = self.get_all_cols()
        selected_cols = self.request.GET.getlist("columns") + default_cols
        exclude_vals = [x for x in all_cols if x not in selected_cols]
        table.exclude = exclude_vals
        return table
    
    def render_to_response(self, context, **kwargs):
        download = self.request.GET.get('zip', None)
        download_plain = self.request.GET.get('zip_plain', None)
        if download:
            zipped_file = BytesIO()
            timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
            zip_name = f"export_{timestamp}.zip"
            texts = self.get_queryset()
            with ZipFile(zipped_file, 'w') as zipped:
                for x in texts:
                    file_name = f"text__{x.id}.txt"
                    zipped.writestr(file_name, f"{x.content}")
            zipped_file.seek(0)
            response = HttpResponse(zipped_file, content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename={timestamp}.zip'
            return response
        elif download_plain:
            zipped_file = BytesIO()
            timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
            zip_name = f"export_{timestamp}.zip"
            texts = self.get_queryset()
            with ZipFile(zipped_file, 'w') as zipped:
                for x in texts:
                    file_name = f"text__{x.id}.txt"
                    zipped.writestr(file_name, f"{x.get_plain_text()}")
            zipped_file.seek(0)
            response = HttpResponse(zipped_file, content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename={timestamp}.zip'
            return response
        else:
            response = super(GenericListView, self).render_to_response(context)
            return response  

class TextVersionDetailView(UserPassesTestMixin, DetailView):
    model = TextVersion
    template_name = 'assignments/textversion_detail.html'

    def test_func(self):
        access = access_for_shib_and_loggedin(self)
        return access


class TextVersionCreate(BaseCreateView):

    model = TextVersion
    form_class = TextVersionForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TextVersionCreate, self).dispatch(*args, **kwargs)


class TextVersionUpdate(BaseUpdateView):

    model = TextVersion
    form_class = TextVersionForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TextVersionUpdate, self).dispatch(*args, **kwargs)


class TextVersionDelete(DeleteView):
    model = TextVersion
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('assignments:browse_textversions')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TextVersionDelete, self).dispatch(*args, **kwargs)


class LearnerListView(UserPassesTestMixin, GenericListView):
    model = Learner
    table_class = LearnerTable
    filter_class = LearnerListFilter
    formhelper_class = LearnerFilterFormHelper
    init_columns = [
        'id',
        'title',
    ]

    def test_func(self):
        access = access_for_shib_and_loggedin(self)
        return access

    def get_all_cols(self):
        all_cols = list(self.table_class.base_columns.keys())
        return all_cols

    def get_context_data(self, **kwargs):
        context = super(LearnerListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        togglable_colums = [x for x in self.get_all_cols() if x not in self.init_columns]
        context['togglable_colums'] = togglable_colums
        return context

    def get_table(self, **kwargs):
        table = super(GenericListView, self).get_table()
        RequestConfig(self.request, paginate={
            'page': 1, 'per_page': self.paginate_by
        }).configure(table)
        default_cols = self.init_columns
        all_cols = self.get_all_cols()
        selected_cols = self.request.GET.getlist("columns") + default_cols
        exclude_vals = [x for x in all_cols if x not in selected_cols]
        table.exclude = exclude_vals
        return table


class LearnerDetailView(UserPassesTestMixin, DetailView):
    model = Learner
    template_name = 'browsing/generic_detail.html'

    def test_func(self):
        access = access_for_shib_and_loggedin(self)
        return access


class LearnerCreate(BaseCreateView):

    model = Learner
    form_class = LearnerForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LearnerCreate, self).dispatch(*args, **kwargs)


class LearnerUpdate(BaseUpdateView):

    model = Learner
    form_class = LearnerForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LearnerUpdate, self).dispatch(*args, **kwargs)


class LearnerDelete(DeleteView):
    model = Learner
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('assignments:browse_learners')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LearnerDelete, self).dispatch(*args, **kwargs)


class LearnerProfileListView(UserPassesTestMixin, GenericListView):
    model = LearnerProfile
    table_class = LearnerProfileTable
    filter_class = LearnerProfileListFilter
    formhelper_class = LearnerProfileFilterFormHelper
    init_columns = [
        'id',
        'type',
    ]

    def test_func(self):
        access = access_for_shib_and_loggedin(self)
        return access

    def get_all_cols(self):
        all_cols = list(self.table_class.base_columns.keys())
        return all_cols

    def get_context_data(self, **kwargs):
        context = super(LearnerProfileListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        togglable_colums = [x for x in self.get_all_cols() if x not in self.init_columns]
        context['togglable_colums'] = togglable_colums
        return context

    def get_table(self, **kwargs):
        table = super(GenericListView, self).get_table()
        RequestConfig(self.request, paginate={
            'page': 1, 'per_page': self.paginate_by
        }).configure(table)
        default_cols = self.init_columns
        all_cols = self.get_all_cols()
        selected_cols = self.request.GET.getlist("columns") + default_cols
        exclude_vals = [x for x in all_cols if x not in selected_cols]
        table.exclude = exclude_vals
        return table


class LearnerProfileDetailView(UserPassesTestMixin, DetailView):
    model = LearnerProfile
    template_name = 'browsing/generic_detail.html'

    def test_func(self):
        access = access_for_shib_and_loggedin(self)
        return access


class LearnerProfileCreate(BaseCreateView):

    model = LearnerProfile
    form_class = LearnerProfileForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LearnerProfileCreate, self).dispatch(*args, **kwargs)


class LearnerProfileUpdate(BaseUpdateView):

    model = LearnerProfile
    form_class = LearnerProfileForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LearnerProfileUpdate, self).dispatch(*args, **kwargs)


class LearnerProfileDelete(DeleteView):
    model = LearnerProfile
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('assignments:browse_texts')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LearnerProfileDelete, self).dispatch(*args, **kwargs)


class CourseGroupListView(UserPassesTestMixin, GenericListView):
    model = CourseGroup
    table_class = CourseGroupTable
    filter_class = CourseGroupListFilter
    formhelper_class = CourseGroupFilterFormHelper
    init_columns = [
        'id',
        'type',
    ]

    def test_func(self):
        access = access_for_shib_and_loggedin(self)
        return access

    def get_all_cols(self):
        all_cols = list(self.table_class.base_columns.keys())
        return all_cols

    def get_context_data(self, **kwargs):
        context = super(CourseGroupListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        togglable_colums = [x for x in self.get_all_cols() if x not in self.init_columns]
        context['togglable_colums'] = togglable_colums
        return context

    def get_table(self, **kwargs):
        table = super(GenericListView, self).get_table()
        RequestConfig(self.request, paginate={
            'page': 1, 'per_page': self.paginate_by
        }).configure(table)
        default_cols = self.init_columns
        all_cols = self.get_all_cols()
        selected_cols = self.request.GET.getlist("columns") + default_cols
        exclude_vals = [x for x in all_cols if x not in selected_cols]
        table.exclude = exclude_vals
        return table


class CourseGroupDetailView(UserPassesTestMixin, DetailView):
    model = CourseGroup
    template_name = 'browsing/generic_detail.html'

    def test_func(self):
        access = access_for_shib_and_loggedin(self)
        return access


class CourseGroupCreate(BaseCreateView):

    model = CourseGroup
    form_class = CourseGroupForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CourseGroupCreate, self).dispatch(*args, **kwargs)


class CourseGroupUpdate(BaseUpdateView):

    model = CourseGroup
    form_class = CourseGroupForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CourseGroupUpdate, self).dispatch(*args, **kwargs)


class CourseGroupDelete(DeleteView):
    model = CourseGroup
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('assignments:browse_groups')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CourseGroupDelete, self).dispatch(*args, **kwargs)


class ParticipantListView(UserPassesTestMixin, GenericListView):
    model = Participant
    table_class = ParticipantTable
    filter_class = ParticipantListFilter
    formhelper_class = ParticipantFilterFormHelper
    init_columns = [
        'id',
        'type',
    ]

    def test_func(self):
        access = access_for_shib_and_loggedin(self)
        return access

    def get_all_cols(self):
        all_cols = list(self.table_class.base_columns.keys())
        return all_cols

    def get_context_data(self, **kwargs):
        context = super(ParticipantListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        togglable_colums = [x for x in self.get_all_cols() if x not in self.init_columns]
        context['togglable_colums'] = togglable_colums
        return context

    def get_table(self, **kwargs):
        table = super(GenericListView, self).get_table()
        RequestConfig(self.request, paginate={
            'page': 1, 'per_page': self.paginate_by
        }).configure(table)
        default_cols = self.init_columns
        all_cols = self.get_all_cols()
        selected_cols = self.request.GET.getlist("columns") + default_cols
        exclude_vals = [x for x in all_cols if x not in selected_cols]
        table.exclude = exclude_vals
        return table


class ParticipantDetailView(UserPassesTestMixin, DetailView):
    model = Participant
    template_name = 'browsing/generic_detail.html'

    def test_func(self):
        access = access_for_shib_and_loggedin(self)
        return access


class ParticipantCreate(BaseCreateView):

    model = Participant
    form_class = ParticipantForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ParticipantCreate, self).dispatch(*args, **kwargs)


class ParticipantUpdate(BaseUpdateView):

    model = Participant
    form_class = ParticipantForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ParticipantUpdate, self).dispatch(*args, **kwargs)


class ParticipantDelete(DeleteView):
    model = Participant
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('assignments:browse_groups')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ParticipantDelete, self).dispatch(*args, **kwargs)
