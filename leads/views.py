from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import generic
from .models import Lead, Agent, Category
from .forms import (
    LeadModelForm,
    CustomUserCreationForm,
    AssignAgentForm,
    LeadCategoryUpdateForm,
    CategoryModelForm
)
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from agents.mixins import OrganizerAndLoginRequiredMixin
#from braces.views import LoginRequiredMixin
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.mixins import LoginRequiredMixin

class LandingPageView(generic.TemplateView):
    template_name = "landing.html"

class BlogPageView(generic.TemplateView):
    template_name = "blog.html"

class AboutPageView(generic.TemplateView):
    template_name = "about.html"

class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = "leads/lead_list.html"
    context_object_name = "leads"

    def get_queryset(self):
        user = self.request.user

        if user.is_organizer:
            queryset = Lead.objects.filter(organization = user.userprofile, agent__isnull=False)
        else:
            queryset = Lead.objects.filter(organization=user.agent.organization, agent__isnull=False)
            queryset = queryset.filter(agent__user=user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(LeadListView, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile, agent__isnull=True)
            context.update({
                "unassigned_leads": queryset
            })
        return context

class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "leads/lead_detail.html"
    context_object_name = "lead"

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entrie organization
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = Lead.objects.filter(organization=user.agent.organization)
            #filter for the agent that is logged in
            queryset = queryset.filter(agent__user=user)
        return queryset

class LeadCreateView(OrganizerAndLoginRequiredMixin, generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm
    def get_success_url(self):
        return reverse("leads:lead-list")

    def form_valid(self, form):
        lead = form.save(commit=False)
        lead.organization = self.request.user.userprofile
        lead.save()
        send_mail(
            subject="A lead has been created",
            message="Go to the website to see the new lead",
            from_email="test@test.com",
            recipient_list=["test2@test.com"]
        )
        return super(LeadCreateView, self).form_valid(form)          


class LeadUpdateView(OrganizerAndLoginRequiredMixin, generic.UpdateView):
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm
    
    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entrie organization
        return Lead.objects.filter(organization=user.userprofile)

    def get_success_url(self):
        return reverse("leads:lead-list")

class LeadDeleteView(OrganizerAndLoginRequiredMixin, generic.DeleteView):
    template_name = "leads/lead_delete.html"
    
    def get_success_url(self):
        return reverse("leads:lead-list")

    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organization=user.userprofile)

class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")

class AssignAgentView(OrganizerAndLoginRequiredMixin, generic.FormView): 
    template_name = "leads/assign_agent.html"
    form_class = AssignAgentForm

    def get_form_kwargs(self, **kwargs):
        kwargs = super(AssignAgentView, self).get_form_kwargs(**kwargs)
        kwargs.update({
            "request": self.request
        })
        return kwargs

    def get_success_url(self):
        return reverse("leads:lead-list")

    def form_valid(self, form):
        #print(form.cleaned_data["agent"])
        agent = form.cleaned_data["agent"]
        lead = Lead.objects.get(id=self.kwargs["pk"])
        lead.agent = agent
        lead.save()
        return super(AssignAgentView, self).form_valid(form)

class CategoryListView(LoginRequiredMixin, generic.ListView):
    template_name = "leads/category_list.html"
    context_object_name = "category_list"
    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        user = self.request.user

        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = Lead.objects.filter(organization=user.agent.organization)

        context.update({
            "unassigned_lead_count": queryset.filter(category__isnull=True).count()})
        return context

    def get_queryset(self):
        user = self.request.user
        if user.is_organizer:
            queryset = Category.objects.filter(organization=user.userprofile)
        else:
            queryset = Category.objects.filter(organization=user.organization)
        return queryset

class CategoryDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "leads/category_detail.html"
    context_object_name = "category"

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        leads = self.get_object().leads.all()

        context.update({
            "leads": leads
        })
        return context

    def get_queryset(self):
        user = self.request.user
        if user.is_organizer:
            queryset = Category.objects.filter(organization=user.userprofile)
        else:
            queryset = Category.objects.filter(organization=user.agent.organization)
        return queryset

class LeadCategoryUpdateView(LoginRequiredMixin, generic.UpdateView):
        template_name = "leads/lead_category_update.html"
        form_class = LeadCategoryUpdateForm

        def get_queryset(self):
            user = self.request.user
            if user.is_organizer:
                queryset = Lead.objects.filter(organization=user.userprofile)
            else:
                queryset = Lead.objects.filter(organization=user.agent.organization)
                queryset = queryset.filter(agent__user=user)
            return queryset

        def get_success_url(self):
            return reverse("leads:lead-detail", kwargs={"pk": self.get_object().id})



class CategoryCreateView(OrganizerAndLoginRequiredMixin, generic.CreateView):
    template_name = "leads/category_create.html"
    form_class = CategoryModelForm

    def get_success_url(self):
        return reverse("leads:category-list")
    def form_valid(self, form):
        category=form.save(commit=False)
        category.organization = self.request.user.userprofile
        category.save()
        return super(CategoryCreateView, self).form_valid(form)

class CategoryUpdateView(OrganizerAndLoginRequiredMixin, generic.UpdateView):#12.49
    template_name = "leads/category_update.html"
    form_class = CategoryModelForm

    def get_success_url(self):
        return reverse("leads:category-list")
    
    def get_queryset(self):
        user = self.request.user
        if user.is_organizer:
            queryset = Category.objects.filter(organization=user.userprofile)
        else:
            queryset = Category.objects.filter(organization=user.agent.organization)
        return queryset

class CategoryDeleteView(OrganizerAndLoginRequiredMixin, generic.DeleteView):
    template_name = "leads/category_delete.html"

    def get_success_url(self):
        return reverse("leads:category-list")
    def get_queryset(self):
        user = self.request.user
        if user.is_organizer:
            queryset = Category.objects.filter(organization=user.userprofile)
        else:
            queryset = Category.objects.filter(organization=user.agent.organization)
        return queryset