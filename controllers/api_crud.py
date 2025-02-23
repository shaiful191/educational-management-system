from odoo import http

class CrudApi(http.Controller):

    # Get
    @http.route('/api/contacts',auth='public',csrf=False, type='json' ,methods=['GET','POST'])
    def getApi(self, **kw):
        contacts= http.request.env['edu.student'].sudo().search([])

        contuct_list=[]
        for contact in contacts:
           contuct_list.append(
               {
               "name": contact.name,
               "email": contact.email,
               }
           )   

        return contuct_list
    


    # Post 
    @http.route('/api/contacts/create',auth='public',csrf=False, type='json' ,methods=['GET','POST'])
    def create(self, **kw):      
        http.request.env['edu.student'].sudo().create({
            "name":kw['name'],
            'email':kw['email'],
            'mobile_number':kw['mobile_number']
        })

        return kw
    

    # Edit 
    @http.route('/api/contacts/edit',auth='public',csrf=False, type='json' ,methods=['GET','POST'])
    def edit(self, **kw): 

        user = http.request.env['edu.student'].sudo().search([("id","=",kw["id"])])  
        user.write(
            { 
                'name':kw['name'],
                'email':kw['email'],
                'mobile_number':kw['mobile_number']

             }
            )   
       

        return kw