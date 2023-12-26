from image_downloader import ImageDownloader

if __name__ == "__main__":
    url_to_scrape = "https://en.wikipedia.org/wiki/Elon_Musk"
    output_directory = "data/elon_musk"
    search_keywords = ["elon musk", "elon", "musk"]

    # if want to go deep add depth
    # max_depth = 2
    max_images_count = 150

    image_download = ImageDownloader(
        url_to_scrape,
        output_directory,
        search_keywords,
        # max_depth,
        max_images=max_images_count,
    )
    image_download.download_images_with_keywords()
