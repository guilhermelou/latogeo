# -*- coding: utf-8 -*-
import os
from django.conf import settings
import json
from .models import Item, ItemSpec, ItemKind

def parseData():
    file = open(os.path.join(settings.PROJECT_ROOT, 'aux_files/data.json'))
    file_data = file.read()
    data = json.loads(file_data)
    equipments = data["Equipamentos"]
    for key in equipments.keys():
        print(key)
        item_kind =ItemKind.objects.create(
                name=key, category = ItemKind.EQUIPAMENT)
        item_spec_array = equipments[key]
        for item_spec in item_spec_array:
            ItemSpec.objects.create(name=item_spec, kind=item_kind)

    accessories = data[u"Acessórios"]
    item_kind =ItemKind.objects.create(
            name=u"Acessórios", category = ItemKind.ACCESSORY)
    for item_spec in accessories:
        ItemSpec.objects.create(name=item_spec, kind=item_kind)

parseData()
