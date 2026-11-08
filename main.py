from extract import scrape_data
from transform import cleaned_data
from load import save_data

books = scrape_data(51)
hasil = cleaned_data(books)

save_data(hasil)