# Django Bootstrap Template

Template ini adalah starter project Django dengan integrasi Bootstrap, cocok untuk membangun aplikasi web modern dengan tampilan responsif dan fitur autentikasi lengkap.

## Fitur

✅ **Sistem Autentikasi Lengkap**
- Login dengan username/password
- Register akun baru
- Forgot Password
- Logout
- Proteksi halaman dengan login required

✅ **Template Responsif**
- Bootstrap 5 integration
- Design modern dan responsive
- Template untuk berbagai halaman

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
   pip install django
   ```

4. **Migrasi database**

   ```bash
   python3 manage.py migrate
   ```

5. **Buat superuser (opsional)**

   ```bash
   python3 manage.py createsuperuser
   ```

6. **Jalankan server**

   ```bash
   python3 manage.py runserver
   ```

7. **Akses aplikasi**

   Buka browser dan akses `http://localhost:8000`

## Kredensial Login

Untuk testing, sudah tersedia akun superuser:
- **Username**: `admin`
- **Password**: `admin123`

## Endpoints

### Autentikasi
- `/login/` - Halaman login
- `/register/` - Halaman register
- `/forget-password/` - Halaman forgot password
- `/logout/` - Logout (redirect ke login)

### Dashboard
- `/dashboard/` - Dashboard utama (login required)
- `/` - Landing page

## Struktur Folder

- `my_app/` : Folder utama aplikasi Django
  - `forms.py` : Form untuk login, register, forgot password
  - `views.py` : Logic untuk autentikasi dan halaman
  - `urls.py` : URL routing
  - `settings.py` : Konfigurasi Django
- `assets/` : Berisi file statis seperti CSS, JS, gambar, font
- `templates/` : Berisi file HTML template
  - `layout/` : Base templates
  - `login.html` : Template login
  - `register.html` : Template register
  - `forget-password.html` : Template forgot password

## Penggunaan

### Login
1. Akses `/login/`
2. Masukkan username dan password
3. Klik "Login"
4. Jika berhasil, redirect ke dashboard

### Register
1. Akses `/register/`
2. Isi form: First Name, Last Name, Username, Email, Password, Confirm Password
3. Klik "Register"
4. Jika berhasil, redirect ke login

### Forgot Password
1. Akses `/forget-password/`
2. Masukkan email
3. Klik "Send"
4. Pesan konfirmasi akan ditampilkan

### Logout
1. Akses `/logout/` atau klik tombol logout
2. Session akan dihapus dan redirect ke login

## Konfigurasi

- File konfigurasi utama: `my_app/settings.py`
- URL login: `/login/`
- Redirect setelah login: `/dashboard/`
- Redirect setelah logout: `/login/`

## Referensi

- Dokumentasi Django: https://docs.djangoproject.com/
- Dokumentasi Bootstrap: https://getbootstrap.com/
- Dokumentasi template: https://trezo-docs.envytheme.com/docs/getting-started/installation/django

---

Template ini dapat dikembangkan sesuai kebutuhan proyek Anda dengan fitur autentikasi yang sudah lengkap dan siap pakai.
