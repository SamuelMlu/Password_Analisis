# mengimport pysimpeGUI
import PySimpleGUI as sg

# menetukan theme dari GUI
sg.theme('Reddit')


def main():
    # Untuk buat menu help
    menu_def = [['&Help', '&About']]

    # Bagian kiri dari GUI
    left_col = [
        [sg.Text("Masukkan Password", pad=(0, 0))],
        [sg.InputText('', size=(20, 1), key='myInput', pad=(0, 0)), sg.Button('Check', size=(13, 1))],
        [sg.InputText(size=(20, 1), key="Saran", disabled=True, pad=(0, 0)), sg.Button('Saran Password', size=(13, 1))],

    ]

    # Bagian kanan GUI
    right_col = [
        [sg.Text('Hasil:', size=(10, 1))],
        [sg.Multiline(size=(40, 5), key="output", disabled=True)],
        # [sg.Text('_' * 80)],

    ]

    # All the stuff inside your window
    # Digabung bagian kiri dan kanan GUI
    # sg.VSeperator() untuk membuat memisahkan kanan GUI dan kiri GUI
    layout = [
        [[sg.Menu(menu_def)],
         [sg.Text('Password Analysis', size=(25, 1), justification='left',
                  font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
         sg.Column(left_col, element_justification='left'), sg.VSeperator(),
         sg.Column(right_col, element_justification='left')]
    ]

    # Buat Window
    window = sg.Window('Check Password', layout, enable_close_attempted_event=True, size=(550, 200), resizable=True)

    # ----- Run the Event Loop -----
    # --------------------------------- Event Loop ---------------------------------

    # melakukan looping pada "event"
    while True:
        event, values = window.read()
        print(event, values)

        if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Exit') and \
                sg.popup_yes_no('Do you really want to exit?') == 'Yes':
            break

        # Memunculkan kotak kalau buka about
        if event == 'About':
            sg.popup('About this program:',
                     'Dibuat Rekayasa Keamanan Siber Angkatan 2020 ',
                     'Samuel Karuniawan (4332001003)',
                     'Rakib Andreansyah (4332001010)',
                     'Isnaeni Hari Yusriyah (4332001032)')

        # Perintah di dalam key Check
        elif event == 'Check':
            import re

            Password = values['myInput']

            def checklength():
                global panjangPassword
                if len(Password) < 12:
                    panjangPassword = "Password kurang dari 12"
                else:
                    panjangPassword = "Password lebih dari 12"
                return panjangPassword

            def checkupper():
                global cekUpper
                regex = re.compile("[A-Z]")
                if (regex.search(Password) == None):
                    cekUpper = "Password tidak terdapat huruf kapital"
                else:
                    cekUpper = "Password terdapat huruf kapital"
                return cekUpper

            def checklower():
                global cekLower
                regex = re.compile("[a-z]")
                if (regex.search(Password) == None):
                    cekLower = "Password tidak terdapat huruf kecil"
                else:
                    cekLower = "Password terdapat huruf kecil"
                return cekLower

            def checknumber():
                global cekNumber
                regex = re.compile("[0-9]")
                if (regex.search(Password) == None):
                    cekNumber = "Password tidak terdapat angka"
                else:
                    cekNumber = "Password terdapat angka"
                return cekNumber

            def checksymbol():
                global cekSimbol
                # r"\W" untuk spesial karakter termasuk space
                regex = re.compile(r"\W")
                if (regex.search(Password) == None):
                    cekSimbol = "Password tidak terdapat simbol "
                else:
                    cekSimbol = "Password terdapat simbol"
                return cekSimbol

            checklength()
            checkupper()
            checklower()
            checknumber()
            checksymbol()

            window['output'].update(
                panjangPassword + "\n" + cekUpper + "\n" + cekLower + "\n" + cekNumber + "\n" + cekSimbol)


        # Perintah di dalam key Saran Password
        elif event == 'Saran Password':
            import string
            import random

            def get_random_string(length):
                global passrandom
                letters = string.ascii_letters + string.digits + string.punctuation
                passrandom = ''.join(random.choice(letters) for i in range(length))
                print(passrandom)

            get_random_string(12)
            window['Saran'].update(passrandom)
    window.close()

# memanggil main()
if __name__ == '__main__':
    main()