from django.test import TestCase
import pytest
from scheduleapp.models import Teacher


@pytest.fixture
def new_teacher(db):
    teacher = Teacher.objects.create(
        name='First_test_teacher',
    )
    return teacher


def test_search_teachers(new_teacher):
    assert Teacher.objects.filter(name='First_test_teacher').exists()

def test_update_teacher(new_teacher):
    new_teacher.name = 'First_test_teacher_renamed'
    new_teacher.save()
    assert Teacher.objects.filter(name='First_test_teacher_renamed').exists()


@pytest.fixture
def another_teacher(db):
    teacher = Teacher.objects.create(
        name = 'Second_test_teacher',
    )
    return teacher

def test_compare_teachers(new_teacher, another_teacher):
    assert new_teacher.pk != another_teacher.pk