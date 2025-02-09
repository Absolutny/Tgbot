import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, FSInputFile
from aiogram.filters import Command
from aiogram import F

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
API_TOKEN = 'ваш токен'  # Замените на ваш токен
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Путь к локальному изображению бойцов
SHELLY = r"D:\tgbotik\imag\shelly.png"
NITA = r"D:\tgbotik\imag\nita.png"
COLT = r"D:\tgbotik\imag\colt.png"
BULL = r"D:\tgbotik\imag\bull.png"
BROCK = r"D:\tgbotik\imag\brock.png"
ELPRIMO = r"D:\tgbotik\imag\elprimo.png"
BARLEY = r"D:\tgbotik\imag\barley.png"
POCO = r"D:\tgbotik\imag\poco.png"
ROSA = r"D:\tgbotik\imag\rosa.png"
JESSIE = r"D:\tgbotik\imag\jessie.png"
DYNAMIKE = r"D:\tgbotik\imag\dinamike.png"
TICK = r"D:\tgbotik\imag\tick.png"
VOSEMBIT = r"D:\tgbotik\imag\vosembit.png"
RICO = r"D:\tgbotik\imag\rico.png"
DARRIL = r"D:\tgbotik\imag\darril.png"
PENNY = r"D:\tgbotik\imag\penny.png"
CARL = r"D:\tgbotik\imag\carl.png"
JACKY = r"D:\tgbotik\imag\jacky.png"
GUS = r"D:\tgbotik\imag\gus.png"
BO = r"D:\tgbotik\imag\bo.png"
EMZ = r"D:\tgbotik\imag\emz.png"
STU = r"D:\tgbotik\imag\stu.png"
PIPER = r"D:\tgbotik\imag\piper.png"
PAM = r"D:\tgbotik\imag\pam.png"
FRANK = r"D:\tgbotik\imag\frank.png"
BIBI = r"D:\tgbotik\imag\bibi.png"
BEA = r"D:\tgbotik\imag\bea.png"
NANI = r"D:\tgbotik\imag\nani.png"
EDGAR = r"D:\tgbotik\imag\edgar.png"
GRIFF = r"D:\tgbotik\imag\griff.png"
GROM = r"D:\tgbotik\imag\grom.png"
BONNIE = r"D:\tgbotik\imag\bonnie.png"
GALE = r"D:\tgbotik\imag\gale.png"
COLETTE = r"D:\tgbotik\imag\collete.png"
BELLE = r"D:\tgbotik\imag\belle.png"
ASH = r"D:\tgbotik\imag\ash.png"
LOLA = r"D:\tgbotik\imag\lola.png"
SAM = r"D:\tgbotik\imag\sam.png"
MANDY = r"D:\tgbotik\imag\mandy.png"
MAISE = r"D:\tgbotik\imag\maise.png"
HANK = r"D:\tgbotik\imag\hank.png"
PEARL = r"D:\tgbotik\imag\pearl.png"
LARRYLAWRIE = r"D:\tgbotik\imag\larrylawrie.png"
ANGELO = r"D:\tgbotik\imag\angelo.png"
BERRY = r"D:\tgbotik\imag\berry.png"
SHADE = r"D:\tgbotik\imag\shade.png"
MEEPLE = r"D:\tgbotik\imag\meeple.png"
MORTIS = r"D:\tgbotik\imag\mortis.png"
TARA = r"D:\tgbotik\imag\tara.png"
GENE = r"D:\tgbotik\imag\gene.png"
MAX = r"D:\tgbotik\imag\max.png"
MRP = r"D:\tgbotik\imag\mrp.png"
SPROUT = r"D:\tgbotik\imag\sprout.png"
BYRON = r"D:\tgbotik\imag\byron.png"
SQUEAK = r"D:\tgbotik\imag\squeak.png"
LOU = r"D:\tgbotik\imag\lou.png"
RUFFS = r"D:\tgbotik\imag\ruffs.png"
BUZZ = r"D:\tgbotik\imag\buzz.png"
FANG = r"D:\tgbotik\imag\fang.png"
EVE = r"D:\tgbotik\imag\eve.png"
JANET = r"D:\tgbotik\imag\janet.png"
OTIS = r"D:\tgbotik\imag\otis.png"
BUSTER = r"D:\tgbotik\imag\buster.png"
GRAY = r"D:\tgbotik\imag\gray.png"
RT = r"D:\tgbotik\imag\rt.png"
WILLOW = r"D:\tgbotik\imag\willow.png"
DOUG = r"D:\tgbotik\imag\doug.png"
CHUCK = r"D:\tgbotik\imag\chuck.png"
CHARLIE = r"D:\tgbotik\imag\charlie.png"
MIKO = r"D:\tgbotik\imag\miko.png"
MELODIE = r"D:\tgbotik\imag\elodie.png"
LILY = r"D:\tgbotik\imag\lily.png"
CLANCY = r"D:\tgbotik\imag\clancy.png"
MOE = r"D:\tgbotik\imag\moe.png"
JUJU = r"D:\tgbotik\imag\juju.png"
OLLIE = r"D:\tgbotik\imag\ollie.png"
SPIKE = r"D:\tgbotik\imag\spike.png"
CROW = r"D:\tgbotik\imag\crow.png"
LEON = r"D:\tgbotik\imag\leon.png"
SANDY = r"D:\tgbotik\imag\sandy.png"
AMBER = r"D:\tgbotik\imag\amber.png"
MEG = r"D:\tgbotik\imag\meg.png"
SURGE = r"D:\tgbotik\imag\surge.png"
CHESTER = r"D:\tgbotik\imag\chester.png"
CORDELIUS = r"D:\tgbotik\imag\cordelius.png"
KIT = r"D:\tgbotik\imag\kit.png"
DRACO = r"D:\tgbotik\imag\draco.png"
KENJT = r"D:\tgbotik\imag\kenji.png"

