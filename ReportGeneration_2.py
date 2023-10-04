import cv2 as cv

from tempfile import gettempdir
from os import path
from os import mkdir
from shutil import rmtree

from reportlab.platypus import SimpleDocTemplate, Image
from reportlab.lib.units import inch
from reportlab.platypus import Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_RIGHT
from reportlab.lib import colors
from reportlab.lib.colors import Color

from Cache import Cache


class ReportGeneration:
    def __init__(self, cache, save_file_name):
        self.cache = cache
        self.save_file_name = save_file_name
        self.current_directory = None

        self.doc = SimpleDocTemplate(self.save_file_name, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
        self.styles = getSampleStyleSheet()
        self.styles.add(ParagraphStyle(name="Justify", alignment=TA_JUSTIFY))
        self.styles.add(ParagraphStyle(name="Heading_C", textColor=Color(0, 0, 0, 1), leading=24, alignment=TA_CENTER))
        self.styles.add(ParagraphStyle(name="Heading_J", textColor=Color(0, 0, 0, 1), leading=24, alignment=TA_JUSTIFY))
        self.content = []

        self.WIDTH = 2.5
        self.HEIGHT = 2.5

        self.generate_report()

    def generate_report(self):
        self.save_images_to_temp_directory()
        print("Images stored in temp directory.")
        self.generate_first_page()
        print("First page generated.")
        self.generate_second_page()
        print("Second page generated.")
        self.generate_third_page()
        print("Third page generated.")
        self.generate_forth_page()
        print("Forth page generated.")
        self.generate_fifth_page()
        print("Fifth page generated.")
        self.doc.build(self.content)
        print("Report generated on path:", self.save_file_name)
        self.cleanup()
        print("Temp directory deleted.")

    def generate_first_page(self):
        self.content.append(Spacer(1, 24))

        nameLabel = Paragraph("<b>Name:</b>")
        nameField = Paragraph(self.cache.name)
        dateLabel = Paragraph("<b>Date:</b>")
        dateField = Paragraph(self.cache.date)
        refLabel = Paragraph("<b>Referred By::</b>")
        refField = Paragraph(self.cache.ref)
        ageLabel = Paragraph("<b>Age:</b>")
        ageField = Paragraph(self.cache.age)
        cpLabel = Paragraph("<b>C/P:</b>")
        cpField = Paragraph(self.cache.specialRemarks)
        idLabel = Paragraph("<b>Patient ID::</b>")
        idField = Paragraph(self.cache.id)
        data1 = [ [nameLabel, nameField, dateLabel, dateField], [refLabel, refField, ageLabel, ageField], [cpLabel, cpField, idLabel, idField] ]
        t1 = Table(data1, style=[ ("GRID", (0, 0), (-1, -1), 1, colors.blue, None, (1, 1, 1)) , ("VALIGN", (0,0), (-1,-1), "MIDDLE") ])
        self.content.append(t1)

        self.content.append(Spacer(1, 48))

        title = "<font face='times' size='14'><strong>DIGITAL THERMOGRAPHY STUDY : BILATERAL BREAST</strong></font>"
        #title = Paragraph("<h1><b>DIGITAL THERMOGRAPHY STUDY : BILATERAL BREAST</b></h1>")
        title = Paragraph(title, self.styles["Heading_C"])
        self.content.append(title)

        self.content.append(Spacer(1, 12))

        disclaimer1 = Paragraph("Digital Thermography of Breast done with CX-640. All standard protocols were followed during scan.")
        self.content.append(disclaimer1)

        self.content.append(Spacer(1, 36))

        findingsLabel = "<font face='times' size='11'><strong>FINDINGS</strong></font>"
        findingsLabel = Paragraph(findingsLabel, self.styles["Heading_J"])
        self.content.append(findingsLabel)

        self.content.append(Spacer(1, 12))

        firstEntry = Paragraph("<b>1]</b>")
        secondEntry = Paragraph("<b>2]</b>")
        leftBreastLabel = Paragraph("<b>Left Breast:</b>")
        rightBreastLabel = Paragraph("<b>Right Breast:</b>")
        leftBreastField = Paragraph(self.cache.remarks[0])
        rightBreastField = Paragraph(self.cache.remarks[1])
        data2 = [ [firstEntry, leftBreastLabel, leftBreastField], ["", "", ""], [secondEntry, rightBreastLabel, rightBreastField]  ]
        #t2 = Table(data2)
        t2 = Table(data2, colWidths=[0.5*inch, 1.5*inch, 4.5*inch], style=[ ("VALIGN", (0,0), (0,2), "TOP"), ("VALIGN", (1,0), (1,2), "TOP"), ("VALIGN", (2,0), (2,2), "TOP") ])
        self.content.append(t2)

        self.content.append(Spacer(1, 36))

        self.insertNNOutput()

        suggestLabel = "<b>Suggest:</b>"
        suggestLabel = Paragraph(suggestLabel)
        suggestField = Paragraph(self.cache.remarks[2])
        data3 = [ [suggestLabel, suggestField] ]
        t3 = Table(data3, colWidths=[1.5*inch, 5*inch], style=[ ("VALIGN", (0,0), (0,1), "TOP") ])
        self.content.append(t3)

        self.content.append(Spacer(1, 48))

        thanksLabel = "Thanks"
        thanksLabel = Paragraph(thanksLabel)
        self.content.append(thanksLabel)

        self.content.append(Spacer(1,24))

        disclaimer2 = "<i>Many thanks for reference. Imaging findings has its own limitations and needs to be correlated clinically.</i>"
        disclaimer2 = Paragraph(disclaimer2)
        self.content.append(disclaimer2)
        self.content.append(PageBreak())

    def insertNNOutput(self):
        output = self.cache.nn[0]
        confidence = self.cache.nn[1]
        confidence = confidence+"%"
        numberLabel = "<b>3]</b>"
        numberLabel = Paragraph(numberLabel)
        nnOutputLabel = "<b>NN Prediction:</b>"
        nnOutputLabel = Paragraph(nnOutputLabel)
        nnOutputField = output
        nnOutputField = Paragraph(nnOutputField)
        nnConfidenceLabel = "<b>Confidence:</b>"
        nnConfidenceLabel = Paragraph(nnConfidenceLabel)
        nnConfidenceField = confidence
        nnConfidenceField = Paragraph(nnConfidenceField)
        style = TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('VALIGN', (0, 0), (-1, -1), 'TOP')])

        # inserting only prediction
        #data1 = [ [numberLabel, nnOutputLabel, nnOutputField, "", ""] ]
        #t1 = Table(data1, colWidths=[0.5 * inch, 1.5 * inch, 1.5 * inch, 1.5 * inch, 1.5 * inch], style=style)
        #self.content.append(t1)

        # inserting both prediction and confidence
        data2 = [[numberLabel, nnOutputLabel, nnOutputField, nnConfidenceLabel, nnConfidenceField]]
        t2 = Table(data2, colWidths=[0.5 * inch, 1.5 * inch, 1.5 * inch, 1.5 * inch, 1.5 * inch], style=style)
        self.content.append(t2)

        self.content.append(Spacer(1, 24))

    def generate_second_page(self):
        originalImages = ["001_o.jpg", "002_o.jpg", "003_o.jpg", "004_o.jpg", "005_o.jpg"]
        anomalies = ["001_a.jpg", "002_a.jpg", "003_a.jpg", "004_a.jpg", "005_a.jpg"]
        edges = ["001_e.jpg", "002_e.jpg", "003_e.jpg", "004_e.jpg", "005_e.jpg"]

        frontViewAnomalyLabel = "<font size='16'>1. Anterior View (Anomaly Detection)</font>"
        frontViewAnomalyLabel = Paragraph(frontViewAnomalyLabel)
        self.content.append(frontViewAnomalyLabel)

        self.content.append(Spacer(1, 24))

        image1 = Image(self.current_directory+originalImages[0], self.WIDTH*inch, self.HEIGHT*inch)
        image2 = Image(self.current_directory+anomalies[0], self.WIDTH*inch, self.HEIGHT*inch)
        data4 = [ [image1, image2] ]
        image_style = TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('VALIGN', (0, 0), (-1, -1), 'CENTER')])
        t4 = Table(data4, colWidths=[(self.WIDTH+0.2) * inch, (self.WIDTH+0.2) * inch], rowHeights=[(self.HEIGHT+0.2) * inch], style=image_style)
        self.content.append(t4)

        self.content.append(Spacer(1, 24))

        obliqueViewAnomalyLabel = "<font size='16'>2. Oblique View (Anomaly Detection)</font>"
        obliqueViewAnomalyLabel = Paragraph(obliqueViewAnomalyLabel)
        self.content.append(obliqueViewAnomalyLabel)

        self.content.append(Spacer(1, 24))

        image3 = Image(self.current_directory+originalImages[4], self.WIDTH*inch, self.HEIGHT*inch)
        image4 = Image(self.current_directory+anomalies[4], self.WIDTH*inch, self.HEIGHT*inch)
        image5 = Image(self.current_directory+originalImages[3], self.WIDTH * inch, self.HEIGHT * inch)
        image6 = Image(self.current_directory+anomalies[3], self.WIDTH * inch, self.HEIGHT * inch)
        data5 = [ [image3, image4], [image5, image6] ]
        t5 = Table(data5, colWidths=[(self.WIDTH + 0.2) * inch, (self.WIDTH + 0.2) * inch], rowHeights=[(self.HEIGHT + 0.2) * inch, (self.HEIGHT + 0.2) * inch], style=image_style)
        self.content.append(t5)
        self.content.append(PageBreak())

    def generate_third_page(self):
        originalImages = ["001_o.jpg", "002_o.jpg", "003_o.jpg", "004_o.jpg", "005_o.jpg"]
        anomalies = ["001_a.jpg", "002_a.jpg", "003_a.jpg", "004_a.jpg", "005_a.jpg"]
        edges = ["001_e.jpg", "002_e.jpg", "003_e.jpg", "004_e.jpg", "005_e.jpg"]

        lateralViewAnomalyLabel = "<font size='16'>3. Lateral View (Anomaly Detection)</font>"
        lateralViewAnomalyLabel = Paragraph(lateralViewAnomalyLabel)
        self.content.append(lateralViewAnomalyLabel)

        self.content.append(Spacer(1,24))

        image7 = Image(self.current_directory+originalImages[2], self.WIDTH * inch, self.HEIGHT * inch)
        image8 = Image(self.current_directory+anomalies[2], self.WIDTH * inch, self.HEIGHT * inch)
        image9 = Image(self.current_directory+originalImages[1], self.WIDTH * inch, self.HEIGHT * inch)
        image10 = Image(self.current_directory+anomalies[1], self.WIDTH * inch, self.HEIGHT * inch)
        data6 = [[image7, image8], [image9, image10]]
        image_style = TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('VALIGN', (0, 0), (-1, -1), 'CENTER')])
        t6 = Table(data6, colWidths=[(self.WIDTH + 0.2) * inch, (self.WIDTH + 0.2) * inch], rowHeights=[(self.HEIGHT + 0.2) * inch, (self.HEIGHT + 0.2) * inch], style=image_style)
        self.content.append(t6)

        self.content.append(Spacer(1, 24))

        frontViewEdgeLabel = "<font size='16'>4. Anterior View(Angiogenesis / Neo - Angiogenesis)</font>"
        frontViewEdgeLabel = Paragraph(frontViewEdgeLabel)
        self.content.append(frontViewEdgeLabel)

        self.content.append(Spacer(1,24))

        image11 = Image(self.current_directory+originalImages[0], self.WIDTH * inch, self.HEIGHT * inch)
        image12 = Image(self.current_directory+edges[0], self.WIDTH * inch, self.HEIGHT * inch)
        data7 = [[image11, image12]]
        t7 = Table(data7, colWidths=[(self.WIDTH + 0.2) * inch, (self.WIDTH + 0.2) * inch],rowHeights=[(self.HEIGHT + 0.2) * inch], style=image_style)
        self.content.append(t7)
        self.content.append(PageBreak())

    def generate_forth_page(self):
        originalImages = ["001_o.jpg", "002_o.jpg", "003_o.jpg", "004_o.jpg", "005_o.jpg"]
        anomalies = ["001_a.jpg", "002_a.jpg", "003_a.jpg", "004_a.jpg", "005_a.jpg"]
        edges = ["001_e.jpg", "002_e.jpg", "003_e.jpg", "004_e.jpg", "005_e.jpg"]

        obliqueViewEdgeLabel = "<font size='16'>5. Oblique View (Angiogenesis / Neo-Angiogenesis)</font>"
        obliqueViewEdgeLabel = Paragraph(obliqueViewEdgeLabel)
        self.content.append(obliqueViewEdgeLabel)

        self.content.append(Spacer(1, 24))

        image13 = Image(self.current_directory+originalImages[4], self.WIDTH * inch, self.HEIGHT * inch)
        image14 = Image(self.current_directory+edges[4], self.WIDTH * inch, self.HEIGHT * inch)
        image15 = Image(self.current_directory+originalImages[3], self.WIDTH * inch, self.HEIGHT * inch)
        image16 = Image(self.current_directory+edges[3], self.WIDTH * inch, self.HEIGHT * inch)
        data8 = [[image13, image14], [image15, image16]]
        image_style = TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('VALIGN', (0, 0), (-1, -1), 'CENTER')])
        t8 = Table(data8, colWidths=[(self.WIDTH + 0.2) * inch, (self.WIDTH + 0.2) * inch], rowHeights=[(self.HEIGHT + 0.2) * inch, (self.HEIGHT + 0.2) * inch], style=image_style)
        self.content.append(t8)

        self.content.append(Spacer(1, 24))

        lateralViewEdgeLabel = "<font size='16'>3. Lateral View (Anomaly Detection)</font>"
        lateralViewEdgeLabel = Paragraph(lateralViewEdgeLabel)
        self.content.append(lateralViewEdgeLabel)

        self.content.append(Spacer(1, 24))

        image17 = Image(self.current_directory+originalImages[2], self.WIDTH * inch, self.HEIGHT * inch)
        image18 = Image(self.current_directory+edges[2], self.WIDTH * inch, self.HEIGHT * inch)
        data9 = [[image17, image18]]
        t9 = Table(data9, colWidths=[(self.WIDTH + 0.2) * inch, (self.WIDTH + 0.2) * inch], rowHeights=[(self.HEIGHT + 0.2) * inch], style=image_style)
        self.content.append(t9)
        self.content.append(PageBreak())

    def generate_fifth_page(self):
        originalImages = ["001_o.jpg", "002_o.jpg", "003_o.jpg", "004_o.jpg", "005_o.jpg"]
        anomalies = ["001_a.jpg", "002_a.jpg", "003_a.jpg", "004_a.jpg", "005_a.jpg"]
        edges = ["001_e.jpg", "002_e.jpg", "003_e.jpg", "004_e.jpg", "005_e.jpg"]

        image19 = Image(self.current_directory+originalImages[1], self.WIDTH * inch, self.HEIGHT * inch)
        image20 = Image(self.current_directory+edges[1], self.WIDTH * inch, self.HEIGHT * inch)
        data10 = [[image19, image20]]
        image_style = TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('VALIGN', (0, 0), (-1, -1), 'CENTER')])
        t10 = Table(data10, colWidths=[(self.WIDTH + 0.2) * inch, (self.WIDTH + 0.2) * inch], rowHeights=[(self.HEIGHT + 0.2) * inch], style=image_style)
        self.content.append(t10)

        self.content.append(Spacer(1,120))

        hmImage = None
        dmImage = None
        WIDTH = 1.5
        HEIGHT = 1.5
        if self.cache.historyMeterScore <= 9:
            hmImage = Image("green.png", WIDTH * inch, HEIGHT * inch)
        elif self.cache.historyMeterScore <= 14:
            hmImage = Image("yellow.jpg", WIDTH * inch, HEIGHT * inch)
        else:
            hmImage = Image("red.png", WIDTH * inch, HEIGHT * inch)
        if self.cache.diagnosticScore <= 50:
            dmImage = Image("green.png", WIDTH * inch, HEIGHT * inch)
        elif self.cache.diagnosticScore <= 74:
            dmImage = Image("yellow.jpg", WIDTH * inch, HEIGHT * inch)
        else:
            dmImage = Image("red.png", WIDTH * inch, HEIGHT * inch)

        hmLabel = "<font size='20'>HM</font>"
        hmLabel = Paragraph(hmLabel)
        dmLabel = "<font size='20'>DM</font>"
        dmLabel = Paragraph(dmLabel)

        data11 = [[hmLabel, hmImage, "", dmLabel, dmImage]]
        custom = TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')])
        t11 = Table(data11, colWidths=[(0.5 + 0.2) * inch, (WIDTH + 0.2) * inch, (0.5 + 0.2) * inch, (0.5 + 0.2) * inch, (WIDTH + 0.2) * inch], rowHeights=[(HEIGHT + 0.2) * inch], style=custom)
        self.content.append(t11)

    def save_images_to_temp_directory(self):
        temp_directory = gettempdir()
        temp_dir_name = "/temp"
        if path.exists(temp_directory + temp_dir_name) is True:
            rmtree(temp_directory + temp_dir_name)
        mkdir(temp_directory + temp_dir_name)
        current_directory = temp_directory + temp_dir_name + "/"
        self.current_directory = current_directory

        originalImages = ["001_o.jpg", "002_o.jpg", "003_o.jpg", "004_o.jpg", "005_o.jpg"]
        anomalies = ["001_a.jpg", "002_a.jpg", "003_a.jpg", "004_a.jpg", "005_a.jpg"]
        edges = ["001_e.jpg", "002_e.jpg", "003_e.jpg", "004_e.jpg", "005_e.jpg"]

        for i in range(len(self.cache.originalImages)):
            cv.imwrite(self.current_directory+originalImages[i], self.cache.originalImages[i])
        for i in range(len(self.cache.anomalies)):
            cv.imwrite(self.current_directory+anomalies[i], self.cache.anomalies[i])
        for i in range(len(self.cache.edges)):
            cv.imwrite(self.current_directory+edges[i], self.cache.edges[i][0])

    def cleanup(self):
        if path.exists(self.current_directory) is True:
            rmtree(self.current_directory)


