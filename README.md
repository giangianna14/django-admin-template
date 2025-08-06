# Django Bootstrap Template

Template ini adalah starter project Django dengan integrasi Bootstrap, cocok untuk membangun aplikasi web modern dengan tampilan responsif.

## Instalasi

1. **Clone repository**

   ```bash
   git clone <url-repo-anda>
   cd django-bootstrap
   ```

2. **Buat dan aktifkan virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Migrasi database**

   ```bash
   python manage.py migrate
   ```

5. **Jalankan server**

   ```bash
   python manage.py runserver
   ```

6. **Akses aplikasi**

   Buka browser dan akses `http://localhost:8000`

## Struktur Folder

- `my_app/` : Folder utama aplikasi Django
- `assets/` : Berisi file statis seperti CSS, JS, gambar, font
- `templates/` : Berisi file HTML template
- `manage.py` : File utama untuk menjalankan perintah Django

## Konfigurasi

- Pastikan variabel lingkungan `DJANGO_SETTINGS_MODULE` sudah mengarah ke `my_app.settings`.
- Untuk deployment, sesuaikan pengaturan di `settings.py` sesuai kebutuhan produksi.

## Referensi

- Dokumentasi Django: https://docs.djangoproject.com/
- Dokumentasi Bootstrap: https://getbootstrap.com/
- Dokumentasi template: https://trezo-docs.envytheme.com/docs/getting-started/installation/django

---

Template ini dapat dikembangkan sesuai kebutuhan proyek Anda.
