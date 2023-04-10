from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.pagesizes import letter
oy=['oy','Yanvar','Fevral','Mart','Aprel','May','Iyun','Iyul','Avgust','Sentabr','Oktabr','Noyabr','Dekabr']
# Open the image

data={
    "seriya":"53243",
    "date_from":"22",
    "date_to":"23",
    "company_name":"GROSS SUG'URTA KOMPANIYASI AJ Toshkent sh., A.Temur koch., 1-chi tor koch., 6 uy",
    "phone_number":"998930045698",
    "car_marka":"TOYOTA",
    "car_year":"2018",
    "car_dvigatel":"22",
    "car_kuzov":"22",
    "car_number":"AA 1234 AA",
    "driver":["HASSANG111HOLIZADEH"," AHMEDREZA",'XXX'],
    "seriya_card":"AB",
    "seriya_number":"0052859"
}
from reportlab.pdfgen import canvas

def police(data):
        img = Image.open('static/jpg (1).jpg')
        img2 = Image.open('static/jpg (2).jpg')
        # Create a drawing object
        draw = ImageDraw.Draw(img)
        draw2 = ImageDraw.Draw(img2)
        # Set the font
        font_path = 'static/font/PrimaSerif_BT_Bold.ttf'
        font = ImageFont.truetype(font_path, size=35)
        # Set the text color
        color = (0, 0, 0)
        #seriya
        text_seriya = data['seriya']
        position = (2090, 390)
        #date
        text_date_from = data['date_from']
        text_date_to = data['date_to']
        position1 = (505, 870)
        position2 = (1110, 870)
        text_oy=oy[4]
        position_oy=(590, 870)
        position2_oy=(1200, 870)
        position3_oy = (910, 2915)
        draw2.text(position3_oy, text_oy, font=ImageFont.truetype(font_path, size=35), fill=color)

        draw.text(position_oy, text_oy, font=ImageFont.truetype(font_path, size=35), fill=color)
        draw.text(position2_oy, text_oy, font=ImageFont.truetype(font_path, size=35), fill=color)

        #draw 2
        position_d2= (545, 2515)
        position_d22= (545, 2560)
        draw2.text(position_d2, text_seriya, font= ImageFont.truetype('arial.ttf', size=38), fill=color)
        draw2.text(position_d22, text_seriya, font= ImageFont.truetype('arial.ttf', size=38), fill=color)
        position_d3= (833, 2918)
        draw2.text(position_d3, text_date_from, font= ImageFont.truetype('arial.ttf', size=38), fill=color)
        #company name
        text_company_name = data['company_name']
        position3=(320,945)
        #user name
        text_user_name = data['driver'][0]+" "+data['driver'][1]+" "+data['driver'][2]
        position4=(550,1130)
        #phone number
        phone_number = data['phone_number']
        x = 940
        y = 1310
        for i in phone_number:
            position5=(x,y)
            draw.text(position5, i, font=ImageFont.truetype(font_path, size=45), fill=color)
            x=x+120
        #########
        #car info
        car=[data['car_marka'],data['car_year'],data['car_dvigatel'],data['car_kuzov'],data['car_number']]
        y1=1650
        x1=250
        for i in car:
            position6=(x1,y1)
            draw.text(position6, i, font=font, fill=color)
            x1=x1+450
        #driver info
        driver=data['driver']
        y3=2150
        x3=330
        for i in driver:
            position7=(x3,y3)
            draw.text(position7, i, font=font, fill=color)
            y3=y3+45
        #driver card
        seriya = data['seriya_card']
        seriya_number = data['seriya_number']
        position_seriya = ( 1290,2195)
        position_seriya_number = ( 1400,2195)
        draw.text(position_seriya, seriya, font=font, fill=color)
        draw.text(position_seriya_number, seriya_number, font=font, fill=color)
        # Draw the text on the image
        draw.text(position, text_seriya, font=font, fill=color)
        draw.text(position1, text_date_from, font=font, fill=color)
        draw.text(position2, text_date_to, font=font, fill=color)
        draw.text(position3, text_company_name, font=font, fill=color)
        draw.text(position4, text_user_name, font=font, fill=color)
        # Save the modified image
        img.save('1-qism.jpg')
        img2.save('2-qism.jpg')
        def pdf(img1,img2):
            image_files = [img1, img2]
            pdf_filename = "combined_ima111ges.pdf"
            canvas_obj = canvas.Canvas(pdf_filename)
            page_width, page_height = letter

            # loop through the image files and add them to the PDF
            for i, image_file in enumerate(image_files):
                # open the image file
                im = Image.open(image_file)

                # set the dimensions of the image on the PDF
                image_width, image_height = im.size
                if i == 0:
                    canvas_obj.setPageSize((image_width, image_height))
                else:
                    canvas_obj.showPage()
                x = 0
                y = 0
                canvas_obj.drawImage(image_file, x, y, width=image_width, height=image_height)

            # save the PDF file
            canvas_obj.save()
        pdf('1-qism.jpg','2-qism.jpg')



police(data)