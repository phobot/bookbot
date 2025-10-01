get_book_text(path_to_file)
    with open(path_to_file) as file:
        content = file.read()

    return content

main()
    get_book_text(books/frankenstein.txt)

main()