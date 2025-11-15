#!/usr/bin/env python3
"""
Portfolio de Marca Personal - Servidor Profesional v3.0
Diseño corporativo minimalista con paleta de colores optimizada
"""

import http.server
import socketserver
import os
import sys
import re
from pathlib import Path

# ============================================================
# CONFIGURACIÓN
# ============================================================
PORT = int(os.environ.get('PORT', 8081))
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

if 'CONDA_DEFAULT_ENV' in os.environ:
    print(f"🐍 Entorno Conda: {os.environ['CONDA_DEFAULT_ENV']}")
    print(f"📂 Directorio: {DIRECTORY}\n")

# ============================================================
# PLANTILLAS HTML PROFESIONALES
# ============================================================

# -------------------- INDEX.HTML --------------------
INDEX_HTML = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Miguel Lucero | Consultoría en Análisis de Datos</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="assets/css/styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@400;700&display=swap" rel="stylesheet">
</head>
<body>
    <!-- Navbar inyectado automáticamente por el servidor -->
    
    <main>
        <!-- Hero Section Profesional -->
        <section class="hero-section">
            <div class="container">
                <div class="row align-items-center min-vh-100">
                    <div class="col-lg-7">
                        <h1 class="hero-title">
                            Transformando Datos en 
                            <span class="text-accent">Decisiones Estratégicas</span>
                        </h1>
                        <h2 class="hero-subtitle">Miguel Ignacio Lucero Gatica</h2>
                        <p class="hero-description">
                            Consultor especializado en análisis de datos con más de 8 años de experiencia 
                            en industrias críticas. Combino metodologías científicas con tecnologías 
                            modernas para entregar insights accionables que impulsan el crecimiento empresarial.
                        </p>
                        <div class="hero-actions">
                            <a href="file:///C:/Users/Alicia_Piero/Documents/Repo_AIEP/Marca_Personal/Portafolio_Web/dashboard_marca_personal.html" class="btn btn-primary">Marca Personal</a>
                            <a href="file:///C:/Users/Alicia_Piero/Documents/Repo_AIEP/Marca_Personal/Portafolio_Web/cv.html" class="btn btn-outline">Conocer Mi Experiencia</a>
                        </div>
                    </div>
                    <div class="col-lg-5">
                        <div class="hero-image">
                            <img src="METGO_3D.JPG" alt="Miguel Lucero - Análisis de Datos" class="img-fluid">
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Propuesta de Valor -->
        <section class="value-section dark-section">
            <div class="container">
                <div class="row g-5 align-items-center">
                    <div class="col-lg-6">
                        <h3 class="section-title">Propuesta de Valor</h3>
                        <p class="section-description">
                            Mi enfoque combina rigor científico con aplicación práctica, 
                            transformando datos complejos en estrategias comprensibles y ejecutables.
                        </p>
                        <div class="value-list">
                            <div class="value-item">
                                <h4>Análisis Predictivo</h4>
                                <p>Modelos estadísticos avanzados para anticipar tendencias y optimizar operaciones.</p>
                            </div>
                            <div class="value-item">
                                <h4>Visualización Ejecutiva</h4>
                                <p>Dashboards intuitivos que facilitan la toma de decisiones a nivel gerencial.</p>
                            </div>
                            <div class="value-item">
                                <h4>Consultoría Estratégica</h4>
                                <p>Acompañamiento integral desde el diagnóstico hasta la implementación de soluciones.</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-6">
                        <div class="stats-grid">
                            <div class="stat-card">
                                <h5>8+</h5>
                                <p>Años de Experiencia</p>
                            </div>
                            <div class="stat-card">
                                <h5>15+</h5>
                                <p>Proyectos Exitosos</p>
                            </div>
                            <div class="stat-card">
                                <h5>3</h5>
                                <p>Industrias Críticas</p>
                            </div>
                            <div class="stat-card">
                                <h5>100%</h5>
                                <p>Compromiso Ético</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Servicios -->
        <section class="services-section">
            <div class="container">
                <h3 class="section-title text-center">Servicios Profesionales</h3>
                <div class="row g-4 mt-4">
                    <div class="col-md-4">
                        <div class="service-card">
                            <h4>Análisis de Datos</h4>
                            <p>Extracción de insights mediante técnicas estadísticas avanzadas y machine learning.</p>
                            <ul class="service-features">
                                <li>Modelos predictivos</li>
                                <li>Análisis descriptivo</li>
                                <li>Segmentación avanzada</li>
                            </ul>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="service-card">
                            <h4>Business Intelligence</h4>
                            <p>Desarrollo de dashboards ejecutivos para monitoreo en tiempo real de KPIs críticos.</p>
                            <ul class="service-features">
                                <li>Dashboards interactivos</li>
                                <li>Reportes automatizados</li>
                                <li>Integración de datos</li>
                            </ul>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="service-card">
                            <h4>Consultoría Estratégica</h4>
                            <p>Asesoramiento especializado para la transformación digital basada en datos.</p>
                            <ul class="service-features">
                                <li>Diagnóstico organizacional</li>
                                <li>Roadmap de datos</li>
                                <li>Capacitación ejecutiva</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- CTA Section -->
        <section class="cta-section">
            <div class="container text-center">
                <h3>¿Listo para potenciar su organización con datos?</h3>
                <p class="lead">Exploremos juntos cómo los datos pueden transformar su negocio</p>
                <div class="cta-actions">
                    <a href="/dashboard_marca_personal.html" class="btn btn-primary btn-lg">Conocer Mi Metodología</a>
                    <a href="#contacto" class="btn btn-outline btn-lg">Agendar Consulta</a>
                </div>
            </div>
        </section>
    </main>

    <footer class="professional-footer">
        <div class="container">
            <div class="row">
                <div class="col-md-6">
                    <p>&copy; 2025 Miguel Ignacio Lucero Gatica. Todos los derechos reservados.</p>
                </div>
                <div class="col-md-6 text-md-end">
                    <a href="/cv.html" class="footer-link">Currículum</a>
                    <a href="/dashboard_marca_personal.html" class="footer-link">Portfolio</a>
                    <a href="mailto:miguellucerogatica@gmail.com" class="footer-link">Contacto</a>
                </div>
            </div>
        </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    <script src="assets/js/scroll.js"></script>
