from enum import Enum
from breeds import CatBreed, DogBreed, RabbitBreed


class Type(Enum):
    cat = "Cat"
    dot = "Dog"
    rabbit = "Rabbit"


class Gender(Enum):
    male = "Male"
    female = "Female"
    unknown = "Unknown"


class Size(Enum):
    small = "Small"
    medium = "Medium"
    large = "Large"
    xlarge = "Xlarge"


class Age(Enum):
    baby = "Baby"
    young = "Young"
    adult = "Adult"
    senior = "Senior"


class ColorBird(Enum):
    black = ("Black",)
    blue = ("Blue",)
    brown = ("Brown",)
    buff = ("Buff",)
    gray = ("Gray",)
    green = ("Green",)
    olive = ("Olive",)
    orange = ("Orange",)
    pink = ("Pink",)
    purple = ("Purple / Violet",)
    red = ("Red",)
    rust = ("Rust / Rufous",)
    tan = ("Tan",)
    white = ("White",)
    yellow = "Yellow"


class ColorDog(Enum):
    apricot_beige = ("Apricot / Beige",)
    bicolor = ("Bicolor",)
    black = ("Black",)
    brindle = ("Brindle",)
    brown_chocolate = ("Brown / Chocolate",)
    golden = ("Golden",)
    gray_blue_silver = ("Gray / Blue / Silver",)
    harlequin = ("Harlequin",)
    merle_blue = ("Merle (Blue)",)
    merle_red = ("Merle (Red)",)
    red_chestnut_orange = ("Red / Chestnut / Orange",)
    sable = ("Sable",)
    tricolor = ("Tricolor (Brown, Black, & White)",)
    white_cream = ("White / Cream",)
    yellow = "Yellow / Tan / Blond / Fawn"


class ColorCat(Enum):
    black = ("Black",)
    tuxedo = ("Black & White / Tuxedo",)
    blue_cream = ("Blue Cream",)
    blue_point = ("Blue Point",)
    brown = ("Brown / Chocolate",)
    buff_white = ("Buff & White",)
    buff_tan = ("Buff / Tan / Fawn",)
    calico = ("Calico",)
    chocolate_point = ("Chocolate Point",)
    cream_ivory = ("Cream / Ivory",)
    cream_point = ("Cream Point",)
    dilute_calico = ("Dilute Calico",)
    dilute_tortoiseshell = ("Dilute Tortoiseshell",)
    flame_point = ("Flame Point",)
    gray_white = ("Gray & White",)
    gray_blue = ("Gray / Blue / Silver",)
    lilac = ("Lilac Point",)
    orange_white = ("Orange & White",)
    orange_red = ("Orange / Red",)
    sela_point = ("Seal Point",)
    smoke = ("Smoke",)
    tabby_brown = ("Tabby (Brown / Chocolate)",)
    tabby_buff = ("Tabby (Buff / Tan / Fawn)",)
    tabby_gray = ("Tabby (Gray / Blue / Silver)",)
    tabby_leopard = ("Tabby (Leopard / Spotted)",)
    tabby_orange = ("Tabby (Orange / Red)",)
    tabby_tiger = ("Tabby (Tiger Striped)",)
    torbie = ("Torbie",)
    tortoiseshell = ("Tortoiseshell",)
    white = ("White",)


class ColorRabbit(Enum):
    agouti = ("Agouti",)
    black = ("Black",)
    blue_gray = ("Blue / Gray",)
    brown_chocolate = ("Brown / Chocolate",)
    cream = ("Cream",)
    lilac = ("Lilac",)
    orange_red = ("Orange / Red",)
    sable = ("Sable",)
    silver_marten = ("Silver Marten",)
    tan = ("Tan",)
    tortoiseshell = ("Tortoiseshell",)
    white = "White"


class Coat(Enum):
    short = "Short"
    medium = "Medium"
    long = "Long"
    wire = "Wire"
    hairless = "Hairless"
    curly = "Curly"


class Status(Enum):
    adoptable = "Adoptable"
    adopted = "Adopted"


class BoolType(Enum):
    no = 0
    yes = 1


class RoleType(Enum):
    user = "user"
    shelter = "shelter"
    admin = "admin"
