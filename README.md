# Django Products App

Bu proje, Django REST Framework ile geliştirilmiş bir ürün yönetim API'si ve React ile yazılmış bir frontend arayüzünden oluşmaktadır.

## 🚀 Özellikler

### Backend (Django)
- JWT Authentication (djangorestframework-simplejwt)
- PostgreSQL veritabanı desteği
- CRUD işlemleri (Ürün oluşturma, listeleme, güncelleme, silme)
- Yetkilendirme (Sadece owner olan kullanıcılar ürünlerini düzenleyebilir)
- Temel test altyapısı (`unittest` ile)

### Frontend (React)
- Login / Logout işlemleri
- Ürün listeleme ve ekleme formu
- TailwindCSS ile stil düzenlemeleri

## 🛠 Kurulum

### 1. Backend

```bash
cd django-api-project
python -m venv venv
source venv/Scripts/activate  # Windows için
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

### Giriş yap
{
  "username": "your_username",
  "password": "your_password"
}

### 2. Frontend
cd frontend/django-products-frontend
npm install
npm start

python manage.py test
## 📁 Dosyalar

django-api-project/
│
├── products/           # API app'i
├── users/              # Custom kullanıcı işlemleri
├── manage.py
├── frontend/
│   └── django-products-frontend/  # React frontend


