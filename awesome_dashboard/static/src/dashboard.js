/** @odoo-module **/

import { Component, onWillStart } from "@odoo/owl";
import { registry } from "@web/core/registry";
import {Layout} from  "@web/search/layout";
import { useService } from "@web/core/utils/hooks";
import { DashboardItem } from "./dashboard_item/dashboard_item";
import { PieChart } from "./pie_chart/pie_chart";

class AwesomeDashboard extends Component {
    static template = "awesome_dashboard.AwesomeDashboard";
    static components = {Layout, DashboardItem, PieChart}
    setup(){
        this.display = {controlPanel:{}}
        this.action = useService("action");
        this.statistics = useService("awesome_dashboard.statistics");
        onWillStart(async () => {
            this.statistics = await this.statistics.loadStatistics();
        });
        // this.rpc = useService("rpc");
        // // this.result = {}
        // onWillStart(async () => {
        //     this.result = await this.rpc("/awesome_dashboard/statistics");
        // });
    }

    showCustomersView() {
        this.action.doAction({
            type: 'ir.actions.act_window',
            res_id: "base.action_partner_form",
            res_model: 'res.partner',
            views: [[false, 'kanban']]});
    }
    showLeadsView() {
        this.action.doAction({
            type: 'ir.actions.act_window',
            res_id: "crm_lead_view_form",
            res_model: 'crm.lead',
            views: [[false, 'list'],[false, 'form']],
        });
    }

    readResult(){
        console.log(this.statistics)
    }
}

registry.category("actions").add("awesome_dashboard.dashboard", AwesomeDashboard);
