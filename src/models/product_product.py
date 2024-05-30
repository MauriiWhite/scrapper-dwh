from dataclasses import dataclass
from typing import Any, List, TypeVar, Callable, Type, cast

T = TypeVar("T")


def from_str(x: Any) -> str:
    return x if isinstance(x, str) else str(x)


def from_stringified_bool(x: str) -> bool:
    if x == "true":
        return True
    if x == "false":
        return False
    assert False


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    return [f(y) for y in x] if x is not None else []


def from_int(x: Any) -> int:
    return x if isinstance(x, int) else int(x)


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    return cast(Any, x).to_dict() if isinstance(x, c) else x


@dataclass
class Attributes:
    default_quantity: int
    content_uom: str
    seller_type: str
    department: int
    volumetric_weight: int
    color: str

    @staticmethod
    def from_dict(obj: Any) -> "Attributes":
        assert isinstance(obj, dict)
        default_quantity = int(from_str(obj.get("defaultQuantity") or "0"))
        content_uom = from_str(obj.get("contentUom"))
        seller_type = from_str(obj.get("sellerType"))
        department = int(from_str(obj.get("department") or "0"))
        volumetric_weight = float(from_str(obj.get("volumetricWeight")))
        color = from_str(obj.get("color"))
        return Attributes(
            default_quantity,
            content_uom,
            seller_type,
            department,
            volumetric_weight,
            color,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["defaultQuantity"] = from_str(str(self.default_quantity))
        result["contentUom"] = from_str(self.content_uom)
        result["sellerType"] = from_str(self.seller_type)
        result["department"] = from_str(str(self.department))
        result["volumetricWeight"] = from_str(str(self.volumetric_weight))
        result["color"] = from_str(self.color)
        return result


@dataclass
class Images:
    default_image: str
    small_image: str
    medium_image: str
    large_image: str
    available_images: List[Any]

    @staticmethod
    def from_dict(obj: Any) -> "Images":
        assert isinstance(obj, dict)
        default_image = from_str(obj.get("defaultImage"))
        small_image = from_str(obj.get("smallImage"))
        medium_image = from_str(obj.get("mediumImage"))
        large_image = from_str(obj.get("largeImage"))
        available_images = from_list(lambda x: x, obj.get("availableImages"))
        return Images(
            default_image, small_image, medium_image, large_image, available_images
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["defaultImage"] = from_str(self.default_image)
        result["smallImage"] = from_str(self.small_image)
        result["mediumImage"] = from_str(self.medium_image)
        result["largeImage"] = from_str(self.large_image)
        result["availableImages"] = from_list(lambda x: x, self.available_images)
        return result


@dataclass
class Price:
    base_price_per_um: str
    base_price_reference: int
    base_price_sales: int
    base_price_tlmc: int
    pack_price: int
    pack_size: int

    @staticmethod
    def from_dict(obj: Any) -> "Price":
        assert isinstance(obj, dict)
        base_price_per_um = from_str(obj.get("BasePricePerUm"))
        base_price_reference = from_int(obj.get("BasePriceReference"))
        base_price_sales = from_int(obj.get("BasePriceSales"))
        base_price_tlmc = from_int(obj.get("BasePriceTLMC"))
        pack_price = from_int(obj.get("packPrice"))
        pack_size = from_int(obj.get("packSize"))
        return Price(
            base_price_per_um,
            base_price_reference,
            base_price_sales,
            base_price_tlmc,
            pack_price,
            pack_size,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["BasePricePerUm"] = from_str(self.base_price_per_um)
        result["BasePriceReference"] = from_int(self.base_price_reference)
        result["BasePriceSales"] = from_int(self.base_price_sales)
        result["BasePriceTLMC"] = from_int(self.base_price_tlmc)
        result["packPrice"] = from_int(self.pack_price)
        result["packSize"] = from_int(self.pack_size)
        return result


@dataclass
class Specification:
    name: str
    order: int
    value: str

    @staticmethod
    def from_dict(obj: Any) -> "Specification":
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        order = from_int(obj.get("order"))
        value = from_str(obj.get("value"))
        return Specification(name, order, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["order"] = from_int(self.order)
        result["value"] = from_str(self.value)
        return result


@dataclass
class Tags:
    campaign_tags: List[Any]
    attribute_tags: List[str]
    delivery_tags: List[str]

    @staticmethod
    def from_dict(obj: Any) -> "Tags":
        assert isinstance(obj, dict)
        campaign_tags = from_list(lambda x: x, obj.get("campaignTags"))
        attribute_tags = from_list(from_str, obj.get("attributeTags"))
        delivery_tags = from_list(from_str, obj.get("deliveryTags"))
        return Tags(campaign_tags, attribute_tags, delivery_tags)

    def to_dict(self) -> dict:
        result: dict = {}
        result["campaignTags"] = from_list(lambda x: x, self.campaign_tags)
        result["attributeTags"] = from_list(from_str, self.attribute_tags)
        result["deliveryTags"] = from_list(from_str, self.delivery_tags)
        return result


@dataclass
class WinningOffer:
    country: str
    international_seller: bool
    seller_id: str
    seller_name: str
    seller_type: str

    @staticmethod
    def from_dict(obj: Any) -> "WinningOffer":
        assert isinstance(obj, dict)
        country = from_str(obj.get("country"))
        international_seller = from_bool(obj.get("internationalSeller"))
        seller_id = from_str(obj.get("sellerId"))
        seller_name = from_str(obj.get("sellerName"))
        seller_type = from_str(obj.get("sellerType"))
        return WinningOffer(
            country, international_seller, seller_id, seller_name, seller_type
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["country"] = from_str(self.country)
        result["internationalSeller"] = from_bool(self.international_seller)
        result["sellerId"] = from_str(self.seller_id)
        result["sellerName"] = from_str(self.seller_name)
        result["sellerType"] = from_str(self.seller_type)
        return result


@dataclass
class ProductProduct:
    id: str
    attributes: Attributes
    brand: str
    description: str
    destacado: bool
    display_name: str
    gtin13: str
    images: Images
    is_mkp: bool
    is_variant: bool
    item_number: int
    keyword: List[str]
    lead_time: int
    long_description: str
    max: int
    posicion: int
    sites: List[str]
    sku: int
    specifications: List[Specification]
    variants: List[Any]
    vendor_id: str
    wfs_eligible: bool
    winning_offer: WinningOffer
    price: Price
    discount: int
    default_quantity: int
    tags: Tags
    categorias: List[str]
    make_public: bool
    available: bool
    ranked_offers: List[Any]

    @staticmethod
    def from_dict(obj: Any) -> "ProductProduct":
        assert isinstance(obj, dict)
        id = from_str(obj.get("ID"))
        attributes = Attributes.from_dict(obj.get("attributes"))
        brand = from_str(obj.get("brand"))
        description = from_str(obj.get("description"))
        destacado = from_bool(obj.get("destacado"))
        display_name = from_str(obj.get("displayName"))
        gtin13 = from_str(obj.get("gtin13"))
        images = Images.from_dict(obj.get("images"))
        is_mkp = from_bool(obj.get("isMKP"))
        is_variant = from_bool(obj.get("isVariant"))
        item_number = int(from_str(obj.get("itemNumber") or "0"))
        keyword = from_list(from_str, obj.get("keyword"))
        lead_time = from_int(obj.get("leadTime"))
        long_description = from_str(obj.get("longDescription"))
        max = from_int(obj.get("max"))
        posicion = from_int(obj.get("posicion"))
        sites = from_list(from_str, obj.get("sites"))
        sku = from_str(obj.get("sku"))
        specifications = from_list(Specification.from_dict, obj.get("specifications"))
        variants = from_list(lambda x: x, obj.get("variants"))
        vendor_id = from_str(obj.get("vendorId"))
        wfs_eligible = from_bool(obj.get("wfsEligible"))
        winning_offer = WinningOffer.from_dict(obj.get("winningOffer"))
        price = Price.from_dict(obj.get("price"))
        discount = from_int(obj.get("discount"))
        default_quantity = from_int(obj.get("defaultQuantity"))
        tags = Tags.from_dict(obj.get("tags"))
        categorias = from_list(from_str, obj.get("categorias"))
        make_public = from_bool(obj.get("makePublic"))
        available = from_bool(obj.get("available"))
        ranked_offers = from_list(lambda x: x, obj.get("rankedOffers"))
        return ProductProduct(
            id,
            attributes,
            brand,
            description,
            destacado,
            display_name,
            gtin13,
            images,
            is_mkp,
            is_variant,
            item_number,
            keyword,
            lead_time,
            long_description,
            max,
            posicion,
            sites,
            sku,
            specifications,
            variants,
            vendor_id,
            wfs_eligible,
            winning_offer,
            price,
            discount,
            default_quantity,
            tags,
            categorias,
            make_public,
            available,
            ranked_offers,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["ID"] = from_str(self.id)
        result["attributes"] = to_class(Attributes, self.attributes)
        result["brand"] = from_str(self.brand)
        result["description"] = from_str(self.description)
        result["destacado"] = from_bool(self.destacado)
        result["displayName"] = from_str(self.display_name)
        result["gtin13"] = from_str(self.gtin13)
        result["images"] = to_class(Images, self.images)
        result["isMKP"] = from_bool(self.is_mkp)
        result["isVariant"] = from_bool(self.is_variant)
        result["itemNumber"] = from_str(str(self.item_number))
        result["keyword"] = from_list(from_str, self.keyword)
        result["leadTime"] = from_int(self.lead_time)
        result["longDescription"] = from_str(self.long_description)
        result["max"] = from_int(self.max)
        result["posicion"] = from_int(self.posicion)
        result["sites"] = from_list(from_str, self.sites)
        result["sku"] = from_str(str(self.sku))
        result["specifications"] = from_list(
            lambda x: to_class(Specification, x), self.specifications
        )
        result["variants"] = from_list(lambda x: x, self.variants)
        result["vendorId"] = from_str(self.vendor_id)
        result["wfsEligible"] = from_bool(self.wfs_eligible)
        result["winningOffer"] = to_class(WinningOffer, self.winning_offer)
        result["price"] = to_class(Price, self.price)
        result["discount"] = from_int(self.discount)
        result["defaultQuantity"] = from_int(self.default_quantity)
        result["tags"] = to_class(Tags, self.tags)
        result["categorias"] = from_list(from_str, self.categorias)
        result["makePublic"] = from_bool(self.make_public)
        result["available"] = from_bool(self.available)
        result["rankedOffers"] = from_list(lambda x: x, self.ranked_offers)
        return result


def product_product_from_dict(s: Any) -> ProductProduct:
    return ProductProduct.from_dict(s)


def product_product_to_dict(x: ProductProduct) -> Any:
    return to_class(ProductProduct, x)
