subj = {}
with open('file4task6.txt', 'r') as f:
    for line in f:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету:\n {subj}')
