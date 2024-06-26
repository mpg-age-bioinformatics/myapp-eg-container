import os

_PRIVATE_ROUTES=['demo']
_PUBLIC_VIEWS=[]
_META_TAGS=[]


user_navbar_links={
    "Home":"https://myapp.localhost",\
    "DemoApp":"https://myapp.localhost/demo/",\
    "Storage":"/storage/",\
    "separator_1":"-",\
    "General":"__title__",\
    "About":"/about/",\
    "Impressum":"/impressum/",\
    "Privacy":"/privacy/",\
    "fixed_separator":"-",\
    "Configuration":"__title__", \
    "Settings":"/settings/",\
    "fixed_separator_2":"-",\
    "Logout":"/logout/"
}

other_nav_dropdowns=[]

###################################
# _PRIVATE_ROUTES=['home'] ## only users added to this route on the admin board / User model will have access
# _PUBLIC_VIEWS=[] ## can be used to set specific rights within the app eg. deactiva Submit buttons.
# other_nav_dropdowns =[ 
#     { \
#         "Eg. DropDown": \
#             {
#                 "Home":"/home/",\
#                 "separator_1":"-",\
#                 "General":"__title__",\
#                 "About":"/about/",\
#                 "Impressum":"/impressum/",\
#                 "Privacy":"/privacy/",\
#                 "fixed_separator":"-",\
#                 "Configuration":"__title__", \
#                 "Settings":"/settings/",\
#                 "Logout":"/logout/"
#             } \
#     }, \
#     { \
#         "Eg. DropDown 2": \
#             {
#                 "Home":"/home/",\
#                 "separator_1":"-",\
#                 "General":"__title__",\
#                 "About":"/about/",\
#                 "Impressum":"/impressum/",\
#                 "Privacy":"/privacy/",\
#                 "fixed_separator":"-",\
#                 "Configuration":"__title__", \
#                 "Settings":"/settings/",\
#                 "Logout":"/logout/"
#             } \
#     }
# ]
###################################