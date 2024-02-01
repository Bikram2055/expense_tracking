from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Record, Category, Expenses
from .forms import RecordForm, CategoryForm, ExpensesForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime, timedelta
from django.db.models import Sum
from django.views.generic import TemplateView
from rest_framework.views import APIView, Response
from .serializer import RecordSerializer


# Create your views here.

class IndexView(View):
    
    template = 'index.html'
    def get(self, request):
        data = []
        if request.user.id:
            user = request.user
            records = Record.objects.filter(user=user)
            data = [r.name for r in records]
        # monthly expenses
            current_month = datetime.now().month
            current_year = datetime.now().year
            monthly_expenses = Expenses.objects.filter(date__month=current_month, date__year=current_year)
            total_monthly_amount = monthly_expenses.aggregate(Sum('amount'))['amount__sum']
            
            yearly_expenses = Expenses.objects.filter(date__year=current_year)
            total_yearly_amount = yearly_expenses.aggregate(Sum('amount'))['amount__sum']
            # weekly expenses
            current_date = datetime.now().date()
            start_of_week = current_date - timedelta(days=current_date.weekday())
            end_of_week = start_of_week + timedelta(days=6)
            weekly_expenses = Expenses.objects.filter(date__range=[start_of_week, end_of_week])
            total_weekly_amount = weekly_expenses.aggregate(Sum('amount'))['amount__sum']
            context = {
                "url": 1,
                "record": data,
                "total_montly_amount": total_monthly_amount,
                "total_weekly_amount": total_weekly_amount,
                "total_yearly_amount": total_yearly_amount,
            }
            return render(request, self.template, context)
        return render(request, self.template)
    
    
class ExpenseView(LoginRequiredMixin, View):
    
    form = ExpensesForm
    template = 'index.html'
    def get(self, request):
        return render(request, self.template, {"form": self.form})
    
    def post(self, request):
        form = self.form(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Success</h1>")
        messages.error("form not submitted !")
        return render(request, self.template, {"form": self.form})
    
    
class RecordView(LoginRequiredMixin, View):
    
    form = RecordForm
    template = 'index.html'
    def get(self, request):
        return render(request, self.template, {"form": self.form})
    
    def post(self, request):
        form = self.form(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save(user=request.user)
            return HttpResponse("<h1>Success</h1>")
        messages.error("form not submitted !")
        return render(request, self.template, {"form": self.form})

    

class CategoryView(LoginRequiredMixin, View):
    
    form = CategoryForm
    template = 'index.html'
    def get(self, request):
        return render(request, self.template, {"form": self.form})
    
    def post(self, request):
        form = self.form(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Success</h1>")
        messages.error("form not submitted !")
        return render(request, self.template, {"form": self.form})


class Home(TemplateView):
    template_name = "home.html"
    
    
class APiV(APIView):
    
    def get(self, request):
        
        records = Record.objects.all()
        data = RecordSerializer(records, many=True)
        return Response(data.data)