{
    'name': "Estate Account",
    'version': '1.0',
    'author': "Younes",
    'category': 'Learning odoo',
    'depends': ['app_one','account'],
    # # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
          ],
    'application': True,
}