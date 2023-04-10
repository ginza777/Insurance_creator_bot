from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, Update,ChatAction,ReplyKeyboardRemove
import random
from telegram.ext import CallbackContext

from django.conf import settings
from telegram import Bot

bot = Bot(token=settings.TOKEN)
# Insurance company name
gros = "GROSS SUG'URTA KOMPANIYASI AJ Toshkent sh., A.Temur koch., 1-chi tor koch., 6 uy"
uzbekinvest = """O'ZBEKINVEST" AJ EKSPORT-IMPORT SUG'URTA KOMPANIYASI" AKSIYADORLIK JAMIYATI"""
oy=['oy','Yanvar','Fevral','Mart','Aprel','May','Iyun','Iyul','Avgust','Sentabr','Oktabr','Noyabr','Dekabr']
company_name = [gros, uzbekinvest]
from reportlab.lib.pagesizes import letter
from PIL import Image, ImageDraw, ImageFont
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
    # seriya
    text_seriya = data['seriya']
    position = (2090, 390)
    # date
    text_date_from = data['date_from']
    text_date_to = data['date_to']
    position1 = (505, 870)
    position2 = (1110, 870)
    text_oy = oy[4]
    position_oy = (590, 870)
    position2_oy = (1200, 870)
    position3_oy = (910, 2915)
    draw2.text(position3_oy, text_oy, font=ImageFont.truetype(font_path, size=35), fill=color)
    draw.text(position_oy, text_oy, font=ImageFont.truetype(font_path, size=35), fill=color)
    draw.text(position2_oy, text_oy, font=ImageFont.truetype(font_path, size=35), fill=color)
    # draw 2
    position_d2 = (545, 2515)
    position_d22 = (545, 2560)
    draw2.text(position_d2, text_seriya, font=ImageFont.truetype('arial.ttf', size=38), fill=color)
    draw2.text(position_d22, text_seriya, font=ImageFont.truetype('arial.ttf', size=38), fill=color)
    position_d3 = (833, 2918)
    draw2.text(position_d3, text_date_from, font=ImageFont.truetype('arial.ttf', size=38), fill=color)
    # company name
    text_company_name = data['company_name']
    position3 = (320, 945)
    # user name
    text_user_name = data['driver'][0] + "   " + data['driver'][1] + "   " + data['driver'][2]
    position4 = (550, 1130)
    # phone number
    phone_number = data['phone_number']
    x = 940
    y = 1310
    for i in phone_number:
        position5 = (x, y)
        draw.text(position5, i, font=ImageFont.truetype(font_path, size=45), fill=color)
        x = x + 120
    #########
    # car info
    car = [data['car_marka'], data['car_year'], data['car_dvigatel'], data['car_kuzov'], data['car_number']]
    y1 = 1650
    x1 = 250
    for i in car:
        position6 = (x1, y1)
        draw.text(position6, i, font=font, fill=color)
        x1 = x1 + 450
    # driver info
    driver = data['driver']
    y3 = 2150
    x3 = 330
    for i in driver:
        position7 = (x3, y3)
        draw.text(position7, i, font=font, fill=color)
        y3 = y3 + 45
    # driver card
    seriya = data['seriya_card']
    seriya_number = data['seriya_number']
    position_seriya = (1290, 2195)
    position_seriya_number = (1400, 2195)
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

    def pdf(img1, img2):
        image_files = [img1, img2]
        pdf_filename = "insurance.pdf"
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

    pdf('1-qism.jpg', '2-qism.jpg')
    with open('insurance.pdf', 'rb') as f:
        bot.send_document(chat_id='@police_insurance', document=f,
        caption=f"""driver: {data['driver'][0]} {data['driver'][1]} {data['driver'][2]} \ndata: {data['date_from']} - {data['date_to']} \ncar: {data['car_marka']} {data['car_year']}\ncompany:{data['company_name']}\nseriya: {data['seriya']} \ngroup:@police_insurance \nbot:@police_insurancebot""")






# Lets us use the /start command
def start_command(update, context):


    update.message.reply_text('Hello there! I\'m a bot_function. What\'s up?'
                              'follow my group @police_insurance',
                              reply_markup=ReplyKeyboardMarkup([['New police']], resize_keyboard=True))


# Lets us use the /help command
def help_command(update, context):
    update.message.reply_text('Try typing anything and I will do my best to respond!')


# Lets us use the /custom command
def custom_command(update, context):
    update.message.reply_text('This is a custom command, you can add whatever text you want here.')


