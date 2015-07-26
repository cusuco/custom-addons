{
    'name': 'To-Do Application',
    'description': 'Manage your personal tasks with this module',
    'author': u'Andrés Reyes Monge',
    'depends': ['mail'],
    'application': True,
    'data': [
        'todo_view.xml',
        'security/ir.model.access.csv',
        'security/todo_access_rules.xml',
    ]
}
