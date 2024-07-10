from django.http import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "singlepageapp/index.html")

# The texts are much longer in reality, but have
# been shortened here to save space
texts = ["Lorem ipsum dolor sit amet consectetur adipisicing elit. Facere earum minima distinctio qui exercitationem maiores adipisci quis fugiat tempore quos quia quisquam voluptas iste blanditiis in similique culpa, veritatis, assumenda placeat. Minima alias iure accusamus rem nihil ipsa sunt suscipit facere dolore fugiat! Id, beatae tempore pariatur perspiciatis libero doloremque?", "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Repellendus, molestiae sed quos nesciunt dolorem earum explicabo error sapiente a at sit officia mollitia quae alias, fuga numquam asperiores? Neque iste, pariatur odio voluptatum delectus quis dolor laborum iusto similique reprehenderit!", "    Lorem ipsum dolor sit amet consectetur adipisicing elit. Magni quae nobis porro fuga totam quia architecto velit adipisci laborum, eum deserunt maiores et ratione, incidunt ducimus placeat possimus, delectus sed quidem? Voluptate nulla tempora, mollitia corporis, voluptatem, vero magnam reprehenderit deserunt dolores labore iste ipsa?"]

def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("No such section")
    
def scroll(request):
    return render(request, "singlepageapp/scroll.html")