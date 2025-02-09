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

rare_buttons = [
    KeyboardButton(text="нита"),
    KeyboardButton(text="кольт"),
    KeyboardButton(text="булл"),
    KeyboardButton(text="брок"),
    KeyboardButton(text="эль примо"),
    KeyboardButton(text="барли"),
    KeyboardButton(text="поко"),
    KeyboardButton(text="роза"),
]
rare_keyboard = ReplyKeyboardMarkup(
    keyboard=[rare_buttons[i:i + 2] for i in range(0, len(rare_buttons), 2)],
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
    KeyboardButton(text="гас")
]
sverhrare_keyboard = ReplyKeyboardMarkup(
    keyboard=[sverhrare_buttons[i:i + 2] for i in range(0, len(sverhrare_buttons), 2)],
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
    KeyboardButton(text="мипл")
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
    KeyboardButton(text="олли")
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
    KeyboardButton(text="кэндзи")
]
legendary_keyboard = ReplyKeyboardMarkup(
    keyboard=[legendary_buttons[i:i + 2] for i in range(0, len(legendary_buttons), 2)],
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
        await message.answer("Выберите редкость бойца:", reply_markup=rarity_keyboard)
    elif message.text == "Карты":
        await message.answer("Вы выбрали Карты!", reply_markup=back_keyboard)

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
                caption="Шелли имеет средний запас здоровья, высокую скорость передвижения, среднюю скорость перезарядки, среднюю дальность атаки и наносит большой урон на близком расстоянии. Её основная атака - выстрел дробью, имеющей некоторый разброс, что делает её менее эффективной на большой дистанции. Её Супер аналогичен обычной атаке, но содержит больше снарядов, наносит больше урона, разрушает препятствия и может отталкивать задетых противников. Шелли очень проста в освоении, что поможет начинающим игрокам. Благодаря первой Звёздной силе её Супер замедляет врагов на 2 секунды, а с помощью второй Звёздной силы она исцеляет здоровье каждые 15 секунд, если его уровень опускается ниже 40%. Её гаджеты позволяют ей делать рывки или увеличивать дальность и уменьшать разброс основной атаки.",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "нита":
        try:
            await message.answer_photo(
                photo=FSInputFile(NITA),  
                caption="Нита имеет средний запас здоровья, высокую скорость перезарядки, среднюю дальность атаки, нормальную скорость передвижения и наносит средний урон. Её основная атака - волна, пробивающая противников, что позволяет наносить урон сразу нескольким целям. Её Супер призывает большого медведя, который атакует противников. Благодаря первой Звёздной силе медведь восстанавливает здоровье Ните, нанося урон, тем временем как Нита — медведю, а с помощью второй Звёздной силы его скорость атаки увеличивается на 60%. При использовании первого гаджета медведь оглушает врагов поблизости с 1 секундой задержкой, а второй гаджет создает временный щит для него.",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "кольт":
        try:
            await message.answer_photo(
                photo=FSInputFile(COLT),  
                caption="Кольт имеет низкий запас здоровья, нормальную скорость передвижения и перезарядки, большую дальность атаки и наносит большой урон. Его основная атака - это очередь из 6-ти пуль, летящих по прямой. Его Супер аналогичен обычной атаке, но содержит 12 пуль, прошивает врагов насквозь и разрушает препятствия. При игре за Кольта необходимо умение прицеливаться, что делает его несколько сложным в освоении. Первая Звёздная сила увеличивает его скорость передвижения, а вторая - дальность атаки и скорость снарядов. Его гаджеты могут восстанавливать патроны или изменять основную атаку с очереди на одну мощную пулю.",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "булл":
        try:
            await message.answer_photo(
                photo=FSInputFile(BULL),  
                caption="У Булла такой же тип атаки, как и у Шелли и Дэррила, но с более короткой дальностью. Он обладает высокой скоростью передвижения, большим количеством здоровья и высоким уроном на ближней дистанции. Его Супер позволит догнать слабого врага или, наоборот, уйти от опасного противника. Гаджет «Сочный стейк» сразу восстанавливает Буллу немного здоровья. Гаджет «Страх и топот» прерывает Cупер Булла, и при активации враги рядом с местом использования замедляются. Звёздная сила «Берсерк» ускоряет перезарядку Булла, если у него осталось менее 60% здоровья. Звёздная сила «Крепкий парень» даёт ему щит, когда его здоровье падает до 40%.",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "брок":
        try:
            await message.answer_photo(
                photo=FSInputFile(BROCK),  
                caption="Брок имеет очень низкое здоровье, нормальную скорость и низкую перезарядку. Его дальнобойные ракеты наносят довольно высокий урон в небольшой области, но перезаряжаются достаточно медленно. Его Супер — град из 9-ти ракет, которые наносят гигантский урон по области. Его первый Гаджет «Реактивные кроссовки» позволяет сделать прыжок ввысь, что сделает Брока неуязвимым к урону на долю секунды и поможет перепрыгнуть через препятствия. Другой гаджет преобразует его следующую атаку в большую взрывную ракету. Его Звёздная сила «Больше ракет» позволяет ему выпускать больше ракет при использовании Супера, а «Ракета №4» увеличивает количество боеприпасов с трёх до четырёх.",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "эль примо":
        try:
            await message.answer_photo(
                photo=FSInputFile(ELPRIMO),  
                caption="Имеет высокую скорость передвижения, очень высокую скорость перезарядки и высокий показатель здоровья, который позволяет выдерживать ему большинство вражеских атак. Эль Примо сражается кулаками, нанося 4 удара нa короткой дистанции. Его Супер позволяет ему совершить прыжок нa большое расстояние, разрушив препятствия в небольшом радиусе и обрушившись нa противников, нанеся им низкий урон, но отталкивая. Используя гаджеты, Эль Примо может подхватить ближайшего врага своими могучими руками и швырнуть его через плечо со всей силы или запустить в ближайшего противника метеорит. Его Звёздная сила «Эль Фуэго» поджигает землю и врагов, попавших в зону действия Супера Эль Примо, a Звёздная сила «Скорость метеорита» увеличит скорость передвижения после Супера.",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "барли":
        try:
            await message.answer_photo(
                photo=FSInputFile(BARLEY),  
                caption="Барли имеет нормальную скорость передвижения, очень низкий уровень здоровья, но обладает атакой, с помощью которой он бросает бутылки с зажигательной смесью, покрывающие землю лужами, наносящими средний урон врагам, стоящим на них, со временем. При помощи Супера Барли покрывает огромную площадь огнём. Его первый гаджет — липкая лужа сиропа, наступив в которую, враги замедляются. Второй гаджет может излечить союзников лечебной жидкостью. Звёздная сила «Лекарство» позволяет восстанавливать здоровье, с помощью основной атаки, не прекращая её саму. Звёздная сила «Опасно для здоровья» увеличивает урон от атаки на 200 очков.",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "поко":
        try:
            await message.answer_photo(
                photo=FSInputFile(POCO),  
                caption="Поко имеет нормальную скорость передвижения и широкий диапазон атаки. Несмотря на это, он имеет и свои слабости: среднее количество единиц здоровья и низкий урон. Его Супер очень полезен и может восстанавливать здоровье себе и своим союзникам, попавшим в зону действия, которая намного больше, чем у основной атаки и проходит сквозь препятствия. Его гаджет «Камертон» восстанавливает 740 очков здоровья ежесекундно ему и союзникам Поко на небольшом радиусе в течение 5 секунд. Гаджет «Катарсис» снимает все негативные эффекты с союзников и даёт иммунитет всем попавшим под радиус гаджета союзникам на 4 секунды. Звёздная сила «Да-Капо!» восстанавливает 962 очков здоровья союзникам, попавших под зону действия основной атаки Поко. А Звёздная сила «Сольный номер» даёт Суперу Поко урон в размере 1520 единиц.",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "роза":
        try:
            await message.answer_photo(
                photo=FSInputFile(ROSA),  
                caption="Роза имеет высокую скорость передвижения, высокое здоровье, средне-высокий урон и высокую скорость перезарядки. Атакой Роза наносит три удара кулаками на небольшую дистанцию. Её Супер — щит, поглощающий 70% нанесенного ей урона. С помощью гаджета «Фитолампа» Роза может посадить кусты вокруг себя. Гаджет «Ядовитые заросли» замедляет противников, находящихся в кустах. Также они получают небольшой урон, что помогает Розе их обнаружить. При помощи Звёздной силы «Отдых на природе» она может восстанавливать здоровье, когда находится в кустах. Звёздная сила «Ежовые рукавицы» увеличивает урон от атаки Розы, пока работает её Супер.",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "джесси":
        try:
            await message.answer_photo(
                photo=FSInputFile(JESSIE),  
                caption="Она обладает нормальной скоростью передвижения, средне-низким здоровьем, средним уроном и средней скоростью перезарядки. Своим Супером она ставит турель со средним здоровьем, низким уроном и очень быстрой атакой. Атаки Джесси средней дальности имеют большой потенциал урона, потому что они могут отскакивать от противника и поражать двух других ближайших врагов, что позволит быстро накопить Супер (если удачно попасть 3 раза по врагам, то можно тут же его зарядить). С первым Гаджетом Турель Джесси порождает ударную волну, замедляющую всех врагов, находящихся в зоне её действия, а со вторым гаджетом она значительно ускоряет свою перезарядку. С помощью первой Звёздной силы Джесси может исцелять здоровье турели с помощью атаки, а со второй Звёздной силой атаки турели Джесси отскакивают от врагов.",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "динамайк":
        try:
            await message.answer_photo(
                photo=FSInputFile(DYNAMIKE),  
                caption="Динамайк имеет высокую скорость передвижения, средне-низкое количество здоровья и высокий урон. Его Супер может моментально убить бойцов с низким запасом здоровья. Первая Звёздные силы Динамайка позволяет ему перепрыгивать препятствия с помощью динамита, а вторая — увеличивает урон от Супера на 1000 очков. При использовании первого гаджета, Динaмайк вращается по оси, разбрасывая вокруг себя динамитные шашки, и при этом ещё и ускоряясь. Со вторым гаджетом Динaмайк оглушает врагов на 1,5 секунды от основной атаки",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "тик":
        try:
            await message.answer_photo(
                photo=FSInputFile(TICK),  
                caption="У него нормальная скорость передвижения, один из двух самых низких запасов здоровья в игре, но очень высокий урон и высокая дальность. Своей основной атакой Тик выстреливает кассетной бомбой, которая распадается на три маленькие мины. Его Супер — бросок головы-камикадзе, которая, найдя ближайшего врага, взрывается, нанося высокий урон. Первый гаджет даёт Тику защиту и отталкивает врагов, нанося урон, а второй— увеличение количества бомб в одной атаке с 3 до 6. Звёздная сила «Как по маслу» позволяет Тику восстанавливать здоровье намного раньше других бойцов, а Звёздная сила «Автома–Тика» навсегда ускоряет перезарядку его основной атаки.",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "8-бит":
        try:
            await message.answer_photo(
                photo=FSInputFile(VOSEMBIT),  
                caption="Обладает средне-высоким количеством здоровья, очень низкой скоростью передвижения (является на данный момент самым медленным бойцом в игре) и высоким уроном. Он использует лазерный пистолет, из которого стреляет лучами по врагам на очень большую дистанцию. Его Супер — усилитель, который увеличивает урон ему и его союзникам в зоне действия. Звёздные силы либо увеличат область и мощность его Супера, либо ускорят скорость передвижения 8-БИТа около усилителя урона. Первый гаджет 8-БИТа — телепорт к своему усилителю, а второй гаджет увеличивает кучность его атаки с 6 до 18 лазерных лучей.",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "рико":
        try:
            await message.answer_photo(
                photo=FSInputFile(RICO),  
                caption="Рико имеет нормальную скорость передвижения, низкий уровень здоровья, и умеренный урон. Его атака — пули, которые могут отскакивать от стен и пролетать на 1.67 клеток больше. Эта способность может позволить Рико наносить урон врагам в укрытиях при правильном прицеливании. Его Супер — увеличенные пули, которые могут прошивать врагов. С Звёздной силой «Суперотскок» пули при отскоке изменяют свою внешность и наносят больше урона. А со Звёздной силой «Отступление машин» Рико при 40% здоровья и меньше двигается быстрее. Гаджет «Шаромёт» запускает по две пули в 8 сторон от Рико, которые могут прошивать врагов, как и Супер, рикошетя. С гаджетом «Надувной замок», Рико может исцеляться с помощью пуль, основной атаки, когда они отскакивают.",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "дэррил":
        try:
            await message.answer_photo(
                photo=FSInputFile(DARRIL),  
                caption="Имеет высокую скорость передвижения и большое количество здоровья. Атакуя, он стреляет дважды из пары двустволок, наносящих высокий урон вблизи. Чем ближе цель, тем больше урон. Используя Супер, Дэррил может позволить себе быстро прокатиться в выбранную сторону. Первый гаджет Дэррила — выстрелы шквальным огнём во все стороны, которые при попадании ещё быстрее заряжают ему Супер, а второй гаджет позволяет ему замедлить врагов в определённой от себя области. Звёздная сила «Стальные обручи» даёт Дэррилу щит на время использования Супера, что сделает наносимый ему урон минимальным, а «Перезарядка на ходу» ускорит время перезарядки в два раза на 5 секунд.",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "пенни":
        try:
            await message.answer_photo(
                photo=FSInputFile(PENNY),  
                caption="Она имеет нормальную скорость передвижения, переменный урон, но низкую скорость перезарядки, большую дальность атаки и средний уровень здоровья. Пенни атакует мешочком фальшивого золота, который может поразить врагов за первоначальной целью с двойным и иногда даже тройным уроном. Её Супер устанавливает мортиру, имеющую среднее здоровье, высокий урон и низкую скорострельность. Она может стрелять по врагам в кустах и оставляет после выброса бомбы небольшой огненный след. Первым гаджетом Пенни ставит бочку, которая защищает её от чужих снарядов, а также позволяет Пенни при попадании по ней взрывать собственные мешочки. Вторым гаджетом пушка Пенни стреляет по всем противникам в радиусе действия. С первой звёздной силой количество золота из мешочков Пенни, а также их дальность увеличиваются. Со второй звёздной силой пушка Пенни будет отбрасывать и наносить урон ближайшим противникам при установке.",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "карл":
        try:
            await message.answer_photo(
                photo=FSInputFile(CARL),  
                caption="Карл имеет нормальную скорость передвижения, средне-высокое количество здоровья и средний урон. Он кидает свою кирку, которая при столкновении с препятствием или пролетев максимальную дистанцию, возвращается обратно к нему. Его Супер позволяет ему вращаться и двигаться намного быстрее, нанося урон всем, кто попал под его удар. Во время использования гаджета «Клапан сброса» следующая атака Карла оставляет за собой огненный след. Если враги наступят на этот след, они получат эффект горения наносящий 400 очков урона в течении 3 секунд. Другой гаджет переносит его вместе с одной атакой. С его Звёздной силой «Усиленный бросок» кирка Карла летит на 12% быстрее. Звёздная сила «Защитный пируэт» даёт Карлу щит во время использования Супера, что уменьшает наносимый противниками урон на 35%.",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "джекки":
        try:
            await message.answer_photo(
                photo=FSInputFile(JACKY),  
                caption="Джеки имеет высокую скорость передвижения, высокий показатель здоровья и высокий показатель урона. Атакой, у которой нормальная перезарядка, она с силой стучит своим буром по земле, и из-за чего её радиус имеет форму окружности. Её Супер — бур, с помощью которого она притягивает к себе врагов. Во время использования первого гаджета Джеки становится быстрее на некоторое время, а вторым она может строить стены. С первой Звёздной силой она возвращает часть урона врагу, а со второй Звёздной силой уменьшает наносимый ей урон в течение всего боя.",
                reply_markup=back_keyboard
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer("Извините, не удалось загрузить изображение.", reply_markup=back_keyboard)
    elif user_input == "гас":
        try:
            await message.answer_photo(
                photo=FSInputFile(GUS),  
                caption="Гас имеет нормальную скорость передвижения, средне-низкое количество здоровья и средний урон. Основной атакой он запускает воздушный шар, каждое попадание которого заполняет шкалу. При полном заполнении следующая атака вызовет призрака, исцеляющего часть здоровья союзникам. Шкала заполняется за три попадания. Своим Супером Гас пускает другой воздушный шар по имени Спуки, который даёт ему или союзнику щит (зависит от того, нажали вы автоатаку или прицелились в другого бойца), работающий как гаджет Эдгара «Крепкий орешек», только с бóльшим количеством здоровья. Его первый гаджет взрывает всех призраков Гаса, а второй забирает часть здоровья Гаса, а взамен полностью заполняет призрачную шкалу. С первой звёздной силой призраки Гаса восстанавливают в 2 раза больше здоровья, а вторая даёт усиление урона при использовании Супера.",
                reply_markup=back_keyboard
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
