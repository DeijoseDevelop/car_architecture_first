# architechture


## Getting started

1. Clone repository

    ```git clone https://github.com/DeijoseDevelop/car_architecture_first.git```

2. Open project folder

    ```cd car_architecture_first```

3. Create tables into database

   3.1. ```sudo docker-compose up --build```

   3.2. ```sudo docker exec architechture_web /code/make_migrations.sh```

    **if the file make_migrations.sh gives permission error run this command:**

    ```sudo chmod 777 make_migrations.sh```

4. Create an user

    ```sudo docker exec -t architechture_web python manage.py createsuperuser```



### Important URLs

1. Admin

    http://localhost:8000/admin/

2. Scrapper and Importer

    http://localhost:8000/home/
