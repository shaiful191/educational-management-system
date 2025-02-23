from odoo import fields,models

class CreateStudentWizard(models.TransientModel):
    _name= 'create.student.wizard'
    _description='Create Student Wizard'


    name=fields.Char('Student Name')
    age=fields.Integer('Age')

    def create_student_view_action(self):
        print("Button is clicked")
