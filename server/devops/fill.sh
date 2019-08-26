#!/usr/bin/env bash

./manage.py migrate
./manage.py loaddata airline/fixtures/aircrafts/aircrafts.json
./manage.py loaddata airline/fixtures/geo/countries.json
./manage.py loaddata airline/fixtures/geo/regions0.json
./manage.py loaddata airline/fixtures/geo/regions1.json
./manage.py loaddata airline/fixtures/geo/regions2.json
./manage.py loaddata airline/fixtures/geo/regions3.json
./manage.py loaddata airline/fixtures/geo/cities0.json
./manage.py loaddata airline/fixtures/geo/cities1.json
./manage.py loaddata airline/fixtures/geo/cities2.json
./manage.py loaddata airline/fixtures/geo/cities3.json
./manage.py loaddata airline/fixtures/geo/cities4.json
./manage.py loaddata airline/fixtures/geo/cities5.json
./manage.py loaddata airline/fixtures/geo/cities6.json
./manage.py loaddata airline/fixtures/geo/cities7.json
./manage.py loaddata airline/fixtures/geo/cities8.json
./manage.py loaddata airline/fixtures/geo/cities9.json
./manage.py loaddata airline/fixtures/geo/cities10.json
./manage.py loaddata airline/fixtures/geo/cities11.json
./manage.py loaddata airline/fixtures/geo/cities12.json
./manage.py loaddata airline/fixtures/geo/cities13.json
./manage.py loaddata airline/fixtures/geo/cities14.json
./manage.py loaddata airline/fixtures/geo/cities15.json
./manage.py loaddata airline/fixtures/geo/cities16.json
./manage.py loaddata airline/fixtures/geo/cities17.json
./manage.py loaddata airline/fixtures/geo/cities18.json
./manage.py loaddata airline/fixtures/geo/cities19.json
./manage.py loaddata airline/fixtures/geo/cities20.json
./manage.py loaddata airline/fixtures/geo/cities21.json
./manage.py loaddata airline/fixtures/geo/cities22.json
./manage.py loaddata airline/fixtures/geo/cities23.json
./manage.py loaddata airline/fixtures/geo/cities24.json
./manage.py loaddata airline/fixtures/geo/cities25.json
./manage.py loaddata airline/fixtures/geo/cities26.json
./manage.py loaddata airline/fixtures/geo/cities27.json
./manage.py loaddata airline/fixtures/geo/cities28.json
./manage.py loaddata airline/fixtures/geo/cities29.json
./manage.py loaddata airline/fixtures/geo/cities30.json
./manage.py loaddata airline/fixtures/geo/cities31.json
./manage.py loaddata airline/fixtures/geo/cities32.json
./manage.py loaddata airline/fixtures/geo/cities33.json
./manage.py loaddata airline/fixtures/geo/cities34.json

./manage.py shell -c "from users.models import CustomUser as User; User.objects.create_superuser('admin@airline.local', 'admin')"
