/** @odoo-module */
import { registry } from "@web/core/registry"
import { useService } from "@web/core/utils/hooks"

const { Component } = owl
const { onWillStart, useState } = owl.hooks;
export class StudentList extends Component {
    setup() {
        this.state = useState({
           
        })
       
        this.rpc = useService("rpc")
        this.actionService = useService("action")
        onWillStart(async () => {
            await this.fetchdata()
        })
        

    }
   
    async fetchdata() {
       
        let StudentInfo = await this.rpc("/api/students")

        StudentInfo = JSON.parse(StudentInfo)

        this.state.StudentInfo = StudentInfo
        console.log(StudentInfo)
    }

    
    
    }
    

StudentList.template= "owl.student_list_owl_view"
registry.category("actions").add("edu_ms.StudentList",StudentList);





