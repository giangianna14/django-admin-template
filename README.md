# Django Bootstrap Template

Template ini adalah starter project Django dengan integrasi Bootstrap, cocok untuk membangun aplikasi web modern dengan tampilan responsif dan fitur autentikasi lengkap.

## Fitur

✅ **Sistem Autentikasi Lengkap**
- Login dengan username/password
- **Login dengan Google OAuth2** 🆕
- Register akun baru
- **Register dengan Google OAuth2** 🆕
- Forgot Password
- Logout
- Proteksi halaman dengan login required

✅ **Template Responsif**
- Bootstrap 5 integration
- Design modern dan responsive
- Template untuk berbagai halaman
- Custom allauth templates yang sesuai dengan design

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
   pip install django django-allauth
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

7. **Setup Google OAuth2 (Opsional)**

   ```bash
   python3 setup_google_oauth.py
   ```

8. **Akses aplikasi**

   Buka browser dan akses `http://localhost:8000`

## Kredensial Login

Untuk testing, sudah tersedia akun superuser:
- **Username**: `admin`
- **Password**: `admin123`

## Endpoints

### Autentikasi
- `/login/` - Halaman login (custom)
- `/accounts/login/` - Halaman login (allauth)
- `/accounts/signup/` - Halaman register (allauth)
- `/accounts/password/reset/` - Reset password (allauth)
- `/accounts/google/login/` - Google OAuth2 login
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

## Google OAuth2 Setup

### 1. Buat Google OAuth2 Credentials

1. Buka [Google Cloud Console](https://console.cloud.google.com/)
2. Buat project baru atau pilih project yang sudah ada
3. Enable **Google+ API** atau **Google Identity API**
4. Buat **OAuth 2.0 Client ID** credentials
5. Set **Authorized redirect URI**: `http://127.0.0.1:8000/accounts/google/login/callback/`
6. Copy **Client ID** dan **Client Secret**

### 2. Konfigurasi di Django

1. Jalankan script setup:
   ```bash
   python3 setup_google_oauth.py
   ```

2. Atau setup manual via Django Admin:
   - Akses `/admin/`
   - Login sebagai superuser
   - Buka **Social Applications**
   - Tambah aplikasi baru:
     - Provider: **Google**
     - Name: **Google OAuth2**
     - Client id: `your-client-id`
     - Secret key: `your-client-secret`
     - Sites: **127.0.0.1:8000**

### 3. Testing

1. Akses `/accounts/login/` atau `/accounts/signup/`
2. Klik tombol Google
3. Login dengan akun Google
4. Akan redirect ke dashboard setelah berhasil

## Penggunaan

### Login
1. **Regular Login**: Akses `/login/` atau `/accounts/login/`
2. **Google OAuth2**: Klik tombol Google di halaman login
3. Masukkan username dan password (untuk regular login)
4. Klik "Login"
5. Jika berhasil, redirect ke dashboard

### Register
1. **Regular Register**: Akses `/register/` atau `/accounts/signup/`
2. **Google OAuth2**: Klik tombol Google di halaman register
3. Isi form: Username, Email, Password, Confirm Password (untuk regular register)
4. Klik "Register"
5. Jika berhasil, redirect ke login

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
