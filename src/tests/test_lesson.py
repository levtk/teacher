from datetime import date, timedelta
import logging
from uuid import uuid4
from lesson.lesson import Lesson, Level, Exercise
import pytest

def test_lesson():
    today = date.today() 
    date_due = today + timedelta(days=5)
    l = Lesson(id=uuid4(), instructor_id=uuid4(), level=Level.A1, title="Fist lesson", language="Spanish",assigned_to=['dave'],
               assigned_on=today,due_by=date_due, exercises=list[Exercise])
    assert l.due_by > l.assigned_on
    
    


