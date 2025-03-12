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
SHELLY = r"заменить на путь к папке с картинками\shelly.png"
NITA = r"заменить на путь к папке с картинками\nita.png"
COLT = r"заменить на путь к папке с картинками\colt.png"
BULL = r"заменить на путь к папке с картинками\bull.png"
BROCK = r"заменить на путь к папке с картинками\brock.png"
ELPRIMO = r"заменить на путь к папке с картинками\elprimo.png"
BARLEY = r"заменить на путь к папке с картинками\barley.png"
POCO = r"заменить на путь к папке с картинками\poco.png"
ROSA = r"заменить на путь к папке с картинками\rosa.png"
JESSIE = r"заменить на путь к папке с картинками\jessie.png"
DYNAMIKE = r"заменить на путь к папке с картинками\dinamike.png"
TICK = r"заменить на путь к папке с картинками\tick.png"
VOSEMBIT = r"заменить на путь к папке с картинками\vosembit.png"
RICO = r"заменить на путь к папке с картинками\rico.png"
DARRIL = r"заменить на путь к папке с картинками\darril.png"
PENNY = r"заменить на путь к папке с картинками\penny.png"
CARL = r"заменить на путь к папке с картинками\carl.png"
JACKY = r"заменить на путь к папке с картинками\jacky.png"
GUS = r"заменить на путь к папке с картинками\gus.png"
BO = r"заменить на путь к папке с картинками\bo.png"
EMZ = r"заменить на путь к папке с картинками\emz.png"
STU = r"заменить на путь к папке с картинками\stu.png"
PIPER = r"заменить на путь к папке с картинками\piper.png"
PAM = r"заменить на путь к папке с картинками\pam.png"
FRANK = r"заменить на путь к папке с картинками\frank.png"
BIBI = r"заменить на путь к папке с картинками\bibi.png"
BEA = r"заменить на путь к папке с картинками\bea.png"
NANI = r"заменить на путь к папке с картинками\nani.png"
EDGAR = r"заменить на путь к папке с картинками\edgar.png"
GRIFF = r"заменить на путь к папке с картинками\griff.png"
GROM = r"заменить на путь к папке с картинками\grom.png"
BONNIE = r"заменить на путь к папке с картинками\bonnie.png"
GALE = r"заменить на путь к папке с картинками\gale.png"
COLETTE = r"заменить на путь к папке с картинками\collete.png"
BELLE = r"заменить на путь к папке с картинками\belle.png"
ASH = r"заменить на путь к папке с картинками\ash.png"
LOLA = r"заменить на путь к папке с картинками\lola.png"
SAM = r"заменить на путь к папке с картинками\sam.png"
MANDY = r"заменить на путь к папке с картинками\mandy.png"
MAISE = r"заменить на путь к папке с картинками\maise.png"
HANK = r"заменить на путь к папке с картинками\hank.png"
PEARL = r"заменить на путь к папке с картинками\pearl.png"
LARRYLAWRIE = r"заменить на путь к папке с картинками\larrylawrie.png"
ANGELO = r"заменить на путь к папке с картинками\angelo.png"
BERRY = r"заменить на путь к папке с картинками\berry.png"
SHADE = r"заменить на путь к папке с картинками\shade.png"
MEEPLE = r"заменить на путь к папке с картинками\meeple.png"
MORTIS = r"заменить на путь к папке с картинками\mortis.png"
TARA = r"заменить на путь к папке с картинками\tara.png"
GENE = r"заменить на путь к папке с картинками\gene.png"
MAX = r"заменить на путь к папке с картинками\max.png"
MRP = r"заменить на путь к папке с картинками\mrp.png"
SPROUT = r"заменить на путь к папке с картинками\sprout.png"
BYRON = r"заменить на путь к папке с картинками\byron.png"
SQUEAK = r"заменить на путь к папке с картинками\squeak.png"
LOU = r"заменить на путь к папке с картинками\lou.png"
RUFFS = r"заменить на путь к папке с картинками\ruffs.png"
BUZZ = r"заменить на путь к папке с картинками\buzz.png"
FANG = r"заменить на путь к папке с картинками\fang.png"
EVE = r"заменить на путь к папке с картинками\eve.png"
JANET = r"заменить на путь к папке с картинками\janet.png"
OTIS = r"заменить на путь к папке с картинками\otis.png"
BUSTER = r"заменить на путь к папке с картинками\buster.png"
GRAY = r"заменить на путь к папке с картинками\gray.png"
RT = r"заменить на путь к папке с картинками\rt.png"
WILLOW = r"заменить на путь к папке с картинками\willow.png"
DOUG = r"заменить на путь к папке с картинками\doug.png"
CHUCK = r"заменить на путь к папке с картинками\chuck.png"
CHARLIE = r"заменить на путь к папке с картинками\charlie.png"
MIKO = r"заменить на путь к папке с картинками\miko.png"
MELODIE = r"заменить на путь к папке с картинками\elodie.png"
LILY = r"заменить на путь к папке с картинками\lily.png"
CLANCY = r"заменить на путь к папке с картинками\clancy.png"
MOE = r"заменить на путь к папке с картинками\moe.png"
JUJU = r"заменить на путь к папке с картинками\juju.png"
OLLIE = r"заменить на путь к папке с картинками\ollie.png"
FINX = r"заменить на путь к папке с картинками\finx.png"
SPIKE = r"заменить на путь к папке с картинками\spike.png"
CROW = r"заменить на путь к папке с картинками\crow.png"
LEON = r"заменить на путь к папке с картинками\leon.png"
SANDY = r"заменить на путь к папке с картинками\sandy.png"
AMBER = r"заменить на путь к папке с картинками\amber.png"
MEG = r"заменить на путь к папке с картинками\meg.png"
SURGE = r"заменить на путь к папке с картинками\surge.png"
CHESTER = r"заменить на путь к папке с картинками\chester.png"
CORDELIUS = r"заменить на путь к папке с картинками\cordelius.png"
KIT = r"заменить на путь к папке с картинками\kit.png"
DRACO = r"заменить на путь к папке с картинками\draco.png"
KENJT = r"заменить на путь к папке с картинками\kenji.png"