</body>
</html>"""

# -------------------- CV.HTML --------------------
CV_HTML = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CV - Miguel Ignacio Lucero Gatica | Analista de Datos</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="assets/css/styles.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@400;700&display=swap" rel="stylesheet">
</head>
<body>
    <!-- Navbar inyectado automáticamente por el servidor -->

    <div class="cv-container">
        <header class="cv-header">
            <div class="container">
                <div class="row align-items-center">
                    <div class="col-lg-8">
                        <h1 class="cv-name">Miguel Ignacio Lucero Gatica</h1>
                        <h2 class="cv-title">Meteorólogo | Analista de Datos & Desarrollador Front-End</h2>
                        <div class="cv-contact">
                            <span class="contact-item">Quilpué, Chile</span>
                            <span class="contact-separator">•</span>
                            <span class="contact-item">+56 9 9931 9162</span>
                            <span class="contact-separator">•</span>
                            <span class="contact-item">miguellucerogatica@gmail.com</span>
                        </div>
                        <div class="cv-links mt-3">
                            <a href="https://linkedin.com/in/metgo3d/" target="_blank" class="professional-link">LinkedIn</a>
                            <a href="https://github.com/miguellucero123" target="_blank" class="professional-link">GitHub</a>
                        </div>
                    </div>
                    <div class="col-lg-4 text-lg-end mt-4 mt-lg-0">
                        <a href="/dashboard_marca_personal.html" class="btn btn-primary">Ver Portfolio</a>
                        <button onclick="window.print()" class="btn btn-outline">Descargar PDF</button>
                    </div>
                </div>
            </div>
        </header>

        <main class="cv-content">
            <div class="container">
                <!-- Resumen Profesional -->
                <section class="cv-section">
                    <h3 class="cv-section-title">Perfil Profesional</h3>
                    <p class="cv-text">
                        Profesional con sólida formación científica y más de 8 años de experiencia operativa en 
                        industrias de alta exigencia (Minería, Meteorología y Contaminación Atmosférica). Actualmente 
                        cursando el último semestre de Técnico en Análisis de Datos y especializándome en Desarrollo Front-End.
                    </p>
                    <p class="cv-text">
                        Poseo un perfil técnico híbrido que combina el dominio de la ciencia de datos (Python, SQL, Big Data) 
                        con habilidades de desarrollo web y una probada capacidad de gestión en terreno. Participante 
                        seleccionado en programa de emprendimiento global (Santander Explorer). Cuento con un portafolio 
                        activo de más de 15 repositorios en GitHub.
                    </p>
                </section>

                <!-- Competencias -->
                <section class="cv-section">
                    <h3 class="cv-section-title">Competencias Técnicas</h3>
                    <div class="row">
                        <div class="col-md-4">
                            <div class="competency-group">
                                <h4>Lenguajes & Frameworks</h4>
                                <ul class="competency-list">
                                    <li>Python (Certificación PCEP)</li>
                                    <li>SQL Avanzado</li>
                                    <li>HTML5 / CSS3 / JavaScript</li>
                                    <li>Git / GitHub</li>
                                </ul>
                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="competency-group">
                                <h4>Ciencia de Datos</h4>
                                <ul class="competency-list">
                                    <li>Pandas / NumPy</li>
                                    <li>Scikit-learn</li>
                                    <li>Matplotlib / Seaborn</li>
                                    <li>Modelos Predictivos</li>
                                </ul>
                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="competency-group">
                                <h4>Herramientas</h4>
                                <ul class="competency-list">
                                    <li>Jupyter Notebooks</li>
                                    <li>VS Code</li>
                                    <li>Power BI</li>
                                    <li>Campbell Scientific</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- Experiencia -->
                <section class="cv-section">
                    <h3 class="cv-section-title">Experiencia Profesional</h3>
                    
                    <div class="experience-block">
                        <div class="experience-header">
                            <h4 class="job-position">Meteorólogo de Operaciones y Medio Ambiente</h4>
                            <span class="job-period">Agosto 2022 – Abril 2024</span>
                        </div>
                        <h5 class="company-name">SGS CHILE LTDA. (Proyecto ENAMI Paipote)</h5>
                        <ul class="experience-details">
                            <li>Elaboración de pronósticos meteorológicos de alta precisión para la programación estratégica de la producción en fundición de cobre</li>
                            <li>Análisis estadístico mensual de concentraciones de ácido sulfúrico para cumplimiento normativo</li>
                        </ul>
                    </div>

                    <div class="experience-block">
                        <div class="experience-header">
                            <h4 class="job-position">Meteorólogo Especialista en Nivología</h4>
                            <span class="job-period">Abril 2019 – Abril 2021</span>
                        </div>
                        <h5 class="company-name">ASESORÍA TÉCNICA PUCARA S.A.</h5>
                        <ul class="experience-details">
                            <li>Análisis de modelos meteorológicos para control de riesgos de avalanchas en alta montaña</li>
                            <li>Elaboración diaria de informes técnicos fundamentales para toma de decisiones operativas</li>
                            <li>Administración de bases de datos climáticas históricas</li>
                        </ul>
                    </div>

                    <div class="experience-block">
                        <div class="experience-header">
                            <h4 class="job-position">Operador Técnico de Meteorología</h4>
                            <span class="job-period">Abril 2017 – Septiembre 2018</span>
                        </div>
                        <h5 class="company-name">COMPAÑÍA MINERA NEVADA S.A. (Proyecto Pascua Lama)</h5>
                        <ul class="experience-details">
                            <li>Responsable de operatividad de red de monitoreo meteorológico sobre 4.000 msnm</li>
                            <li>Validación y limpieza de datos en tiempo real</li>
                        </ul>
                    </div>
                </section>

                <!-- Formación -->
                <section class="cv-section">
                    <h3 class="cv-section-title">Formación Académica</h3>
                    
                    <div class="education-block">
                        <h4 class="degree">Técnico de Nivel Superior en Análisis de Datos</h4>
                        <div class="education-details">
                            <span class="institution">Instituto Profesional AIEP</span>
                            <span class="education-period">2024 – Presente (En curso, último semestre)</span>
                        </div>
                    </div>

                    <div class="education-block">
                        <h4 class="degree">Diplomado en Big Data & Ciencia de Datos</h4>
                        <div class="education-details">
                            <span class="institution">Universidad de los Andes</span>
                            <span class="education-period">Mayo 2023 – Agosto 2024</span>
                        </div>
                    </div>

                    <div class="education-block">
                        <h4 class="degree">Bootcamp Front-End Development (Beca Talento Digital)</h4>
                        <div class="education-details">
                            <span class="institution">SENCE</span>
                            <span class="education-period">Octubre 2025 – Presente</span>
                        </div>
                    </div>
                </section>

                <!-- Certificaciones -->
                <section class="cv-section">
                    <h3 class="cv-section-title">Certificaciones</h3>
                    <div class="certification-block">
                        <h4 class="certification-name">PCEP™ – Certified Entry-Level Python Programmer</h4>
                        <span class="certification-issuer">Python Institute • Febrero 2025</span>
                    </div>
                </section>

                <!-- Proyectos -->
                <section class="cv-section">
                    <h3 class="cv-section-title">Proyectos Destacados</h3>
                    
                    <div class="project-block">
                        <h4 class="project-name">Portafolio GitHub</h4>
                        <p class="project-description">
                            Más de 15 proyectos que demuestran evolución técnica desde scripts de análisis 
                            de datos hasta desarrollo web completo. 
                            <a href="https://github.com/miguellucero123" target="_blank" class="text-link">github.com/miguellucero123</a>
                        </p>
                    </div>

                    <div class="project-block">
                        <h4 class="project-name">Plataforma de Gestión de Datos (Santander Explorer)</h4>
                        <p class="project-description">
                            Liderazgo en el diseño y prototipado de una aplicación web para optimización 
                            y visualización de datos operativos. Proyecto en fase de validación.
                        </p>
                    </div>
                </section>

                <div class="cv-actions mt-5">
                    <a href="/index.html" class="btn btn-outline">Volver al Inicio</a>
                    <a href="/dashboard_marca_personal.html" class="btn btn-primary">Ver Dashboard de Marca Personal</a>
                </div>
            </div>
        </main>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>"""

