#!/usr/bin/env bash

./manage.py migrate
./manage.py loaddata airline/fixtures/aircrafts.json
./manage.py loaddata airline/fixtures/countries.json
./manage.py loaddata airline/fixtures/regions0.json
./manage.py loaddata airline/fixtures/regions1.json
./manage.py loaddata airline/fixtures/regions2.json
./manage.py loaddata airline/fixtures/regions3.json
./manage.py loaddata airline/fixtures/cities0.json
./manage.py loaddata airline/fixtures/cities1.json
./manage.py loaddata airline/fixtures/cities2.json
./manage.py loaddata airline/fixtures/cities3.json
./manage.py loaddata airline/fixtures/cities4.json
./manage.py loaddata airline/fixtures/cities5.json
./manage.py loaddata airline/fixtures/cities6.json
./manage.py loaddata airline/fixtures/cities7.json
./manage.py loaddata airline/fixtures/cities8.json
./manage.py loaddata airline/fixtures/cities9.json
./manage.py loaddata airline/fixtures/cities10.json
./manage.py loaddata airline/fixtures/cities11.json
./manage.py loaddata airline/fixtures/cities12.json
./manage.py loaddata airline/fixtures/cities13.json
./manage.py loaddata airline/fixtures/cities14.json
./manage.py loaddata airline/fixtures/cities15.json
./manage.py loaddata airline/fixtures/cities16.json
./manage.py loaddata airline/fixtures/cities17.json
./manage.py loaddata airline/fixtures/cities18.json
./manage.py loaddata airline/fixtures/cities19.json
./manage.py loaddata airline/fixtures/cities20.json
./manage.py loaddata airline/fixtures/cities21.json
./manage.py loaddata airline/fixtures/cities22.json
./manage.py loaddata airline/fixtures/cities23.json
./manage.py loaddata airline/fixtures/cities24.json
./manage.py loaddata airline/fixtures/cities25.json
./manage.py loaddata airline/fixtures/cities26.json
./manage.py loaddata airline/fixtures/cities27.json
./manage.py loaddata airline/fixtures/cities28.json
./manage.py loaddata airline/fixtures/cities29.json
./manage.py loaddata airline/fixtures/cities30.json
./manage.py loaddata airline/fixtures/cities31.json
./manage.py loaddata airline/fixtures/cities32.json
./manage.py loaddata airline/fixtures/cities33.json
./manage.py loaddata airline/fixtures/cities34.json

./manage.py shell -c "from users.models import CustomUser as User; User.objects.create_superuser('admin@airline.local', 'admin')"