# Проверка существования файла
if not os.path.exists(SHELLY):
    logging.error(f"Файл {SHELLY} не найден!")
else:
    logging.info(f"Файл {SHELLY} найден.")

# Создаем клавиатуру с кнопкой "Назад"
back_button = KeyboardButton(text="назад")
back_keyboard = ReplyKeyboardMarkup(
    keyboard=[[back_button]],
    resize_keyboard=True
)

# Создаем клавиатуру для выбора редкости бойца
rarity_buttons = [
    KeyboardButton(text="Начальный"),
    KeyboardButton(text="Редкий"),
    KeyboardButton(text="Сверхредкий"),
    KeyboardButton(text="Эпический"),
    KeyboardButton(text="Мифический"),
    KeyboardButton(text="Легендарный")
]
rarity_keyboard = ReplyKeyboardMarkup(
    keyboard=[rarity_buttons[i:i + 2] for i in range(0, len(rarity_buttons), 2)],
    resize_keyboard=True
)

# Создаем клавиатуру с кнопкой "Шелли" для обычной редкости
nachalny_button= KeyboardButton(text="Шелли")
nachalny_keyboard = ReplyKeyboardMarkup(
    keyboard=[[nachalny_button, back_button]],  # Кнопка "Шелли" и "Назад"
    resize_keyboard=True
)
# бойцы
rare_buttons = [
    KeyboardButton(text="нита"),
    KeyboardButton(text="кольт"),
    KeyboardButton(text="булл"),
    KeyboardButton(text="брок"),
    KeyboardButton(text="эль примо"),
    KeyboardButton(text="барли"),
    KeyboardButton(text="поко"),
    KeyboardButton(text="роза"),
    KeyboardButton(text="назад")
]
rare_keyboard = ReplyKeyboardMarkup(
    keyboard=[rare_buttons[i:i + 3] for i in range(0, len(rare_buttons), 3)],
    resize_keyboard=True
)

