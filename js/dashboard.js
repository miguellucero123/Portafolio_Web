(function(){
    const timelineData = [
        {
            x: ['Mes 1','Mes 2','Mes 3','Mes 4'],
            y: [1,1,1,1],
            type: 'bar',
            marker: {color: ['#1f77b4','#2ca02c','#ff7f0e','#d62728']},
            text: [
                '<b>FUNDACIÓN</b><br>Casos 1-2<br><i>Setup perfil, Templates, Primeros análisis</i>',
                '<b>ACELERACIÓN</b><br>Casos 3-4<br><i>Networking activo, Visualizaciones creativas</i>',
                '<b>CONSOLIDACIÓN</b><br>Casos 5-6<br><i>Portfolio web, Machine Learning avanzado</i>',
                '<b>CULMINACIÓN</b><br>Casos 7-8<br><i>Casos sofisticados, Evaluación final</i>'
            ],
            hovertemplate: '%{text}<extra></extra>',
            textposition: 'inside',
            showlegend: false
        }
    ];
    const timelineLayout = {
        title: {text: 'CRONOGRAMA DEL PROYECTO - 4 MESES', font: {family: 'Inter, sans-serif', size: 20}, x: 0.5},
        xaxis: {showgrid: false},
        yaxis: {visible: false},
        margin: {l: 0, r: 0, t: 60, b: 40},
        plot_bgcolor: 'white',
        paper_bgcolor: 'white',
        height: 360
    };
    Plotly.newPlot('timeline-chart', timelineData, timelineLayout, {responsive: true});

    const weeks = Array.from({length:16}, (_,i)=>i+1);
    const engagement = [5,6.2,7.4,8.6,9.8,11,12.2,13.4,14.6,15.8,17,18.2,18.8,19.2,19.5,19.8];
    const followers = [120,140,165,190,215,240,265,290,315,340,365,390,415,440,465,500];
    const connections = [15,20,25,30,35,40,45,50,55,60,66,72,78,84,90,96];
    const metricsData = [
        {
            x: weeks,
            y: engagement,
            mode: 'lines+markers',
            name: 'Engagement',
            line: {color: '#1f77b4', width: 3},
            marker: {size: 8},
            fill: 'tozeroy',
            fillcolor: 'rgba(31,119,180,0.2)'
        },
        {
            x: weeks,
            y: followers,
            mode: 'lines+markers',
            name: 'Seguidores',
            line: {color: '#2ca02c', width: 3},
            marker: {size: 8},
            fill: 'tozeroy',
            fillcolor: 'rgba(44,160,44,0.2)'
        },
        {
            x: weeks,
            y: connections,
            mode: 'lines+markers',
            name: 'Conexiones',
            line: {color: '#ff7f0e', width: 3},
            marker: {size: 8},
            fill: 'tozeroy',
            fillcolor: 'rgba(255,127,14,0.2)'
        }
    ];
    const metricsLayout = {
        title: {text: 'PROYECCIÓN DE MÉTRICAS CLAVE', font: {family: 'Inter, sans-serif', size: 22}, x: 0.5},
        showlegend: true,
        legend: {orientation: 'h', y: -0.2},
        plot_bgcolor: 'white',
        paper_bgcolor: '#f5f7fa',
        height: 480,
        annotations: [{text: 'Meta: 20%', x: 1, xref: 'paper', y: 20, yref: 'y1', showarrow: false, font: {size: 14}}],
        shapes: [{type: 'line', x0: 1, x1: 16, y0: 20, y1: 20, line: {color: '#d62728', dash: 'dash'}}],
        margin: {l: 60, r: 20, t: 80, b: 60}
    };
    Plotly.newPlot('metrics-chart', metricsData, metricsLayout, {responsive: true});

    const contentData = [{
        type: 'scatterpolar',
        r: [85,78,92,75,88,83,79,90,85],
        theta: ['Retail','Marketing','Salud','Social Media','Telecom','Finanzas','Logística','Seguridad','Retail'],
        fill: 'toself',
        fillcolor: 'rgba(31,119,180,0.3)',
        line: {color: '#1f77b4', width: 2},
        marker: {size: 10},
        text: ['Análisis Predictivo','Clustering','Dashboards','NLP','Machine Learning','Series Temporales','Optimización','Detección de anomalías','Análisis Predictivo'],
        hovertemplate: '<b>%{theta}</b><br>Técnica: %{text}<br>Impacto: %{r}%<extra></extra>'
    }];
    const contentLayout = {
        title: {text: 'ESTRATEGIA DE CONTENIDO POR INDUSTRIA', font: {family: 'Inter, sans-serif', size: 20}, x: 0.5},
        polar: {radialaxis: {visible: true, range: [0,100], ticksuffix: '%'}},
        showlegend: false,
        height: 420
    };
    Plotly.newPlot('content-chart', contentData, contentLayout, {responsive: true});

    const riskData = [{
        type: 'scatter',
        mode: 'markers+text',
        x: [70,60,50,40,50],
        y: [80,80,70,60,40],
        text: ['Bajo engagement inicial','Falta de tiempo','Agotamiento de ideas','Críticas técnicas','Competencia saturada'],
        textposition: 'top center',
        customdata: ['Promoción cruzada + Beta testing','Batch creation + Templates','Banco 20+ ideas + Colaboraciones','Triple verificación + Respuesta 24h','Nicho específico + Calidad premium'],
        hovertemplate: '<b>%{text}</b><br>Probabilidad: %{x}%<br>Impacto: %{y}%<br>Estrategia: %{customdata}<extra></extra>',
        marker: {
            size: [28,28,23,18,23],
            color: ['#d62728','#d62728','#ff7f0e','#ff7f0e','#ff7f0e'],
            line: {color: 'white', width: 2}
        }
    }];
    const riskLayout = {
        title: {text: 'MATRIZ DE RIESGOS Y MITIGACIÓN', font: {family: 'Inter, sans-serif', size: 20}, x: 0.5},
        showlegend: false,
        xaxis: {title: 'Probabilidad (%)', range: [0,100]},
        yaxis: {title: 'Impacto (%)', range: [0,100]},
        shapes: [
            {type: 'rect', x0: 50, x1: 100, y0: 50, y1: 100, fillcolor: 'rgba(214,39,40,0.15)', line: {width: 0}},
            {type: 'rect', x0: 0, x1: 50, y0: 50, y1: 100, fillcolor: 'rgba(255,127,14,0.15)', line: {width: 0}},
            {type: 'rect', x0: 50, x1: 100, y0: 0, y1: 50, fillcolor: 'rgba(255,127,14,0.15)', line: {width: 0}},
            {type: 'rect', x0: 0, x1: 50, y0: 0, y1: 50, fillcolor: 'rgba(44,160,44,0.15)', line: {width: 0}}
        ],
        height: 420
    };
    Plotly.newPlot('risk-chart', riskData, riskLayout, {responsive: true});
})();

