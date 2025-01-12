from random import randint


class Employee:
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.name = kwargs['name']

    def get_info(self):
        return f'id - {self.id}; name - {self.name}'


class Manager(Employee):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.department = kwargs['department']

    def get_info(self):
        return f'{super().get_info()}; department - {self.department}'

    def manage_project(self, title):
        print(f'{self.name} from the department {self.department} headed a new project - {title}')


class Technician(Employee):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.specialization = kwargs['specialization']

    def get_info(self):
        return f'{super().get_info()}; specialization - {self.specialization}'

    def perform_maintenance(self, breakdown):
        print(f'{self.name}, the {self.specialization}, is fixing {breakdown} now...')


class TechManager(Manager, Technician):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.specialization = kwargs['specialization']
        self.team = []

    def get_info(self):
        return f'{super().get_info()}'

    def add_employee(self, employee: Employee):
        self.team.append(employee)

    def get_team_info(self):
        return f'total subordinates - {len(self.team)}\n' + '\n'.join([f'{i+1}. {self.team[i].get_info()}' for i in range(len(self.team))])

ppl1 = Employee(id='CZ1996OG', name='Leo Bonhart')
ppl2 = Employee(id='SN1925MT', name='Vito Scaletta')
mng = Manager(id='25BD6674', name="Kim Kitsuragi", department='InfoSec 57')
thn = Technician(id='KHR4546B', name='Ryley Robinson', specialization='Non-Essential Systems Maintenance Chief')
tmg = TechManager(id='DC7A8309', name='Harrier Du Bois', department='Infosec 41', specialization='Cyber Security Officer')
tmg.add_employee(ppl1)
tmg.add_employee(ppl2)
tmg.add_employee(mng)
tmg.add_employee(thn)
print(tmg.get_info())
print(tmg.get_team_info())
thn.perform_maintenance('some stuff')
mng.manage_project('creating a quantum computer')
thn.perform_maintenance('fire extinguishing system')