sverhrare_buttons = [
    KeyboardButton(text="джесси"),
    KeyboardButton(text="динамайк"),
    KeyboardButton(text="тик"),
    KeyboardButton(text="8-бит"),
    KeyboardButton(text="рико"),
    KeyboardButton(text="дэррил"),
    KeyboardButton(text="пенни"),
    KeyboardButton(text="карл"),
    KeyboardButton(text="джеки"),
    KeyboardButton(text="гас"),
    KeyboardButton(text="назад")
]
sverhrare_keyboard = ReplyKeyboardMarkup(
    keyboard=[sverhrare_buttons[i:i + 3] for i in range(0, len(sverhrare_buttons), 2)],
    resize_keyboard=True
)

epic_buttons = [
    KeyboardButton(text="бо"),
    KeyboardButton(text="эмз"),
    KeyboardButton(text="сту"),
    KeyboardButton(text="пайпер"),
    KeyboardButton(text="пэм"),
    KeyboardButton(text="фрэнк"),
    KeyboardButton(text="биби"),
    KeyboardButton(text="беа"),
    KeyboardButton(text="нани"),
    KeyboardButton(text="эдгар"),
    KeyboardButton(text="грифф"),
    KeyboardButton(text="гром"),
    KeyboardButton(text="бонни"),
    KeyboardButton(text="гэйл"),
    KeyboardButton(text="колетт"),
    KeyboardButton(text="белль"),
    KeyboardButton(text="эш"),
    KeyboardButton(text="лола"),
    KeyboardButton(text="сэм"),
    KeyboardButton(text="мэнди"),
    KeyboardButton(text="мэйси"),
    KeyboardButton(text="хэнк"),
    KeyboardButton(text="перл"),
    KeyboardButton(text="ларри и лори"),
    KeyboardButton(text="анджело"),
    KeyboardButton(text="берри"),
    KeyboardButton(text="шейд"),
    KeyboardButton(text="мипл"),
    KeyboardButton(text="назад")
]
epic_keyboard = ReplyKeyboardMarkup(
    keyboard=[epic_buttons[i:i + 4] for i in range(0, len(epic_buttons), 4)],
    resize_keyboard=True
)

mithic_buttons = [
    KeyboardButton(text="мортис"),
    KeyboardButton(text="тара"),
    KeyboardButton(text="джин"),
    KeyboardButton(text="макс"),
    KeyboardButton(text="пистер п."),
    KeyboardButton(text="спраут"),
    KeyboardButton(text="байрон"),
    KeyboardButton(text="скуик"),
    KeyboardButton(text="лу"),
    KeyboardButton(text="гавс"),
    KeyboardButton(text="базз"),
    KeyboardButton(text="фэнг"),
    KeyboardButton(text="ева"),
    KeyboardButton(text="джанет"),
    KeyboardButton(text="отис"),
    KeyboardButton(text="бастер"),
    KeyboardButton(text="грей"),
    KeyboardButton(text="r-t"),
    KeyboardButton(text="виллоу"),
    KeyboardButton(text="даг"),
    KeyboardButton(text="чак"),
    KeyboardButton(text="чарли"),
    KeyboardButton(text="мико"),
    KeyboardButton(text="мелоди"),
    KeyboardButton(text="лили"),
    KeyboardButton(text="клэнси"),
    KeyboardButton(text="мо"),
    KeyboardButton(text="джуджу"),
    KeyboardButton(text="олли"),
    KeyboardButton(text="финкс"),
    KeyboardButton(text="назад")
]
mithic_keyboard = ReplyKeyboardMarkup(
    keyboard=[mithic_buttons[i:i + 4] for i in range(0, len(mithic_buttons), 4)],
    resize_keyboard=True
)

