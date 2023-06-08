from django import forms
from django.forms.utils import ValidationError
from .models import Course, Question

# class CourseForm(forms.ModelForm):
#     class Meta:
#         model = Course
#         fields = '__all__'

    
class BaseAnswerInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()

        has_one_correct_answer = False
        for form in self.forms:
            if not form.cleaned_data.get('DELETE', False):
                if form.cleaned_data.get('is_correct', False):
                    has_one_correct_answer = True
                    break
        if not has_one_correct_answer:
            raise ValidationError('Mark at least one answer as correct.', code='no_correct_answer')

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('text', )