import PyPDF2


# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def crea_pdf(input_pdf, pagina):
    """
  Crea un PDF contenente 6 copie della pagina specificata.

  Args:
    input_pdf: Il PDF di input.
    pagina: Il numero della pagina da copiare.

  Returns:
    Il PDF di output.
  """

    # Apri il PDF di input
    input_file = open(input_pdf, "rb")
    input_pdf = PyPDF2.PdfReader(input_file)

    # Ottieni la pagina specificata
    pagina_pdf = input_pdf.pages[pagina]

    # Crea un nuovo PDF
    output_pdf = PyPDF2.PdfWriter()

    # Aggiungi 6 copie della pagina specificata al nuovo PDF
    for i in range(6):
        output_pdf.add_page(pagina_pdf)

    # Salva il nuovo PDF
    output_file = open("output.pdf", "wb")
    output_pdf.write(output_file)
    output_file.close()

    return "output.pdf"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    input_pdf = "Marrone Rustico Caffè Etichetta_20231216_193816_0000.pdf"
    pagina = 2

    output_pdf = crea_pdf(input_pdf, pagina)

    print(f"Il PDF di output è stato creato con successo.")
