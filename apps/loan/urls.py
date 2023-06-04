from django.urls import path
from apps.loan import views

urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path('loans/', views.LoanListView.as_view(), name='loanslist'),
    path('create/loan/', views.AddLoanView.as_view(), name='create_loan'),
    path('delete/loan/<int:pk>/', views.DeleteLoan.as_view(), name='delete_loan'),
    path('agg-info/', views.AggListView.as_view(), name='agglist'),
    path('history/', views.LoanhistoryListView.as_view(), name='historylist'),
    path('inquery/', views.InqueryListView.as_view(), name='inquerylist'),
    path('results/', views.ResultListView.as_view(), name='resultlist'),
    path('calendar/', views.CalendarListView.as_view(), name='calendartlist'),
    path('bail/', views.BailListView.as_view(), name='bailtlist'),
    path('bail-type/', views.BailtypeListView.as_view(), name='bail-typelist'),
    path('loanhistories/', views.LoanhistoryListView.as_view(), name='historieslist'),

    path('create/loan-history/', views.AddLoanHistory.as_view(), name='create_loanhistory'),
    path('create/agg-info/', views.AddAgg.as_view(), name='create_agg'),
    path('create/bail/', views.AddBail.as_view(), name='create_bail'),
    path('create/inquery/', views.AddInquery.as_view(), name='create_inquery'),
    path('create/calendar/', views.AddCalendar.as_view(), name='create_calendar'),

    path('loan/<int:pk>/', views.LoanDetailView.as_view(), name='loan-detail'),
    path('loanhistories/<int:pk>/', views.LoanHistoryDetailView.as_view(), name='loanhistories-detail'),
    path('agg-info/<int:pk>/', views.AggDetailView.as_view(), name='agg-detail'),
    path('bail/<int:pk>/', views.BailDetailView.as_view(), name='bail-detail'),

    path('loan/<int:pk>/update/', views.LoanUpdateView.as_view(), name='loan-update'),
    path('loanhistories/<int:pk>/update/', views.LoanHistoryUpdateView.as_view(), name='loan_history-update'),
    path('agg-info/<int:pk>/update/', views.AggUpdateView.as_view(), name='agg-update'),

]
