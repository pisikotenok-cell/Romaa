import asyncio
import json
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command, CommandObject

TOKEN = "8889068408:AAEU-ausU_lzK2HqgZNZD9hrgU6EQJtYPSM"
ADMIN_IDS = [8096163880]
CHAT_LINK = "https://t.me/+ambpt14lLwI3YmM6"
SUPPORT_LINK = "https://t.me/romanchiki_vopr_bot"

bot = Bot(token=TOKEN)
dp = Dispatcher()

ALL_ROLES = [
    "Петр І Алексеевич", "Екатерина I Алексеевна", "Петр ІІ Алексеевна", "Анна Иоанновна",
    "Елизавета Петровна", "Петр III Федорович", "Екатерина II Алексеевна", "Павел І Петрович",
    "Александр I Павлович", "Николай I Павлович", "Александр ІІ Николаевич", "Александр ІІІ Александрович",
    "Николай II Александрович", "Мария Долгорукова", "Евдокия Стрешнева", "Мария Милославская",
    "Наталья Нарышкина", "Марфа Апраксина", "Мария Фёдоровна (Павел I)", "Елизавета Алексеевна",
    "Александра Фёдоровна (Николай I)", "Мария Александровна", "Мария Фёдоровна (Александр III)",
    "Татьяна Николаевна", "Анастасия Николаевна", "Ольга Николаевна", "Мария Николаевна",
    "Алексей Николаевич", "Александра Федоровна (Николай II)"
]

def load_busy_roles():
    if os.path.exists("roles.json"):
        with open("roles.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_busy_roles(data):
    with open("roles.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

busy_roles = load_busy_roles()

def get_main_menu():
    buttons = [
        [InlineKeyboardButton(text="📜 Правила", callback_data="view_rules")],
        [InlineKeyboardButton(text="🎭 Выбрать роль", callback_data="choose_role")],
        [InlineKeyboardButton(text="🚀 Пройти тест", callback_data="start_test")],
        [InlineKeyboardButton(text="🆘 Поддержка", url=SUPPORT_LINK)]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

@dp.message(Command("start"))
async def cmd_start(message: Message):
    welcome_text = (
        "Привет! Добро пожаловать к Романовым 📜\n\n"
        "Чтобы получить ссылку на флуд и не вылететь при первой же чистке, "
        "нужно прочитать правила и сдать по ним быстрый тест. Это займет всего минуту.\n\n"
        "Сначала жми кнопку **📜 Правила**, чтобы быть в курсе!"
    )
    await message.answer(welcome_text, reply_markup=get_main_menu())

@dp.callback_query(F.data == "view_rules")
async def view_rules(callback: CallbackQuery):
    rules_text = (
        "📜 **ПРАВИЛА НАШЕГО ФЛУДА:**\n\n"
        "📌 Норма — 50 соо в неделю, чистка в воскресенье.\n\n"
        "1. Любой контент 18+ запрещён.\n"
        "2. Реклама и прочие рассылки запрещены.\n"
        "3. Ссориться лучше в лс.\n"
        "4. Любой спам — мут.\n"
        "5. Можно записывать кружки, гс, присылать фото и видео.\n"
        "6. Калл призывают только админы!\n"
        "7. За любые оскорбления варн!\n"
        "8. Если хотите пригласить кого-то во флуд, нужно согласовать с влд.\n\n"
        "Прочитал? Жми назад и переходи к тесту!"
    )
    await callback.message.edit_text(rules_text, reply_markup=get_main_menu())

@dp.callback_query(F.data == "start_test")
async def test_q1(callback: CallbackQuery):
    q1_text = "❓ **Вопрос 1:** Какова норма активности в неделю, чтобы не попасть под чистку в воскресенье?"
    buttons = [
        [InlineKeyboardButton(text="А) Да сколько получится.", callback_data="test_wrong")],
        [InlineKeyboardButton(text="Б) Минимум 50 сообщений.", callback_data="test_q2")],
        [InlineKeyboardButton(text="В) Хватит одного сообщения.", callback_data="test_wrong")]
    ]
    await callback.message.edit_text(q1_text, reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons))

@dp.callback_query(F.data == "test_q2")
async def test_q2(callback: CallbackQuery):
    q2_text = "❓ **Вопрос 2:** Что будет за оскорбления в чате и где нужно выяснять отношения?"
    buttons = [
        [InlineKeyboardButton(text="А) Ничего не будет, спорим где хотим.", callback_data="test_wrong")],
        [InlineKeyboardButton(text="Б) За оскорбления дадут варн, а ссориться надо в ЛС.", callback_data="test_q3")],
        [InlineKeyboardButton(text="В) Админы рассудят в общем чате.", callback_data="test_wrong")]
    ]
    await callback.message.edit_text(q2_text, reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons))

@dp.callback_query(F.data == "test_q3")
async def test_q3(callback: CallbackQuery):
    q3_text = "❓ **Вопрос 3:** Можно ли кидать контент 18+ или без спроса звать друзей?"
    buttons = [
        [InlineKeyboardButton(text="А) Нет, 18+ запрещено, а друзей — только через влд.", callback_data="test_win")],
        [InlineKeyboardButton(text="Б) Можно всё, чат же для флуда.", callback_data="test_wrong")]
    ]
    await callback.message.edit_text(q3_text, reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons))

