from django.views.generic import TemplateView,ListView
from questions.models import Question
from taggit.models import Tag


# class HomePage(TemplateView):
#     template_name = 'index.html'
#
#
#     def get_context_data(self,**kwargs):
#         questions = Question.objects.all()
#         context = super(HomePage, self).get_context_data(**kwargs)
#         context.update({'questions':posts})
#         return context

class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin,self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

class IndexPage(TagMixin,ListView):
    template_name = 'index.html'
    model = Question
    paginate_by = '10'
    queryset = Question.objects.all()
    context_object_name = 'questions'

class TagIndexView(TagMixin,ListView):
    template_name = 'index.html'
    model = Question
    paginate_by = '10'
    queryset = Question.objects.all()
    context_object_name = 'questions'

    def get_queryset(self):
        return Question.objects.filter(tags__slug=self.kwargs.get('slug'))


class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'
