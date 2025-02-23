from odoo import fields,models,api

class Student(models.Model):
    _name= 'edu.student'
    _description='Student Model'


    name=fields.Char('Student Name')
    email=fields.Char('E-mail Address')
    mobile_number=fields.Char(string='Mobile Number')

    # student_list_field=fields.Html(string='Student List')
    # @api.depends()
    # def _compute_student_list_field(self):
    #     for record in self:
    #         record.student_list_field= "<div> <t t-esc='widget('student_list')' /t> </div>"
            