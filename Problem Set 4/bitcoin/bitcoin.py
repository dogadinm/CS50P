from requests import get
import json
import sys


if len(sys.argv) != 2:
    print('Missing command-line argument')
    sys.exit(1)
else:
    request = get('https://api.coindesk.com/v1/bpi/currentprice.json')
    try:
        float(sys.argv[1])
    except ValueError:
        print('Commaind line argument is not a number')
        sys.exit(1)
        
    info = request.json()
    price = info['bpi']['USD']['rate_float']
    total_price = float(price) * float(sys.argv[1])
    print(f'${total_price:,.4f}')

