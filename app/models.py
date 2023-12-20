'''Importing model class '''
from django.db import models


#Create custom model class
class MyModel(models.Model):
    #Define choices
    SHIRT_SIZES = [
        ("S","Small"),
        ("M","Medium"),
        ("L","Large"),
            ]
    
    user_id = models.CharField(max_length=10,
                                 primary_key=True)  # Define a CharField for the user ID
    # Other fields of the model
    field1 = models.CharField(max_length=100)
    #added choice field
    shirt_size = models.CharField(max_length=1,
                                  choices= SHIRT_SIZES)
    shirt_type_2 = models.TextChoices("ShirtType","Small Medium Large") #added another type of choice field
    
    def save(self, *args, **kwargs):
        if not self.custom_id:  # Generate custom ID only if it's not provided
            last_id = MyModel.objects.order_by('-custom_id').first()

            if last_id:
                # Extract the numeric part, increment it by 1, and format it with 'AES01' prefix
                last_numeric_id = int(last_id.custom_id[3:]) + 1
                self.custom_id = f'AES{str(last_numeric_id).zfill(3)}'
            else:
                # If no existing records, start with 'AES010001'
                self.custom_id = 'AES11'

        super().save(*args, **kwargs)  # Call the original save() method

    # ... other model fields and methods
