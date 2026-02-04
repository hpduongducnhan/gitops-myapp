import os
import django
import sys

# Add project root to path
sys.path.append('/home/nhan/Projects/SvrManager/apps/my-app')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')
django.setup()

from shop.models import Product

try:
    count = Product.objects.count()
    print(f"Total Products: {count}")
    
    slugs = ['muoi-ot-tay-ninh', 'banh-trang-tron-tay-ninh']
    for s in slugs:
        p = Product.objects.filter(slug=s).first()
        if p:
            print(f"Product: {p.name}")
            print(f"Image: {p.image}")
        else:
            print(f"Product {s} not found")

except Exception as e:
    print(f"Error: {e}")
