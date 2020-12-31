var ctx = document.getElementById("barchart");
var mybarChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر"],
        datasets: [{
            label: 'درخواست گذرنامه',
            backgroundColor: "#26B99A",
            data: [51, 30, 40, 28, 92, 50, 45]
        }, {
            label: 'درخواست کارت ملی',
            backgroundColor: "#03586A",
            data: [41, 56, 25, 48, 72, 34, 12]
        },{
            label: 'درخواست گواهینامه',
            backgroundColor: "#2d2d2d",
            data: [38, 45, 32, 75, 10, 15, 40]
        }]
    },

    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});
