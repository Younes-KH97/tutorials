/** @odoo-module **/

import { Component, useState, useRef, onMounted } from "@odoo/owl";
import { TodoItem } from "./todo_item";
export class TodoList extends Component {
    static template = "awesome_owl.TodoList"
    static components = {TodoItem}

    setup() {
        this.todos = useState([
            { id: 1, description: "do stuff", isCompleted: false },
            { id: 2, description: "buy stuff", isCompleted: true },
            { id: 3, description: "buy milk", isCompleted: false }]);
        this.id = 7;
        this.myRef = useRef('ref_descr');
        // onMounted(() => {
        //    console.log(this.myRef.el);
        // });
    }

    addTodo(e) {
        let description = e.target.value
        if(e.keyCode === 13 && description != ""){
            this.todos.push({id: this.id, description: description, isCompleted: false})
            this.id++
            console.log(this.myRef.el.value)
            e.target.value = ""
            
        }
    }
}