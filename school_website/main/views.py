from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View
from .forms import RegistrationForm, PostForm
from .models import Student, Post, Teacher, Category
from django.views.generic import ListView,DetailView,CreateView,TemplateView,UpdateView


class Homepage(ListView):
    model = Student 
    template_name = 'homepage.html'


class RegistrationView(View):
    template_name = 'registration/signup.html'

    def get(self, request):
        form = RegistrationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            student = Student.objects.create(
                user=user,
                strand=form.cleaned_data['strand'],
                grade_level=form.cleaned_data['grade_level']
            )
            login(request, user)
            return redirect('homepage')
        return render(request, self.template_name, {'form': form})



class Details(DetailView):
    model = Post
    template_name = 'details.html'

class CategoryDetailView(DetailView):
    model = Category 
    template_name = 'category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Filter posts based on the category or subject associated with the current view
        context['posts'] = Post.objects.filter(category=self.object)  # You can use 'subject' here too if needed
        
        return context



class Physics(ListView):
    model = Post
    template_name = '12_stem/physics.html'



def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.user, request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

            teacher = Teacher.objects.get(teacher=request.user)
            chosen_subject = post.subject

            try:
                category = Category.objects.get(subject=chosen_subject)
            except Category.DoesNotExist:
                return render(request, 'error.html', {'error_message': 'Category not found for the chosen subject'})

            post.category = category
            post.save()
            return redirect('homepage')
    else:
        form = PostForm(request.user)
    return render(request, 'post.html', {'form': form})
