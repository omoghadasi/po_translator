from googletrans import Translator


def translate_po_file(input_file, output_file):
    # ایجاد نمونه Translator
    translator = Translator(
        service_urls=['translate.google.com'], timeout=None)

    # متغیرهای کنترلی ترجمه
    is_msgid = False
    is_msgstr = False
    msgid = ""
    msgstr = ""

    total_lines = 0
    translated_lines = 0

    # باز کردن فایل ورودی و فایل خروجی
    with open(input_file, 'r') as input_po, open(output_file, 'w') as output_po:
        # خواندن خط به خط فایل ورودی
        for line in input_po:
            total_lines += 1

            if line.startswith('msgid'):
                is_msgid = True
                is_msgstr = False
                msgid = line.strip()[7:-1]  # برداشتن بخش متنی از msgid
            elif line.startswith('msgstr'):
                is_msgid = False
                is_msgstr = True
                msgstr = line.strip()[8:-1]  # برداشتن بخش متنی از msgstr
            elif is_msgid and line.startswith('"'):
                # برداشتن بخش متنی از خطوط بعدی msgid
                msgid += line.strip()[1:-1]
            elif is_msgstr and line.startswith('"'):
                # برداشتن بخش متنی از خطوط بعدی msgstr
                msgstr += line.strip()[1:-1]

            # ترجمه متن و نوشتن در فایل خروجی
            if not line.strip() and msgid:
                translation = translator.translate(msgid, dest='fa')
                output_po.write('msgid "' + msgid + '"\n')
                output_po.write('msgstr "' + translation.text + '"\n\n')
                translated_lines += 1

                print("EN: " + msgid)
                print("FA: " + translation.text)
                print('Translated Lines: ' + str(translated_lines))
                print('\n----------------------------------------------------\n')

                msgid = ""
                msgstr = ""

            else:
                output_po.write(line)

    print("##########################################")
    print("ترجمه با موفقیت انجام شد.")
    progress = (translated_lines / total_lines) * 100
    print("پیشرفت ترجمه: %.2f%%" % progress)


# ترجمه فایل PO
translate_po_file('input.po', 'output.po')