# -------------------- DASHBOARD_MARCA_PERSONAL.HTML --------------------
DASHBOARD_HTML = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <title>Dashboard de Marca Personal - Miguel Lucero</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="assets/css/styles.css">
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body id="top">
    <!-- Navbar inyectado automáticamente por el servidor -->

    <main class="dashboard-main">
        <div class="container-fluid">
            <!-- Header del Dashboard -->
            <section class="dashboard-header">
                <div class="container">
                    <div class="row align-items-center">
                        <div class="col-lg-8">
                            <h1 class="dashboard-title">Dashboard de Marca Personal</h1>
                            <p class="dashboard-subtitle">
                                Plan estratégico de posicionamiento profesional como experto en análisis de datos
                            </p>
                            <p class="dashboard-description">
                                Este dashboard presenta el desarrollo sistemático de mi marca personal, 
                                enfocado en establecerme como referente en la transformación de datos 
                                en decisiones estratégicas para el sector empresarial.
                            </p>
                        </div>
                        <div class="col-lg-4 text-lg-end">
                            <div class="dashboard-status">
                                <h5>Estado del Proyecto</h5>
                                <div class="progress" style="height: 10px;">
                                    <div class="progress-bar" role="progressbar" style="width: 65%;" aria-valuenow="65" aria-valuemin="0" aria-valuemax="100"></div>
                                </div>
                                <p class="progress-label">65% Completado</p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Métricas Clave -->
            <section class="metrics-section">
                <div class="container">
                    <h2 class="section-title">Indicadores de Desempeño</h2>
                    <div class="row g-4">
                        <div class="col-md-3">
                            <div class="metric-card">
                                <h3 class="metric-value">8</h3>
                                <p class="metric-label">Casos de Estudio</p>
                                <p class="metric-description">Publicaciones técnicas planificadas</p>
                            </div>
                        </div>
                        <div class="col-md-3">
                            <div class="metric-card">
                                <h3 class="metric-value">20%</h3>
                                <p class="metric-label">Engagement Objetivo</p>
                                <p class="metric-description">Interacción mínima requerida</p>
                            </div>
                        </div>
                        <div class="col-md-3">
                            <div class="metric-card">
                                <h3 class="metric-value">+30%</h3>
                                <p class="metric-label">Crecimiento de Red</p>
                                <p class="metric-description">Expansión de contactos profesionales</p>
                            </div>
                        </div>
                        <div class="col-md-3">
                            <div class="metric-card">
                                <h3 class="metric-value">4</h3>
                                <p class="metric-label">Meses</p>
                                <p class="metric-description">Duración del proyecto</p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Estrategia de Marca -->
            <section class="strategy-section">
                <div class="container">
                    <div class="row g-5">
                        <div class="col-lg-6">
                            <h2 class="section-title">Estrategia de Posicionamiento</h2>
                            <div class="strategy-content">
                                <h4>Propuesta de Valor Única</h4>
                                <p class="strategy-text">
                                    "Combino pensamiento analítico avanzado con comunicación efectiva para 
                                    traducir datos complejos en decisiones accionables con ética y calidad."
                                </p>
                                
                                <h4 class="mt-4">Pilares de Contenido</h4>
                                <ul class="pillar-list">
                                    <li>Análisis predictivo aplicado a industrias críticas</li>
                                    <li>Visualización de datos para decisiones ejecutivas</li>
                                    <li>Metodologías ágiles en proyectos de datos</li>
                                    <li>Ética y privacidad en el manejo de información</li>
                                </ul>
                            </div>
                        </div>
                        <div class="col-lg-6">
                            <h2 class="section-title">Plan de Implementación</h2>
                            <div class="timeline">
                                <div class="timeline-item">
                                    <h5>Mes 1: Fundación</h5>
                                    <p>Establecimiento de identidad visual y primeras publicaciones técnicas</p>
                                </div>
                                <div class="timeline-item">
                                    <h5>Mes 2: Aceleración</h5>
                                    <p>Networking estratégico y colaboraciones con expertos del sector</p>
                                </div>
                                <div class="timeline-item">
                                    <h5>Mes 3: Consolidación</h5>
                                    <p>Publicación de casos de estudio complejos y análisis sectoriales</p>
                                </div>
                                <div class="timeline-item">
                                    <h5>Mes 4: Culminación</h5>
                                    <p>Evaluación de impacto y planificación de siguiente fase</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Visualizaciones de Datos -->
            <section class="charts-section">
                <div class="container">
                    <h2 class="section-title">Análisis Visual del Progreso</h2>
                    <div class="row g-4">
                        <div class="col-xl-6">
                            <div class="chart-card">
                                <h4 class="chart-title">Distribución de Contenidos por Mes</h4>
                                <div id="timeline-chart" class="chart-container"></div>
                            </div>
                        </div>
                        <div class="col-xl-6">
                            <div class="chart-card">
                                <h4 class="chart-title">Objetivos de Crecimiento</h4>
                                <div id="metrics-chart" class="chart-container"></div>
                            </div>
                        </div>
                        <div class="col-xl-6">
                            <div class="chart-card">
                                <h4 class="chart-title">Mix de Contenidos</h4>
                                <div id="content-chart" class="chart-container"></div>
                            </div>
                        </div>
                        <div class="col-xl-6">
                            <div class="chart-card">
                                <h4 class="chart-title">Análisis de Riesgos</h4>
                                <div id="risk-chart" class="chart-container"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Publicaciones Planificadas -->
            <section class="publications-section">
                <div class="container">
                    <h2 class="section-title">Calendario de Publicaciones</h2>
                    <div class="table-responsive">
                        <table class="publication-table">
                            <thead>
                                <tr>
                                    <th>Fecha</th>
                                    <th>Título</th>
                                    <th>Tema Principal</th>
                                    <th>Estado</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>06/09/2025</td>
                                    <td>Insights en Retail con Power BI</td>
                                    <td>Business Intelligence</td>
                                    <td><span class="status-badge status-published">Publicado</span></td>
                                </tr>
                                <tr>
                                    <td>20/09/2025</td>
                                    <td>Optimización Logística con Python</td>
                                    <td>Análisis Predictivo</td>
                                    <td><span class="status-badge status-review">En Revisión</span></td>
                                </tr>
                                <tr>
                                    <td>03/10/2025</td>
                                    <td>Segmentación Predictiva de Clientes</td>
                                    <td>Machine Learning</td>
                                    <td><span class="status-badge status-scheduled">Programado</span></td>
                                </tr>
                                <tr>
                                    <td>17/10/2025</td>
                                    <td>Análisis de Sentimiento en Redes</td>
                                    <td>NLP y Analytics</td>
                                    <td><span class="status-badge status-scheduled">Programado</span></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </section>

            <!-- Conclusiones -->
            <section class="conclusion-section">
                <div class="container">
                    <div class="conclusion-card">
                        <h2>Conclusiones del Proyecto</h2>
                        <p>
                            El desarrollo sistemático de una marca personal profesional requiere la combinación 
                            estratégica de contenido de valor, consistencia en la comunicación y métricas claras 
                            de seguimiento. Este dashboard permite monitorear el progreso hacia el posicionamiento 
                            como referente en análisis de datos empresariales.
                        </p>
                        <div class="conclusion-actions">
                            <a href="/cv.html" class="btn btn-outline">Ver Experiencia</a>
                            <a href="#contacto" class="btn btn-primary">Solicitar Consultoría</a>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Formulario de Contacto -->
            <section id="contacto" class="contact-section">
                <div class="container">
                    <div class="contact-card">
                        <div class="row g-5">
                            <div class="col-lg-5">
                                <h2 class="section-title">Trabajemos Juntos</h2>
                                <p class="contact-description">
                                    Si está buscando transformar los datos de su organización en ventajas 
                                    competitivas, conversemos sobre cómo puedo ayudarle.
                                </p>
                                <div class="contact-info">
                                    <div class="info-item">
                                        <h5>Email</h5>
                                        <p>miguellucerogatica@gmail.com</p>
                                    </div>
                                    <div class="info-item">
                                        <h5>Teléfono</h5>
                                        <p>+56 9 9931 9162</p>
                                    </div>
                                    <div class="info-item">
                                        <h5>LinkedIn</h5>
                                        <p><a href="https://linkedin.com/in/metgo3d/" target="_blank" class="text-link">linkedin.com/in/metgo3d</a></p>
                                    </div>
                                </div>
                            </div>
                            <div class="col-lg-7">
                                <form class="contact-form">
                                    <div class="row g-3">
                                        <div class="col-md-6">
                                            <label for="name" class="form-label">Nombre Completo</label>
                                            <input type="text" class="form-control" id="name" required>
                                        </div>
                                        <div class="col-md-6">
                                            <label for="email" class="form-label">Email Corporativo</label>
                                            <input type="email" class="form-control" id="email" required>
                                        </div>
                                        <div class="col-12">
                                            <label for="company" class="form-label">Empresa</label>
                                            <input type="text" class="form-control" id="company">
                                        </div>
                                        <div class="col-12">
                                            <label for="message" class="form-label">Descripción del Proyecto</label>
                                            <textarea class="form-control" id="message" rows="4" required></textarea>
                                        </div>
                                        <div class="col-12">
                                            <button type="submit" class="btn btn-primary btn-lg">Enviar Consulta</button>
                                        </div>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    </main>

    <footer class="professional-footer">
        <div class="container">
            <div class="row">
                <div class="col-md-6">
                    <p>&copy; 2025 Miguel Ignacio Lucero Gatica. Todos los derechos reservados.</p>
                </div>
                <div class="col-md-6 text-md-end">
                    <a href="/index.html" class="footer-link">Inicio</a>
                    <a href="/cv.html" class="footer-link">CV</a>
                    <a href="mailto:miguellucerogatica@gmail.com" class="footer-link">Contacto</a>
                </div>
            </div>
        </div>
    </footer>

    <button class="btn-scroll-top" id="btnScrollTop" onclick="window.scrollTo({top: 0, behavior: 'smooth'})">↑</button>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    <script src="assets/js/dashboard.js"></script>
    <script src="assets/js/scroll.js"></script>
