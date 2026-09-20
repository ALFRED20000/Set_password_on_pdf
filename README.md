# About Set_password_on_pdf
```
Set_password_on_pdf is a single-purpose tool that set password on a pdf file to encrypt pdfs quickly. It will also create moderately safe passwords for said files, so you don't have to worry
```
## Disclaimer
Encrypting PDFs is, at best, protection against the prying eyes of an opportunistic attacker. Do not rely on the above program or password-protected PDFs in general for critical information. this is owned by Alfred Mensah.

---
## Installation

git clone https://github.com/ALFRED20000/Set_password_on_pdf.git

## Dependencies 
<h4> Set_password_on_pdf uses the PyPDF module.

The specific versions can be found in the requirements file. The modules can be installed manually or using said file:

Linux/OSX:
</h4>

<h4> WINDOWS </h4>
<h4> install https://code.visualstudio.com/download?_exp_download=d53503e735</h4>
<h4> pip install pypdf</h4>
---
<h5> 
from pypdf import PdfReader, PdfWriter 
reader = PdfReader("dataAnalysisNotes.pdf")
writer = PdfWriter()

writer.append(reader)
#remove the hash tag and run to set password
#writer.encrypt("2461")

with open("protected.pdf", "wb") as file : writer.write(file)
</h5>
---
