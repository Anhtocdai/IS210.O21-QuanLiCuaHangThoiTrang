# from django.shortcuts import render

# Create your views here.
# views.py
from django.http import HttpResponse
from .utils import call_stored_procedure, generate_report  # Đảm bảo đúng đường dẫn

def download_report(request):
    results = call_stored_procedure()
    
    # Tạo báo cáo từ dữ liệu lấy được
    wb = generate_report(results)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=shipping_addresses_report.xlsx'

    wb.save(response)
    return response
