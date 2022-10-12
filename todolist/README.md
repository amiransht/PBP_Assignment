# PBP Tugas 5 & Tugas 6

Nama : Amira Nisrina Nashita

NPM : 2106703815

Kelas : PBP - F


## LINK

[To Do List](http://amiransht.herokuapp.com/todolist)




## TUGAS 5
## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

### Internal CSS
Internal CSS adalah kode CSS yang ditulis di dalam tag `<style>` dan kode HTML dituliskan di bagian atas (header) file HTML.
Kelebihan:
1. Perubahan pada Internal CSS hanya berlaku pada satu halaman saja.
2. Class dan ID bisa digunakan oleh internal stylesheet.
Kekurangan:
1. Tidak efisien apabila Anda ingin menggunakan CSS yang sama dalam beberapa file.
2. Membuat performa website lebih lemot. Sebab, CSS yang berbeda-beda akan mengakibatkan loading ulang setiap kali Anda ganti halaman website. 

### Inline CSS
Inline CSS adalah kode CSS yang ditulis langsung pada atribut elemen HTML. Setiap elemen HTML memiliki atribut style, di situ lah inline CSS ditulis.
Kelebihan:
1. Berguna untuk memperbaiki kode dengan cepat.
2. Proses permintaan HTTP yang lebih kecil dan proses load website akan lebih cepat.
3. Sangat membantu ketika hanya ingin menguji dan melihat perubahan pada satu elemen.
Kekurangan:
1. Tidak efisien karena Inline style CSS hanya bisa diterapkan pada satu elemen HTML.

### Eksternal CSS
Eksternal CSS adalah kode CSS yang ditulis terpisah dengan kode HTML Eksternal CSS ditulis di sebuah file khusus yang berekstensi .css. 
Kelebihan:
1. Ukuran file HTML akan menjadi lebih kecil dan struktur dari kode HTML jadi lebih rapi.
2. Loading website menjadi lebih cepat
3. File CSS dapat digunakan di beberapa halaman website sekaligus. 
Kekurangan:
1. Halaman akan menjadi berantakan, ketika file CSS gagal dipanggil oleh file HTML.

##  Jelaskan tag HTML5 yang kamu ketahui.

1. `<button>`   : Creates a clickable button.
2. `<div>`      : Specifies a division or a section in a document.
3. `<form>`     : Defines an HTML form for user input.
4. `<span>`     : Defines an inline styleless section in a document.
5. `<video>`    : Embeds video content in an HTML document.
6. `<section>`  : Defines a section of a document, such as header, footer etc.
7. `<nav>`      : Defines a section of navigation links.
8. `<header>`   : Represents the header of a document or a section.
9. `<footer>`   : Represents the footer of a document or a section.
10. `<embed>`   : Embeds external application, typically multimedia content like audio or video into an HTML document.

##  Jelaskan tipe-tipe CSS selector yang kamu ketahui.

1. Tag Selector
Tag selector menggunakan tag HTML sebagai selectornya
2. ID Selector
ID selector menggunakan atribut “id” pada element HTML sebagai selectornya. Kemudian mengimplementasikannya dengan tanda pagar(#)
3. Class Selector
Class selector cara menggunakannya hampir sama dengan ID selector, namun pada class selector tentunya menggunakan atribut class pada element HTML yang akan dipilih. Diimplementasikan dengan tanda titik (.)
4. Universal Selector
Universal selector hanya ada 1 di dalam CSS, yaitu tanda bintang “*”. Selector ini bertujuan untuk ‘mencari’ semua tag yang ada.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Mendefinisikan link src bootstrap ke dalam tag `<head>`
2. Membuat struktur HTML dengan menggunakan class dan menyesuaikan bootstrap sesuai kebutuhan, untuk membuat cards pada todolist menggunakan `class="card"`
3. Mengubah style dari tampilan bootstrap dengan menambahkan Internal CSS ke dalam tag `<style>`
4. Deploy aplikasi ke Heroku


## TUGAS 6

### Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Synchronous adalah proses jalannya program secara sequential , disini yang dimaksud sequential ada berdasarkan antrian ekseskusi program. memungkinkan untuk menjalankan banyak proses secara bersamaan tanpa harus menunggu proses lain selesai.

Asynchronous adalah proses jalannya program bisa dilakukan secara bersamaan tanpa harus menunggu proses antrian. Synchronous merupakan bagian dari Asynchronous (1 antrian) dimana proses akan dieksekusi secara bersamaan dan untuk hasil tergantung lama proses suatu fungsi synchronous 

### Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Event Driven Programming merupakan paradigma pemrograman di mana objek dapat berkomunikasi secara tidak langsung dengan mengirimkan pesan satu sama lain melalui perantara. Pengiriman pesan tersebut dilakukan melalui event stream. Paradigma ini bergantung pada event dengan memperhatikan operasi apa yang akan diimplementasikan dari adanya event. Penerapan paradigma dalam tugas ini terdapat pada implementasi tombol submit form penambahan task. Apabila tombol ditekan, maka akan terdapat event yang di trigger dan ditangani oleh AJAX sebagai perantara untuk mengirim data yang diisi dari form ke server, Selain itu, AJAX akan memperbarui data pada section Todo list secara asynchronous.

### Jelaskan penerapan asynchronous programming pada AJAX.
Membuat view serta url path baru yang mereturn sebuah response JSON. Implementasi asynchronous programming AJAX dalam tugas ini terdapat pada function get serta post untuk mengambil serta mengirim data JSON ke server, serta mengatur tampilan pada Todo list secara asynchronous sesuai data yang ada pada database

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Membuat function baru yang mereturn response berupa JSON
2. Menambahkan attribute onClick pada button create task yang diintegrasikan dengan AJAX serta modals pop up
3. Menambahkan beberapa function javascript untuk melakukan get dan post request ke server
4. Memindahkan component card menjadi response dari post request AJAX dengan data pada card yang didapat dari get request.