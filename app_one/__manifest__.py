{
    'name': "App One",
    'version': '1.0',
    'author': "Younes",
    'category': 'Learning odoo',
    'depends': ['base'],
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/property_view.xml',
        'views/property_type_view.xml',
        'views/property_tag_view.xml',
        'views/property_offer_view.xml',
        'views/res_users_view.xml'
          ],
    'application': True,
}