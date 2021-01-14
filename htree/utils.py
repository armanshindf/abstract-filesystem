from .models import Pseudofs

def get_children(qs_child):
    res = []
    psfs = Pseudofs.objects.filter()
    for psfs in qs_child:
        c = {
            'parent_id': Pseudofs.get_parent,
            'is_child': Pseudofs.is_child
        }
        if Pseudofs.pseudofs_children.exists():
            c['children'] = get_children(Pseudofs.pseudofs_children.all())
        res.append(c)
    return res

def create_file_tree(qs):
    res = []
    callf = Pseudofs()
    for callf in qs:
        c = {
            'parent_id' : Pseudofs.get_parent,
            'is_child' : Pseudofs.is_child
        }
        if Pseudofs.pseudofs_children:
            c['children'] = get_children(Pseudofs.pseudofs_children)
        if not Pseudofs.is_child:
            res.append(c)
        return res
