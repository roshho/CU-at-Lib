# Pitch + Demo
https://youtu.be/4l-oOLacSHw

# Instructions to run
- You should only need to use ``app.py``, ``CUStudySeat.zip``, and ``library-occupancy.zip``. ``Assets`` and ``temp-working`` are working code files 
1) navigate to folder with ``app.py``
2) ``python app.py`` or ``python3 app.py`` to run the mock flask server
3) download localwp
4) import ``CUStudySeat.zip`` into localwp (i.e. importing the wordpress website into localwp``
5) run the imported website in localwp
6) install a plugin
7) upload ``library-occupancy.zip`` into the plugin upload page in localwp website
8) money $$$

# File Structure
library-occupancy/
├── block.json
├── library-occupancy.php 
├── admin/
│   ├── css/
│   │   └── admin-style.css
│   ├── views/
│   │   ├── dashboard.phpW
│   │   └── settings.php
│   └── admin.php
├── includes/
│   └── functions.php
├── public/
│   ├── css/
│   │   └── block-style.css
│   └── js/
│       └── block.js
│       └── front-end.js
├── README.md
└── app.py 

- CUStudySeat.zip: the wordpress zip (import into local.wp)
- library-occupancy.zip: current working version of plugin (import into local.wp website plugin)
- app.py: the flask server (ls to the folder and ``python3 app.py``)
- asset: code for library-occupancy.zip 
- temp-working: temp archive to keep past working frontend files

# Resources used
- WordPress.tv 
- https://www.youtube.com/watch?v=tYLfC8nNPLs
- https://www.youtube.com/watch?v=JZslURB8tos