legendary_buttons = [
    KeyboardButton(text="спайк"),
    KeyboardButton(text="ворон"),
    KeyboardButton(text="леон"),
    KeyboardButton(text="сэнди"),
    KeyboardButton(text="амбер"),
    KeyboardButton(text="мэг"),
    KeyboardButton(text="вольт"),
    KeyboardButton(text="честер"),
    KeyboardButton(text="корделиус"),
    KeyboardButton(text="кит"),
    KeyboardButton(text="драко"),
    KeyboardButton(text="кэндзи"),
    KeyboardButton(text="назад")
]
legendary_keyboard = ReplyKeyboardMarkup(
    keyboard=[legendary_buttons[i:i + 3] for i in range(0, len(legendary_buttons), 3)],
    resize_keyboard=True
)

# Обработчик команды /start
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer("Привет! Выбери редкость бойца про которого хотел бы узнать:", reply_markup=rarity_keyboard)

# Обработчик выбора редкости бойца
@dp.message(F.text.in_(["Начальный", "Редкий", "Сверхредкий", "Эпический", "Мифический", "Легендарный"]))
async def handle_rarity(message: types.Message):
    rarity = message.text
    if rarity == "Начальный":
        await message.answer("Вы выбрали редкость: Начальный. Выберите бойца:", reply_markup=nachalny_keyboard)
    elif rarity == "Редкий":
        await message.answer("Вы выбрали редкость: Редкий. Выберите бойца:", reply_markup=rare_keyboard)
    elif rarity == "Сверхредкий":
        await message.answer("Вы выбрали редкость: Сверхредкий. Выберите бойца:", reply_markup=sverhrare_keyboard)
    elif rarity == "Эпический":
        await message.answer("Вы выбрали редкость: Эпический. Выберите бойца:", reply_markup=epic_keyboard)
    elif rarity == "Мифический":
        await message.answer("Вы выбрали редкость: Мифический. Выберите бойца:", reply_markup=mithic_keyboard)
    elif rarity == "Легендарный":
        await message.answer("Вы выбрали редкость: Легендарный. Выберите бойца:", reply_markup=legendary_keyboard)
    else:
        await message.answer(f"Вы выбрали редкость: {rarity}. Введите имя бойца:", reply_markup=back_keyboard)

