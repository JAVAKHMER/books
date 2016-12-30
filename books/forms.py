from django.forms import ModelForm
from books.models import Books
class BookForm(ModelForm):
    class Meta:
        model = Books
        fields = '__all__'

