from flask import Flask, render_template
from summarizer import summarize_text
import spacy
from textblob import TextBlob
import nltk  # Importa nltk

# Puedes inicializar los datos necesarios de nltk, si es necesario
nltk.download('punkt') 
app = Flask(__name__)

# Cargar el modelo de spaCy
nlp = spacy.load("en_core_web_sm")

# Datos estáticos de los artículos
articles = [
    {
        "id": 1,
        "title": "Artículo sobre Aprendizaje Automático",
        "authors": ["Juan Pérez", "Ana Gómez"],
        "year": 2023,
        "url": "https://example.com/articulo1",
        "abstract": "Este artículo explora los fundamentos del aprendizaje automático y sus aplicaciones en diversos campos.",
        "text": """
        El aprendizaje automático, una rama de la inteligencia artificial (IA), ha revolucionado múltiples industrias mediante el desarrollo de modelos que permiten a las máquinas aprender de los datos. Este artículo profundiza en los conceptos básicos del aprendizaje automático, comenzando con una explicación de los tipos de aprendizaje: supervisado, no supervisado y por refuerzo. En el aprendizaje supervisado, los modelos son entrenados con datos etiquetados, permitiéndoles hacer predicciones o clasificaciones sobre datos nuevos. En contraste, el aprendizaje no supervisado se enfoca en identificar patrones y estructuras ocultas en datos no etiquetados, mientras que el aprendizaje por refuerzo enseña a los modelos a tomar decisiones a través de la experiencia, optimizando una función de recompensa.

        Uno de los algoritmos más comunes en el aprendizaje automático es el de regresión lineal, que se utiliza para modelar la relación entre una variable dependiente y una o más variables independientes. Por otro lado, los algoritmos de clasificación, como el de máquinas de vectores de soporte (SVM) y los árboles de decisión, son empleados para categorizar datos en clases distintas. En el aprendizaje profundo, una subárea del aprendizaje automático, se utilizan redes neuronales profundas para capturar características complejas de los datos, y ha mostrado resultados excepcionales en tareas como el reconocimiento de imágenes y el procesamiento del lenguaje natural.

        Además de los algoritmos, el preprocesamiento de datos juega un papel crucial en el éxito de los modelos de aprendizaje automático. Técnicas como la normalización, la limpieza de datos y la selección de características son fundamentales para mejorar la precisión y eficiencia de los modelos. La evaluación de los modelos se realiza mediante métricas como la precisión, el recall y la puntuación F1, que ayudan a medir el desempeño y a ajustar los parámetros del modelo.

        El aprendizaje automático también plantea desafíos éticos y técnicos, como el sesgo en los datos, la privacidad y la interpretabilidad de los modelos. A medida que la tecnología avanza, es esencial abordar estos problemas para garantizar el desarrollo responsable y equitativo de los sistemas basados en aprendizaje automático. Este artículo concluye con una discusión sobre las tendencias futuras en el campo, incluyendo la integración de técnicas de aprendizaje automático con otras tecnologías emergentes, como el Internet de las Cosas (IoT) y la computación cuántica.
        """
    },
    {
        "id": 2,
        "title": "Investigación en Inteligencia Artificial",
        "authors": ["Carlos López", "María Fernández"],
        "year": 2022,
        "url": "https://example.com/articulo2",
        "abstract": "En esta investigación, se discuten las últimas tendencias y avances en inteligencia artificial.",
        "text": """
        La inteligencia artificial (IA) ha experimentado un crecimiento exponencial en las últimas décadas, transformando industrias y sectores a nivel mundial. Este artículo se centra en las últimas tendencias y avances en el campo de la IA, incluyendo el desarrollo de algoritmos más sofisticados, el aumento de la capacidad computacional y la expansión de aplicaciones en diversas áreas.

        Uno de los avances más significativos en IA es el desarrollo de modelos de lenguaje natural, como los transformers, que han mejorado la capacidad de las máquinas para comprender y generar texto humano. Modelos como GPT-3 y BERT han establecido nuevos estándares en procesamiento del lenguaje natural (NLP), facilitando tareas como la traducción automática, el análisis de sentimientos y la generación de texto.

        La robótica también ha visto grandes avances gracias a la IA, con la creación de robots autónomos que pueden realizar tareas complejas en entornos dinámicos. Estos robots están equipados con sensores y algoritmos de IA que les permiten interactuar con el entorno, tomar decisiones en tiempo real y aprender de la experiencia.

        La combinación de IA con otras tecnologías emergentes, como la realidad aumentada (AR) y la realidad virtual (VR), está creando nuevas oportunidades para aplicaciones innovadoras. En el ámbito de la salud, la IA se está utilizando para mejorar el diagnóstico y el tratamiento de enfermedades, con algoritmos que pueden analizar imágenes médicas y predecir brotes de enfermedades.

        Sin embargo, el rápido avance de la IA también plantea desafíos éticos y sociales. La automatización de trabajos, el sesgo en los algoritmos y la privacidad de los datos son temas críticos que deben abordarse para garantizar un desarrollo equitativo y responsable de la tecnología. Este artículo concluye con una reflexión sobre el impacto futuro de la IA en la sociedad y las estrategias para mitigar los riesgos asociados con su implementación.
        """
    },
    {
        "id": 3,
        "title": "Tendencias en Ciencia de Datos",
        "authors": ["Laura Martínez", "Pedro Sánchez"],
        "year": 2024,
        "url": "https://example.com/articulo3",
        "abstract": "El artículo analiza las tendencias actuales en el campo de la ciencia de datos y sus implicaciones futuras.",
        "text": """
        La ciencia de datos se ha convertido en un campo crucial para las organizaciones que buscan aprovechar el valor de sus datos. Este artículo examina las tendencias actuales en la ciencia de datos y cómo están moldeando el futuro del análisis de datos y la toma de decisiones basadas en datos.

        Una de las principales tendencias es la integración de técnicas de aprendizaje automático con la ciencia de datos para crear modelos predictivos y prescriptivos. Estos modelos ayudan a las empresas a identificar patrones en grandes conjuntos de datos, predecir resultados futuros y tomar decisiones informadas. El aprendizaje automático automatiza el proceso de análisis, permitiendo a los científicos de datos centrarse en tareas de mayor valor agregado, como la interpretación de resultados y la estrategia empresarial.

        Otra tendencia importante es el auge de la analítica en tiempo real. Con el aumento de la capacidad de procesamiento y el acceso a datos en tiempo real, las organizaciones pueden obtener información instantánea sobre sus operaciones y el comportamiento de los clientes. Esto facilita la toma de decisiones rápida y la capacidad de responder a cambios en el mercado de manera ágil.

        La visualización de datos también está evolucionando, con herramientas más avanzadas que permiten a los usuarios explorar y comprender los datos de manera interactiva. Las técnicas de visualización moderna, como los gráficos interactivos y las dashboards, hacen que los datos sean más accesibles y comprensibles para las partes interesadas no técnicas.

        La ética en la ciencia de datos es otra área de enfoque creciente. A medida que las organizaciones recopilan y analizan más datos, surge la necesidad de abordar cuestiones relacionadas con la privacidad de los datos, el consentimiento informado y el uso responsable de la información. Los científicos de datos deben ser conscientes de estos desafíos y trabajar para garantizar que sus prácticas cumplan con las normas éticas y legales.

        Finalmente, la ciencia de datos está cada vez más conectada con la inteligencia artificial y el aprendizaje automático, creando un ciclo continuo de innovación y mejora. A medida que las tecnologías avanzan, la ciencia de datos seguirá desempeñando un papel fundamental en la transformación digital y en la creación de valor para las organizaciones.
        """
    }
]
@app.route('/')
def index():
    try:
        # Generar resúmenes para cada artículo
        summarized_articles = []
        for article in articles:
            summary = summarize_text(article["text"])
            if summary is None:
                summary = "Resumen no disponible"
            summarized_articles.append({
                "id": article["id"],
                "title": article["title"],
                "authors": article["authors"],
                "year": article["year"],
                "url": article["url"],
                "abstract": article["abstract"],
                "summary": summary
            })
        return render_template('index.html', articles=summarized_articles)
    except Exception as e:
        return f"Error al generar los resúmenes: {e}", 500

