import json
from odoo import http
from odoo.http import request


class Student(http.Controller):
        
        @http.route('/api/students',auth='public', type='json')
        def getApi(self, **data):
            print("%"*50,"This is Shaiful")
            students=request.env['edu.student'].search([])
          
            if not students:
                 return json.dumps([])

            student_list=[]
            for student in students:
                student_list.append(
                 {
                    "name": student.name,
                    "email": student.email,
                    "mobile":student.mobile_number
                  }
                 )   
            print("^"*50,student_list)
            return json.dumps(student_list)