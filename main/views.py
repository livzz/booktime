from django.views.generic.edit import FormView
from main import forms


class ContactUsView(FormView):
    template_name = "contact_form.html"
    form_class = forms.ContactForm
    success_url = "/"

    # def contact_us(self, request):
    #     if request.method == 'POST':
    #         form = forms.ContactForm(request.POST)
    #     if form.is_valid():
    #         form.send_mail()
    #         return HttpResponseRedirect('/')
    #     else:
    #         form = forms.ContactForm()
    #     return render(request, 'contact_form.html', {'form': form})

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)