def handle_response(text) -> str:
    # Create your own response logic

    if 'hello' in text:
        return 'Hey there!'

    if 'how are you' in text:
        return 'I\'m good!'

    return text[::-1]


def message_police(data):
    simbol = "❓❓❓❓"
    # seriya is not exist
    if data['seriya'] == 0:
        seriya = simbol
    else:
        seriya = data['seriya']
    # vaqtdan is not exist
    if data['vaqtdan'] == 0:
        vaqtdan = simbol
    else:
        vaqtdan = data['vaqtdan']
    # gacha is not exist
    if data['gacha'] == 0:
        gacha = simbol
    else:
        gacha = data['gacha']
    # company_name is not exist
    if data['company_name'] == 0:
        company_name = simbol
    else:
        company_name = data['company_name']
    # ismi is not exist
    if data['ismi'] == 0:
        ismi = simbol
    else:
        ismi = data['ismi']
    # familiyasi is not exist
    if data['familiyasi'] == 0:
        familiyasi = simbol
    else:
        familiyasi = data['familiyasi']
    # otasining_ismi is not exist
    if data['otasining_ismi'] == 0:
        otasining_ismi = simbol
    else:
        otasining_ismi = data['otasining_ismi']
    # phone is not exist
    if data['phone'] == 0:
        phone = simbol
    else:
        phone = data['phone']
    # model is not exist
    if data['model'] == 0:
        model = simbol
    else:
        model = data['model']
    # yili is not exist
    if data['yili'] == 0:
        yili = simbol
    else:
        yili = data['yili']
    # davlat_raqami is not exist
    if data['davlat_raqami'] == 0:
        davlat_raqami = simbol
    else:
        davlat_raqami = data['davlat_raqami']
    # dvigatel_raqami is not exist
    if data['dvigatel_raqami'] == 0:
        dvigatel_raqami = simbol
    else:
        dvigatel_raqami = data['dvigatel_raqami']
    # kuzov_raqami is not exist
    if data['kuzov_raqami'] == 0:
        kuzov_raqami = simbol
    else:
        kuzov_raqami = data['kuzov_raqami']
    # guvohnoma_seriya is not exist
    if data['guvohnoma_seriya'] == 0:
        guvohnoma_seriya = simbol
    else:
        guvohnoma_seriya = data['guvohnoma_seriya']
    # guvohnoma_raqami is not exist
    if data['guvohnoma_raqami'] == 0:
        guvohnoma_raqami = simbol
    else:
        guvohnoma_raqami = data['guvohnoma_raqami']

    msg = (f"""   Seriya: EGIL {seriya}
    Vaqtdan:     {vaqtdan}
    Gacha:   {gacha}
    Sug'urta company:    {company_name}
    Ismi:    {ismi}
    Familiyasi:  {familiyasi}
    Otasining ismi:     {otasining_ismi}
    Phone:  {phone}
    Model:    {model}
    Yili:   {yili}
    Davlat raqami:  {davlat_raqami}
    Dvigatel raqami:    {dvigatel_raqami}
    Kuzov raqami:    {kuzov_raqami}
    Guvohnoma seriya:    {guvohnoma_seriya}
    Guvohnoma raqami:    {guvohnoma_raqami}

    """)
    return msg


def New_police(update, context):





    seriya = random.randint(52800, 53800)
    context.user_data['seriya'] = seriya
    context.user_data['vaqtdan'] = 0
    context.user_data['gacha'] = 0
    context.user_data['company_name'] = 0
    context.user_data['ismi'] = 0
    context.user_data['familiyasi'] = 0
    context.user_data['otasining_ismi'] = 0
    context.user_data['phone'] = 0
    context.user_data['model'] = 0
    context.user_data['yili'] = 0
    context.user_data['davlat_raqami'] = 0
    context.user_data['dvigatel_raqami'] = 0
    context.user_data['kuzov_raqami'] = 0
    context.user_data['guvohnoma_seriya'] = 0
    context.user_data['guvohnoma_raqami'] = 0
    data = context.user_data
    msg = message_police(data)


    chat_id = update.message.chat_id
    message = context.bot.send_message(chat_id=chat_id, text=f"{msg}\n1.Qaysi kundan boshlab :",reply_markup=ReplyKeyboardRemove())
    context.user_data['message_id'] =message.message_id
    context.user_data['chat_id'] = chat_id




    return '1'


