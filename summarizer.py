from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk

def summarize_text(text, sentence_count=3):
    try:
        # Asegúrate de que el tokenizer está disponible
        tokenizer = Tokenizer("english")
        
        # Crear el parser y el resumidor
        parser = PlaintextParser.from_string(text, tokenizer)
        summarizer = LsaSummarizer()
        
        # Generar el resumen
        summary = summarizer(parser.document, sentence_count)
        
        # Devolver el resumen como una cadena
        return ' '.join(str(sentence) for sentence in summary)
    
    except Exception as e:
        # Manejo de errores
        print(f"An error occurred: {e}")
        return None
