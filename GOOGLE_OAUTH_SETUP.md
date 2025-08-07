## 🔧 GOOGLE OAUTH CONFIGURATION SETUP

### Problem yang terjadi:
**Error**: `redirect_uri_mismatch`
**Penyebab**: URL redirect di Google Console tidak sesuai dengan yang digunakan aplikasi

### ✅ Yang sudah dikonfigurasi di aplikasi Django:
- Google Client ID: your-google-client-id.apps.googleusercontent.com  
- Google Secret: your-google-client-secret
- Site domain: 127.0.0.1:8000
- Django allauth provider: ✅ Configured

### ⚙️ YANG PERLU DIKONFIGURASI DI GOOGLE CONSOLE:

1. **Pergi ke Google Cloud Console**: https://console.cloud.google.com/
2. **Pilih project Anda** atau buat project baru
3. **Pergi ke APIs & Services > Credentials**
4. **Klik pada OAuth 2.0 Client ID yang sudah ada** (your-google-client-id.apps.googleusercontent.com)

5. **Tambahkan Authorized JavaScript origins**:
   ```
   http://127.0.0.1:8000
   http://localhost:8000
   ```

6. **Tambahkan Authorized redirect URIs**:
   ```
   http://127.0.0.1:8000/accounts/google/login/callback/
   http://localhost:8000/accounts/google/login/callback/
   ```

7. **Klik SAVE**

### 🔄 Alternatif jika tetap error:

Jika masih ada masalah, coba juga tambahkan:

**Authorized JavaScript origins**:
```
http://127.0.0.1:8000
http://localhost:8000
https://127.0.0.1:8000
https://localhost:8000
```

**Authorized redirect URIs**:
```
http://127.0.0.1:8000/accounts/google/login/callback/
http://localhost:8000/accounts/google/login/callback/
https://127.0.0.1:8000/accounts/google/login/callback/
https://localhost:8000/accounts/google/login/callback/
```

### 🧪 Test setelah konfigurasi:
1. Simpan perubahan di Google Console
2. Tunggu 5-10 menit untuk propagasi
3. Restart Django server
4. Coba login dengan Google lagi

### 📝 Notes:
- Pastikan menggunakan HTTP (bukan HTTPS) untuk development
- Domain harus exact match dengan yang di Django ALLOWED_HOSTS
- Callback URL case-sensitive, pastikan ada trailing slash "/"
