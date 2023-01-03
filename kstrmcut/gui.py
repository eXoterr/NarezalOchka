import PySimpleGUI as sg
from kstrmcut.core.convert import createVideo

def runGui():
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('Создать нарезку клипов', justification='center')],
                [sg.Text('Файл субтитров', size=(20, 1)), sg.InputText(expand_x=True), sg.FileBrowse()],
                [sg.Text('Файл видео', size=(20, 1)), sg.InputText(expand_x=True), sg.FileBrowse()],
                [sg.Text('Искомое слово(фраза)', size=(20, 1)), sg.InputText(expand_x=True)],
                [sg.Text('Сохранить итог как' , size=(20, 1)), sg.InputText(expand_x=True), sg.SaveAs()],
                [sg.Button('Ok'), sg.Button('Cancel')] 
            ]

    layout2 = [
        [
            [sg.Text('Создать нарезку клипов')],
            [sg.Text('Файл субтитров')],
            [sg.Text('Файл видео')],
            [sg.Text('Искомое слово(фраза)')],
            [sg.Text('Сохранить итог как')],


        ],
        [
            [sg.InputText(expand_x=True), sg.FileBrowse()],
            [sg.InputText(expand_x=True)],
            [sg.InputText(expand_x=True), sg.FileBrowse()],
            [sg.InputText(expand_x=True), sg.SaveAs()],
        ],
        [[sg.Button('Ok'), sg.Button('Cancel')]]
    ]

    # Create the Window
    window = sg.Window('НарезалОчка', layout, element_justification='c')
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        
        createVideo(textFile=values[0], sourceFile=values[1], keyword=values[2], targetFile=values[3], endOffset=1)
        

    window.close()