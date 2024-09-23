
from django.shortcuts import get_object_or_404
from college_app.models import College
from department_app.models import Department
from college_app.serializers import CollegeSerializer
from department_app.serializers import DepartmentSerializer
from campus_app.serializers import CampusSerializer
from educational_organizations_app.serializers import EducationalOrganizationsSerializer

class CollegeDataService:
    def __init__(self, college_id):
        self.college = self._get_college_by_id(college_id)

    def _get_college_by_id(self, college_id):
        try:
            return get_object_or_404(College, id=college_id)
        except Exception as e:
            return None

    def get_college_data(self):
        if not self.college:
            return None
        return CollegeSerializer(self.college).data

    def get_department_data(self):
        if not self.college:
            return []
        departments = Department.objects.filter(college=self.college)
        return DepartmentSerializer(departments, many=True).data

    def get_campus_data(self):
        if not self.college or not self.college.campus:
            return None
        
        campus_data = CampusSerializer(self.college.campus).data
        
        if 'organization' in campus_data:
            del campus_data['organization']

        return campus_data

    def get_organization_data(self):
        if not self.college or not self.college.campus or not self.college.campus.educational_organization:
            return None

        organization_data = EducationalOrganizationsSerializer(self.college.campus.educational_organization).data
        return organization_data

    def get_full_college_data(self):
        if not self.college:
            return {'college': None, 'departments': [], 'campus': None, 'organization': None}
        return {
            'college': self.get_college_data(),
            'departments': self.get_department_data(),
            'campus': self.get_campus_data(),
            'organization': self.get_organization_data(),
        }

    @staticmethod
    def get_all_colleges_data():
        return [
            CollegeDataService(college.id).get_full_college_data()
            for college in College.objects.all()
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

    def get_flat_college_data(self):
        college_data = self.get_full_college_data()
        flat_data = {}

        # Flatten the college data with prefix
        if college_data.get('college'):
            flat_data.update(self.flatten_data([college_data['college']], prefix=f"college_{self.college.id}_"))
        
        # Flatten the department data with prefix
        if college_data.get('departments'):
            flat_data.update(self.flatten_data(college_data['departments'], prefix=f"department_{self.college.id}_"))
        
        # Flatten the campus data with prefix
        if college_data.get('campus'):
            flat_data.update(self.flatten_data([college_data['campus']], prefix=f"campus_{self.college.id}_"))

        # Flatten the organization data separately without the campus prefix
        organization_data = college_data.get('organization')
        if organization_data:
            organization_prefix = f"organization_{organization_data['id']}_"
            flat_data.update(self.flatten_data([organization_data], prefix=organization_prefix))

        return flat_data

    @staticmethod
    def get_all_flat_colleges_data():
        return [
            CollegeDataService(college.id).get_flat_college_data()
            for college in College.objects.all()
        ]
