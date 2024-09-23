# common/models.py
from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords
from simple_history import register
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class SoftDeleteQuerySet(models.QuerySet):
    def delete(self):
        """Override delete method to perform a soft delete."""
        return super().update(deleted_at=timezone.now())

    def hard_delete(self):
        """Actually delete the objects from the database."""
        return super().delete()

    def active(self):
        """Return only non-deleted objects."""
        return self.filter(deleted_at__isnull=True)

    def with_deleted(self):
        """Include deleted objects in the queryset."""
        return self

class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        """Return only non-deleted objects by default."""
        return SoftDeleteQuerySet(self.model, using=self._db).active()

    def with_deleted(self):
        """Include deleted objects in the queryset."""
        return self.get_queryset().with_deleted()

    def active(self):
        """Return only non-deleted objects."""
        return self.get_queryset().active()
    
class SoftDeleteModel(models.Model):
    deleted_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = SoftDeleteManager()
    all_objects = SoftDeleteQuerySet.as_manager()  # Ensure the all_objects manager doesn't filter by default

    class Meta:
        abstract = True

    def soft_delete(self):
        """Mark the object as deleted by setting the deleted_at field to the current time."""
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        """Restore the object by setting the deleted_at field to None."""
        self.deleted_at = None
        self.save()

    def delete(self, *args, **kwargs):
        """Override the delete method to perform a soft delete instead of a hard delete."""
        self.soft_delete()


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)  # Default value set to the time of creation
    updated_at = models.DateTimeField(auto_now=True)  # Automatically updated whenever the model is saved

    class Meta:
        abstract = True
        
        
class ResearchInterestOptions(SoftDeleteModel, TimestampedModel):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    topic = models.CharField(max_length=255)
    history = HistoricalRecords()

    def __str__(self):
        return f"Research Interest Options: {self.topic} (User ID: {self.user_id})"


class SkillOptions(SoftDeleteModel, TimestampedModel):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    skill_name = models.CharField(max_length=255)
    history = HistoricalRecords()

    def __str__(self):
        return f"Skill Option: {self.skill_name} (User ID: {self.user_id})"
    
    
class Document(SoftDeleteModel, TimestampedModel):
    IMAGE = 'image'
    PDF = 'pdf'
    DOCUMENT_TYPE_CHOICES = [
        (IMAGE, 'IMAGE'),
        (PDF, 'PDF'),
    ]

    id = models.AutoField(primary_key=True)
    image = models.FileField(upload_to='documents/', null=True, blank=True)
    type = models.CharField(max_length=5, choices=DOCUMENT_TYPE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_name = models.TextField()
    file_name_system = models.TextField()
    history = HistoricalRecords()

    def __str__(self):
        return self.file_name

  
        
        
class UserDocument(SoftDeleteModel, TimestampedModel):
    IMAGE = 'image'
    ORG_LOGO = 'organization_logo'
    RESUME = 'resume'
    SOP = 'sop'
    BIRTH_CERTIFICATE = 'birth_certificate'
    PASSPORT = 'passport'
    TEST_SCORE_DOCUMENT = 'test_score_document'
    DOCUMENT_USE_CHOICES = [
        (RESUME, 'Resume'),
        (SOP, 'SOP'),
        (IMAGE, 'Image'),
        (ORG_LOGO, 'Image'),
        (BIRTH_CERTIFICATE, 'Birth Certificate'),
        (PASSPORT, 'Passport'),
        (TEST_SCORE_DOCUMENT, ('Test Score Document')),
        # Add more document uses as needed
    ]

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    use = models.CharField(max_length=20, choices=DOCUMENT_USE_CHOICES)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.get_use_display()} for {self.document}"
    
    
    
class State(models.Model):
    name = models.CharField(max_length=255)
    country_id = models.PositiveIntegerField()
    country_code = models.CharField(max_length=2)
    fips_code = models.CharField(max_length=255, null=True, blank=True)
    iso2 = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=191, null=True, blank=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    flag = models.BooleanField(default=True)
    wikiDataId = models.CharField(max_length=255, null=True, blank=True, help_text='Rapid API GeoDB Cities')

    class Meta:
        indexes = [
            models.Index(fields=['country_id']),
        ]


class EthnicityOptions:
    # Static choices for ethnicity
    ETHNICITY_CHOICES = [
        ('', 'Select One'),
        ('Native American', 'Native American'),
        ('Asian', 'Asian'),
        ('Black/African American', 'Black/African American'),
        ('White', 'White'),
        ('Mixed Ethnicity', 'Mixed Ethnicity'),
        ('Other', 'Other'),
    ]

    @staticmethod
    def get_ethnicity_choices():
        return EthnicityOptions.ETHNICITY_CHOICES
    
    
class TitleOptions:
    # Static choices for title
    TITLE_OPTIONS = [
        ('Dr.', 'Dr.'),
        ('Mr.', 'Mr.'),
        ('Mrs.', 'Mrs.'),
        ('Ms.', 'Ms.'),
        ('Prof.', 'Prof.'),
    ]

    @staticmethod
    def get_title_options():
        return TitleOptions.TITLE_OPTIONS
    
class Language(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(max_length=11, null=True, blank=True)
    properties_name = models.CharField(max_length=46, null=True, blank=True)
    properties_charset = models.CharField(max_length=11, null=True, blank=True)

    class Meta:
        pass

    def __str__(self):
        return f"ID: {self.id}, Key: {self.key}, Name: {self.properties_name}, Charset: {self.properties_charset}"



class Countries(SoftDeleteModel, TimestampedModel):
    country_name = models.CharField(max_length=255)
    country_code = models.CharField(max_length=200, unique=True)
    history = HistoricalRecords()


class GeoAdmin1(SoftDeleteModel, TimestampedModel):
    country = models.ForeignKey('Countries', on_delete=models.CASCADE)
    geo_admin_1_code = models.CharField(max_length=100, unique=True)
    geo_admin_1_name = models.CharField(max_length=255)
    history = HistoricalRecords()


class GeoAdmin2(SoftDeleteModel, TimestampedModel):
    country = models.ForeignKey('Countries', on_delete=models.CASCADE)
    geo_admin_1 = models.ForeignKey('GeoAdmin1', on_delete=models.CASCADE)
    geo_admin_2_code = models.CharField(max_length=100)
    geo_admin_2_name = models.CharField(max_length=255)
    history = HistoricalRecords()





from educational_organizations_app.models import EducationalOrganizations
from college_app.models import College
from django.db import models
from django.contrib.auth.models import Group as DjangoGroup  
from django.contrib.auth.models import Permission 
    
class CustomGroup(models.Model):
    name = models.CharField(max_length=255)
    organization = models.ForeignKey(EducationalOrganizations, on_delete=models.CASCADE, related_name='groups', null=True, blank=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='groups', null=True, blank=True)
    permissions = models.ManyToManyField(Permission, blank=True)

    class Meta:
        unique_together = ('name', 'organization', 'college')  # Ensures the combination is unique

    def __str__(self):
        org_name = self.organization.name if self.organization else "No Org"
        col_name = self.college.name if self.college else "No College"
        return f"{self.name} - {org_name} - {col_name}"
    
    def clean(self):
        if not self.organization and not self.college:
            raise ValidationError('Either organization or college must be set.')
        
        if self.organization and self.college:
            raise ValidationError('Either organization or college must be set not both.')