$(document).ready(function () {
    var divgroup3 = $("#divgroup2"); // ID'yi kontrol edin
    var divgroup3col1 = $("#animationy");

    var hasAnimated = false; // Animasyon durumunu takip eden bayrak

    $(window).scroll(function () {
        var scrollTop = $(window).scrollTop();
        var divgroup3Top = divgroup3.offset().top;

        if (scrollTop >= divgroup3Top && !hasAnimated) {
            // Animasyonu tetikle ve bayrağı true olarak ayarla
            divgroup3col1.addClass("animated-slide");
            hasAnimated = true;
        }
    });
});



document.addEventListener("DOMContentLoaded", function() {
    const canvas = document.getElementById('myDonutChart');
    const ctx = canvas.getContext('2d');

    const data = {
        datasets: [{
            data: [0],
            backgroundColor: ['#15b8ae'],
        }],
    };

    const options = {
        responsive: false,
        maintainAspectRatio: false,
        cutout: '89%',
        plugins: {
            doughnut: {
                borderWidth: 0.1,
            }
        }
    };

    const chartConfig = {
        type: 'doughnut',
        data: data,
        options: options,
    };

    const myDonutChart = new Chart(ctx, chartConfig);

    const chartContainer = document.getElementById('chart');
    const centerText = document.querySelector('.center-text');

    let currentPercentage = 0;

    function updatePercentage() {
        centerText.innerHTML = currentPercentage + '%';
        myDonutChart.data.datasets[0].data[0] = currentPercentage;
        myDonutChart.update();
        currentPercentage++;

        if (currentPercentage > 100) {
            clearInterval(interval);
        }
    }

    const interval = setInterval(updatePercentage, 13); // Her 100 milisaniyede bir güncelle
});



document.addEventListener("DOMContentLoaded", function() {
    const canvas = document.getElementById('myDonutChart2');
    const ctx = canvas.getContext('2d');

    const data = {
        datasets: [{
            data: [0],
            backgroundColor: ['#15b8ae'],
        }],
    };

    const options = {
        responsive: false,
        maintainAspectRatio: false,
        cutout: '89%',
        plugins: {
            doughnut: {
                borderWidth: 0.1,
            }
        }
    };

    const chartConfig = {
        type: 'doughnut',
        data: data,
        options: options,
    };

    const myDonutChart = new Chart(ctx, chartConfig);

    const chartContainer = document.getElementById('chart2');
    const centerText = document.querySelector('#chart2value');

    let currentPercentage = 0;

    function updatePercentage() {
        centerText.innerHTML = currentPercentage + '%';
        myDonutChart.data.datasets[0].data[0] = currentPercentage;
        myDonutChart.update();
        currentPercentage++;

        if (currentPercentage > 100) {
            clearInterval(interval);
        }
    }

    const interval = setInterval(updatePercentage, 13); // Her 100 milisaniyede bir güncelle
});