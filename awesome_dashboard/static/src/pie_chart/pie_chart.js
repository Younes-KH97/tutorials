/** @odoo-module **/

import { Component, onWillStart, onMounted, onWillUnmount, useRef } from "@odoo/owl"
import { useService } from "@web/core/utils/hooks";
import { getColor } from "@web/core/colors/colors";
import { loadJS } from "@web/core/assets";

export class PieChart extends Component {
    static template = "awesome_dashboard.PieChart"

    setup() {
        this.canvasRef = useRef("canvas")
        this.statistics = useService("awesome_dashboard.statistics");
        onWillStart(() => loadJS(["/web/static/lib/Chart/Chart.js"]));
        onWillStart(async () => this.statistics = await this.statistics.loadStatistics());
        onMounted(() => this.renderChart())
        onWillUnmount(() => this.chart.destroy())

    }

    renderChart() {
        let stats = this.statistics["orders_by_size"]
        console.log(stats)
        console.log(stats)
        let labels = Object.keys(stats)
        let label = "Some title"
        let data = Object.values(stats)
        let color = labels.map((_, index) => getColor(index));
        console.log(labels)
        console.log(data)
        this.chart = new Chart(this.canvasRef.el, {
          type: "pie",
          data: {
              labels: labels,
              datasets: [
                  {
                      label: this.props.label,
                      data: data,
                      backgroundColor: color,
                  },
              ],
          },
      });
          // return "this.chart"
    }
}