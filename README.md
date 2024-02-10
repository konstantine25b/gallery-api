# Gallery API

The Gallery API is a RESTful API designed to manage artists, artwork, and exhibitions within a gallery setting. It leverages Django, Django REST Framework, and Django Filters to provide robust functionality and efficient data handling.

## Features

- **Artists**: Maintain comprehensive information about artists, including their biographical details and a collection of associated artworks.
- **Artwork**: Store detailed information about each artwork, such as title, description, medium, and the artist who created it.
- **Exhibitions**: Organize exhibitions with relevant details like title, description, location, and the artworks featured within each exhibition.
- **Filtering**: Utilize Django Filters to allow users to filter data based on various criteria, such as artist name, artwork medium, or exhibition date.

## Setup

### Prerequisites

Ensure you have the following installed:

- Python (3.7 or higher)
- Django
- Django REST Framework
- Django Filters

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/konstantine25b/gallery-api
    cd gallery_api
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:

    ```bash
    python manage.py migrate
    ```

4. Run the development server:

    ```bash
    python manage.py runserver
    ```

The API will be accessible at `http://localhost:8000/`.

## Usage

### Endpoints

- **Artists**: `/api/artists/`
- **Artwork**: `/api/artwork/`
- **Exhibitions**: `/api/exhibitions/`
