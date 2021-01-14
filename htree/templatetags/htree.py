from django.template import Library
from django.utils.html import mark_safe


register = Library()


@register.filter
def ffile_filter(fs_list):
    res = """
        <ul>
            {}
        </ul>
        """
    i =''
    for fs in fs_list:
        i+= """
            <li>
                {pseudo_id}
            </li>
            """.format(pseudofs_id=pseudofs['ffile'])
        if pseudofs.get('children'):
            i += pseudofs_filter(pseudofs['children'])

    return mark_safe(res.format(i_))

