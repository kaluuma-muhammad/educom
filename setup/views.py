from django.shortcuts import render, get_object_or_404, redirect
from .models import Level, Term, Grade, Subject, House
from django.contrib.auth import get_user_model

User = get_user_model()

# ==================================================== levels =======================================================================
# Create
def create_level(request):
    if request.method == 'POST':
        title = request.POST['title']

        added_by = request.user.id
        user = User.objects.get(id=added_by) if added_by else None

        Level.objects.create(title=title, user_id=user.id)

        return redirect('setup:levels')
    return render(request, 'setup/levels.html')

# Read
def level_list(request):
    levels = Level.objects.all().order_by('created_at')
    return render(request, 'setup/levels.html', {'levels': levels})

# Update
def update_level(request, id):
    level = get_object_or_404(Level, id=id)
    if request.method == 'POST':
        level.title = request.POST['title']
        level.save()
        return redirect('setup:levels')
    return render(request, 'setup/levels.html')

# Status
def change_status(request, id):
    level = get_object_or_404(Level, id=id)

    if request.method == 'POST':
        if level.status == 0:
            level.status = 1
        else:
            level.status = 0
        level.save()
        return redirect('setup:levels')
    return render(request, 'setup/levels.html')

# Delete
def delete_level(request, id):
    level = get_object_or_404(Level, id=id)
    if request.method == 'POST':
        level.delete()
        return redirect('setup:levels')
    return render(request, 'setup/levels.html')

# Detail View
def level_detail(request, id):
    level = get_object_or_404(Level, id=id)
    return render(request, 'level_detail.html', {'level': level})


# ==================================================== terms =======================================================================
# Create
def create_term(request):
    if request.method == 'POST':
        title = request.POST['title']
        symbol = request.POST['abbrev']

        added_by = request.user.id
        user = User.objects.get(id=added_by) if added_by else None

        Term.objects.create(title=title, symbol=symbol, user_id=user.id)

        return redirect('setup:terms')
    return render(request, 'setup/terms.html')

# Read
def term_list(request):
    terms = Term.objects.all().order_by('created_at')
    return render(request, 'setup/terms.html', {'terms': terms})

# Update
def update_term(request, id):
    term = get_object_or_404(Term, id=id)
    if request.method == 'POST':
        term.title = request.POST['title']
        term.symbol = request.POST['abbrev']
        term.save()
        return redirect('setup:terms')
    return render(request, 'setup/terms.html')

# Status
def change_term_status(request, id):
    term = get_object_or_404(Term, id=id)

    if request.method == 'POST':
        if term.status == 0:
            term.status = 1
        else:
            term.status = 0
        term.save()
        return redirect('setup:terms')
    return render(request, 'setup/terms.html')

# Delete
def delete_term(request, id):
    term = get_object_or_404(Term, id=id)
    if request.method == 'POST':
        term.delete()
        return redirect('setup:terms')
    return render(request, 'setup/terms.html')

# Detail View
def term_detail(request, id):
    term = get_object_or_404(Term, id=id)
    return render(request, 'term_detail.html', {'term': term})



# ==================================================== grades =======================================================================
# Create
def create_grade(request):
    if request.method == 'POST':
        title = request.POST['title']
        level = request.POST['level']
        abbrev = request.POST['abbrev']

        level_id = Level.objects.get(id=level) if level else None
        added_by = request.user.id
        user = User.objects.get(id=added_by) if added_by else None

        Grade.objects.create(title=title, level_id=level_id, symbol=abbrev, user_id=user.id)

        return redirect('setup:grades')
    return render(request, 'setup/grades.html')

# Read
def grade_list(request):
    grades = Grade.objects.all().order_by('created_at')
    levels = Level.objects.all().order_by('created_at')
    return render(request, 'setup/grades.html', {'grades': grades, 'levels': levels})