def From_time(update: Update, context: CallbackContext):
    context.user_data['vaqtdan'] = update.message.text
    context.user_data['gacha'] = int(context.user_data['vaqtdan']) - 1
    data = context.user_data
    msg = message_police(data)

    chat_id = update.message.chat_id
    message = context.bot.send_message(chat_id=chat_id, text=msg + "3.Sug'urta kompaniyasini tanlang:",reply_markup=ReplyKeyboardMarkup([company_name], resize_keyboard=True))
    context.bot.delete_message(chat_id=chat_id, message_id=context.user_data['message_id'])
    context.bot.delete_message(chat_id=chat_id, message_id=update.message.message_id)
    context.user_data['message_id'] =message.message_id
    return '2'


def Company_name(update: Update, context: CallbackContext):
    context.user_data['company_name'] = update.message.text
    data = context.user_data
    msg = message_police(data)
    chat_id = update.message.chat_id
    message = context.bot.send_message(chat_id=chat_id, text=msg + "4.Ismingizni kiriting :",reply_markup=ReplyKeyboardRemove())
    context.bot.delete_message(chat_id=chat_id, message_id=context.user_data['message_id'])
    context.bot.delete_message(chat_id=chat_id, message_id=update.message.message_id)
    context.user_data['message_id'] =message.message_id

    return '3'


def Name(update: Update, context: CallbackContext):
    context.user_data['ismi'] = update.message.text
    data = context.user_data
    msg = message_police(data)


    chat_id = update.message.chat_id
    message = context.bot.send_message(chat_id=chat_id, text=msg + "5.Familiyangizni kiriting :",reply_markup=ReplyKeyboardRemove())
    context.bot.delete_message(chat_id=chat_id, message_id=context.user_data['message_id'])
    context.bot.delete_message(chat_id=chat_id, message_id=update.message.message_id)
    context.user_data['message_id'] =message.message_id
    return '4'


def Surname(update: Update, context: CallbackContext):
    context.user_data['familiyasi'] = update.message.text
    data = context.user_data
    msg = message_police(data)

    chat_id = update.message.chat_id
    message = context.bot.send_message(chat_id=chat_id, text=msg + "6.Otasining ismini kiriting :",reply_markup=ReplyKeyboardMarkup([['XXX']], resize_keyboard=True))
    context.bot.delete_message(chat_id=chat_id, message_id=context.user_data['message_id'])
    context.bot.delete_message(chat_id=chat_id, message_id=update.message.message_id)
    context.user_data['message_id'] =message.message_id


    return '5'


def Father_name(update: Update, context: CallbackContext):
    context.user_data['otasining_ismi'] = update.message.text
    data = context.user_data
    msg = message_police(data)

    chat_id = update.message.chat_id
    message = context.bot.send_message(chat_id=chat_id, text=msg + "7.Telefon raqamingizni kiriting :",
                                       reply_markup=ReplyKeyboardMarkup([['998930045698']], resize_keyboard=True))
    context.bot.delete_message(chat_id=chat_id, message_id=context.user_data['message_id'])
    context.bot.delete_message(chat_id=chat_id, message_id=update.message.message_id)
    context.user_data['message_id'] = message.message_id

    return '6'


def Phone_number(update: Update, context: CallbackContext):
    context.user_data['phone'] = update.message.text
    data = context.user_data
    msg = message_police(data)


    chat_id = update.message.chat_id
    message = context.bot.send_message(chat_id=chat_id, text=msg + "8.Modelini kiriting :",
                                       reply_markup=ReplyKeyboardRemove())
    context.bot.delete_message(chat_id=chat_id, message_id=context.user_data['message_id'])
    context.bot.delete_message(chat_id=chat_id, message_id=update.message.message_id)
    context.user_data['message_id'] = message.message_id
    return '7'


def Model(update: Update, context: CallbackContext):
    context.user_data['model'] = update.message.text
    data = context.user_data
    msg = message_police(data)


    chat_id = update.message.chat_id
    message = context.bot.send_message(chat_id=chat_id, text=msg + "9.Yilini kiriting :",
                                       reply_markup=ReplyKeyboardRemove())
    context.bot.delete_message(chat_id=chat_id, message_id=context.user_data['message_id'])
    context.bot.delete_message(chat_id=chat_id, message_id=update.message.message_id)
    context.user_data['message_id'] = message.message_id
    return '8'


def Year(update: Update, context: CallbackContext):
    context.user_data['yili'] = update.message.text
    data = context.user_data
    msg = message_police(data)


    chat_id = update.message.chat_id
    message = context.bot.send_message(chat_id=chat_id, text=msg + "10.Davlat raqamini kiriting :",
                                       reply_markup=ReplyKeyboardRemove())
    context.bot.delete_message(chat_id=chat_id, message_id=context.user_data['message_id'])
    context.bot.delete_message(chat_id=chat_id, message_id=update.message.message_id)
    context.user_data['message_id'] = message.message_id
    return '9'


