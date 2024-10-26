from PyQt6.QtWidgets import QApplication, QListWidget, QTextEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QLineEdit
import json

def add_s():
    global lessons
    name = studentname.text()
    if major.text().lower() == 'οικονομικά':
        lessons[name] = {'έκθεση': [], 'μαθηματικά': [], 'αεππ': [], 'αοθ': []}
        add_name()
    elif major.text().lower() in ['θετική', 'πολυτεχνικά']:
        lessons[name] = {'έκθεση': [], 'μαθηματικά': [], 'χημεία': [], 'φυσική': []}
        add_name()
    elif major.text().lower() == 'υγείας':
        lessons[name] = {'έκθεση': [], 'βιολογία': [], 'χημεία': [], 'φυσική': []}
        add_name()
    elif major.text().lower() == 'θεωρητική':
        lessons[name] = {'έκθεση': [], 'αρχαία': [], 'λατινικά': [], 'ιστορία': []}
        add_name()

def add_name():
    global students
    global student_list
    name = studentname.text()
    student_list.addItem(name)
    students.append(name)
    with open("names.json", "w") as file:
        json.dump(lessons, file)

def loadstudent():
    index = student_list.currentRow()
    display.setText(students[index] + "\nεισάγετε τους βαθμούς στα μαθήματα, χωρισμένους από κόμματα και κενό (πχ '96, 85, 70, 89')")
    i = 0
    for key in lessons[students[index]]:
        input_fields[i].setPlaceholderText(key + ':')
        i += 1

def add_m():
    global lessons
    i = 0
    keys = []   
    key = students[student_list.currentRow()]
    for j in lessons[key]:
        keys.append(j)
    for j in input_fields:
        for k in j.text().split(', '):
            lessons[key][keys[i]].append(k)
        i += 1
    print(lessons)

app = QApplication([])
w = QWidget()
w.setWindowTitle("Βαθμοί μαθητών")
w.resize(800, 600)
student_list = QListWidget()
students = []
pb1 = QPushButton("add")
pb2 = QPushButton('add')
studentname = QLineEdit()
studentname.setPlaceholderText('Όνομα μαθητή:')
major = QLineEdit()
major.setPlaceholderText('Κατεύθυνση:')
display = QTextEdit()
display.setText('εισάγετε και επιλέξτε μαθητή')
input1 = QLineEdit()
input2 = QLineEdit()
input3 = QLineEdit()
input4 = QLineEdit()
input_fields = [input1, input2, input3, input4]
with open('names.json', 'r') as file:
    lessons = json.load(file)
lv1 = QVBoxLayout()
lv2 = QVBoxLayout()
lh1 = QHBoxLayout()
lv1.addWidget(student_list)
lv1.addWidget(studentname)
lv1.addWidget(major)
lv1.addWidget(pb1)
for key in lessons:
    student_list.addItem(key)
    students.append(key)
lv2.addWidget(display)
for i in input_fields:
    lv2.addWidget(i)
lv2.addWidget(pb2)
lh1.addLayout(lv1)
lh1.addLayout(lv2)
w.setLayout(lh1)
w.show()
pb1.clicked.connect(add_s)
student_list.currentRowChanged.connect(loadstudent)
pb2.clicked.connect(add_m)
app.exec()