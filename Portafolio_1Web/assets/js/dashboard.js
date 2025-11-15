// Dashboard interactivo con Plotly
document.addEventListener('DOMContentLoaded', function() {
    
    // Configuración común para todos los gráficos
    const commonLayout = {
        paper_bgcolor: 'rgba(0,0,0,0)',
        plot_bgcolor: 'rgba(248,250,252,0.5)',
        font: { family: 'Inter, sans-serif', size: 12 },
        margin: { t: 40, r: 20, b: 40, l: 40 }
    };
    
    const config = { 
        responsive: true, 
        displayModeBar: false 
    };
    
    // Gráfico 1: Cronograma del proyecto
    if (document.getElementById('timeline-chart')) {
        const timelineData = [{
            x: ['Mes 1', 'Mes 2', 'Mes 3', 'Mes 4'],
            y: [2, 2, 2, 2],
            type: 'bar',
            name: 'Casos planificados',
            marker: {
                color: ['#63a8d3', '#ff9a68', '#ffb191', '#4f6fad'],
                line: { color: '#fff', width: 2 }
            },
            text: [2, 2, 2, 2],
            textposition: 'auto',
            hovertemplate: '<b>%{x}</b><br>Casos: %{y}<extra></extra>'
        }];
        
        const timelineLayout = {
            ...commonLayout,
            title: { text: 'Distribución de casos por mes', font: { size: 16 } },
            yaxis: { title: 'Número de publicaciones', gridcolor: '#e0e0e0' },
            xaxis: { title: '' }
        };
        
        Plotly.newPlot('timeline-chart', timelineData, timelineLayout, config);
    }
    
    // Gráfico 2: Proyección de métricas clave
    if (document.getElementById('metrics-chart')) {
        const metricsData = [{
            x: ['Engagement', 'Crecimiento Red', 'Casos Publicados'],
            y: [20, 30, 8],
            type: 'bar',
            name: 'Objetivos',
            marker: {
                color: '#ff9a68',
                line: { color: '#fff', width: 2 }
            },
            text: ['20%', '+30%', '8 casos'],
            textposition: 'auto',
            hovertemplate: '<b>%{x}</b><br>Meta: %{text}<extra></extra>'
        }];
        
        const metricsLayout = {
            ...commonLayout,
            title: { text: 'Objetivos del proyecto', font: { size: 16 } },
            yaxis: { title: 'Valor objetivo', gridcolor: '#e0e0e0' },
            xaxis: { title: '' }
        };
        
        Plotly.newPlot('metrics-chart', metricsData, metricsLayout, config);
    }
    
    // Gráfico 3: Estrategia de contenido (Pie Chart)
    if (document.getElementById('content-chart')) {
        const contentData = [{
            labels: ['Casos de estudio', 'Artículos técnicos', 'Videos tutoriales', 'Infografías'],
            values: [8, 4, 2, 3],
            type: 'pie',
            marker: {
                colors: ['#63a8d3', '#ff9a68', '#ffb191', '#4f6fad'],
                line: { color: '#fff', width: 2 }
            },
            textinfo: 'label+percent',
            textposition: 'inside',
            hovertemplate: '<b>%{label}</b><br>Cantidad: %{value}<br>Porcentaje: %{percent}<extra></extra>'
        }];
        
        const contentLayout = {
            ...commonLayout,
            title: { text: 'Distribución de tipos de contenido', font: { size: 16 } },
            showlegend: true,
            legend: { orientation: 'h', y: -0.1 }
        };
        
        Plotly.newPlot('content-chart', contentData, contentLayout, config);
    }
    
    // Gráfico 4: Matriz de riesgos (Heatmap)
    if (document.getElementById('risk-chart')) {
        const riskData = [{
            x: ['Bajo', 'Medio', 'Alto'],
            y: ['Tiempo', 'Recursos', 'Engagement'],
            z: [[1, 2, 1], [2, 3, 2], [1, 2, 3]],
            type: 'heatmap',
            colorscale: [
                [0, '#78d9ad'],
                [0.5, '#ffe28f'],
                [1, '#f59898']
            ],
            showscale: true,
            hovertemplate: '<b>%{y}</b><br>Nivel: %{x}<br>Riesgo: %{z}<extra></extra>',
            colorbar: {
                title: 'Nivel de<br>Riesgo',
                tickvals: [1, 2, 3],
                ticktext: ['Bajo', 'Medio', 'Alto']
            }
        }];
        
        const riskLayout = {
            ...commonLayout,
            title: { text: 'Análisis de riesgos del proyecto', font: { size: 16 } },
            xaxis: { title: 'Probabilidad', side: 'bottom' },
            yaxis: { title: 'Factor de riesgo' }
        };
        
        Plotly.newPlot('risk-chart', riskData, riskLayout, config);
    }
    
    // Hacer los gráficos responsivos
    window.addEventListener('resize', function() {
        const charts = ['timeline-chart', 'metrics-chart', 'content-chart', 'risk-chart'];
        charts.forEach(chartId => {
            const chartDiv = document.getElementById(chartId);
            if (chartDiv) {
                Plotly.Plots.resize(chartDiv);
            }
        });
    });
});

// Manejo del formulario de contacto
const contactForm = document.querySelector('.form-corporate');
if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const name = document.getElementById('contactName').value;
        const email = document.getElementById('contactEmail').value;
        
        // Simulación de envío exitoso
        alert(`¡Gracias ${name}! Tu mensaje ha sido enviado correctamente. Te contactaremos a ${email} pronto.`);
        
        // Limpiar formulario
        this.reset();
    });
}
