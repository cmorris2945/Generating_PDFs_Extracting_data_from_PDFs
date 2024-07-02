from fpdf import FPDF
pdf = FPDF(orientation='P', unit='pt')

pdf.add_page()

pdf.image("/home/user01/Desktop/Generating_PDFs_Extracting_data_from_PDFs/tiger.jpeg", w=80,h=50)

pdf.set_font(family="Times", style="B", size=24)
pdf.cell(w=0,h=50, txt='Malayan Tigen "ova heeya"', align='C', ln=1)

pdf.set_font(family="Times", style="B", size=14)

pdf.cell(w=0,h=50,txt='Description', ln=1)


pdf.set_font(family="Times", size=12)
txt1 = """The Malayan tiger is a tiger from a specific population of the 
Panthera tigris tigris subspecies that is native to Peninsular Malaysia.[5] 
This population inhabits the southern and central parts of the Malay Peninsula 
and has been classified as critically endangered on the IUCN Red List since 2015.
As of April 2014, the population was estimated at 80 to 120 mature individuals 
with a continuous declining trend"""

pdf.multi_cell(w=0,h=50,txt=txt1)

pdf.set_font(family="Times", style="B", size=14)
pdf.cell(w=100,h=25, txt='KINGDOM:')

pdf.set_font(family="Times", size=14)
pdf.cell(w=100,h=25, txt='Animalia', ln=1)


pdf.set_font(family="Times", size=14)
pdf.cell(w=100,h=25, txt='Phylum', ln=1)

pdf.set_font(family="Times", size=14)
pdf.cell(w=100,h=25, txt='Chordata', ln=1)








pdf.output("output.pdf")


