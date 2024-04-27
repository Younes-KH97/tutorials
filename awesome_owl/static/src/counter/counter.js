/** @odoo-module **/
import { Component, useState } from "@odoo/owl";

export class Counter extends Component {
    static template = "awesome_owl.counter"

    static props = {
        onchange: {type: Function, optional: true}
    }

    setup() {
        this.state = useState({ value: 1  });;    
    }

    increment() {
        this.state.value = this.state.value + 1
        if(this.props.onchange){
            this.props.onchange()
        }
    }
}