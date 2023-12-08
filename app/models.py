from django.db import models

class MyModel(models.Model):
    custom_id = models.CharField(max_length=10, primary_key=True)  # Define a CharField for the custom ID

    # Other fields of the model
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()

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
