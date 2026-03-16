import os
import django
from django.core.files.base import ContentFile

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import get_user_model
from showroom.models import Car

User = get_user_model()

def create_initial_data():
    # Create Superuser
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')
        print("Superuser 'admin' created (password: admin)")
    else:
        print("Superuser 'admin' already exists")

    # Create Sample Cars
    if Car.objects.count() == 0:
        # Car 1: Rental
        Car.objects.create(
            title="Porsche 911 GT3",
            category="RENT",
            price=1200.00,
            specs="0-100: 3.4s\nEngine: 4.0L Flat-6\nPower: 502 hp",
            is_featured=True,
            description="L'esperienza di guida definitiva. Noleggia la potenza."
        )
        
        # Car 2: Sale
        Car.objects.create(
            title="Mercedes-AMG GT Black Series",
            category="SALE",
            price=350000.00,
            specs="0-100: 3.2s\nEngine: V8 Biturbo\nPower: 730 hp",
            is_featured=True,
            description="Un mostro da pista omologato per la strada. Disponibile per l'acquisto immediato."
        )

        # Car 3: Rental
        Car.objects.create(
            title="Audi RS6 Avant",
            category="RENT",
            price=800.00,
            specs="0-100: 3.6s\nEngine: V8 Mild-Hybrid\nPower: 600 hp",
            is_featured=False,
            description="Potenza e comfort per i tuoi viaggi business."
        )

        # Car 4: Standard Rental
        Car.objects.create(
            title="Fiat Panda City Life",
            category="RENT",
            price=45.00,
            specs="Motore: 1.0 Hybrid\nPosti: 5\nConsumo: 20 km/l",
            is_featured=True,
            description="L'auto perfetta per la città. Economica e agile."
        )

        # Car 5: Standard Sale
        Car.objects.create(
            title="Ford Fiesta",
            category="SALE",
            price=15500.00,
            specs="Motore: 1.1 Benzina\nAnno: 2023\nColore: Race Red",
            is_featured=True,
            description="Compatta, tecnologica e divertente da guidare."
        )

        print("Sample cars created.")
    else:
        print("Cars already exist in the database.")

if __name__ == '__main__':
    create_initial_data()