</body>
</html>"""

# ============================================================
# ESTILOS CSS PROFESIONALES
# ============================================================
PROFESSIONAL_CSS = """
/* ====================================
   SISTEMA DE DISEÑO PROFESIONAL
   Marca Personal - Miguel Lucero
   ==================================== */

/* Variables de Diseño Corporativo */
:root {
    /* Paleta Principal - Profesional y Legible */
    --primary-color: #4f6fad;        /* Azul Marino Suavizado */
    --secondary-color: #6b91c2;      /* Azul Corporativo Claro */
    --accent-color: #7ab0e6;         /* Azul Acento Luminoso */
    
    /* Colores Neutros */
    --dark-gray: #58627a;            /* Texto Principal */
    --medium-gray: #73819b;          /* Texto Secundario */
    --light-gray: #96a3ba;           /* Texto Terciario */
    --border-gray: #edf2fb;          /* Bordes */
    --bg-light: #f7fafc;             /* Fondo Claro */
    --white: #ffffff;
    
    /* Colores de Estado */
    --success: #6dc897;              /* Verde Profesional Claro */
    --warning: #f1c866;              /* Amarillo Dorado Suave */
    --danger: #f47b7b;               /* Rojo Corporativo Suave */
    --info: #7fb2e8;                 /* Azul Informativo Claro */
    
    /* Tipografía */
    --font-primary: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    --font-heading: 'Playfair Display', Georgia, serif;
    
    /* Espaciado */
    --spacing-xs: 0.5rem;
    --spacing-sm: 1rem;
    --spacing-md: 1.5rem;
    --spacing-lg: 2rem;
    --spacing-xl: 3rem;
    --spacing-xxl: 4rem;
    
    /* Sombras Sutiles */
    --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.05);
    --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.07);
    --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
    --shadow-xl: 0 20px 25px rgba(0, 0, 0, 0.1);
}

/* Reset y Base */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    font-family: var(--font-primary);
    font-size: 16px;
    line-height: 1.6;
    color: var(--dark-gray);
    background-color: var(--white);
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

/* Tipografía Base */
h1, h2, h3, h4, h5, h6 {
    font-family: var(--font-heading);
    font-weight: 700;
    line-height: 1.2;
    color: var(--primary-color);
}

h1 { font-size: 2.5rem; }
h2 { font-size: 2rem; }
h3 { font-size: 1.75rem; }
h4 { font-size: 1.5rem; }
h5 { font-size: 1.25rem; }
h6 { font-size: 1rem; }

p {
    margin-bottom: 1rem;
    color: var(--medium-gray);
}

/* Enlaces */
a {
    color: var(--secondary-color);
    text-decoration: none;
    transition: color 0.3s ease;
}

a:hover {
    color: var(--primary-color);
}

/* Navegación Profesional */
.professional-nav {
    background-color: var(--white);
    box-shadow: var(--shadow-sm);
    position: sticky;
    top: 0;
    z-index: 1000;
}

.nav-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 var(--spacing-md);
}

.nav-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 72px;
}

.nav-brand {
    font-family: var(--font-heading);
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--primary-color);
}

.nav-menu {
    display: flex;
    list-style: none;
    gap: var(--spacing-lg);
    margin: 0;
    padding: 0;
}

.nav-link {
    font-weight: 500;
    color: var(--medium-gray);
    padding: var(--spacing-xs) var(--spacing-sm);
    border-bottom: 2px solid transparent;
    transition: all 0.3s ease;
}

.nav-link:hover,
.nav-link.active {
    color: var(--primary-color);
    border-bottom-color: var(--accent-color);
}

/* Botones Profesionales */
.btn {
    display: inline-block;
    padding: 0.75rem 2rem;
    font-weight: 600;
    text-align: center;
    border-radius: 4px;
    transition: all 0.3s ease;
    cursor: pointer;
    border: none;
    font-size: 1rem;
}

.btn-primary {
    background-color: var(--primary-color);
    color: var(--white);
}

.btn-primary:hover {
    background-color: var(--secondary-color);
    transform: translateY(-1px);
    box-shadow: var(--shadow-md);
    color: var(--white);
}

.btn-outline {
    background-color: transparent;
    color: var(--primary-color);
    border: 2px solid var(--primary-color);
}

.btn-outline:hover {
    background-color: var(--primary-color);
    color: var(--white);
}

.btn-lg {
    padding: 1rem 2.5rem;
    font-size: 1.125rem;
}

/* Hero Section */
.hero-section {
    padding: var(--spacing-xxl) 0;
    background-color: var(--bg-light);
}

.hero-title {
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: var(--spacing-sm);
    color: var(--primary-color);
}

.hero-subtitle {
    font-size: 1.5rem;
    font-weight: 400;
    color: var(--secondary-color);
    margin-bottom: var(--spacing-md);
}

.hero-description {
    font-size: 1.125rem;
    color: var(--medium-gray);
    margin-bottom: var(--spacing-lg);
    max-width: 600px;
}

.hero-actions {
    display: flex;
    gap: var(--spacing-sm);
    flex-wrap: wrap;
}

.text-accent {
    color: var(--accent-color);
}

/* Secciones */
.value-section,
.services-section,
.cta-section {
    padding: var(--spacing-xxl) 0;
}

.dark-section {
    color: #f2f6ff;
}

.dark-section .section-title {
    color: #ffffff;
}

.dark-section .section-title::after {
    background-color: rgba(255, 255, 255, 0.75);
}

.dark-section p,
.dark-section h4,
.dark-section h5,
.dark-section li {
    color: #edf3ff;
}

.dark-section .value-item p {
    color: #e7eefc;
}

.dark-section .stat-card {
    background-color: rgba(255, 255, 255, 0.12);
    border: 1px solid rgba(255, 255, 255, 0.2);
    box-shadow: none;
}

.dark-section .stat-card h5 {
    color: #ffffff;
}

.dark-section .stat-card p {
    color: #e6edff;
}

.section-title {
    font-size: 2.25rem;
    margin-bottom: var(--spacing-lg);
    color: var(--primary-color);
    position: relative;
    padding-bottom: var(--spacing-sm);
}

.section-title::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 60px;
    height: 3px;
    background-color: var(--accent-color);
}

.section-description {
    font-size: 1.125rem;
    color: var(--medium-gray);
    margin-bottom: var(--spacing-lg);
}

/* Value Items */
.value-item {
    margin-bottom: var(--spacing-lg);
}

.value-item h4 {
    color: var(--secondary-color);
    margin-bottom: var(--spacing-xs);
}

.value-item p {
    color: var(--medium-gray);
}

