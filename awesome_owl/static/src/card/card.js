/** @odoo-module **/
import { Component, useState } from "@odoo/owl";

export class Card extends Component {
    static template = "awesome_owl.Card"
    static props = {
        title: String,
        // content: [String, Number]
        slots: {
            type: Object,
            shape: {
                default: true
            },
        }
    }
    setup(){
        this.toggleState = useState({value : true});
    }
    onToggleState() {
        this.toggleState.value = !this.toggleState.value
    }
}
