
from django import forms  
from .models import items  
class itemForm(forms.ModelForm):  
    class Meta:  
        # specify model to be used
        model = items  
        # fields = "__all__"   # another way of getting all the fields that are in table
         # specify fields to be used
        fields = [
            "item_name",
            "item_desc",
            "item_price",
            "item_img",
        ]
