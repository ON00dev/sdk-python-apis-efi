# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'id': 1
}

body = {
    'items': [{
        'name': 'Product 1',
        'value': 1000,
        'amount': 2
    }],
    'payment': {
        'credit_card': {
            'payment_token': '5cffb658d047093b3fbdf7eff8c434c3d26a4bd1',
            'billing_address': {
                'street': 'Av. JK',
                'number': 909,
                'neighborhood': 'Bauxita',
                'zipcode': '35400000',
                'city': 'Ouro Preto',
                'state': 'MG'
            },
            'customer': {
                'name': 'Gorbadoc Oldbuck',
                'email': 'oldbuck@efipay.com.br',
                'cpf': '94271564656',
                'birth': '1977-01-15',
                'phone_number': '5144916523'
            }
        }
    }
}

response = efi.create_one_step_subscription(params=params, body=body)
print(response)
