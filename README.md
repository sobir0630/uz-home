# 🏡 UzHome — Eʼlonlar Platformasi

UzHome — bu foydalanuvchilar uchun qulay va xavfsiz **ko‘chmas mulk va umumiy eʼlonlar platformasi**. Loyiha Django asosida yozilgan bo‘lib, real loyiha sifatida ishlab chiqilgan va production muhitga tayyor.

---

## 🚀 Asosiy imkoniyatlar

### 👤 Foydalanuvchi funksiyalari

* Ro‘yxatdan o‘tish (username, email, password)
* Login / Logout (Session authentication)
* Foydalanuvchi profili
* Foydalanuvchini **active / inactive** holatda boshqarish
* Superuser va admin panel

---

### 📢 Eʼlonlar (Announcements)

* Eʼlon qo‘shish
* Eʼlonlarni tahrirlash va o‘chirish
* Barcha eʼlonlarni ko‘rish
* Faqat `published` holatdagi eʼlonlarni ko‘rsatish
* Eʼlonlar kategoriya va joylashuv bo‘yicha

---

### 🔐 Xavfsizlik

* Django Session Authentication
* Login talab qilinadigan sahifalar
* CSRF himoyasi
* `.env` orqali maxfiy sozlamalar

---

### 🧪 Testlar

Loyihada **unit testlar** yozilgan:

* Login testi
* User modeli testlari
* Eʼlon qo‘shish testi
* Eʼlonlarni ko‘rsatish testlari

Testlarni ishga tushirish:

```bash
python manage.py test
```

---

## 🛠 Texnologiyalar

* **Backend:** Django
* **Database:** PostgreSQL
* **Containerization:** Docker & Docker Compose
* **Auth:** Django Session Auth
* **Tests:** Django TestCase

---

## 🐳 Docker orqali ishga tushirish

### 1️⃣ `.env` fayl yarating

```env
SECRET_KEY=your-secret-key
DEBUG=False
DB_NAME=uzhome
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

---

### 2️⃣ Containerlarni ishga tushirish

```bash
docker compose build
docker compose up -d
```

---

### 3️⃣ Migration va admin

```bash
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

---

## 📂 Loyihaning tuzilishi

```
UzHome/
│── add_page/        # Eʼlon qo‘shish
│── show_page/       # Eʼlonlarni ko‘rsatish
│── users/           # User va auth
│── templates/       # HTML sahifalar
│── static/          # Static fayllar
│── media/           # Yuklangan rasmlar
│── Dockerfile
│── docker-compose.yml
│── requirements.txt
│── README.md
```

---

## 🌍 Production tayyorligi

* Docker bilan deploy
* PostgreSQL bilan ishlash
* Nginx + Gunicorn ulash mumkin
* HTTPS (Let’s Encrypt) qo‘llab-quvvatlanadi

---

## 👨‍💻 Muallif

**Sobirjon Mamasoliyev**
Python / Django Developer

📌 Loyiha portfoliya va real loyiha sifatida ishlab chiqilgan.

---

## ⭐ Yakuniy so‘z

UzHome — bu faqatgina o‘quv loyihasi emas, balki **real hayotda ishlashga tayyor platforma**. Kod tozaligi, testlar va Docker qo‘llanilgani uni professional darajaga olib chiqadi.

Agar loyiha yoqsa ⭐ bosing va rivojlantirishda davom eting 🚀
