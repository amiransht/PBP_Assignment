# PBP Tugas 3

Nama : Amira Nisrina Nashita

NPM : 2106703815

Kelas : PBP - F


## LINK

[HTML](http://tugas3-amiransht.herokuapp.com/mywatchlist/html/)
[XML](http://tugas3-amiransht.herokuapp.com/mywatchlist/xml/)
[JSON](http://tugas3-amiransht.herokuapp.com/mywatchlist/json/)

## Perbedaan antara JSON, XML, HTML

### JSON
 - Data disimpan dengan format text dalam JavaScript Object
 - Menyimpan data dengan efisien tetapi tidak rapi untuk dilihat
 - JSON digunakan untuk mengirimkan data dengan cara data diuraikan dan dikirimkan melalui internet
 - Hanya mendukung data bertipe primitif
 - Tidak dapat melakukan pemrosesan ataupun perhitungan pada data
 - Size dari file json relatif lebih kecil sehingga lebih cepat dalam mentransfer data

### XML
- XML merupakan bahasa markup
- Menyimpan data secara terstruktur, mudah dibaca, tetapi kurang efisien
- Mendukung banyak tipe data kompleks seperti charts, bagan, dan data non primitif.
- Dapat melakukan pemrosesan serta pemformatan dokumen dan object
- Size dari file xml relatif lebih besar sehingga lebih lambat dalam mentransfer data

### HTML
- HTML merupakan bahasa markup
- Berguna untuk menampilkan data
- Dapat melakukan pemrosesan serta pemformatan data atau object


## Fungsi data delivery dalam pengimplementasian sebuah platform

Data delivery dapat memberikan manfaat yang signifikan ke dalam industri aplikasi seperti membuat aplikasi menjadi dinamis dan lebih interaktif, adanya data delivery membuat aplikasi-aplikasi pada sebuah platform dapat berkomunikasi serta bertukar informasi satu sama lain.

## Implementasi Poin 1-3

1. Membuat aplikasi baru bernama `mywatchlist` dengan menjalankan perintah
    `python manage.py startapp mywatchlist`

2. Mendaftarkan aplikasi ke dalam **INSTALLED_APPS** di file `settings.py`
    ```shell
    INSTALLED_APPS = [
    .....,
    .....,
    'mywatchlist',
    ]
    ```

3. Buat model dalam file `models.py` pada folder `mywatchlist` dengan variabel:
    - watched (BooleanField)
    - title (TextField)
    - rating (FloatField)
    - release_date (TextField)
    - review (TextField)

4. Menjalankan perintah
    ```shell
    python manage.py makemigrations
    python manage.py migrate
    ```
5. Membuat data review film dalam format json pada folder `fixtures` dengan nama file `initial_mywatchlist_data.json`

6. Mengisi 10 data film yang akan di review dalam file json tersebut, contoh:
    ```shell
    {
        "model": "mywatchlist.mywatchlist",
        "pk": 1,
        "fields": {
            "watched": true,
            "title": "Mencuri Raden Saleh",
            "rating": 4.5,
            "release_date": "2022",
            "review": "This movie was a lot better than I expected. At first I thought it would be a bit cheesy especially looking at the cast that consisted of young actors and actresses. But as I continued watching, it was surprisingly good with some smooth transition between one plot to another and a wonderful story telling with some excitement throughout the movie."
        }
    }, ...
    ```
7. Selanjutnya loaddata json menggunakan perintah
    `python manage.py loaddata initial_mywatchlist_data.json`

8. Dalam file `views.py` pada folder `mywatchlist` buat fungsi-fungsi untuk menampilkan data dalam format html, json, dan xml
    ```shell
    def show_html(request):
        .........
    def show_xml(request):
        .........
    def show_json(request):
        .........
    ```

9. Membuat folder `template` di dalam folder `mywatchlist` berisi film html untuk menampilkan data

10. Tambahkan path url dengan membuat file `urls.py` di dalam folder `mywatchlist` dan isi dengan path untuk melakukan routing ke fungsi-fungsi yang ada fi `views.py`
    ```shell
    from mywatchlist.views import show_html
    from mywatchlist.views import show_xml 
    from mywatchlist.views import show_json

    app_name = 'mywatchlist'

    urlpatterns = [
        path('', show_html, name='show_html'),
        path('html/', show_html, name='show_html'),
        path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'),
    ]
    ```

11. Daftarkan app `mywatchlist` ke dalam url pattern pada file `urls.py` di folder `project_django`
    ```shell
    urlpatterns = [
    .........,
    path('mywatchlist/', include('mywatchlist.urls')),
    .........,
    ]
    ```

12. Deploy ke Heroku dengan mendaftarkan nama aplikasi heroku ke secrets github

## Postman

![HTML](/assets/postman_html.png)
![JSON](/assets/postman_json.png)
![XML](/assets/postman_xml.png)

    

