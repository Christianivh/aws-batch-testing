from enum import Enum

enum_country = Enum(
    value='country',
    names=[
        ('BO', 0),
        ('CL', 1),
        ('CO', 2),
        ('CR', 3),
        ('DO', 4),
        ('EC', 5),
        ('GT', 6),
        ('MX', 7),
        ('PA', 8),
        ('PE', 9),
        ('PR', 10),
        ('SV', 11)
        ]
)

execute_parameters = [
    {'country': 'BO', 'vcpus':4, 'memory': 65535},
    {'country': 'CL', 'vcpus':4, 'memory': 65535},
    {'country': 'CO', 'vcpus':16, 'memory': 65535},
    {'country': 'CR', 'vcpus':8, 'memory': 65535},
    {'country': 'DO', 'vcpus':8, 'memory': 65535},
    {'country': 'EC', 'vcpus':8, 'memory': 65535},
    {'country': 'GT', 'vcpus':8, 'memory': 65535},
    {'country': 'MX', 'vcpus':8, 'memory': 65535},
    {'country': 'PA', 'vcpus':4, 'memory': 65535},
    {'country': 'PE', 'vcpus':16, 'memory': 65535},
    {'country': 'PR', 'vcpus':4, 'memory': 65535},
    {'country': 'SV', 'vcpus':4, 'memory': 65535}
]