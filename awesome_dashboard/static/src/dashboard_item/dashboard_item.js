/** @odoo-module **/

import {Component} from "@odoo/owl";

export class DashboardItem extends Component {
    static template = "awesome_dashboard.DashboardItem"
    static props = {
        size: { type: Number,
                default: 1,
                optional: true
              },
        // content: [String, Number]
        slots: {
            type: Object,
            shape: {
                default: true
            },
        },
        result: {
            type: Object,
            optional: true
        }
    }
    // setup() {
        
    // }
}