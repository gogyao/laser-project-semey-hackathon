let chartInstance = null;

document.getElementById("chartsModal").addEventListener("show.bs.modal", function (event) {
    const button = event.relatedTarget; 
    const chartType = button.getAttribute("data-chart");

    renderChart(chartType, button); 
});

function renderChart(type, button) {
    const ctx = document.getElementById("chartCanvas").getContext("2d");

    if (chartInstance) {
        chartInstance.destroy();
    }

    let data;
    let chartConfig = {};

    if (type === "fields") {
        data = JSON.parse(button.getAttribute("data-fields"));

        chartConfig = {
            type: "bar",
            data: {
                labels: data.map(f => f.name),
                datasets: [{
                    label: "Площадь участков",
                    data: data.map(f => f.area),
                    backgroundColor: "rgba(0, 123, 255, 0.5)"
                }]
            },
            options: { responsive: true }
        };
    }

    if (type === "operations") {
        data = JSON.parse(button.getAttribute("data-operations"));

        chartConfig = {
            type: "line",
            data: {
                labels: data.map(o => o.field_name),
                datasets: [{
                    label: "Найдено сорняков",
                    data: data.map(o => o.detected_weeds),
                    borderColor: "rgba(255, 99, 132, 1)",
                    backgroundColor: "rgba(255, 99, 132, 0.2)",
                    fill: true
                }]
            },
            options: { responsive: true }
        };
    }

    chartInstance = new Chart(ctx, chartConfig);
}
