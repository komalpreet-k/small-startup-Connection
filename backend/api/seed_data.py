from api.models import Country, State, City, Category


def run():
    # Countries
    india, _ = Country.objects.get_or_create(name="India", code="IN")
    canada, _ = Country.objects.get_or_create(name="Canada", code="CA")

    # States - India
    punjab, _ = State.objects.get_or_create(name="Punjab", country=india)
    maharashtra, _ = State.objects.get_or_create(name="Maharashtra", country=india)

    # States - Canada
    ontario, _ = State.objects.get_or_create(name="Ontario", country=canada)
    alberta, _ = State.objects.get_or_create(name="Alberta", country=canada)

    # Cities - India
    City.objects.get_or_create(name="Amritsar", state=punjab)
    City.objects.get_or_create(name="Mumbai", state=maharashtra)

    # Cities - Canada
    City.objects.get_or_create(name="Toronto", state=ontario)
    City.objects.get_or_create(name="Calgary", state=alberta)

    # Categories
    Category.objects.get_or_create(name="Home Bakery", slug="home-bakery")
    Category.objects.get_or_create(name="Makeup Artist", slug="makeup-artist")
    Category.objects.get_or_create(name="Tailoring", slug="tailoring")

    print("Initial data seeded successfully.")
