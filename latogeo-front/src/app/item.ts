export class Item {
    id: number;
    patrimony: string;
    spec: ItemSpec;
    kind: ItemKind;
}

export class ItemSpec{
    id: number;
    name: string;
    description: string;
    items_available: Item[] = [];
    items_total: number;
}

export class ItemKind {
    id: number;
    name: string;
    description: string;
    spec_kind: ItemSpec[] = [];
}
