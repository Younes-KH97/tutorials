/** @odoo-module **/
import { Component } from "@odoo/owl";

export class TodoItem extends Component {
    static template = "awesome_owl.TodoItem"

    static props = {
        todo : {type: Object,
                shape: { id: Number, description: String, isCompleted: Boolean }
        },
        toggleState: {type: Function},
        removeTodo: {type: Function},
        id: {type: Number}
    }

    toggleState(){
        this.props.toggleState(this.props.id)
    }

    removeTodo(){
        this.props.removeTodo(this.props.id)
    }

}