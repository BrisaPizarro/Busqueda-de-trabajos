import requests
from bs4 import BeautifulSoup

def buscar_ofertas_linkedin(termino_busqueda, ubicacion=None):
    url_base = "https://www.linkedin.com/jobs/search"

    params = {
        "keywords": termino_busqueda,
        "location": ubicacion if ubicacion else "",
        "trk": "public_jobs_jobs-search-bar_search-submit",
        "redirect": "false",
        "position": "1",
        "pageNum": "0"
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }

    response = requests.get(url_base, params=params, headers=headers)

    if response.status_code != 200:
        print("Error al acceder a LinkedIn")
        return [{"titulo": "No se encontró trabajo con los términos que usted especificó", "empresa": "N/A", "ubicacion": "N/A", "link": ""}]

    soup = BeautifulSoup(response.text, "html.parser")
    ofertas = soup.find_all("div", class_="base-card")

    resultados = []

    for oferta in ofertas[:10]:
        try:
            titulo_element = oferta.find("h3", class_="base-search-card__title")
            titulo = titulo_element.text.strip() if titulo_element else "Sin título"

            empresa_element = oferta.find("h4", class_="base-search-card__subtitle")
            empresa = empresa_element.text.strip() if empresa_element else "Sin empresa"

            ubicacion_element = oferta.find("span", class_="job-search-card__location")
            ubicacion = ubicacion_element.text.strip() if ubicacion_element else "Sin ubicación"

            link_element = oferta.find("a", class_="base-card__full-link")
            link = link_element["href"] if link_element else ""

            resultados.append({
                "titulo": titulo,
                "empresa": empresa,
                "ubicacion": ubicacion,
                "link": link
            })
        except AttributeError:
            continue

    return resultados

