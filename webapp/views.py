from django.shortcuts import render
from django.views import generic

from .forms import IndexForm
from .utils import save_image, predict

# class IndexView(generic.FormView):
#     template_name = 'webapp/index.html'
#     form_class = IndexForm
#     success_url = '/result/'

#     def form_valid(self, form):
#         form.send_picture()
#         return super().form_valid(form)

def index(request):
    if request.method == 'POST':
        print("OK")
        form = IndexForm(request.POST, request.FILES)
        if form.is_valid():
            img = save_image(request.FILES['image'])
            pred = predict(img)
            return render(request, 'webapp/result.html', {'pred': pred})

    else:
        form = IndexForm()

    return render(request, 'webapp/index.html', {'form': form})

def result(request):
    return render(request, 'webapp/result.html')