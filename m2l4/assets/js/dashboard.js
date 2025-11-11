(function () {
    const rootStyles = getComputedStyle(document.documentElement);
    const palette = {
        primary: rootStyles.getPropertyValue('--brand-secondary').trim() || '#1f77b4',
        accent: rootStyles.getPropertyValue('--brand-primary').trim() || '#c62828',
        success: rootStyles.getPropertyValue('--brand-success').trim() || '#1f9d55',
        warning: rootStyles.getPropertyValue('--brand-warning').trim() || '#f59f00',
        neutral: '#f1f5f9',
        surface: '#ffffff'
    };
    const fontFamily = rootStyles.getPropertyValue('--font-family-base').trim() || 'Inter, sans-serif';

    const hexToRgba = (hex, alpha = 1) => {
        const sanitized = hex.replace('#', '');
        const bigint = parseInt(sanitized, 16);
        const r = (bigint >> 16) & 255;
        const g = (bigint >> 8) & 255;
        const b = bigint & 255;
        return `rgba(${r}, ${g}, ${b}, ${alpha})`;
    };

    const defaultConfig = { responsive: true, displayModeBar: false };
    const withBaseLayout = (overrides = {}) => Object.assign({
        font: { family: fontFamily, color: '#1f2937' },
        paper_bgcolor: palette.surface,
        plot_bgcolor: palette.surface,
        margin: { l: 40, r: 20, t: 60, b: 60 }
    }, overrides);

    const timelinePhases = [
        {
            month: 'Mes 1',
            title: 'Fundación',
            detail: 'Casos 1-2 · Setup perfil, templates y primeros análisis',
            color: palette.primary
        },
        {
            month: 'Mes 2',
            title: 'Aceleración',
            detail: 'Casos 3-4 · Networking activo y visualizaciones creativas',
            color: palette.success
        },
        {
            month: 'Mes 3',
            title: 'Consolidación',
            detail: 'Casos 5-6 · Portfolio web y machine learning avanzado',
            color: palette.warning
        },
        {
            month: 'Mes 4',
            title: 'Culminación',
            detail: 'Casos 7-8 · Casos sofisticados y evaluación final',
            color: palette.accent
        }
    ];

    const timelineData = [{
        x: timelinePhases.map(phase => phase.month),
        y: timelinePhases.map(() => 1),
        type: 'bar',
        marker: {
            color: timelinePhases.map(phase => phase.color),
            line: { color: palette.surface, width: 1.5 }
        },
        text: timelinePhases.map(phase => phase.title.toUpperCase()),
        textposition: 'inside',
        textfont: { family: fontFamily, size: 14, color: '#ffffff' },
        textangle: 0,
        insidetextanchor: 'middle',
        hovertemplate: '<b>%{text}</b><br>%{customdata}<extra></extra>',
        customdata: timelinePhases.map(phase => phase.detail),
        showlegend: false
    }];
    const timelineLayout = withBaseLayout({
        title: {text: 'CRONOGRAMA DEL PROYECTO · 4 MESES', font: {family: fontFamily, size: 20}, x: 0.5},
        xaxis: {showgrid: false},
        yaxis: {visible: false},
        margin: {l: 0, r: 0, t: 60, b: 40},
        height: 360
    });
    Plotly.newPlot('timeline-chart', timelineData, timelineLayout, defaultConfig);

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
            line: {color: palette.primary, width: 3},
            marker: {size: 8},
            fill: 'tozeroy',
            fillcolor: hexToRgba(palette.primary, 0.18)
        },
        {
            x: weeks,
            y: followers,
            mode: 'lines+markers',
            name: 'Seguidores',
            line: {color: palette.success, width: 3},
            marker: {size: 8},
            fill: 'tozeroy',
            fillcolor: hexToRgba(palette.success, 0.18)
        },
        {
            x: weeks,
            y: connections,
            mode: 'lines+markers',
            name: 'Conexiones',
            line: {color: palette.warning, width: 3},
            marker: {size: 8},
            fill: 'tozeroy',
            fillcolor: hexToRgba(palette.warning, 0.18)
        }
    ];
    const metricsLayout = withBaseLayout({
        title: {text: 'PROYECCIÓN DE MÉTRICAS CLAVE', font: {family: fontFamily, size: 22}, x: 0.5},
        showlegend: true,
        legend: {orientation: 'h', y: -0.2},
        plot_bgcolor: palette.surface,
        paper_bgcolor: palette.neutral,
        height: 480,
        annotations: [{text: 'Meta: 20%', x: 1, xref: 'paper', y: 20, yref: 'y1', showarrow: false, font: {size: 14}}],
        shapes: [{type: 'line', x0: 1, x1: 16, y0: 20, y1: 20, line: {color: palette.accent, dash: 'dash'}}]
    });
    Plotly.newPlot('metrics-chart', metricsData, metricsLayout, defaultConfig);

    const contentData = [{
        type: 'scatterpolar',
        r: [85,78,92,75,88,83,79,90,85],
        theta: ['Retail','Marketing','Salud','Social Media','Telecom','Finanzas','Logística','Seguridad','Retail'],
        fill: 'toself',
        fillcolor: hexToRgba(palette.primary, 0.22),
        line: {color: palette.primary, width: 2},
        marker: {size: 10},
        text: ['Análisis Predictivo','Clustering','Dashboards','NLP','Machine Learning','Series Temporales','Optimización','Detección de anomalías','Análisis Predictivo'],
        hovertemplate: '<b>%{theta}</b><br>Técnica: %{text}<br>Impacto: %{r}%<extra></extra>'
    }];
    const contentLayout = withBaseLayout({
        title: {text: 'ESTRATEGIA DE CONTENIDO POR INDUSTRIA', font: {family: fontFamily, size: 20}, x: 0.5},
        polar: {radialaxis: {visible: true, range: [0,100], ticksuffix: '%'}},
        showlegend: false,
        height: 420
    });
    Plotly.newPlot('content-chart', contentData, contentLayout, defaultConfig);

    const riskLabels = ['Bajo engagement inicial','Falta de tiempo','Agotamiento de ideas','Críticas técnicas','Competencia saturada'];
    const riskX = [70,60,50,40,50];
    const riskY = [80,80,70,60,40];
    const riskStrategies = [
        'Promoción cruzada + Beta testing',
        'Batch creation + Templates',
        'Banco 20+ ideas + Colaboraciones',
        'Triple verificación + Respuesta 24h',
        'Nicho específico + Calidad premium'
    ];

    const riskData = [{
        type: 'scatter',
        mode: 'markers',
        x: riskX,
        y: riskY,
        text: riskLabels.map(label => label.toUpperCase()),
        textposition: ['top center','top right','top left','top left','bottom right'],
        textfont: { family: fontFamily, size: 12, color: '#0f172a' },
        hovertemplate: '<b>%{text}</b><br>Probabilidad: %{x}%<br>Impacto: %{y}%<br>Estrategia: %{customdata}<extra></extra>',
        customdata: riskStrategies,
        marker: {
            size: [28,28,23,18,23],
            color: [palette.accent,palette.accent,palette.warning,palette.warning,palette.warning],
            line: {color: 'white', width: 2}
        }
    },
    {
        type: 'scatter',
        mode: 'markers',
        x: riskX,
        y: riskY,
        marker: {
            size: [28,28,23,18,23],
            opacity: 0,
            color: 'rgba(0,0,0,0)'
        },
        showlegend: false,
        hoverinfo: 'none'
    }];
    const riskLayout = withBaseLayout({
        title: {text: 'MATRIZ DE RIESGOS Y MITIGACIÓN', font: {family: fontFamily, size: 20}, x: 0.5},
        showlegend: false,
        xaxis: {title: 'Probabilidad (%)', range: [0,100]},
        yaxis: {title: 'Impacto (%)', range: [0,100]},
        shapes: [
            {type: 'rect', x0: 50, x1: 100, y0: 50, y1: 100, fillcolor: 'rgba(198,40,40,0.12)', line: {width: 0}},
            {type: 'rect', x0: 0, x1: 50, y0: 50, y1: 100, fillcolor: 'rgba(245,159,0,0.12)', line: {width: 0}},
            {type: 'rect', x0: 50, x1: 100, y0: 0, y1: 50, fillcolor: 'rgba(245,159,0,0.12)', line: {width: 0}},
            {type: 'rect', x0: 0, x1: 50, y0: 0, y1: 50, fillcolor: 'rgba(31,157,85,0.12)', line: {width: 0}}
        ],
        height: 420
    });
    Plotly.newPlot('risk-chart', riskData, riskLayout, defaultConfig);
})();

