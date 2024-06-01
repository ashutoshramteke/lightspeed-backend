import graphene

class Version(graphene.ObjectType):
    min = graphene.Float()
    max = graphene.Float()

class Type(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()
    deleted_at = graphene.String()
    version=graphene.Float()

class CategoryPathItem(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()

class ProductCategory(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()
    leaf_category = graphene.Boolean()
    category_path = graphene.List(CategoryPathItem)

class Supplier(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()
    source = graphene.String()
    description = graphene.String()
    deleted_at = graphene.String()
    version = graphene.Float()

class Brand(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()
    description = graphene.String()
    deleted_at = graphene.String()
    version = graphene.Float()

class VariantOption(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()
    value = graphene.String()

class Category(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()
    deleted_at = graphene.String()
    version=graphene.Float()

class ProductCode(graphene.ObjectType):
    id = graphene.String()
    type = graphene.String()
    code = graphene.String()

class ProductSupplier(graphene.ObjectType):
    id = graphene.String()
    product_id = graphene.String()
    supplier_id = graphene.String()
    supplier_name = graphene.String()
    code = graphene.String()
    price = graphene.Float()

class Packaging(graphene.ObjectType):
    made_from = graphene.List(graphene.String)
    breaks_into = graphene.List(graphene.String)
class Sizes(graphene.ObjectType):
    raw=graphene.String()
    original= graphene.String()
    sl= graphene.String()
    sm= graphene.String()
    ss= graphene.String()
    st=graphene.String()
    standard= graphene.String()
    thumb= graphene.String()

class Image(graphene.ObjectType):
    id= graphene.String()
    url= graphene.String()
    version= graphene.Float()
    sizes= graphene.Field(Sizes)



class Datum(graphene.ObjectType):
    id = graphene.String()
    source_id = graphene.String()
    source_variant_id = graphene.String()
    variant_parent_id = graphene.String()
    name = graphene.String()
    variant_name = graphene.String()
    handle = graphene.String()
    sku = graphene.String()
    active = graphene.Boolean()
    ecwid_enabled_webstore = graphene.Boolean()
    has_inventory = graphene.Boolean()
    is_composite = graphene.Boolean()
    description = graphene.String()
    image_url = graphene.String()
    created_at = graphene.String()
    updated_at = graphene.String()
    deleted_at = graphene.String()
    source = graphene.String()
    supply_price = graphene.Float()
    version = graphene.Float()
    type = graphene.Field(Type)
    product_category = graphene.Field(ProductCategory)
    supplier = graphene.Field(Supplier)
    brand = graphene.Field(Brand)
    variant_options = graphene.List(VariantOption)
    categories = graphene.List(Category)
    images = graphene.List(Image)
    sku_images = graphene.List(graphene.String)
    has_variants = graphene.Boolean()
    variant_count = graphene.Int()
    button_order = graphene.Int()
    price_including_tax = graphene.Float()
    price_excluding_tax = graphene.Float()
    loyalty_amount = graphene.Float()
    product_codes = graphene.List(ProductCode)
    product_suppliers = graphene.List(ProductSupplier)
    packaging = graphene.Field(Packaging)
    weight = graphene.Float()
    length = graphene.Float()
    width = graphene.Float()
    height = graphene.Float()
    dimensions_unit = graphene.Float()
    attributes = graphene.List(graphene.String)
    supplier_id = graphene.String()
    is_active = graphene.Boolean()
    image_thumbnail_url = graphene.String()
    product_type_id = graphene.String()
    brand_id = graphene.String()
    tag_ids = graphene.List(graphene.String)

class Model(graphene.ObjectType):
    data = graphene.List(Datum)
    version = graphene.Field(Version)

class Model2(graphene.ObjectType):
    data = graphene.Field(Datum)
    


# schema = graphene.Schema(query=Model)