def setup_cache(cache):
    cache.id = "2021-05-07,23:59:02.527544"
    cache.name = "Ms. temp1 tmep2 temp3"
    cache.ref = "Dr. tmp1 tmp2 tmp3"
    cache.age = "57"
    cache.specialRemarks = "special remark1\nnext line remark"
    cache.historyMeterScore = 5

    originalImages = ["001_o.jpg", "002_o.jpg", "003_o.jpg", "004_o.jpg", "005_o.jpg"]
    anomalies = ["001_a.jpg", "002_a.jpg", "003_a.jpg", "004_a.jpg", "005_a.jpg"]
    edges = ["001_e.jpg", "002_e.jpg", "003_e.jpg", "004_e.jpg", "005_e.jpg"]

    for i in range(len(cache.originalImages)):
        cache.originalImages[i] = cv.imread(originalImages[i])

    for i in range(len(cache.anomalies)):
        cache.anomalies[i] = cv.imread(anomalies[i])

    for i in range(len(cache.edges)):
        cache.edges[i][0] = cv.imread(edges[i])
        cache.edges[i][0] = cv.cvtColor(cache.edges[i][0], cv.COLOR_BGR2GRAY)

    cache.remarks = ["left breast findings asddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd\\nnew line\nthird line\nforth line\nfifth line", "right breast findings\nnew line", "suggestions and findings\nnew line\n\n\n\n\n\n\n\nvery last line"]
    cache.diagnosticScore = 49
    cache.nn = ["Negative Breast Mass Characteristics", "82.45"]

    return cache


if __name__ == "__main__":
    cache = Cache()
    cache = setup_cache(cache)
    cache.print()
    save_path = gettempdir() + "\\" + "report.pdf"
    obj = ReportGeneration(cache, save_path)

