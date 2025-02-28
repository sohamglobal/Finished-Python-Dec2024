from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(filename):
    # Create a canvas object with the filename and page size
    c = canvas.Canvas(filename, pagesize=letter)
    
    # Set the title and add some text
    c.setTitle("My First PDF")
    c.drawString(100, 750, "Hello, this is my first PDF!")
    
    # Draw a line
    c.line(100, 740, 400, 740)
    
    # Draw some more text
    c.drawString(100, 120, "This PDF was created using ReportLab.")
    
    # Save the PDF
    c.save()

# Call the function to create the PDF
create_pdf("my_first_pdf.pdf")
