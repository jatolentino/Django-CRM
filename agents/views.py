from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from django.shortcuts import reverse
from .forms import AgentModelForm
from .mixins import OrganizerAndLoginRequiredMixin
from django.core.mail import send_mail
import random

class AgentListView(OrganizerAndLoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_list.html"

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization) #Changed this return Agent.objects.all()

class AgentCreateView(OrganizerAndLoginRequiredMixin, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agent-list")

    def form_valid(self, form):
        #create the user type agent
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organizer = False
        user.set_password(f"{random.randint(0, 100000)}")  #ADDED, need to reset pass
        user.save()
        # create the agent for that user
        Agent.objects.create(
            user=user,
            organization=self.request.user.userprofile
            )
        send_mail(
            subject="You are invited to be an agent",
            message="You were added as an agent on CRM. Please come login to stat working.",
            from_email="admin@test.com",
            recipient_list=[user.email]
            )
        return super(AgentCreateView, self).form_valid(form)

class AgentDetailView(OrganizerAndLoginRequiredMixin, generic.DetailView):
    template_name = "agents/agent_detail.html"
    context_object_name = "agent"
    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)

class AgentUpdateView(OrganizerAndLoginRequiredMixin, generic.UpdateView):
    template_name = "agents/agent_update.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agent-list")

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)

class AgentDeleteView(OrganizerAndLoginRequiredMixin, generic.DeleteView):
    template_name = "agents/agent_delete.html"
    context_object_name = "agent"

    def get_success_url(self):
        return reverse("agents:agent-list")

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)