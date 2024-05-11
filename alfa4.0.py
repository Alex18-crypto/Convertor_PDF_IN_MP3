import PyPDF2  # Importă modulul PyPDF2 pentru manipularea fișierelor PDF
from gtts import gTTS  # Importă clasa gTTS din modulul gtts pentru generarea de vorbire din text
import os  # Importă modulul os pentru operații de sistem (de exemplu, manipularea de căi de fișiere)
import pyfiglet  # Importă modulul pyfiglet pentru afișarea de text în stil ASCII art
from tqdm import tqdm  # Importă clasa tqdm pentru afișarea barelor de progres în iterații

def display_intro():
    # Afiseaza titlul programului folosind ASCII art
    intro_text = pyfiglet.figlet_format("Convertor PDF in MP3")  # Creează textul ASCII art pentru titlu
    sub_text = pyfiglet.figlet_format("Autor JBL")  # Creează textul ASCII art pentru autor
    print(intro_text)  # Afișează titlul programului
    print(sub_text)  # Afișează autorul programului

def pdf_to_text(pdf_path):
    # Extrage textul din fișierul PDF specificat
    text = ""  # Inițializează un șir gol pentru a stoca textul extras din PDF
    with open(pdf_path, 'rb') as file:  # Deschide fișierul PDF în mod binar pentru citire
        reader = PyPDF2.PdfReader(file)  # Inițializează un cititor de PDF-uri
        # Parcurge fiecare pagină și extrage textul
        for page_num in tqdm(range(len(reader.pages)), desc="Extragere text", unit="pagină"):
            page = reader.pages[page_num]  # Obține pagina curentă
            text += page.extract_text()  # Extrage textul din pagina curentă și îl adaugă la textul general
    return text  # Returnează textul extras din PDF

def text_to_speech(text, output_path):
    # Converteste textul dat într-un fișier MP3 utilizând gTTS
    tts = gTTS(text=text, lang='ro')  # Inițializează un obiect gTTS cu textul dat și limba română
    tts.save(output_path)  # Salvează fișierul MP3 la calea specificată

def pdf_to_mp3(pdf_path, output_path):
    pages_converted = 0  # Inițializează numărul de pagini convertite cu 0
    try:
        print("Conversie PDF în MP3 începută...")  # Afișează mesajul de începere a conversiei
        # Extrage textul din PDF
        text = pdf_to_text(pdf_path)
        print("\nText extras cu succes. Generare MP3...")  # Afișează mesajul de reușită a extragerii textului
        # Converteste textul extras în fișier MP3
        text_to_speech(text, output_path)
        # Numără paginile din PDF
        pages_converted = len(PyPDF2.PdfReader(pdf_path).pages)
        print(f"\nFișierul MP3 a fost creat la {output_path}.")  # Afișează mesajul de reușită a conversiei
    except Exception as e:
        print("\nA apărut o eroare în timpul conversiei:")  # Afișează mesajul de eroare
        print(e)  # Afișează eroarea specifică
    finally:
        return pages_converted  # Returnează numărul de pagini convertite

if __name__ == "__main__":
    # Afiseaza titlul și autorul programului
    display_intro()
    pdf_file = "a.pdf"  # Numele fișierului PDF de convertit
    output_file = "output.mp3"  # Numele fișierului MP3 de ieșire
    retry = True  # Inițializează variabila pentru repetare cu True
    while retry:
        # Converteste fișierul PDF în fișier MP3
        converted_pages = pdf_to_mp3(pdf_file, output_file)
        print(f"Numărul de pagini convertite cu succes: {converted_pages}")  # Afișează numărul de pagini convertite
        choice = input("\nDoriți să reîncercați conversia? (da/nu): ").lower()  # Solicită opțiunea de reîncercare
        if choice != 'da':
            retry = False  # Întrerupe bucla dacă utilizatorul nu dorește reîncercarea conversiei
    input("\nApasă o tastă pentru a ieși din program...")  # Așteaptă o intrare pentru a încheia programul

