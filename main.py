import random
from googletrans import Translator
import time


def translate_po_file(input_file, output_file):
    # ایجاد نمونه Translator
    translator = Translator(
        service_urls=['translate.google.com'])
    msgid = ""
    msgstr = ""
    count_translated = 0

    # باز کردن فایل ورودی و فایل خروجی
    with open(input_file, 'r') as input_po, open(output_file, 'w') as output_po:
        # خواندن خط به خط فایل ورودی
        for line in input_po:
            if line.startswith('msgid'):
                print('find msgid line')
                msgid = line.strip()[7:-1]  # برداشتن بخش متنی از msgid
                print('msgid: ' + msgid)
                output_po.write(line)
                print("Line: " + line)

            elif line.startswith('msgstr'):
                print('find msgstr line')
                if msgid:
                    print('start translating{' + msgid + ' }')
                    translation = translator.translate(str(msgid), dest='fa')
                    print('end translating{' + msgid + ' }')
                    count_translated += 1
                    msgstr = translation.text
                    print('msgstr: ' + msgstr)
                    output_po.write('msgstr "' + msgstr + '"\n\n')
                    print('count: ' + str(count_translated))
            else:
                output_po.write(line)
                print("Line: " + line)
            time.sleep(random.randrange(1, 10))

    print("\n##########################################")
    print("ترجمه با موفقیت انجام شد.")


# ترجمه فایل PO
translate_po_file('input.po', 'output.po')
