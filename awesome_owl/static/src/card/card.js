/** @odoo-module **/
import { Component } from "@odoo/owl";

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
}