/* Stats Grid */
.stats-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: var(--spacing-md);
}

.stat-card {
    background-color: var(--white);
    padding: var(--spacing-lg);
    text-align: center;
    border-radius: 8px;
    box-shadow: var(--shadow-md);
    transition: transform 0.3s ease;
}

.stat-card:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-lg);
}

.stat-card h5 {
    font-size: 2.5rem;
    color: var(--accent-color);
    margin-bottom: var(--spacing-xs);
}

.stat-card p {
    color: var(--medium-gray);
    font-weight: 500;
}

/* Service Cards */
.service-card {
    background-color: var(--white);
    padding: var(--spacing-lg);
    border-radius: 8px;
    box-shadow: var(--shadow-sm);
    height: 100%;
    transition: all 0.3s ease;
    border: 1px solid var(--border-gray);
}

.service-card:hover {
    box-shadow: var(--shadow-lg);
    transform: translateY(-5px);
    border-color: var(--accent-color);
}

.service-card h4 {
    color: var(--primary-color);
    margin-bottom: var(--spacing-sm);
}

.service-features {
    list-style: none;
    padding: 0;
    margin-top: var(--spacing-md);
}

.service-features li {
    padding: var(--spacing-xs) 0;
    color: var(--medium-gray);
    position: relative;
    padding-left: 1.5rem;
}

.service-features li::before {
    content: "→";
    position: absolute;
    left: 0;
    color: var(--accent-color);
}

/* CTA Section */
.cta-section {
    background-color: var(--bg-light);
    text-align: center;
}

.cta-section h3 {
    font-size: 2rem;
    margin-bottom: var(--spacing-sm);
}

.cta-actions {
    display: flex;
    gap: var(--spacing-md);
    justify-content: center;
    margin-top: var(--spacing-lg);
}

/* CV Styles */
.cv-container {
    background-color: var(--white);
    min-height: 100vh;
}

.cv-header {
    background-color: var(--bg-light);
    padding: var(--spacing-xl) 0;
    border-bottom: 1px solid var(--border-gray);
}

.cv-name {
    font-size: 2.5rem;
    margin-bottom: var(--spacing-xs);
}

.cv-title {
    font-size: 1.25rem;
    color: var(--secondary-color);
    font-weight: 400;
    margin-bottom: var(--spacing-md);
}

.cv-contact {
    display: flex;
    flex-wrap: wrap;
    gap: var(--spacing-sm);
    font-size: 0.875rem;
    color: var(--medium-gray);
}

.contact-separator {
    color: var(--light-gray);
}

.cv-links {
    display: flex;
    gap: var(--spacing-md);
}

.professional-link {
    color: var(--secondary-color);
    font-weight: 500;
    padding: var(--spacing-xs) var(--spacing-sm);
    border: 1px solid var(--secondary-color);
    border-radius: 4px;
    transition: all 0.3s ease;
}

.professional-link:hover {
    background-color: var(--secondary-color);
    color: var(--white);
}

.cv-content {
    padding: var(--spacing-xl) 0;
}

.cv-section {
    margin-bottom: var(--spacing-xl);
}

.cv-section-title {
    font-size: 1.5rem;
    color: var(--primary-color);
    margin-bottom: var(--spacing-lg);
    padding-bottom: var(--spacing-xs);
    border-bottom: 2px solid var(--accent-color);
}

.cv-text {
    line-height: 1.8;
    color: var(--medium-gray);
}

/* Competencias */
.competency-group {
    margin-bottom: var(--spacing-lg);
}

.competency-group h4 {
    font-size: 1.125rem;
    color: var(--secondary-color);
    margin-bottom: var(--spacing-sm);
}

.competency-list {
    list-style: none;
    padding: 0;
}

.competency-list li {
    padding: var(--spacing-xs) 0;
    color: var(--medium-gray);
}

/* Experiencia */
.experience-block,
.education-block,
.project-block {
    margin-bottom: var(--spacing-lg);
    padding-bottom: var(--spacing-lg);
    border-bottom: 1px solid var(--border-gray);
}

.experience-block:last-child,
.education-block:last-child,
.project-block:last-child {
    border-bottom: none;
}

.experience-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: var(--spacing-xs);
}

.job-position,
.degree,
.project-name {
    font-size: 1.25rem;
    color: var(--primary-color);
    font-weight: 600;
}

.job-period,
.education-period {
    color: var(--light-gray);
    font-size: 0.875rem;
    font-weight: 500;
}

.company-name,
.institution {
    color: var(--secondary-color);
    font-size: 1rem;
    font-weight: 500;
    margin-bottom: var(--spacing-sm);
}

.experience-details {
    list-style: none;
    padding: 0;
}

.experience-details li {
    position: relative;
    padding-left: 1.5rem;
    margin-bottom: var(--spacing-xs);
    color: var(--medium-gray);
}

.experience-details li::before {
    content: "•";
    position: absolute;
    left: 0;
    color: var(--accent-color);
}

/* Dashboard Styles */
.dashboard-main {
    background-color: var(--bg-light);
    min-height: 100vh;
}

.dashboard-header {
    background-color: var(--white);
    padding: var(--spacing-xl) 0;
    border-bottom: 1px solid var(--border-gray);
}

.dashboard-title {
    font-size: 2.5rem;
    margin-bottom: var(--spacing-sm);
}

.dashboard-subtitle {
    font-size: 1.25rem;
    color: var(--secondary-color);
    font-weight: 500;
    margin-bottom: var(--spacing-xs);
}

.dashboard-description {
    color: var(--medium-gray);
    max-width: 800px;
}

.dashboard-status {
    background-color: var(--bg-light);
    padding: var(--spacing-md);
    border-radius: 8px;
    border: 1px solid var(--border-gray);
}

.dashboard-status h5 {
    font-size: 1rem;
    color: var(--primary-color);
    margin-bottom: var(--spacing-sm);
}

.progress {
    background-color: var(--border-gray);
    border-radius: 4px;
    overflow: hidden;
}

.progress-bar {
    background-color: var(--accent-color);
    transition: width 0.6s ease;
}

.progress-label {
    font-size: 0.875rem;
    color: var(--medium-gray);
    margin-top: var(--spacing-xs);
}

/* Métricas */
.metrics-section {
    padding: var(--spacing-xl) 0;
    background-color: var(--white);
}

.metric-card {
    background-color: var(--bg-light);
    padding: var(--spacing-lg);
    text-align: center;
    border-radius: 8px;
    height: 100%;
    transition: all 0.3s ease;
    border: 1px solid var(--border-gray);
}

.metric-card:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-md);
    border-color: var(--accent-color);
}

.metric-value {
    font-size: 2.5rem;
    color: var(--accent-color);
    margin-bottom: var(--spacing-xs);
}

.metric-label {
    font-size: 1.125rem;
    font-weight: 600;
    color: var(--primary-color);
    margin-bottom: var(--spacing-xs);
}

.metric-description {
    font-size: 0.875rem;
    color: var(--medium-gray);
}

/* Estrategia */
.strategy-section {
    padding: var(--spacing-xl) 0;
    background-color: var(--bg-light);
}

.strategy-content {
    background-color: var(--white);
    padding: var(--spacing-lg);
    border-radius: 8px;
    box-shadow: var(--shadow-sm);
}

.strategy-text {
    font-size: 1.125rem;
    color: var(--medium-gray);
    font-style: italic;
    border-left: 4px solid var(--accent-color);
    padding-left: var(--spacing-md);
    margin: var(--spacing-md) 0;
}

.pillar-list {
    list-style: none;
    padding: 0;
}

.pillar-list li {
    padding: var(--spacing-sm) 0;
    padding-left: 2rem;
    position: relative;
    color: var(--medium-gray);
}

.pillar-list li::before {
    content: "▪";
    position: absolute;
    left: 0;
    color: var(--accent-color);
    font-size: 1.25rem;
}

