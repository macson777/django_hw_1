from django.http import HttpResponse

# Create your views here.


def index2(request):
   date = request.POST.get('date')
   date = date.split('/')
   if len(date[0]) > 2:
       year = date[0]
       month = date[1]
       day = date[2]
   else:
       year = date[2]
       month = date[1]
       day = date[0]

   if str(day) == '01' and str(month) == '01':
       return HttpResponse(f'Happy New {year} Year')
   else:
       return HttpResponse(f'{year}/{month}/{day}')





