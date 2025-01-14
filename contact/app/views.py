# contacts/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm

# Home page, showing all contacts
def home(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/index.html', {'contacts': contacts})

# Display individual contact details
def contact_detail(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    return render(request, 'contacts/contactdetail.html', {'contact': contact})

def list_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contactlist.html', {'contacts': contacts})

# Add a new contact
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'contacts/addcontact.html', {'form': form})

def edit_contact(request, id):
    contact = get_object_or_404(Contact, pk=id)  # Fetch the contact based on the provided id
    if request.method == 'POST':
        # Handle form submission (e.g., save changes to the contact)
        contact.name = request.POST['name']
        contact.phone = request.POST['phone']
        contact.email = request.POST['email']
        contact.save()
        return redirect('list_contacts')  # Redirect to the contact list page
    return render(request, 'contacts/editcontact.html', {'contact': contact})

# Delete a contact
def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    contact.delete()
    return redirect('home')

def call_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contacts/call_contact.html', {'contact': contact})

def view_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contacts/viewcontact.html', {'contact': contact})