/* Timeline */
.timeline {
    position: relative;
    padding-left: 2rem;
}

.timeline::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 2px;
    background-color: var(--border-gray);
}

.timeline-item {
    position: relative;
    padding-bottom: var(--spacing-lg);
}

.timeline-item::before {
    content: '';
    position: absolute;
    left: -2.5rem;
    top: 0.5rem;
    width: 12px;
    height: 12px;
    background-color: var(--accent-color);
    border-radius: 50%;
    border: 2px solid var(--white);
    box-shadow: var(--shadow-sm);
}

.timeline-item h5 {
    color: var(--primary-color);
    margin-bottom: var(--spacing-xs);
}

.timeline-item p {
    color: var(--medium-gray);
    font-size: 0.875rem;
}

/* Gráficos */
.charts-section {
    padding: var(--spacing-xl) 0;
    background-color: var(--white);
}

.chart-card {
    background-color: var(--bg-light);
    padding: var(--spacing-lg);
    border-radius: 8px;
    height: 100%;
    box-shadow: var(--shadow-sm);
}

.chart-title {
    font-size: 1.125rem;
    color: var(--primary-color);
    margin-bottom: var(--spacing-md);
}

.chart-container {
    min-height: 300px;
}

/* Tabla de Publicaciones */
.publications-section {
    padding: var(--spacing-xl) 0;
    background-color: var(--bg-light);
}

.publication-table {
    width: 100%;
    background-color: var(--white);
    border-radius: 8px;
    overflow: hidden;
    box-shadow: var(--shadow-sm);
}

.publication-table thead {
    background-color: var(--primary-color);
    color: var(--white);
}

.publication-table th {
    padding: var(--spacing-md);
    font-weight: 600;
    text-align: left;
}

.publication-table td {
    padding: var(--spacing-md);
    border-bottom: 1px solid var(--border-gray);
    color: var(--medium-gray);
}

.publication-table tbody tr:hover {
    background-color: var(--bg-light);
}

.status-badge {
    padding: 0.25rem 0.75rem;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
}

.status-published {
    background-color: #e5f6ea;
    color: #2f8a55;
}

.status-review {
    background-color: #fff7dd;
    color: #9c7a21;
}

.status-scheduled {
    background-color: #e4f4f8;
    color: #2f7a86;
}

/* Conclusiones */
.conclusion-section {
    padding: var(--spacing-xl) 0;
    background-color: var(--white);
}

.conclusion-card {
    background-color: var(--primary-color);
    color: var(--white);
    padding: var(--spacing-xl);
    border-radius: 8px;
    text-align: center;
}

.conclusion-card h2 {
    color: var(--white);
    margin-bottom: var(--spacing-md);
}

.conclusion-card p {
    color: rgba(255, 255, 255, 0.9);
    font-size: 1.125rem;
    margin-bottom: var(--spacing-lg);
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
}

.conclusion-actions {
    display: flex;
    gap: var(--spacing-md);
    justify-content: center;
}

.conclusion-card .btn-outline {
    border-color: var(--white);
    color: var(--white);
}

.conclusion-card .btn-outline:hover {
    background-color: var(--white);
    color: var(--primary-color);
}

/* Formulario de Contacto */
.contact-section {
    padding: var(--spacing-xl) 0;
    background-color: var(--bg-light);
}

.contact-card {
    background-color: var(--white);
    padding: var(--spacing-xl);
    border-radius: 8px;
    box-shadow: var(--shadow-md);
}

.contact-description {
    font-size: 1.125rem;
    color: var(--medium-gray);
    margin-bottom: var(--spacing-lg);
}

.contact-info {
    margin-top: var(--spacing-lg);
}

.info-item {
    margin-bottom: var(--spacing-md);
}

