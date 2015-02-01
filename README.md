# MapAction Map Review Tool

This project is being supported by MapAction, ACAPS, SIIEM and DRL.  It aims to
get a better understanding of when data are being used during crises and from
what sources. This will help with understanding many things - e.g. are we
making data available in the appropriate timescales, are some data/sources more
readily available than others, what role do governmental data sources play,
what vital datasets are not being used etc etc.

## Contributing

Fork the repo (`mapaction/map_review`) and submit a Pull Request.


## Running the tool


    $- pip install requirements.txt
    $- export DJANGO_SETTINGS_MODULE=map_review.settings.devel
    $- ./manage.py syncdb
    $- ./manage.py migrate
    $- ./manage.py runserver 0.0.0.0:8080


Note that you can add your own `devel_...` file to settings dir

