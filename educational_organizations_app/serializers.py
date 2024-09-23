import os
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext_lazy
from rest_framework import serializers
from common.models import *
from .models import *
from django_countries import countries
from rest_framework.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify


class EducationalOrganizationsCategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255,  error_messages={
        'max_length': _("Ensure this field has no more than 255 characters.")
    })
    description = serializers.CharField(allow_blank=True, allow_null=True)

    class Meta:
        model = EducationalOrganizationsCategory
        fields = ['id', 'name', 'description']
        
        
def validate_file_extension(value):
    if value is not None:
        ext = os.path.splitext(value.name)[1]  # Get file extension
        valid_extensions = ['.jpg', '.jpeg', '.png']
        if not ext.lower() in valid_extensions:
            raise ValidationError(_('Unsupported file extension. Please upload a JPG, JPEG, or PNG file.'))

    
            
class EducationalOrganizationsSerializer(serializers.ModelSerializer):
    
    def validate_document_file(self, value):
        if value:
            content_type = value.content_type
            if not content_type.startswith('image/') and content_type != 'application/pdf' and content_type != 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
                raise serializers.ValidationError("Only JPG, PNG, GIF images, PDFs, and DOCX files are allowed.")
        return value
    
    name = serializers.CharField(
        max_length=255,
        error_messages={
            'max_length': _("Ensure this field has no more than 255 characters.")
        }
    )
    
    slug = serializers.SerializerMethodField()
    
    web_address = serializers.URLField(
        allow_blank=True,
        allow_null=True,
        error_messages={
            'invalid': _("Enter a valid URL.")
        }
    )
    statement = serializers.CharField(
        allow_blank=True,
        allow_null=True
    )

    address_line1 = serializers.CharField(
        max_length=255,
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        error_messages={
            'max_length': gettext_lazy("Ensure this field has no more than 255 characters."),
        })
    address_line2 = serializers.CharField(
        max_length=255,
        required=False,
        allow_blank=True,
        trim_whitespace=True,
        error_messages={
            'max_length': gettext_lazy("Ensure this field has no more than 255 characters."),
        })
    city = serializers.CharField(
        max_length=255,
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        error_messages={
            'max_length': gettext_lazy("Ensure this field has no more than 255 characters."),
        })
    state_province = serializers.PrimaryKeyRelatedField(
        queryset=State.objects.all(),
        required=False,
        allow_null=True
    )
    state_province_name = serializers.CharField(
        source='state_province.name', read_only=True
    )
    under_category = serializers.PrimaryKeyRelatedField(
        queryset=EducationalOrganizationsCategory.objects.all(),
        required=False,
        allow_null=True
    )
    under_category_name = serializers.CharField(
        source='under_category.name', read_only=True
    )
    postal_code = serializers.CharField(
        max_length=20,
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        error_messages={
            'max_length': gettext_lazy("Ensure this field has no more than 20 characters."),
        })
    country_code = serializers.CharField(
        max_length=2,
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        error_messages={
            'max_length': gettext_lazy("Ensure this field has no more than 2 characters."),
        })
    country_name = serializers.SerializerMethodField()
    document_name = serializers.SerializerMethodField()
    
    created_by = serializers.ReadOnlyField(source='created_by.username')
    updated_by = serializers.ReadOnlyField(source='updated_by.username')
    
    
    class Meta:
        model = EducationalOrganizations
        fields = [
            'id', 'name', 'under_category', 'web_address', 'statement', 'status',
            'updated_at',
            'created_by','updated_by',
            'address_line1', 'address_line2', 'city', 'document', 'document_name',
            'state_province', 'state_province_name', 'under_category_name', 'postal_code', 'country_code', 'country_name',
            'slug'
            ]
        extra_kwargs = {
            'under_category': {
                'error_messages': {
                    'null': _("Category is required."),
                    'invalid': _("Invalid category.")
                }
            }
        }
        
        
    def validate_name(self, value):
        instance = self.instance
        under_category = self.initial_data.get('under_category') or (instance.under_category.id if instance and instance.under_category else None)
        country_code = self.initial_data.get('country_code') or (instance.country if instance else None)
        city = self.initial_data.get('city') or (instance.city if instance else None)

        existing_instance = EducationalOrganizations.objects.filter(
            name=value,
            under_category=under_category,
            country_code=country_code,
            city=city
        ).exclude(pk=instance.pk if instance else None).first()
        
        if existing_instance:
            raise serializers.ValidationError(_("A duplicate entry with the same name, category, country, and city already exists."))

        return value

    
    def create(self, validated_data):
        request = self.context.get('request')
        if request is None:
            raise KeyError("The 'request' context is not available.")
        
        user = request.user
        validated_data['created_by'] = user
        validated_data['updated_by'] = user
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        request = self.context.get('request')
        if request is None:
            raise KeyError("The 'request' context is not available.")
        
        user = request.user
        validated_data['updated_by'] = user
        return super().update(instance, validated_data)
    
    def get_country_name(self, obj):
        return countries.name(obj.country_code) if obj.country_code else None

    def get_document_name(self, obj):
        return obj.document.file_name_system if obj.document else None
    
    def get_slug(self, obj):
        return slugify(obj.name)