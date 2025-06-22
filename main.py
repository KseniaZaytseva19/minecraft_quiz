from PyQt6.QtCore import Qt
from PyQt6.QtDBus import QDBusMessage
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout,
                             QRadioButton, QMessageBox, QGroupBox, QButtonGroup)
from random import shuffle
class Question:
    def __init__(self, text, correct_answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.text = text
        self.correct_answer = correct_answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3

questions = []
questions.append(Question('who lives in a pineapple under the sea?', 'Sponge Bob Square Pants', 'Plankton', 'mr Krabs', 'Patrick'))
questions.append(Question('What color is the sky?', 'Blue', 'Green', 'Yellow', 'Red'))
questions.append(Question('Who lives in the forest?', 'Bear', 'Human', 'Cat', 'Pigeon'))
questions.append(Question('What color is the sun?', 'Yellow', 'Blue', 'Green', 'Black'))
questions.append(Question('how many colors are there in a rainbow?', '7', '5', '8', '6'))
questions.append(Question('Who is meowing?', 'Cat', 'Dog', 'Cow', 'Elephant'))
questions.append(Question('what is the release year of minecraft?', '2009', '2011', '2015', '2018'))
questions.append(Question('how many months are in a year?', '12', '13', '10', '11'))
questions.append(Question('When it is snowing?', 'In winter', 'In summer', 'In autumn', 'In spring'))
questions.append(Question('how many notes are there in the musical scale?', '7', '8', '9', '6'))
questions.append(Question('Which is the capital of Great Britain?', 'London', 'Moscow', 'Paris', 'Berlin'))

active_question = 0

app = QApplication([])
win = QWidget()
win.setFixedSize(450, 250)

win.setWindowTitle('Memory Card')
question_label = QLabel('какого ...?')
answer_button = QPushButton('Ответить')
answers_group_box = QGroupBox('Варианты ответов:')
layout_answers = QHBoxLayout()
next_question_button = QPushButton('Next question')
result_group_box = QGroupBox('Result')
correct_answer_label = QLabel('лешего')
correctness_label = QLabel('correct/wrong')

amount_correct = 0
final_result = QLabel('Result of the quiz:')
amount_correct_label = QLabel(str(amount_correct))
start_again = QPushButton('Try again')

ans1 = QRadioButton('...')
ans2 = QRadioButton('чо')
ans3 = QRadioButton('пон')
ans4 = QRadioButton('лешего')
answer_buttons = [ans1, ans2, ans3, ans4]
answers_group = QButtonGroup()
answers_group.addButton(ans1)
answers_group.addButton(ans2)
answers_group.addButton(ans3)
answers_group.addButton(ans4)

layout1 = QVBoxLayout()
layout2 = QVBoxLayout()
result_layout = QVBoxLayout()

layout2.addWidget(ans1)
layout2.addWidget(ans2)
layout1.addWidget(ans3)
layout1.addWidget(ans4)
result_layout.addWidget(correctness_label)
result_layout.addWidget(correct_answer_label)

layout_answers.addLayout(layout1)
layout_answers.addLayout(layout2)

result_group_box.setLayout(result_layout)
answers_group_box.setLayout(layout_answers)
layout_main = QVBoxLayout()
layout_main.addWidget(question_label, alignment=Qt.AlignmentFlag.AlignCenter)
layout_main.addWidget(answers_group_box)
layout_main.addWidget(result_group_box)

layout_main.addWidget(answer_button, alignment=Qt.AlignmentFlag.AlignCenter)
layout_main.addWidget(next_question_button, alignment=Qt.AlignmentFlag.AlignCenter)

layout_main.addWidget(final_result,  alignment=Qt.AlignmentFlag.AlignCenter)
layout_main.addWidget(amount_correct_label, alignment=Qt.AlignmentFlag.AlignCenter)
layout_main.addWidget(start_again, alignment=Qt.AlignmentFlag.AlignCenter)
final_result.hide()
amount_correct_label.hide()
start_again.hide()

win.setLayout(layout_main)
result_group_box.hide()
next_question_button.hide()

def next_question():
    global active_question
    global questions
    result_group_box.hide()
    next_question_button.hide()
    answer_button.show()
    answers_group_box.show()
    final_result.hide()
    amount_correct_label.hide()
    start_again.hide()

    active_question += 1
    if active_question == len(questions):
        answer_button.hide()
        answers_group_box.hide()
        final_result.show()
        amount_correct_label.show()
        start_again.show()


        return
    show_question(questions[active_question])

def answer():
    result_group_box.show()
    next_question_button.show()
    answer_button.hide()
    answers_group_box.hide()
    check_answer()

def show_question(question):
    question_label.setText(question.text)
    shuffle(answer_buttons)
    answer_buttons[0].setText(question.correct_answer)
    answer_buttons[1].setText(question.wrong_answer1)
    answer_buttons[2].setText(question.wrong_answer2)
    answer_buttons[3].setText(question.wrong_answer3)
    correct_answer_label.setText(question.correct_answer)
    answers_group.setExclusive(False)
    ans1.setChecked(False)
    ans2.setChecked(False)
    ans3.setChecked(False)
    ans4.setChecked(False)
    answers_group.setExclusive(True)

def check_answer():
    global amount_correct
    if answer_buttons[0].isChecked():
        correctness_label.setText('Correct')
        amount_correct += 1
        amount_correct_label.setText(str(amount_correct))
    else:
        correctness_label.setText('Wrong')


def try_again():
    global active_question, amount_correct
    active_question = 0
    show_question(questions[active_question])
    amount_correct = 0
    amount_correct_label.setText(str(amount_correct))
    answer_button.show()
    answers_group_box.show()
    final_result.hide()
    amount_correct_label.hide()
    start_again.hide()

show_question(questions[active_question])
answer_button.clicked.connect(answer)
next_question_button.clicked.connect(next_question)
start_again.clicked.connect(try_again)

win.show()
app.exec()
