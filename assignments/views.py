from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django_tables2 import RequestConfig

from browsing.browsing_utils import GenericListView, BaseCreateView, BaseUpdateView

from .models import *
from .tables import *
from .filters import *
from .forms import *


class AssignmentListView(GenericListView):
    model = Assignment
    table_class = AssignmentTable
    filter_class = AssignmentListFilter
    formhelper_class = AssignmentFilterFormHelper
    init_columns = [
        'id',
        'title',
    ]

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


class AssignmentDetailView(DetailView):
    model = Assignment
    template_name = 'assignments/assignment_detail.html'


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


class TextListView(GenericListView):
    model = Text
    table_class = TextTable
    filter_class = TextListFilter
    formhelper_class = TextFilterFormHelper
    init_columns = [
        'legacy_id',
        'type',
    ]

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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TextListView, self).dispatch(*args, **kwargs)


class TextDetailView(DetailView):
    model = Text
    template_name = 'assignments/text_detail.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TextDetailView, self).dispatch(*args, **kwargs)


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


class TextVersionListView(GenericListView):
    model = TextVersion
    table_class = TextVersionTable
    filter_class = TextVersionListFilter
    formhelper_class = TextVersionFilterFormHelper
    init_columns = [
        'legacy_id',
        'type',
    ]

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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TextVersionListView, self).dispatch(*args, **kwargs)


class TextVersionDetailView(DetailView):
    model = TextVersion
    template_name = 'assignments/textversion_detail.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TextVersionDetailView, self).dispatch(*args, **kwargs)


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