def Davlat_raqami(update: Update, context: CallbackContext):
    context.user_data['davlat_raqami'] = update.message.text
    data = context.user_data
    msg = message_police(data)


    chat_id = update.message.chat_id
    message = context.bot.send_message(chat_id=chat_id, text=msg + "11.Divigatel raqamini kiriting :",
                                       reply_markup=ReplyKeyboardRemove())
    context.bot.delete_message(chat_id=chat_id, message_id=context.user_data['message_id'])
    context.bot.delete_message(chat_id=chat_id, message_id=update.message.message_id)
    context.user_data['message_id'] = message.message_id
    return '10'


def Motor(update: Update, context: CallbackContext):
    context.user_data['dvigatel_raqami'] = update.message.text
    data = context.user_data
    msg = message_police(data)


    chat_id = update.message.chat_id
    message = context.bot.send_message(chat_id=chat_id, text=msg + "12.Kuzov raqamini kiriting :",
                                       reply_markup=ReplyKeyboardRemove())
    context.bot.delete_message(chat_id=chat_id, message_id=context.user_data['message_id'])
    context.bot.delete_message(chat_id=chat_id, message_id=update.message.message_id)
    context.user_data['message_id'] = message.message_id
    return '11'


def Kuzov_raqami(update: Update, context: CallbackContext):
    context.user_data['kuzov_raqami'] = update.message.text
    data = context.user_data
    msg = message_police(data)



    chat_id = update.message.chat_id
    message = context.bot.send_message(chat_id=chat_id, text=msg + "13.Guvohnoma seriyasini kiriting :",
                                       reply_markup=ReplyKeyboardRemove())
    context.bot.delete_message(chat_id=chat_id, message_id=context.user_data['message_id'])
    context.bot.delete_message(chat_id=chat_id, message_id=update.message.message_id)
    context.user_data['message_id'] = message.message_id
    return '12'


def Guvohnoma_seriya(update: Update, context: CallbackContext):
    context.user_data['guvohnoma_seriya'] = update.message.text.upper()
    data = context.user_data
    msg = message_police(data)


    chat_id = update.message.chat_id
    message = context.bot.send_message(chat_id=chat_id, text=msg + "14.Guvohnoma raqamini kiriting :",
                                       reply_markup=ReplyKeyboardRemove())
    context.bot.delete_message(chat_id=chat_id, message_id=context.user_data['message_id'])
    context.bot.delete_message(chat_id=chat_id, message_id=update.message.message_id)
    context.user_data['message_id'] = message.message_id
    return '13'


def Guvohnoma_raqami(update: Update, context: CallbackContext):
    context.user_data['guvohnoma_raqami'] = update.message.text
    data = context.user_data
    msg = message_police(data)


    chat_id = update.message.chat_id
    message = context.bot.send_message(chat_id=chat_id, text=msg + "15.Sizning sug'urtangiz  yaratildi",
                                       reply_markup=ReplyKeyboardMarkup([['/start'],['New police']], resize_keyboard=True))
    context.bot.delete_message(chat_id=chat_id, message_id=context.user_data['message_id'])
    context.bot.delete_message(chat_id=chat_id, message_id=update.message.message_id)
    context.user_data['message_id'] = message.message_id


    driver=[]
    driver.append(context.user_data['ismi'].upper())
    driver.append(context.user_data['familiyasi'].upper())
    driver.append(context.user_data['otasining_ismi'].upper())
    data={
        "seriya":f"{context.user_data['seriya']}",
        "date_from":f"{context.user_data['vaqtdan']}",
        "date_to":f"{context.user_data['gacha']}",
        "company_name":f"{context.user_data['company_name']}",
        "phone_number":f"{context.user_data['phone']}",
        "car_marka":f"{context.user_data['model'].upper()}",
        "car_year":f"{context.user_data['yili']}",
        "car_number":f"{context.user_data['davlat_raqami'].upper()}",
        "car_dvigatel":f"{context.user_data['dvigatel_raqami'].upper()}",
        "car_kuzov":f"{context.user_data['kuzov_raqami'].upper()}",
        "driver":driver,
        "seriya_card":f"{context.user_data['guvohnoma_seriya'].upper()}",
        "seriya_number":f"{context.user_data['guvohnoma_raqami']}"

    }

    police(data)

    return 'pdf'


def pdf(update: Update, context: CallbackContext):
    update.message.reply_text("Sizning guvohnomangiz yaratildi")