@dp.callback_query(F.data == "test_wrong")
async def test_wrong(callback: CallbackQuery):
    await callback.message.edit_text(
        "❌ **Неправильно.** Прочитай правила внимательнее и попробуй ещё раз.",
        reply_markup=get_main_menu()
    )

@dp.callback_query(F.data == "test_win")
async def test_win(callback: CallbackQuery):
    win_text = (
        "🎉 **Тест пройден!**\n\n"
        "Правила ты знаешь, теперь можно и во флуд.\n\n"
        "🔗 **Ссылка на чат:** {CHAT_LINK}\n\n"
        "Не забудь выбрать свободную роль в меню!"
    ).format(CHAT_LINK=CHAT_LINK)
    await callback.message.edit_text(win_text, reply_markup=get_main_menu())

@dp.callback_query(F.data == "choose_role")
async def choose_role(callback: CallbackQuery):
    keyboard_buttons = []
    for role in ALL_ROLES:
        if role in busy_roles:
            text = f"❌ {role} (занят {busy_roles[role]})"
            cd = "role_busy_info"
        else:
            text = f"👑 {role}"
            cd = f"take_{role}"
        keyboard_buttons.append([InlineKeyboardButton(text=text, callback_data=cd)])
    
    keyboard_buttons.append([InlineKeyboardButton(text="🔙 Назад", callback_data="back_main")])
    await callback.message.edit_text(
        "🎭 **Выбери свободную роль:**\n(Занятые отмечены крестиком)",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)
    )

@dp.callback_query(F.data == "role_busy_info")
async def role_busy_info(callback: CallbackQuery):
    await callback.answer("Эта роль уже занята!", show_alert=True)

@dp.callback_query(F.data.startswith("take_"))
async def take_role(callback: CallbackQuery):
    role_name = callback.data.split("take_")[1]
    username = f"@{callback.from_user.username}" if callback.from_user.username else callback.from_user.full_name
    
    global busy_roles
    busy_roles[role_name] = username
    save_busy_roles(busy_roles)
    
    await callback.message.edit_text(
        f"👑 Отлично, теперь ты: **{role_name}**.\n\nСсылка на флуд открыта в главном меню!",
        reply_markup=get_main_menu()
    )

@dp.callback_query(F.data == "back_main")
async def back_main(callback: CallbackQuery):
    await callback.message.edit_text("Главное меню:", reply_markup=get_main_menu())

@dp.message(Command("busy"))
async def admin_busy(message: Message, command: CommandObject):
    if message.from_user.id not in ADMIN_IDS:
        return
    if not command.args:
        await message.answer("Пиши так: `/busy Екатерина II @username`")
        return
    try:
        parts = command.args.split()
        user = parts[-1]
        role = " ".join(parts[:-1])
        if role in ALL_ROLES:
            busy_roles[role] = user
            save_busy_roles(busy_roles)
            await message.answer(f"✅ Роль **{role}** закреплена за {user}")
        else:
            await message.answer("❌ Нет такой роли в списке.")
    except Exception:
        await message.answer("Ошибка. Пиши строго: `/busy Название Роли @юзер`")

@dp.message(Command("free"))
async def admin_free(message: Message, command: CommandObject):
    if message.from_user.id not in ADMIN_IDS:
        return
    role = command.args
    if role in busy_roles:
        del busy_roles[role]
        save_busy_roles(busy_roles)
        await message.answer(f"✅ Роль **{role}** снова свободна.")
    else:
        await message.answer("❌ Роль и так свободна.")

async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())