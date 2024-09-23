from django.shortcuts import get_object_or_404
from college_app.models import College
from department_app.models import Department
from campus_app.models import Campus
from educational_organizations_app.models import EducationalOrganizations
from college_app.serializers import CollegeSerializer
from department_app.serializers import DepartmentSerializer
from campus_app.serializers import CampusSerializer
from educational_organizations_app.serializers import EducationalOrganizationsSerializer

class DepartmentDataService:
    def __init__(self, department_id):
        self.department = self._get_department_by_id(department_id)

    def _get_department_by_id(self, department_id):
        try:
            return get_object_or_404(Department, id=department_id)
        except Exception as e:
            return None

    def get_department_data(self):
        if not self.department:
            return None
        return DepartmentSerializer(self.department).data

    def get_college_data(self):
        if not self.department or not self.department.college:
            return None
        return CollegeSerializer(self.department.college).data

    def get_campus_data(self):
        if not self.department or not self.department.college or not self.department.college.campus:
            return None
        
        campus_data = CampusSerializer(self.department.college.campus).data
        
        if 'organization' in campus_data:
            del campus_data['organization']

        return campus_data

    def get_organization_data(self):
        if not self.department or not self.department.college or not self.department.college.campus or not self.department.college.campus.educational_organization:
            return None

        organization_data = EducationalOrganizationsSerializer(self.department.college.campus.educational_organization).data
        return organization_data

    def get_full_department_data(self):
        if not self.department:
            return {'department': None, 'college': None, 'campus': None, 'organization': None}
        return {
            'department': self.get_department_data(),
            'college': self.get_college_data(),
            'campus': self.get_campus_data(),
            'organization': self.get_organization_data(),
        }

    @staticmethod
    def get_all_departments_data():
        return [
            DepartmentDataService(department.id).get_full_department_data()
            for department in Department.objects.all()
        ]

    def flatten_data(self, data_list, prefix):
        flat_data = {}
        if not isinstance(data_list, list):
            print(f"Expected a list but got: {type(data_list)}")
            return flat_data

        for i, item in enumerate(data_list):
            if isinstance(item, dict):
                for k, v in item.items():
                    flat_data[f"{prefix}{k}"] = v  # Removed index from the flattened key
            else:
                print(f"Item {i} is not a dictionary: {item} (type: {type(item)})")
                flat_data[f"{prefix}{i}_value"] = str(item)

        return flat_data

    def get_flat_department_data(self):
        department_data = self.get_full_department_data()
        flat_data = {}

        
        if department_data.get('department'):
            flat_data.update(self.flatten_data([department_data['department']], prefix=f"department_{self.department.id}_"))
        
        
        if department_data.get('college'):
            flat_data.update(self.flatten_data([department_data['college']], prefix=f"college_{self.department.id}_"))
        
        
        if department_data.get('campus'):
            flat_data.update(self.flatten_data([department_data['campus']], prefix=f"campus_{self.department.id}_"))

        
        organization_data = department_data.get('organization')
        if organization_data:
            organization_prefix = f"organization_{organization_data['id']}_"
            flat_data.update(self.flatten_data([organization_data], prefix=organization_prefix))

        return flat_data

    @staticmethod
    def get_all_flat_departments_data():
        return [
            DepartmentDataService(department.id).get_flat_department_data()
            for department in Department.objects.all()
        ]
