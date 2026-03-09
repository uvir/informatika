disk_size_in_mb= 1.44
pages=100
lines=50
symbols=25
size_symbols_in_b=4

disk_size_in_kb=disk_size_in_mb*1024
disk_size_in_b=disk_size_in_kb*1024
size_book_in_b=size_symbols_in_b*symbols*lines*pages
numbers_of_books= disk_size_in_b // size_book_in_b

print("Количество книг, помещающихся на дискету:", int(numbers_of_books))
