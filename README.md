# AVERAGE COLOR SERVER
Made specifically for the [Podcasts](https://github.com/Kandros9/podcasts-akvelon-education) app using Django


## API
### POST `/process_image/get_color`
#### Request
```
{
    "image_urls": [
        "https://cdn-images-1.listennotes.com/podcasts/alexa-stop-podcast-robert-belgrave-jim-bowes-5f2IEtTmaYv-5jn9XD-Irgu.300x300.jpg", 
        "https://cdn-images-1.listennotes.com/podcasts/this-week-in-tech-mp3-twit-FhH4pxNJ7MD-rOsjyMdh_cW.300x300.jpg"
    ]
}
```
#### Response
```
{
    "dominant_colors": [
        [14,149,145],
        [46,98,104]
    ]
}
```

## Running the project
1. Install `python 3` and `virtualenv` (if not)
2. Clone the repo
3. Create a virtualenv
    ```
    cd podcast-server-akvelon-education
    virtualenv -p python3 ./venv
    ```
4. Activate virtualenv

    **Windows**
    ```
    .\venv\Scripts\activate
    ```
    **MacOS/Linux**
    ```
    source ./venv/bin/activate
    ```
5. Install requirements from `requirements.txt` file
    ```
    pip install -r requirements.txt
    ```
