from pypdf import PdfReader, PdfWriter 
reader = PdfReader("dataAnalysisNotes.pdf")
writer = PdfWriter()

writer.append(reader)
writer.encrypt("2461")

with open("protected.pdf", "wb") as file : writer.write(file)
