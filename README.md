# PBP Tugas 2

Nama : Amira Nisrina Nashita

NPM : 2106703815

Kelas : PBP - F



## LINK

[Link Deployment](http://tugas2-amiransht.herokuapp.com/katalog)

## Soal

1. **Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut**
   **kaitan antara urls.py, views.py, models.py, dan berkas html;**

   ![Bagan](/assets/images/bagan.jpeg)

   1) Client akan melakukan request ke sistem dengan cara mengakses URL yang tersedia, 
      melalui framework Django untuk masuk ke environment 
   2) Jika URL tersedia pada urls.py, urls.py akan melakukan routing dan mapping kepada views.py. 
      Argumen urls.py nantinya akan diekstraksi dan dikirim ke views.py
   3) Dalam views.py, terdapat fungsi yang terkait dengan template html dan models.py. 
      Objek-objek akan dipanggil melalui models.py ke views.py. Data-data objek yang telah diekstrak 
      oleh models.py akan ditampilkan oleh fungsi dalam views.py menggunakan template html. 
   4) Ketika file html di request oleh views.py untuk menampilkan data, pemanggilan file html ini 
      juga akan disertai dengan konteks data yang akan ditampilkan. 
      Pastinya, variabel yang ada pada file html harus disesuaikan dengan konteks
   5) Ketika konsep MVT dari views.py, models.py, dan file html telah dijalankan, 
      client akan menerima respon dari request pertama berupa tambilan website

2. **Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web** 
   **berbasis Django tanpa menggunakan virtual environment?**

   Virtual environment digunakan untuk membangun ekskulisifitas antar beberapa orang yang membangun sebuah aplikasi website. Hal ini dilakukan untuk memastikan bahwa aplikasi website yang kita buat dapat berjalan dengan baik pada sistem operasi yang sama, meskipun pada dependencies yang berbeda - beda. 

3. **Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.**
   Pertama, buat fungsi bernama show_katalog dengan menggunakan variabel request yang dipanggil jika client mengakses URL. Dalam fungsi, terdapat data yang berasal dari file .json ditambah dengan nama dan npm. Funngsi ini mereturn request dari template htm yang diisi dengan data tersebut.

   Daftarkan nama routing yang akan digunakan yaitu "katalog/". Daftarkan nama aplikasi pada route ini dengan nama 'katalog', selanjutnya daftarkan nama route tadi pada urlpatterns dengan memanggil fungsi katalog dari views.py untuk ditampilkan. Kemudian daftarkan nama aplikasi di program utama yaitu sttings.py dan urls.py di project_django

   Setelah views.py, models.py, dan urls.py telah selesai untuk dikonfigurasi, cocokkan data dalam fungsi views.py dengan template html yang tersedia. Gunakan bracker {{}} untuk memanggil data dari fungsi.

   Setelah semua konfigurasi selesai, tambahkan file dpl.yml untuk konfigurasi Heroku dan tambahkan PROJECT_ROOT & STATIC_ROOT di settings.py project_django. Setelah selesai, deploy pada website dengan melakukan push ke repository yang telah dibuat. 

   Buat aplikasi di Heroku dengan nama tugas2-amiransht, masukkan API Key dan nama aplikasi ke dalam secrets pada repository github.



