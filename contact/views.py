from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template


def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name', '')
            contact_email = request.POST.get(
                'contact_email', '')
            form_content = request.POST.get('content', '')

            template = get_template('contact/contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "Contact Us Form",
                content,
                "Titan Computer Parts" + '',
                ['TitanComputerPartsUNO@gmail.com'],
                headers={'Reply-To': contact_email}
            )
            email.send()
            return redirect('success')
    return render(request, 'contact/contact.html', {
        'form': form_class,
    })