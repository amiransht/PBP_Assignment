# PBP Tugas 4

Nama : Amira Nisrina Nashita

NPM : 2106703815

Kelas : PBP - F


## LINK

[To Do List](http://amiransht.herokuapp.com/todolist)

## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen?

`{% csrf_token %}` berfungsi untuk menjamin keamanan user dan site agar tidak terkena serangan dari pihak eksternal. Selain itu DJango mengharuskan adanya token tersebut pada pembuatan form. 

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

Ya. Jika membuat form sebagai object kemudian mengisi input fields secara manual pada HTML, maka form dapat dibuat.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

browser akan meresponse dengan mengirm POST ke server saat user membuat request dengan cara menekan button login, register, tambah task, dll. Kemudian akan terdapat perubahan pada server dengan adanya event POST. Setelah itu views.py akan merespon dengan mereturn atau mengupdate data dengan melakukan user redirect ke views sebelumnya sehingga tampilan akan mengupdate data baru. 

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Membuat aplikasi baru bernama `todolist` dengan menjalankan perintah
    `python manage.py startapp todolist`

2. Mendaftarkan aplikasi ke dalam **INSTALLED_APPS** di file `settings.py`
    ```shell
    INSTALLED_APPS = [
    .....,
    .....,
    'todolist',
    ]
    ```

3. Buat model dalam file `models.py` pada folder `todolist` dengan variabel:
    - user 
    - date 
    - title 
    - description 

4. Menjalankan perintah
    ```shell
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Membuat fungsi-fungsi yang dibutuhkan pada `views.py`:
    ```shell
    def register(request):
        ......
    def login_user(request):
        ......
    def logout_user(request):
        ......
    @login_required(login_url='/todolist/login/')
    def create(request):
        ......
    def delete(request, title):
        ......
    ```

6. Membuat folder `template` di dalam folder `todolist` berisi file-file html yang dibutuhkan menampilkan data

7. Tambahkan path url dengan membuat file `urls.py` di dalam folder `todolist` dan isi dengan path untuk melakukan routing ke fungsi-fungsi yang ada fi `views.py`
    ```shell
    from django.urls import path
    from todolist.views import delete, register, login_user, logout_user, show_todos, create, delete

    app_name = 'todolist'

    urlpatterns = [
        path('', show_todos, name='show_todos'),
        path('create/', create,  name='create'),
        path('register/', register, name='register'),
        path('login/', login_user, name='login'),
        path('logout/', logout_user, name='logout'),
        path('delete/<str:task_titile>/', delete, name="delete"),
        
    ]

    ```

8. Daftarkan app `todolist` ke dalam url pattern pada file `urls.py` di folder `project_django`
    ```shell
    urlpatterns = [
    .........,
    path('todolist/', include('todolist.urls')),
    .........,
    ]
    ```



