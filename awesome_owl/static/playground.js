/** @odoo-module **/

import { Component, useState } from "@odoo/owl";

export class MyComponent extends Component {
    static template = "awesome_owl.playground"

    setup() {
        this.state = useState({ val : 101  });
    }
}