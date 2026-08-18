"""
Створіть клас Employee, який має атрибути name та salary.
Далі створіть два класи, Manager та Developer, які успадковуються від Employee.
Клас Manager повинен мати додатковий атрибут department, а клас Developer - атрибут programming_language.
Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer.Цей клас представляє керівника з команди розробників.
Клас TeamLead повинен мати всі атрибути як Manager (ім'я, зарплата, відділ),
а також атрибут team_size, який вказує на кількість розробників у команді, якою керує керівник.
Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead
"""

class Employee:
    _mandatory_fields = {'name', 'salary'}
    def __init__(self, **kwargs):
        self._validate_mandatory_fields(set(kwargs.keys()))
        self.name = kwargs['name']
        self.salary = kwargs['salary']

    def _validate_mandatory_fields(self, provided_fields:set):
        required_fields = self.__class__.get_mandatory_fields()
        if not required_fields.issubset(provided_fields):
            raise TypeError (f'Following mandatory parameter(s) for "{self.__class__.__name__}" instance are lost: {required_fields - provided_fields}')

    def __str__(self):
        self_keys = {x for x in dir(self) if not (callable(getattr(self, x)) or x.startswith("_"))}
        result_string = f'"{self.name}" is instance of "{self.__class__.__name__}" class and has the following parameters: \n'
        for key in self_keys:
            result_string += f'\t {key} = {self.__dict__[key]} \n'
        return result_string

    @classmethod
    def get_mandatory_fields(cls):
        return cls._mandatory_fields

class Manager(Employee):
    _mandatory_fields = Employee.get_mandatory_fields().union({'department'})

    def __init__(self, **kwargs):
        # Check mandatory fields
        if type(self) is Manager:
            self._validate_mandatory_fields(set(kwargs.keys()))
        # Set 'department' for Manager or TeamLead
        if type(self) in [Manager, TeamLead]:
            self.department = kwargs['department']
        # Set rest of params via parent class
        super().__init__(**kwargs)

class Developer(Employee):
    _mandatory_fields = Employee.get_mandatory_fields().union({'programming_language'})

    def __init__(self, **kwargs):
        # Check all mandatory fields are provided
        if type(self) is Developer:
            self._validate_mandatory_fields(set(kwargs.keys()))
            # Set 'programming_language' only for Developer
            self.programming_language = kwargs['programming_language']
        # Set rest of params via parent class
        super().__init__(**kwargs)

class TeamLead(Manager, Developer):
    _mandatory_fields = Manager.get_mandatory_fields().union({'team_size'})

    def __init__(self, **kwargs):
        # Check mandatory fields
        self._validate_mandatory_fields(set(kwargs.keys()))
        # Set 'team_size' only for TeamLead
        self.team_size = kwargs['team_size']
        # Set rest of params via parent class
        super().__init__(**kwargs)

def check_team_lead_inherits_all_attrs(team_lead_instance:TeamLead):
    provided_team_lead_attributes = {x for x in dir(team_lead_instance) if not (callable(x) or x.startswith("_"))}

    for target_class in (Developer, Manager):
        print(f"\nCheck if '{team_lead_instance.name}' has all attributes from '{target_class.__name__}' class: ", end='')
        if target_class.get_mandatory_fields().issubset(provided_team_lead_attributes):
            print("PASSED")
        else:
            print(f"FAILED\n\tFollowing attributes are missed: {target_class.get_mandatory_fields() - provided_team_lead_attributes}")

dev_instance = Developer(name = 'Artem', salary = 2500, programming_language = 'Java')
manager_instance = Manager(name = 'Svyat', salary = 4000, department = 'QA')
team_lead_instance = TeamLead(name = 'Viktor', salary = 4500, department = 'R&D', team_size = 12)

print(dev_instance)
print(manager_instance)
print(team_lead_instance)

check_team_lead_inherits_all_attrs(team_lead_instance)