.info-item h5 {
    font-size: 0.875rem;
    color: var(--primary-color);
    margin-bottom: var(--spacing-xs);
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

.info-item p {
    color: var(--medium-gray);
    margin: 0;
}

.text-link {
    color: var(--secondary-color);
    text-decoration: none;
}

.text-link:hover {
    text-decoration: underline;
}

/* Formularios */
.contact-form .form-label {
    color: var(--primary-color);
    font-weight: 500;
    margin-bottom: var(--spacing-xs);
}

.contact-form .form-control {
    border: 1px solid var(--border-gray);
    border-radius: 4px;
    padding: 0.75rem 1rem;
    font-size: 1rem;
    transition: all 0.3s ease;
}

.contact-form .form-control:focus {
    border-color: var(--accent-color);
    box-shadow: 0 0 0 0.2rem rgba(43, 108, 176, 0.1);
    outline: none;
}

/* Footer Profesional */
.professional-footer {
    background-color: var(--primary-color);
    color: var(--white);
    padding: var(--spacing-lg) 0;
}

.professional-footer p {
    margin: 0;
    color: rgba(255, 255, 255, 0.8);
}

.footer-link {
    color: rgba(255, 255, 255, 0.8);
    margin-left: var(--spacing-md);
    transition: color 0.3s ease;
}

.footer-link:hover {
    color: var(--white);
}

/* Botón Scroll Top */
.btn-scroll-top {
    position: fixed;
    bottom: 2rem;
    right: 2rem;
    width: 48px;
    height: 48px;
    background-color: var(--primary-color);
    color: var(--white);
    border: none;
    border-radius: 50%;
    font-size: 1.5rem;
    display: none;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: var(--shadow-md);
}

.btn-scroll-top:hover {
    background-color: var(--secondary-color);
    transform: translateY(-3px);
    box-shadow: var(--shadow-lg);
}

/* Utilidades */
.text-center { text-align: center; }
.text-md-end { text-align: right; }

/* Responsive */
@media (max-width: 768px) {
    .hero-title { font-size: 2rem; }
    .hero-subtitle { font-size: 1.25rem; }
    
    .nav-menu {
        flex-direction: column;
        position: absolute;
        top: 100%;
        left: 0;
        right: 0;
        background-color: var(--white);
        box-shadow: var(--shadow-md);
        display: none;
    }
    
    .stats-grid {
        grid-template-columns: 1fr;
    }
    
    .experience-header {
        flex-direction: column;
        align-items: flex-start;
    }
    
    .cta-actions,
    .hero-actions {
        flex-direction: column;
        width: 100%;
    }
    
    .btn {
        width: 100%;
    }
    
    .footer-link {
        display: block;
        margin: var(--spacing-xs) 0;
    }
}

/* Print Styles */
@media print {
    body {
        background-color: white;
        color: #2e3747;
    }
    
    .nav-container,
    .btn-scroll-top,
    .cv-actions,
    .dashboard-actions {
        display: none !important;
    }
    
    .cv-header {
        background-color: white;
        border-bottom: 2px solid #50607a;
    }
    
    .cv-section-title {
        border-bottom-color: #50607a;
    }
    
    a {
        color: #2e3747;
        text-decoration: underline;
    }
}
"""

# ============================================================
# [RESTO DEL CÓDIGO PYTHON DEL SERVIDOR]
# ============================================================

class MetGoHandler(http.server.SimpleHTTPRequestHandler):
    """Handler personalizado que inyecta navbar profesional"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def do_GET(self):
        """Procesa peticiones GET e inyecta navbar"""
        
        # Mapeo de rutas
        path_mapping = {
            '/': '/index.html',
            '/cv': '/cv.html',
            '/dashboard': '/dashboard_marca_personal.html',
            '/inicio': '/index.html'
        }
        
        # Normalizar path
        if self.path in path_mapping:
            self.path = path_mapping[self.path]
        
        # Verificar si es archivo HTML
        if self.path.endswith('.html'):
            try:
                file_path = DIRECTORY + self.path
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Inyectar navbar profesional
                modified_content = self.inject_navbar(content, self.path)
                
                # Enviar respuesta
                self.send_response(200)
                self.send_header('Content-type', 'text/html; charset=utf-8')
                self.send_header('Content-Length', len(modified_content.encode('utf-8')))
                self.end_headers()
                self.wfile.write(modified_content.encode('utf-8'))
                
                print(f"✅ Servido: {self.path}")
                return
                
            except FileNotFoundError:
                self.send_error(404, f"Archivo no encontrado: {self.path}")
                return
        
        # Para otros archivos (CSS, JS, imágenes)
        super().do_GET()
    
    def inject_navbar(self, html_content, current_path):
        """Inyecta navbar profesional en todas las páginas"""
        
        # Determinar página activa
        active_index = 'active' if 'index' in current_path else ''
        active_cv = 'active' if 'cv' in current_path else ''
        active_dashboard = 'active' if 'dashboard' in current_path else ''
        
        navbar_html = f"""
<nav class="professional-nav">
    <div class="nav-container">
        <div class="nav-content">
            <a href="/index.html" class="nav-brand">Miguel Lucero</a>
            <ul class="nav-menu">
                <li><a href="/index.html" class="nav-link {active_index}">Inicio</a></li>
                <li><a href="/cv.html" class="nav-link {active_cv}">Currículum</a></li>
                <li><a href="/dashboard_marca_personal.html" class="nav-link {active_dashboard}">Dashboard</a></li>
            </ul>
        </div>
    </div>
</nav>
"""
        
        # Insertar navbar después del <body>
        if '<!-- Navbar inyectado automáticamente por el servidor -->' in html_content:
            html_content = html_content.replace(
                '<!-- Navbar inyectado automáticamente por el servidor -->',
                navbar_html
            )
        elif '<body' in html_content:
            html_content = re.sub(
                r'(<body[^>]*>)',
                r'\1\n' + navbar_html,
                html_content,
                count=1
            )
        
        return html_content
    
    def log_message(self, format, *args):
        """Personalizar mensajes de log"""
        print(f"🌐 [{self.log_date_time_string()}] {format % args}")


# ============================================================
# FUNCIONES AUXILIARES
# ============================================================
def create_html_files():
    """Crea los archivos HTML si no existen"""
    
    files = {
        'index.html': INDEX_HTML,
        'cv.html': CV_HTML,
        'dashboard_marca_personal.html': DASHBOARD_HTML
    }
    
    for filename, content in files.items():
        filepath = Path(DIRECTORY) / filename
        if not filepath.exists():
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Creado: {filename}")
        else:
            print(f"ℹ️  Ya existe: {filename}")


def create_assets_structure():
    """Crea la estructura de carpetas y archivos CSS/JS"""
    
    assets_dir = Path(DIRECTORY) / 'assets'
    css_dir = assets_dir / 'css'
    js_dir = assets_dir / 'js'
    
    # Crear directorios
    css_dir.mkdir(parents=True, exist_ok=True)
    js_dir.mkdir(parents=True, exist_ok=True)
    
    # Crear styles.css con diseño profesional
    styles_path = css_dir / 'styles.css'
    if not styles_path.exists():
        with open(styles_path, 'w', encoding='utf-8') as f:
            f.write(PROFESSIONAL_CSS)
        print(f"✅ Creado: assets/css/styles.css")
    
    # Crear dashboard.js actualizado
    dashboard_js = js_dir / 'dashboard.js'
    if not dashboard_js.exists():
        dashboard_content = """
// Dashboard Profesional - Gráficos con Plotly
document.addEventListener('DOMContentLoaded', function() {
    
    // Configuración común profesional
    const commonLayout = {
        paper_bgcolor: 'rgba(0,0,0,0)',
        plot_bgcolor: 'rgba(247, 250, 252, 0.5)',
        font: {
            family: 'Inter, -apple-system, sans-serif',
            size: 12,
            color: '#4a5568'
        },
        margin: { t: 50, r: 30, b: 50, l: 50 }
    };
    
    const config = {
        responsive: true,
        displayModeBar: false
    };
    
    // Paleta de colores profesional
    const colors = {
        primary: '#1a365d',
        secondary: '#2c5282',
        accent: '#2b6cb0',
        success: '#38a169',
        warning: '#d69e2e',
        danger: '#e53e3e'
    };
    
    // 1. Distribución de Contenidos por Mes
    if (document.getElementById('timeline-chart')) {
        const timelineData = [{
            x: ['Mes 1', 'Mes 2', 'Mes 3', 'Mes 4'],
            y: [2, 2, 2, 2],
            type: 'bar',
            name: 'Publicaciones',
            marker: {
                color: [colors.primary, colors.secondary, colors.accent, colors.primary],
                line: { color: '#fff', width: 2 }
            },
            text: ['2 casos', '2 casos', '2 casos', '2 casos'],
            textposition: 'outside',
            hovertemplate: '<b>%{x}</b><br>Publicaciones: %{y}<br>%{text}<extra></extra>'
        }];
        
        const timelineLayout = {
            ...commonLayout,
            title: {
                text: 'Distribución Mensual de Publicaciones',
                font: { size: 16, color: colors.primary }
            },
            yaxis: {
                title: 'Número de Casos',
                gridcolor: '#e2e8f0',
                zeroline: false
            },
            xaxis: {
                title: '',
                tickfont: { size: 12 }
            }
        };
        
        Plotly.newPlot('timeline-chart', timelineData, timelineLayout, config);
    }
    
    // 2. Objetivos de Crecimiento
    if (document.getElementById('metrics-chart')) {
        const metricsData = [{
            x: ['Engagement', 'Crecimiento Red', 'Casos Totales'],
            y: [20, 30, 8],
            type: 'bar',
            marker: {
                color: [colors.success, colors.accent, colors.secondary]
            },
            text: ['20%', '+30%', '8 casos'],
            textposition: 'outside',
            hovertemplate: '<b>%{x}</b><br>Meta: %{text}<extra></extra>'
        }];
        
        const metricsLayout = {
            ...commonLayout,
            title: {
                text: 'Objetivos del Proyecto',
                font: { size: 16, color: colors.primary }
            },
            yaxis: {
                title: 'Valor Objetivo',
                gridcolor: '#e2e8f0',
                zeroline: false
            },
            xaxis: { title: '' }
        };
        
        Plotly.newPlot('metrics-chart', metricsData, metricsLayout, config);
    }
    
    // 3. Mix de Contenidos
    if (document.getElementById('content-chart')) {
        const contentData = [{
            values: [8, 4, 2, 3],
            labels: ['Casos de Estudio', 'Artículos Técnicos', 'Videos', 'Infografías'],
            type: 'pie',
            marker: {
                colors: [colors.primary, colors.secondary, colors.accent, colors.success],
                line: { color: '#fff', width: 2 }
            },
            textfont: { size: 12, color: '#fff' },
            hovertemplate: '<b>%{label}</b><br>Cantidad: %{value}<br>%{percent}<extra></extra>'
        }];
        
        const contentLayout = {
            ...commonLayout,
            title: {
                text: 'Distribución de Tipos de Contenido',
                font: { size: 16, color: colors.primary }
            },
            showlegend: true,
            legend: {
                orientation: 'h',
                yanchor: 'bottom',
                y: -0.2,
                xanchor: 'center',
                x: 0.5
            }
        };
        
        Plotly.newPlot('content-chart', contentData, contentLayout, config);
    }
    
    // 4. Análisis de Riesgos
    if (document.getElementById('risk-chart')) {
        const riskData = [{
            x: ['Bajo', 'Medio', 'Alto'],
            y: ['Tiempo', 'Recursos', 'Engagement'],
            z: [[1, 2, 1], [2, 3, 2], [1, 2, 3]],
            type: 'heatmap',
            colorscale: [
                [0, colors.success],
                [0.5, colors.warning],
                [1, colors.danger]
            ],
            showscale: true,
            hovertemplate: '<b>%{y}</b><br>Probabilidad: %{x}<br>Nivel: %{z}<extra></extra>',
            colorbar: {
                title: {
                    text: 'Nivel de<br>Riesgo',
                    side: 'right'
                },
                tickvals: [1, 2, 3],
                ticktext: ['Bajo', 'Medio', 'Alto'],
                thickness: 15
            }
        }];
        
        const riskLayout = {
            ...commonLayout,
            title: {
                text: 'Matriz de Evaluación de Riesgos',
                font: { size: 16, color: colors.primary }
            },
            xaxis: {
                title: 'Probabilidad',
                side: 'bottom',
                tickfont: { size: 12 }
            },
            yaxis: {
                title: 'Factor de Riesgo',
                tickfont: { size: 12 }
            }
        };
        
        Plotly.newPlot('risk-chart', riskData, riskLayout, config);
    }
    
    // Hacer los gráficos responsivos
    window.addEventListener('resize', function() {
        const charts = ['timeline-chart', 'metrics-chart', 'content-chart', 'risk-chart'];
        charts.forEach(chartId => {
            const chartDiv = document.getElementById(chartId);
            if (chartDiv && chartDiv.data) {
                Plotly.Plots.resize(chartDiv);
            }
        });
    });
});

// Manejo del formulario de contacto profesional
document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.querySelector('.contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const company = document.getElementById('company').value;
            
            // Mensaje profesional
            alert(`Gracias por su interés, ${name}. Su consulta ha sido recibida y será respondida en las próximas 24-48 horas hábiles a ${email}.`);
            
            // Limpiar formulario
            this.reset();
        });
    }
});
"""
        with open(dashboard_js, 'w', encoding='utf-8') as f:
            f.write(dashboard_content)
        print(f"✅ Creado: assets/js/dashboard.js")
    
    # Crear scroll.js mejorado
    scroll_js = js_dir / 'scroll.js'
    if not scroll_js.exists():
        scroll_content = """
// Funcionalidad de scroll profesional

// Botón Scroll to Top
window.addEventListener('scroll', function() {
    const scrollBtn = document.getElementById('btnScrollTop');
    if (scrollBtn) {
        if (window.pageYOffset > 300) {
            scrollBtn.style.display = 'flex';
        } else {
            scrollBtn.style.display = 'none';
        }
    }
});

// Smooth scroll para enlaces internos
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        
        if (target) {
            const navHeight = document.querySelector('.professional-nav')?.offsetHeight || 0;
            const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - navHeight - 20;
            
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }
    });
});

// Navbar activo basado en scroll
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-link');

function highlightNavigation() {
    const scrollY = window.pageYOffset;
    
    sections.forEach(section => {
        const sectionHeight = section.offsetHeight;
        const sectionTop = section.offsetTop - 100;
        const sectionId = section.getAttribute('id');
        
        if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href').includes(sectionId)) {
                    link.classList.add('active');
                }
            });
        }
    });
}

window.addEventListener('scroll', highlightNavigation);

// Animación de entrada profesional
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '0';
            entry.target.style.transform = 'translateY(20px)';
            
            setTimeout(() => {
                entry.target.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }, 100);
            
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Observar elementos clave
document.addEventListener('DOMContentLoaded', () => {
    const elementsToAnimate = document.querySelectorAll('.stat-card, .service-card, .metric-card, .timeline-item');
    elementsToAnimate.forEach(el => {
        observer.observe(el);
    });
});

console.log('✅ Scripts de navegación cargados correctamente');
"""
        with open(scroll_js, 'w', encoding='utf-8') as f:
            f.write(scroll_content)
        print(f"✅ Creado: assets/js/scroll.js")


def validate_files():
    """Valida la existencia de archivos HTML"""
    
    required_files = ['index.html', 'cv.html', 'dashboard_marca_personal.html']
    missing = []
    
    for filename in required_files:
        filepath = Path(DIRECTORY) / filename
        if not filepath.exists():
            missing.append(filename)
    
    if missing:
        print(f"⚠️  Faltaban archivos: {', '.join(missing)}")
        return False
    
    print("✅ Todos los archivos HTML están listos")
    return True


def check_image():
    """Verifica si existe la imagen METGO_3D.JPG"""
    
    img_path = Path(DIRECTORY) / 'METGO_3D.JPG'
    if not img_path.exists():
        print(f"\n⚠️  ADVERTENCIA: No se encontró METGO_3D.JPG")
        print(f"   Por favor, coloca tu imagen profesional en: {DIRECTORY}")
        print(f"   Recomendación: Usa una imagen profesional o logo corporativo.\n")
    else:
        print("✅ Imagen METGO_3D.JPG encontrada")


# ============================================================
# FUNCIÓN PRINCIPAL
# ============================================================
def start_server():
    """Inicia el servidor web profesional"""
    
    print("=" * 70)
    print("🎯 Portfolio Profesional de Marca Personal v3.0")
    print("=" * 70)
    print("\n📋 PASO 1: Verificando archivos HTML...")
    
    # Crear archivos HTML si no existen
    create_html_files()
    
    print("\n📋 PASO 2: Creando estructura de assets...")
    
    # Crear estructura de assets
    create_assets_structure()
    
    print("\n📋 PASO 3: Validando archivos...")
    
    # Validar archivos
    if not validate_files():
        print("\n❌ Error: Archivos HTML no pudieron crearse.")
        return
    
    # Verificar imagen
    check_image()
    
    print("\n📋 PASO 4: Iniciando servidor web...")
    
    # Configurar servidor
    try:
        with socketserver.TCPServer(("", PORT), MetGoHandler) as httpd:
            print(f"\n{'='*70}")
            print(f"✅ SERVIDOR PROFESIONAL ACTIVO")
            print(f"{'='*70}")
            print(f"\n🌐 Accede a tu portfolio profesional en:")
            print(f"   📍 http://localhost:{PORT}")
            print(f"   📍 http://127.0.0.1:{PORT}")
            print(f"\n📄 Páginas disponibles:")
            print(f"   🏢 Inicio:     http://localhost:{PORT}/index.html")
            print(f"   📋 CV:         http://localhost:{PORT}/cv.html")
            print(f"   📊 Dashboard:  http://localhost:{PORT}/dashboard_marca_personal.html")
            print(f"\n📂 Directorio raíz: {DIRECTORY}")
            print(f"\n💡 CARACTERÍSTICAS DEL DISEÑO PROFESIONAL:")
            print(f"   ✓ Paleta de colores corporativa (Azul Marino)")
            print(f"   ✓ Tipografía profesional (Inter + Playfair)")
            print(f"   ✓ Navegación clara entre todas las páginas")
            print(f"   ✓ Diseño minimalista sin iconos innecesarios")
            print(f"   ✓ Enfoque en marca personal profesional")
            print(f"   ✓ 100% responsive y listo para imprimir")
            print(f"\n⏹️  Presiona Ctrl+C para detener el servidor")
            print(f"{'='*70}\n")
            
            httpd.serve_forever()
            
    except OSError as e:
        if e.errno == 48 or e.errno == 98:  # Puerto en uso
            print(f"\n❌ Error: El puerto {PORT} ya está en uso.")
            print(f"   Opciones:")
            print(f"   1. Cierra el proceso que usa el puerto {PORT}")
            print(f"   2. Cambia la variable PORT en el código a otro valor (ej. 8081)")
        else:
            print(f"\n❌ Error al iniciar servidor: {e}")
    except KeyboardInterrupt:
        print("\n\n🛑 Servidor detenido por el usuario")
        print("👋 ¡Gracias por usar el Portfolio Profesional!")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")


# ============================================================
# PUNTO DE ENTRADA
# ============================================================
if __name__ == "__main__":
    start_server()