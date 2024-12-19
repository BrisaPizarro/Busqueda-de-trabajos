# Búsqueda de trabajos
**Propuesta:**
- Crear una página web para la búsqueda de empleos, comparando ofertas en diversas plataformas.
La página web estará diseñada para recopilar información sobre ofertas de trabajo específicas en múltiples portales dedicados al empleo. El sistema identificará la plataforma con las mejores condiciones(como salario,ubicación o requisitos) según los criterios establecidos por el usuario, al tiempo que mostrará otras alternativas disponibles.

**Motivación:**
- Las personas que buscan empleo a menudo invierten horas navegando por diversas plataformas para encontrar las ofertas que más se ajusten a sus necesidades y expectativas. Este proceso puede ser tedioso y consumir tiempo valioso. Una herramienta que centralice y facilite la búsqueda puede ayudar a reducir significativamente el tiempo dedicado a esta tarea, brindando resultados óptimos de manera rápida y eficiente.

**Propósito:**
- El objetivo del proyecto es ofrecer una herramienta digital que permita a los usuarios encontrar y comparar ofertas de empleo disponibles en diferentes plataformas, priorizando las que cumplan con sus preferencias y mostrando todas las opciones relevantes.

**Objetivos:**

**Objetivo general:**
- Desarrollar una página web que permita a los usuarios buscar ofertas de trabajo en múltiples plataformas, identificar aquellas que mejor se adapten a sus criterios, y presentar todas las alternativas disponibles de manera ordenada.

**Objetivos específicos:**
- Diseñar un sistema automatizado para recopilar información actualizada sobre ofertas de empleo en diversas plataformas mediante técnicas como web scraping o integración de APIs.
- Implementar una interfaz web intuitiva y fácil de usar, que permita a los usuarios filtrar, comparar y visualizar las ofertas de empleo de manera clara y detallada.
- Optimizar el tiempo de búsqueda para los usuarios, mostrando resultados personalizados basados en sus preferencias, como ubicación, salario, tipo de contrato o requisitos específicos.
- Garantizar que el sistema mantenga la información actualizada y ofrezca un rendimiento eficiente para gestionar grandes volúmenes de datos provenientes de distintas fuentes.

# Preparación del entorno
Se configuró el entorno con las siguientes herramientas y bibliotecas:

**Flask:** Framework web ligero utilizado para construir la interfaz de la aplicación y manejar las rutas.
**Requests:** Realiza solicitudes HTTP para obtener el contenido de las páginas web.
**BeautifulSoup (bs4):** Biblioteca para analizar y extraer datos de HTML y XML. Fundamental para el web scraping.

# Instalación de dependencias
Para instalar las bibliotecas necesarias se ejecuto el siguiente código:

```python
import requests
from bs4 import BeautifulSoup
from flask import Flask, request
```
# Función del código app.py
```python
from flask import Flask, render_template, request
from scraping.Computrabajo import buscar_ofertas_computrabajo
from scraping.Trabajando_pe import buscar_ofertas_trabajando
from scraping.Jora import buscar_ofertas_jora

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/resultados", methods=["GET"])
def resultados():
    tipo_trabajo = request.args.get("tipo_trabajo")
    empresa = request.args.get("empresa")
    ubicacion = request.args.get("ubicacion")

    ofertas_computrabajo = buscar_ofertas_computrabajo(tipo_trabajo, ubicacion)
    ofertas_trabajando = buscar_ofertas_trabajando(tipo_trabajo, ubicacion)
    ofertas_jora = buscar_ofertas_jora(tipo_trabajo, ubicacion)

    return render_template("resultados.html", 
                           ofertas_computrabajo=ofertas_computrabajo,
                           ofertas_trabajando=ofertas_trabajando,
                           ofertas_jora=ofertas_jora)

if __name__ == "__main__":
    app.run(debug=True)
```

Este código crea una aplicación web que:

Permite a los usuarios buscar ofertas laborales en tres plataformas de empleo populares (Computrabajo, Trabajando.pe, y Jora).
Extrae y organiza las ofertas laborales utilizando técnicas de web scraping.
Muestra los resultados en una página web estructurada e interactiva.
Es útil para quienes buscan centralizar múltiples fuentes de búsqueda de empleo en un solo lugar, ahorrando tiempo al combinar los resultados de distintas plataformas.

# Conclusión
Este proyecto demuestra cómo se pueden integrar diferentes fuentes de información y ofrecer un servicio que mejora la experiencia del usuario al buscar empleo. La utilización de web scraping y la creación de una aplicación web interactiva optimizan el proceso, ahorrando tiempo y esfuerzo a los usuarios. Además, la arquitectura modular permite fácilmente añadir más plataformas de empleo en el futuro, extendiendo así el alcance de la aplicación. En resumen, la aplicación es una herramienta útil y eficiente para quienes buscan empleo en diversas plataformas, mejorando la accesibilidad y eficiencia en el proceso de búsqueda.


**Fuente de datos:**
- Computrabajo:
(https://pe.computrabajo.com/)
- Bumeran:
(https://www.bumeran.com.pe/empleos.html/?utm_source=google&utm_medium=cpc&utm_campaign=B2C-GS-Category&gad_source=1&gclid=CjwKCAiAmMC6BhA6EiwAdN5iLbzlA92OPab-e_ofv3Txs8mIIktpa0j-6PsRJdHnJUkYm0npEeal5RoCqDcQAvD_BwE)
- Indeed:
(https://pe.indeed.com/?from=gnav-jobsearch--indeedmobile)

**Otros:**
- https://trabajando.pe/
- https://pe.jobomas.com/
- https://www.linkedin.com/jobs/

**Desarrolladores:**
- Montufar Paiva Yeraldi Mercedes
https://github.com/Yeraldii
- Pizarro de la Torre Brisa Antonella
https://github.com/BrisaPizarro
- Vasquez Velasquez, Flavia Mercedes
https://github.com/Flavia-Vasquez
