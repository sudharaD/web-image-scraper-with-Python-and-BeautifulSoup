import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse


class ImageDownloader:
    def __init__(
        self, url, output_folder, keywords, max_images=150
    ):  # Add max depth if want to go deep | ex: max_depth=2
        self.url = url
        self.output_folder = output_folder
        self.keywords = keywords

        #  Add max depth
        # self.max_depth = max_depth

        self.max_images = max_images
        self.download_count = 0  # Initialize a global count variable

    def download_images_with_keywords(self):
        """
        Downloads images from a web page based on specified keywords.

        This method initiates the download process by creating the output folder,
        setting up a visited_urls set to avoid duplicate downloads, and calling
        the internal recursive function for processing the specified URL.
        (If want to call the recursive function remove the related comments)

        Returns:
            None
        """
        os.makedirs(self.output_folder, exist_ok=True)
        visited_urls = set()

        # if want to go deep initiate attribute to catch deapth | ex: def download_images_internal(current_url, depth):
        def download_images_internal(current_url):
            """
            Recursively processes a web page, downloads images, and follows links.

            Args:
                current_url (str): The URL of the current web page.
                depth (int): The depth of the recursion, representing the level of links.
                (Reactive recursion if want to go deep)

            Returns:
                None
            """
            # Codes related to go deep
            # if (
            #     depth > self.max_depth
            #     or current_url in visited_urls
            #     or self.download_count >= self.max_images
            # ):
            #     return

            # debugging statement - Print the current URL for debugging
            print(f"Processing: {current_url}")

            # Codes related to go deep
            # visited_urls.add(current_url)

            response = requests.get(current_url)
            soup = BeautifulSoup(response.text, "html.parser")

            # Find images with alt attribute containing any of the keywords
            image_tags = soup.find_all(
                "img",
                {
                    "alt": lambda x: x
                    and any(keyword.lower() in x.lower() for keyword in self.keywords)
                },
            )
            for img_tag in image_tags:
                img_url = img_tag.get("src")
                # if img_url and self.download_count < self.max_images:
                if (
                    img_url
                    and self.download_count < self.max_images
                    and not img_url.startswith("data:image")
                ):
                    img_url = urljoin(current_url, img_url)
                    img_data = requests.get(img_url).content
                    # Construct a unique filename based on search keywords and index
                    domain_name = urlparse(current_url).netloc.replace(".", "_")
                    img_filename = os.path.join(
                        self.output_folder,
                        # f'{"_".join(self.keywords)}_{self.download_count + 1}.jpg',
                        f'{domain_name}_{"_".join(self.keywords)}_{self.download_count + 1}.jpg',
                    )
                    with open(img_filename, "wb") as img_file:
                        img_file.write(img_data)
                    print(f"Downloaded: {img_filename}")
                    self.download_count += 1

            # If want to go deep activate the recursive function
            # Follow links recursively
            # for link in soup.find_all("a", href=True):
            #     next_url = urljoin(current_url, link["href"])
            #     download_images_internal(next_url, depth + 1)

        download_images_internal(
            self.url
        )  # send the depth value if want to go deep: ex:(self.url, 0)
