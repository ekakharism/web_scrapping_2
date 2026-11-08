import pandas as pd

def cleaned_data(books):
    clean_books = []

    RATING_MAP = {
        'One' : 1,
        'Two' : 2,
        'Three' : 3,
        'Four' : 4,
        'Five' : 5
    }

    for book in books:
        title = book['Title']
        price = book['Price'].replace('Â','')
        rating = RATING_MAP.get(book['Rating'], None)
        status = book['Status Stok'].strip()
        link = book['Link']
        clean_books.append({
                    'Title' : title,
                    'Price' : price,
                    'Rating' :rating,
                    'Status Stok' : status,
                    'Link' : link
                })
    hasil = pd.DataFrame(clean_books)
    
    return hasil
        