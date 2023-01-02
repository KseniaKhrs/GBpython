import body
import view
import logger


def run():
    mode = view.choose_mode()
    if mode == '1':
        old_name = view.old_contact()
        contact_book = logger.read_phone_book()
        old_phone = body.find_contact(old_name, contact_book)
        view.print_phone(old_phone)

    elif mode == '2':
        name = view.new_name()
        number = view.new_number()
        logger.add_new_contact(name, number)