# Update
def update_grade(request, id):
    grade = get_object_or_404(Grade, id=id)
    if request.method == 'POST':
        grade.title = request.POST['title']
        level_id = request.POST.get('level')
        grade.symbol = request.POST['abbrev']

        if level_id:
            grade.level_id = Level.objects.get(id=level_id)
        grade.save()
        return redirect('setup:grades')
    return render(request, 'setup/grades.html')

# Status
def change_grade_status(request, id):
    grade = get_object_or_404(Grade, id=id)

    if request.method == 'POST':
        if grade.status == 0:
            grade.status = 1
        else:
            grade.status = 0
        grade.save()
        return redirect('setup:grades')
    return render(request, 'setup/grades.html')

# Delete
def delete_grade(request, id):
    grade = get_object_or_404(Grade, id=id)
    if request.method == 'POST':
        grade.delete()
        return redirect('setup:grades')
    return render(request, 'setup/grades.html')

# Detail View
def grade_detail(request, id):
    grade = get_object_or_404(Grade, id=id)
    return render(request, 'grade_detail.html', {'grade': grade})


# ==================================================== subjects =======================================================================
# Create
def create_subject(request):
    if request.method == 'POST':
        title = request.POST['title']
        abbrev = request.POST['abbrev']

        added_by = request.user.id
        user = User.objects.get(id=added_by) if added_by else None

        Subject.objects.create(title=title, symbol=abbrev, user_id=user.id)

        return redirect('setup:subjects')
    return render(request, 'setup/subjects.html')

# Read
def subject_list(request):
    subjects = Subject.objects.all().order_by('created_at')
    return render(request, 'setup/subjects.html', {'subjects': subjects})

# Update
def update_subject(request, id):
    subject = get_object_or_404(Subject, id=id)
    if request.method == 'POST':
        subject.title = request.POST['title']
        subject.symbol = request.POST['abbrev']
        subject.save()
        return redirect('setup:subjects')
    return render(request, 'setup/subjects.html')

# Status
def change_subject_status(request, id):
    subject = get_object_or_404(Subject, id=id)

    if request.method == 'POST':
        if subject.status == 0:
            subject.status = 1
        else:
            subject.status = 0
        subject.save()
        return redirect('setup:subjects')
    return render(request, 'setup/subjects.html')

# Delete
def delete_subject(request, id):
    subject = get_object_or_404(Subject, id=id)
    if request.method == 'POST':
        subject.delete()
        return redirect('setup:subjects')
    return render(request, 'setup/subjects.html')

# Detail View
def subject_detail(request, id):
    subject = get_object_or_404(Subject, id=id)
    return render(request, 'subject_detail.html', {'subject': subject})



# ==================================================== houses =======================================================================
# Create
def create_house(request):
    if request.method == 'POST':
        title = request.POST['title']

        added_by = request.user.id
        user = User.objects.get(id=added_by) if added_by else None

        House.objects.create(title=title, user_id=user.id)

        return redirect('setup:houses')
    return render(request, 'setup/houses.html')

# Read
def house_list(request):
    houses = House.objects.all().order_by('created_at')
    return render(request, 'setup/houses.html', {'houses': houses})

# Update
def update_house(request, id):
    house = get_object_or_404(House, id=id)
    if request.method == 'POST':
        house.title = request.POST['title']
        house.save()
        return redirect('setup:houses')
    return render(request, 'setup/houses.html')

# Status
def change_house_status(request, id):
    house = get_object_or_404(House, id=id)

    if request.method == 'POST':
        if house.status == 0:
            house.status = 1
        else:
            house.status = 0
        house.save()
        return redirect('setup:houses')
    return render(request, 'setup/houses.html')

# Delete
def delete_house(request, id):
    house = get_object_or_404(House, id=id)
    if request.method == 'POST':
        house.delete()
        return redirect('setup:houses')
    return render(request, 'setup/houses.html')

# Detail View
def house_detail(request, id):
    house = get_object_or_404(House, id=id)
    return render(request, 'house_detail.html', {'house': house})