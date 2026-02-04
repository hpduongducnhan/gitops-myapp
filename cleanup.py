import os
import django
import sys

sys.path.append('/home/nhan/Projects/SvrManager/apps/my-app')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')
django.setup()

from shop.models import Category, Product, Page

print("Cleaning up old Tay Ninh data...")

# Slugs to delete
product_slugs = [
    'muoi-ot-tay-ninh', 'muoi-tom-tay-ninh', 'muoi-tieu-tay-ninh',
    'muoi-rang-tay-ninh', 'muoi-sate-tay-ninh', 'muoi-toi-ot-tay-ninh',
    'muoi-me-rang-tay-ninh', 'muoi-vung-den-tay-ninh', 'muoi-ot-xanh-tay-ninh',
    'banh-trang-tron-tay-ninh', 'banh-trang-nuong-mam-ruoc', 'banh-trang-phoi-suong',
    'banh-trang-dua-non', 'banh-trang-me-den', 'banh-trang-toi-phi',
    'banh-trang-cuon', 'banh-trang-tom-tuoi', 'banh-trang-sua'
]

# Delete Products
products = Product.objects.filter(slug__in=product_slugs)
print(f"Deleting {products.count()} products")
products.delete()

# Delete Categories (Cascade should delete products)
cats = Category.objects.filter(slug__in=['muoi-tay-ninh', 'banh-trang-tay-ninh'])
print(f"Deleting {cats.count()} categories")
cats.delete()

# Delete Pages
pages = Page.objects.filter(slug__in=['gioi-thieu', 'lien-he'])
print(f"Deleting {pages.count()} pages")
pages.delete()

print("Cleanup done.")
