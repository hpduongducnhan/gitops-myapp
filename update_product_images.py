import os
import django
import sys

# Add project root to path
sys.path.append('/home/nhan/Projects/SvrManager/apps/my-app')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')
django.setup()

from shop.models import Product

# Define product to image mappings for Tay Ninh products
product_image_map = {
    # Existing products
    'muoi-ot-tay-ninh': 'products/muoi-ot-tay-ninh.png',
    'banh-trang-tron-tay-ninh': 'products/banh-trang-tron-tay-ninh.png',
    
    # Additional Tay Ninh products (if they exist)
    'muoi-me-rang-tay-ninh': 'products/muoi-me-rang-tay-ninh.png',
    'muoi-ot-xanh-tay-ninh': 'products/muoi-ot-xanh-tay-ninh.png',
    'muoi-rang-tay-ninh': 'products/muoi-rang-tay-ninh.png',
    'muoi-sate-tay-ninh': 'products/muoi-sate-tay-ninh.png',
    'muoi-tieu-tay-ninh': 'products/muoi-tieu-tay-ninh.png',
    'muoi-toi-ot-tay-ninh': 'products/muoi-toi-ot-tay-ninh.png',
    'muoi-tom-tay-ninh': 'products/muoi-tom-tay-ninh.png',
    'muoi-vung-den-tay-ninh': 'products/muoi-vung-den-tay-ninh.png',
    'banh-trang-dua-non': 'products/banh-trang-dua-non.png',
    'banh-trang-nuong-mam-ruoc': 'products/banh-trang-nuong-mam-ruoc.png',
    'banh-trang-phoi-suong': 'products/banh-trang-phoi-suong.png',
}

try:
    print("Đang cập nhật hình ảnh cho sản phẩm...\n")
    updated_count = 0
    not_found_count = 0
    
    for slug, image_path in product_image_map.items():
        try:
            product = Product.objects.get(slug=slug)
            product.image = image_path
            product.save()
            print(f"✓ Đã cập nhật: {product.name} -> {image_path}")
            updated_count += 1
        except Product.DoesNotExist:
            print(f"✗ Không tìm thấy sản phẩm: {slug}")
            not_found_count += 1
    
    print(f"\n{'='*60}")
    print(f"Tổng kết:")
    print(f"  - Sản phẩm đã cập nhật: {updated_count}")
    print(f"  - Sản phẩm không tìm thấy: {not_found_count}")
    print(f"{'='*60}\n")
    
    # Kiểm tra kết quả
    print("Kiểm tra kết quả:\n")
    products_with_images = Product.objects.exclude(image='').exclude(image=None)
    for p in products_with_images[:5]:  # Show first 5
        print(f"  {p.name}: {p.image}")
    
    print(f"\nTổng số sản phẩm có hình ảnh: {products_with_images.count()}")
    
except Exception as e:
    print(f"Lỗi: {e}")
    import traceback
    traceback.print_exc()
