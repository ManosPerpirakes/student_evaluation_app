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
    global lessons
    if len(students) > 0:
        index = student_list.currentRow()
        key = [students[index]]
        keys = []  
        for i in lessons[key[0]]:
            keys.append(i) 
        flag = True
        for i in range(4):
            if lessons[key[0]][keys[i]] != []:
                flag = False
        if not flag:
            show_results()
            i = 0
            for key in lessons[students[index]]:
                input_fields[i].setPlaceholderText(key + ':')
                i += 1
        else:
            display.setText(students[index] + "\nεισάγετε τους βαθμούς στα μαθήματα, χωρισμένους από κόμματα και κενό (πχ '96, 85, 70, 89')")
            i = 0
            for key in lessons[students[index]]:
                input_fields[i].setPlaceholderText(key + ':')
                i += 1
    else:
        display.setText('εισάγετε και επιλέξτε μαθητή')

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
    with open("names.json", "w") as file:
        json.dump(lessons, file)
    show_results()

def show_results():
    try:
        key = students[student_list.currentRow()]
        keys = []
        mean = 0.0  
        meanfinal = 0.0 
        text = ''
        text += key + '\n'
        for i in lessons[key]:
            keys.append(i)
        i = 0
        count = 0
        for j in lessons[key]:
            text += (j + ':')
            for k in range(len(lessons[key][keys[i]])):
                text += '\n' + lessons[key][keys[i]][k]
                mean += float(lessons[key][keys[i]][k])
                count += 1
            if count > 0:
                mean /= count
                meanfinal += mean
                text += "\nμέσος όρος: " + str(mean) + '\n'
            i += 1
            mean = 0
            count = 0
        meanfinal /= 4
        text += '\nσυνολικός μέσος όρος: ' + str(meanfinal)
        display.setText(text)
    except:
        pass

def delete():
    global lessons
    global students
    key = students[student_list.currentRow()]
    del lessons[key]
    students = []
    student_list.clear()
    for i in lessons:
        student_list.addItem(i)
        students.append(i)
    with open("names.json", "w") as file:
        json.dump(lessons, file)

app = QApplication([])
w = QWidget()
w.setWindowTitle("Βαθμοί μαθητών")
w.resize(800, 600)
student_list = QListWidget()
students = []
pb1 = QPushButton("εισαγωγή")
pb2 = QPushButton('αποτέλεσματα:')
pb3 = QPushButton('διαγραφή')
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
lv1.addWidget(pb3)
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
pb3.clicked.connect(delete)
app.exec()