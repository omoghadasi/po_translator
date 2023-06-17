from googletrans import Translator


def translate_po_file(input_file, output_file):
    # ایجاد نمونه Translator
    translator = Translator(
        service_urls=['translate.google.com'], timeout=None)
    msgid = ""
    msgstr = ""

    # باز کردن فایل ورودی و فایل خروجی
    with open(input_file, 'r') as input_po, open(output_file, 'w') as output_po:
        # خواندن خط به خط فایل ورودی
        for line in input_po:
            if line.startswith('msgid'):
                msgid = line.strip()[7:-1]  # برداشتن بخش متنی از msgid
                output_po.write(line)
            elif line.startswith('msgstr'):
                if msgid:
                    translation = translator.translate(msgid, dest='fa')
                    msgstr = translation.text
                output_po.write('msgstr "' + msgstr + '"\n\n')
            # elif is_msgid and line.startswith('"'):
            #     # برداشتن بخش متنی از خطوط بعدی msgid
            #     msgid += line.strip()[1:-1]
            # elif is_msgstr and line.startswith('"'):
            #     # برداشتن بخش متنی از خطوط بعدی msgstr
            #     msgstr += line.strip()[1:-1]
            else:
                output_po.write(line)

    print("##########################################")
    print("ترجمه با موفقیت انجام شد.")


# ترجمه فایل PO
translate_po_file('input.po', 'output.po')