# Путь к локальному изображению карт


# Проверка существования файла
if not os.path.exists(SHELLY):
    logging.error(f"Файл {SHELLY} не найден!")
else:
    logging.info(f"Файл {SHELLY} найден.")

# Создаем основную клавиатуру с кнопками "Бойцы" и "Карты"
button_fighters = KeyboardButton(text="Бойцы")
button_maps = KeyboardButton(text="Карты")
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[[button_fighters, button_maps]],
    resize_keyboard=True
)

# Создаем клавиатуру с кнопкой "Назад"
back_button = KeyboardButton(text="Назад")
back_keyboard = ReplyKeyboardMarkup(
    keyboard=[[back_button]],
    resize_keyboard=True
)

# Обработчик команды /start
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer("Привет! Выберите одну из кнопок:", reply_markup=main_keyboard)

# Обработчик нажатия на кнопки "Бойцы" и "Карты"
@dp.message(F.text.in_(["Бойцы", "Карты"]))
async def handle_buttons(message: types.Message):
    if message.text == "Бойцы":
        await message.answer("Вы выбрали Бойцы! Введите имя бойца (например, Шелли):", reply_markup=back_keyboard)
    elif message.text == "Карты":
        await message.answer("Вы выбрали Карты!", reply_markup=back_keyboard)

# Обработчик текста после нажатия "Бойцы"
@dp.message(F.text)
async def handle_text_after_fighters(message: types.Message):
    # Убираем лишние пробелы и приводим текст к нижнему регистру
    user_input = message.text.strip().lower()

    if user_input == "шелли":
        try:
            await message.answer_photo(
                photo=FSInputFile(SHELLY),  
                caption="Шелли — это отличный боец с мощным дробовиком!",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "нита":
        try:
            await message.answer_photo(
                photo=FSInputFile(NITA),  
                caption="нита",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(COLT),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(BULL),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(BROCK),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(ELPRIMO),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(BARLEY),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(POCO),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(ROSA),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(JESSIE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(DYNAMIKE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(TICK),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(VOSEMBIT),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(RICO),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(DARRIL),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(PENNY),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(CARL),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(JACKY),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(GUS),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(BO),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(EMZ),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(STU),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(PIPER),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(PAM),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(FRANK),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(BIBI),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(BEA),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(NANI),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(EDGAR),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(GRIFF),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(GROM),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(BONNIE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(GALE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(COLETTE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(BELLE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(ASH),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(LOLA),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(SAM),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(MANDY),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(MAISE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(HANK),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(PEARL),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(LARRYLAWRIE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(ANGELO),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(BERRY),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(SHADE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(MEEPLE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(MORTIS),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(TARA),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(GENE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(MAX),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(MRP),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(SPROUT),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(BYRON),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(SQUEAK),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(LOU),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(RUFFS),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(BUZZ),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(FANG),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(EVE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(JANET),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(OTIS),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(BUSTER),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(GRAY),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(RT),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(WILLOW),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(DOUG),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(CHUCK),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(CHARLIE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(MIKO),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(MELODIE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(LILY),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(CLANCY),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(MOE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(JUJU),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(OLLIE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(SPIKE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(CROW),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(LEON),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(SANDY),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(AMBER),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(MEG),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(SURGE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(CHESTER),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(CORDELIUS),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(KIT),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(DRACO),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "":
        try:
            await message.answer_photo(
                photo=FSInputFile(KENJT),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "назад":
        await message.answer("Возвращаемся назад:", reply_markup=main_keyboard)
    else:
        await message.answer(f"Я не знаю бойца по имени {message.text}. Попробуйте ещё раз!", reply_markup=back_keyboard)

# Обработчик кнопки "Назад"
@dp.message(F.text == "Назад")
async def handle_back_button(message: types.Message):
    await message.answer("Возвращаемся назад:", reply_markup=main_keyboard)

# Запуск бота
if __name__ == '__main__':
    dp.run_polling(bot)
