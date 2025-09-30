from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from weasyprint import HTML
from django.utils import timezone

def home(request):
    entity_info = {
        "name": "ABENT 3T",
        "rfc": "",
        "street": "Homero 1500",
        "no_ext": "Despacho 302",
        "no_int": "Polanco Ii Seccion",
        "neighborhood": "Miguel Hidalgo",
        "municipality": "Miguel Hidalgo",
        "state": "Ciudad De Mexico",
        "zipcode": "11530",
    }
    card_expenses_summary = [
      {
        "user_id": 1,
        "card_number": "1234-5678-9012-3456",
        "card_type": "credit",
        "amount": 100.00
      },
      {
        "user_id": 1,
        "card_number": "1234-5678-9012-3456",
        "card_type": "credit",
        "amount": 100.00
      },
      {
        "user_id": 1,
        "card_number": "1234-5678-9012-3456",
        "card_type": "credit",
        "amount": 100.00
      },
      {
        "user_id": 1,
        "card_number": "1234-5678-9012-3456",
        "card_type": "credit",
        "amount": 100.00
      },
      {
        "user_id": 1,
        "card_number": "1234-5678-9012-3456",
        "card_type": "credit",
        "amount": 100.00
      },
      {
        "user_id": 1,
        "card_number": "1234-5678-9012-3456",
        "card_type": "credit",
        "amount": 100.00
      },
      {
        "user_id": 1,
        "card_number": "1234-5678-9012-3456",
        "card_type": "credit",
        "amount": 100.00
      },
      {
        "user_id": 1,
        "card_number": "1234-5678-9012-3456",
        "card_type": "credit",
        "amount": 100.00
      },
      {
        "user_id": 1,
        "card_number": "1234-5678-9012-3456",
        "card_type": "credit",
        "amount": 100.00
      },
      {
        "user_id": 1,
        "card_number": "1234-5678-9012-3456",
        "card_type": "credit",
        "amount": 100.00
      },
    ]
    movement_expenses_summary = [
      {
        "operation_date": timezone.now().date(),
        "user_id": 1,
        "card_number": "1234-5678-9012-3456",
        "establishment_name": "Store A",
        "amount": 50.00
      },
      {
        "operation_date": timezone.now().date(),
        "user_id": 1,
        "card_number": "1234-5678-9012-3456",
        "establishment_name": "Store A",
        "amount": 50.00
      },
      {
        "operation_date": timezone.now().date(),
        "user_id": 1,
        "card_number": "1234-5678-9012-3456",
        "establishment_name": "Store A",
        "amount": 50.00
      },
      {
        "operation_date": timezone.now().date(),
        "user_id": 1,
        "card_number": "1234-5678-9012-3456",
        "establishment_name": "Store A",
        "amount": 50.00
      },
      {
        "operation_date": timezone.now().date(),
        "user_id": 1,
        "card_number": "1234-5678-9012-3456",
        "establishment_name": "Store A",
        "amount": 50.00
      },
      {
        "operation_date": timezone.now().date(),
        "user_id": 1,
        "card_number": "1234-5678-9012-3456",
        "establishment_name": "Store A",
        "amount": 50.00
      },
      {
        "operation_date": timezone.now().date(),
        "user_id": 1,
        "card_number": "1234-5678-9012-3456",
        "establishment_name": "Store A",
        "amount": 50.00
      },
      {
        "operation_date": timezone.now().date(),
        "user_id": 1,
        "card_number": "1234-5678-9012-3456",
        "establishment_name": "Store A",
        "amount": 50.00
      },
      {
        "operation_date": timezone.now().date(),
        "user_id": 1,
        "card_number": "1234-5678-9012-3456",
        "establishment_name": "Store A",
        "amount": 50.00
      },
      {
        "operation_date": timezone.now().date(),
        "user_id": 1,
        "card_number": "1234-5678-9012-3456",
        "establishment_name": "Store A",
        "amount": 50.00
      },
      {
        "operation_date": timezone.now().date(),
        "user_id": 1,
        "card_number": "1234-5678-9012-3456",
        "establishment_name": "Store A",
        "amount": 50.00
      },
      {
        "operation_date": timezone.now().date(),
        "user_id": 1,
        "card_number": "1234-5678-9012-3456",
        "establishment_name": "Store A",
        "amount": 50.00
      },
      {
        "operation_date": timezone.now().date(),
        "user_id": 1,
        "card_number": "1234-5678-9012-3456",
        "establishment_name": "Store A",
        "amount": 50.00
      },
      {
        "operation_date": timezone.now().date(),
        "user_id": 1,
        "card_number": "1234-5678-9012-3456",
        "establishment_name": "Store A",
        "amount": 50.00
      },
      {
        "operation_date": timezone.now().date(),
        "user_id": 1,
        "card_number": "1234-5678-9012-3456",
        "establishment_name": "Store A",
        "amount": 50.00
      },
      {
        "operation_date": timezone.now().date(),
        "user_id": 1,
        "card_number": "1234-5678-9012-3456",
        "establishment_name": "Store A",
        "amount": 50.00
      },
      {
        "operation_date": timezone.now().date(),
        "user_id": 1,
        "card_number": "1234-5678-9012-3456",
        "establishment_name": "Store A",
        "amount": 50.00
      },
    ]
    context = {
        "start_date": timezone.now().date(),
        "end_date": timezone.now().date(),
        "entity_info": entity_info,
        "transcurred_days": 30,
        "initial_collateral": 10,
        "final_collateral": 200,
        "activated_cards": 10,
        "deposits_amount": 100,
        "refund_amount": 100,
        "devolution_amount": 100,
        "collateral_return_amount": 100,
        "receipt_amount": 100,
        "retention_amount_isr": 100,
        "retention_amount_iva": 100,
        "card_expenses_summary": card_expenses_summary,
        "movement_expenses_summary": movement_expenses_summary,
        "card_expenses_total_amount": 100,
        "movement_summary_total_amount": 100,
    }

    template = loader.get_template('cuenta/account.html')
    html = template.render(context)
    pdf = HTML(string=html).write_pdf()

    # 4. Devolver el PDF como una respuesta HTTP
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="documento.pdf"'
    return response