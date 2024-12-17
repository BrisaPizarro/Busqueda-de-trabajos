from flask import Flask, render_template, request
from scraping.Computrabajo import buscar_ofertas_computrabajo
from scraping.Trabajando_pe import buscar_ofertas_trabajando

app = Flask(__name__)

# Ruta para el formulario de búsqueda (GET)
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# Ruta para mostrar los resultados de la búsqueda
@app.route("/resultados", methods=["GET"])
def resultados():
    # Obtener los datos de búsqueda de la URL
    tipo_trabajo = request.args.get("tipo_trabajo")
    empresa = request.args.get("empresa")
    ubicacion = request.args.get("ubicacion")

    # Llamar a las funciones de scraping
    ofertas_computrabajo = buscar_ofertas_computrabajo(tipo_trabajo, empresa)
    ofertas_trabajando = buscar_ofertas_trabajando(tipo_trabajo, ubicacion)

    # Renderizar la página de resultados con los datos obtenidos
    return render_template("resultados.html", 
                           ofertas_computrabajo=ofertas_computrabajo,
                           ofertas_trabajando=ofertas_trabajando)

if __name__ == "__main__":
    app.run(debug=True)