# Обработчик текста после нажатия "Бойцы"
@dp.message(F.text)
async def handle_text_after_fighters(message: types.Message):
    # Убираем лишние пробелы и приводим текст к нижнему регистру
    user_input = message.text.strip().lower()

    if user_input == "шелли":
        try:
            await message.answer_photo(
                photo=FSInputFile(SHELLY),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "нита":
        try:
            await message.answer_photo(
                photo=FSInputFile(NITA),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "кольт":
        try:
            await message.answer_photo(
                photo=FSInputFile(COLT),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "булл":
        try:
            await message.answer_photo(
                photo=FSInputFile(BULL),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "брок":
        try:
            await message.answer_photo(
                photo=FSInputFile(BROCK),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "эль примо":
        try:
            await message.answer_photo(
                photo=FSInputFile(ELPRIMO),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "барли":
        try:
            await message.answer_photo(
                photo=FSInputFile(BARLEY),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "поко":
        try:
            await message.answer_photo(
                photo=FSInputFile(POCO),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "роза":
        try:
            await message.answer_photo(
                photo=FSInputFile(ROSA),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "джесси":
        try:
            await message.answer_photo(
                photo=FSInputFile(JESSIE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "динамайк":
        try:
            await message.answer_photo(
                photo=FSInputFile(DYNAMIKE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "тик":
        try:
            await message.answer_photo(
                photo=FSInputFile(TICK),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "8-бит":
        try:
            await message.answer_photo(
                photo=FSInputFile(VOSEMBIT),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "рико":
        try:
            await message.answer_photo(
                photo=FSInputFile(RICO),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "дэррил":
        try:
            await message.answer_photo(
                photo=FSInputFile(DARRIL),  
                caption="",
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "пенни":
        try:
            await message.answer_photo(
                photo=FSInputFile(PENNY),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "карл":
        try:
            await message.answer_photo(
                photo=FSInputFile(CARL),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "джекки":
        try:
            await message.answer_photo(
                photo=FSInputFile(JACKY),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "гас":
        try:
            await message.answer_photo(
                photo=FSInputFile(GUS),  
                caption=""
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "бо":
        try:
            await message.answer_photo(
                photo=FSInputFile(BO),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "эмз":
        try:
            await message.answer_photo(
                photo=FSInputFile(EMZ),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "сту":
        try:
            await message.answer_photo(
                photo=FSInputFile(STU),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "пайпер":
        try:
            await message.answer_photo(
                photo=FSInputFile(PIPER),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "пэм":
        try:
            await message.answer_photo(
                photo=FSInputFile(PAM),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "френк":
        try:
            await message.answer_photo(
                photo=FSInputFile(FRANK),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "биби":
        try:
            await message.answer_photo(
                photo=FSInputFile(BIBI),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "беа":
        try:
            await message.answer_photo(
                photo=FSInputFile(BEA),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "нани":
        try:
            await message.answer_photo(
                photo=FSInputFile(NANI),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "эдгар":
        try:
            await message.answer_photo(
                photo=FSInputFile(EDGAR),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "грифф":
        try:
            await message.answer_photo(
                photo=FSInputFile(GRIFF),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "гром":
        try:
            await message.answer_photo(
                photo=FSInputFile(GROM),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "бонни":
        try:
            await message.answer_photo(
                photo=FSInputFile(BONNIE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "гэйл":
        try:
            await message.answer_photo(
                photo=FSInputFile(GALE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "колетт":
        try:
            await message.answer_photo(
                photo=FSInputFile(COLETTE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "белль":
        try:
            await message.answer_photo(
                photo=FSInputFile(BELLE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "эш":
        try:
            await message.answer_photo(
                photo=FSInputFile(ASH),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "лола":
        try:
            await message.answer_photo(
                photo=FSInputFile(LOLA),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "сэм":
        try:
            await message.answer_photo(
                photo=FSInputFile(SAM),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "мэнди":
        try:
            await message.answer_photo(
                photo=FSInputFile(MANDY),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "мэйси":
        try:
            await message.answer_photo(
                photo=FSInputFile(MAISE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "хэнк":
        try:
            await message.answer_photo(
                photo=FSInputFile(HANK),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "перл":
        try:
            await message.answer_photo(
                photo=FSInputFile(PEARL),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "ларри и лори":
        try:
            await message.answer_photo(
                photo=FSInputFile(LARRYLAWRIE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "анджела":
        try:
            await message.answer_photo(
                photo=FSInputFile(ANGELO),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "берри":
        try:
            await message.answer_photo(
                photo=FSInputFile(BERRY),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "шейд":
        try:
            await message.answer_photo(
                photo=FSInputFile(SHADE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "мипл":
        try:
            await message.answer_photo(
                photo=FSInputFile(MEEPLE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "мортис":
        try:
            await message.answer_photo(
                photo=FSInputFile(MORTIS),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "тара":
        try:
            await message.answer_photo(
                photo=FSInputFile(TARA),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "джин":
        try:
            await message.answer_photo(
                photo=FSInputFile(GENE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "макс":
        try:
            await message.answer_photo(
                photo=FSInputFile(MAX),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "мистер п.":
        try:
            await message.answer_photo(
                photo=FSInputFile(MRP),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "спраут":
        try:
            await message.answer_photo(
                photo=FSInputFile(SPROUT),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "байрон":
        try:
            await message.answer_photo(
                photo=FSInputFile(BYRON),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "скуик":
        try:
            await message.answer_photo(
                photo=FSInputFile(SQUEAK),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "лу":
        try:
            await message.answer_photo(
                photo=FSInputFile(LOU),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "гавс":
        try:
            await message.answer_photo(
                photo=FSInputFile(RUFFS),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "базз":
        try:
            await message.answer_photo(
                photo=FSInputFile(BUZZ),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "фэнг":
        try:
            await message.answer_photo(
                photo=FSInputFile(FANG),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "ева":
        try:
            await message.answer_photo(
                photo=FSInputFile(EVE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "джанет":
        try:
            await message.answer_photo(
                photo=FSInputFile(JANET),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "отис":
        try:
            await message.answer_photo(
                photo=FSInputFile(OTIS),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "бастер":
        try:
            await message.answer_photo(
                photo=FSInputFile(BUSTER),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "грей":
        try:
            await message.answer_photo(
                photo=FSInputFile(GRAY),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "r-t":
        try:
            await message.answer_photo(
                photo=FSInputFile(RT),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "виллоу":
        try:
            await message.answer_photo(
                photo=FSInputFile(WILLOW),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "даг":
        try:
            await message.answer_photo(
                photo=FSInputFile(DOUG),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "чак":
        try:
            await message.answer_photo(
                photo=FSInputFile(CHUCK),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "чарли":
        try:
            await message.answer_photo(
                photo=FSInputFile(CHARLIE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "мико":
        try:
            await message.answer_photo(
                photo=FSInputFile(MIKO),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "мелоди":
        try:
            await message.answer_photo(
                photo=FSInputFile(MELODIE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "лили":
        try:
            await message.answer_photo(
                photo=FSInputFile(LILY),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "клэнси":
        try:
            await message.answer_photo(
                photo=FSInputFile(CLANCY),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "мо":
        try:
            await message.answer_photo(
                photo=FSInputFile(MOE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "джуджу":
        try:
            await message.answer_photo(
                photo=FSInputFile(JUJU),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "олли":
        try:
            await message.answer_photo(
                photo=FSInputFile(OLLIE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "финкс":
        try:
            await message.answer_photo(
                photo=FSInputFile(FINX),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "спайк":
        try:
            await message.answer_photo(
                photo=FSInputFile(SPIKE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "ворон":
        try:
            await message.answer_photo(
                photo=FSInputFile(CROW),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "леон":
        try:
            await message.answer_photo(
                photo=FSInputFile(LEON),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "сэнди":
        try:
            await message.answer_photo(
                photo=FSInputFile(SANDY),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "амбер":
        try:
            await message.answer_photo(
                photo=FSInputFile(AMBER),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "мэг":
        try:
            await message.answer_photo(
                photo=FSInputFile(MEG),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "вольт":
        try:
            await message.answer_photo(
                photo=FSInputFile(SURGE),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "честер":
        try:
            await message.answer_photo(
                photo=FSInputFile(CHESTER),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "корделиус":
        try:
            await message.answer_photo(
                photo=FSInputFile(CORDELIUS),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "кит":
        try:
            await message.answer_photo(
                photo=FSInputFile(KIT),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "драко":
        try:
            await message.answer_photo(
                photo=FSInputFile(DRACO),  
                caption="",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "кэндзи":
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
        await message.answer("Привет! Выбери редкость бойца про которого хотел бы узнать:", reply_markup=rarity_keyboard)
    else:
        await message.answer(f"Я не знаю бойца по имени {message.text}. Попробуйте ещё раз!", reply_markup=back_keyboard)

# Обработчик кнопки "Назад"
@dp.message(F.text == "назад")
async def handle_back_button(message: types.Message):
    await message.answer("Привет! Выбери редкость бойца про которого хотел бы узнать:", reply_markup=rarity_keyboard)

# Запуск бота
if __name__ == '__main__':
    dp.run_polling(bot)