@app.route('/article/<int:article_id>')
def view_article(article_id):
    try:
        # Encuentra el artículo correspondiente por su ID
        article = next((art for art in articles if art["id"] == article_id), None)
        if article is None:
            return "Artículo no encontrado", 404

        # Procesar el texto del artículo para extraer entidades clave
        doc = nlp(article["text"])

        # Filtrar entidades y limitar el número de entidades
        entities = [(ent.text, ent.label_) for ent in doc.ents if ent.label_ in ["PERSON", "ORG", "GPE"]]
        entities = entities[:10]  # Limitar a las primeras 10 entidades

        # Generar el resumen para el artículo
        summary = summarize_text(article["text"])
        if summary is None:
            summary = "Resumen no disponible"

        # Realizar el análisis de sentimientos
        sentiment_info = analyze_sentiment(article["text"])

        # Pasar todos los datos a la plantilla
        return render_template('view_article.html', article=article, summary=summary, entities=entities, sentiment_info=sentiment_info)
    except Exception as e:
        return f"Error al procesar el artículo: {e}", 500


def analyze_sentiment(text):
    # Análisis de sentimiento usando TextBlob
    blob = TextBlob(text)
    sentiment_polarity = blob.sentiment.polarity
    sentiment_subjectivity = blob.sentiment.subjectivity
    
    # Determinar el sentimiento general
    if sentiment_polarity > 0:
        sentiment = "Positivo"
    elif sentiment_polarity < 0:
        sentiment = "Negativo"
    else:
        sentiment = "Neutral"
    
    # Determinar la descripción de la subjetividad
    if sentiment_subjectivity > 0.5:
        subjectivity_description = "Subjetivo"
    else:
        subjectivity_description = "Objetivo"

    return {
        'sentiment': sentiment,
        'polarity': sentiment_polarity,
        'subjectivity': sentiment_subjectivity,
        'subjectivity_description': subjectivity_description
    }


if __name__ == '__main__':
    app.run(debug=True)