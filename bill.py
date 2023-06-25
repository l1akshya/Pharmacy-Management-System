def pdf_creater():
    from fpdf import FPDF
    file=open("bill.txt", "r+")
    file.readline()
    f= FPDF()
    f.add_page()
    f.set_font('Arial',size=30)
    y=20
    f.set_font('Arial',size=12)
    for i in file:
        i=str(i)
        print(i)
        if i=='Across\n' or i == "Down\n":
            f.set_font('Arial',size=25)
            f.text(10,y,txt=i)
        else:
            f.set_font('Arial',size=12)
            f.text(10,y,txt=i)
        y+=15
    f.output('bill.pdf')
pdf_creater()