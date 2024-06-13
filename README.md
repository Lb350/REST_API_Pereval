# REST API for the Pereval application :mountain:
## A fully functional project written in Python using the Django framework that makes it possible to add and edit information about various mountain passes

### :scroll: Description:
The project was developed for the `"ФСТР" Russian Sports Tourism Federation ` ( site - https://pereval.online/ ) to maintain a base of mountain passes, which is filled with tourists. In the mountains, people will enter data about the pass into the application and send it to the `"ФСТР"` as soon as Internet access is available. A moderator from the federation will verify and enter information received from users into the database, and they, in turn, will be able to see the moderation status in the mobile application and view the database with objects entered by others.

## The content of the project
### Usage possibilities for the user:
1) Entering information about a new object (pass) into the object card.
2) Editing of object data not sent to the FSTR server in the application. The Internet does not always work at the pass.
3) Filling in the full name and contact details (phone and e-mail).
4) Sending data to the "ФСТР" server.
5) Receiving notification of the sending status (successful/unsuccessful).

### Data about the pass transmitted to the "ФСТР":
1) The name of the object;
2) Time;
3) Information about the user who transmitted the data about the pass:
   * user name (full name in a string);
   * mail;
   * telephone.
4) The coordinates of the object and its height;
5) Level of difficulty of the route depending on the season of the year;
6) Some photos;

> [!NOTE]
> Example of a Json file:

```
{
    "status": "NW",
    "beauty_title": "pass",
    "title": "Bear Gate Pass",
    "other_title": "Bear Gate",
    "connect": "new",
    "add_time": "2024-05-02T10:39:01.595478Z",
    "user": {
        "email": "testemail@mail.ru",
        "fam": "Surname",
        "name": "Name",
        "otc": "Middle name",
        "phone": "+7 555 55 55"
    },
    "coord": {
        "latitude": "55.38420000",
        "longitude": "89.15250000",
        "height": 3000
    },
    "level": {
        "winter": "3A",
        "spring": "2A",
        "summer": "1А",
        "autumn": "1А"
    },
    "images": [
        {
            "data": "https://image.jpg",
            "title": "Descent"
        },
        {
            "data": "https://image.jpg",
            "title": "Сlimbing"
        }
    ]
}
```
### Acceptable values of the status field:
  1) new; (NW) - new;
  2) pending (PN) — if the moderator has taken over the work;
  3) accepted (AC)  — moderation was successful;
  4) rejected (RJ) — moderation was passed, the information was not accepted.

### Result of the method: JSON
  * status — HTTP code, integer:
  * 500 — error when performing the operation;
  * 400 — Bad Request (if there are not enough fields);
  * 200 is a success.

The `partial_update` method in the `PerevalAddedViewset` allows for `updating` specific fields of a pass entry. If the pass is `new (status 'NW')`, it can be partially updated. Valid updates are saved and confirmed with a `success` message `(state: 1)`. Invalid data results in an error message detailing the issues `(state: 0)`. If the pass isn't new, the update is rejected, and the reason based on the pass's current status is provided. This method ensures that only certain updates are allowed depending on the pass's status, maintaining the integrity of the data.

> [!IMPORTANT]
> * You cannot change the data when the pass status is different from "NW".
> * You cannot change user data.

### Models
* User:
  > This model represents a user with a unique ID, email address, surname (fam), first name (name), patronymic (otc), and phone number. It's designed to store personal information about the users of the application.
* Coord:
  > The Coord model holds geographical coordinates, including latitude, longitude, and height. It's used to represent a specific location of the path.
* Level:
  > This model defines the different levels of difficulty of the routes for the passes, classified by season: winter, spring, summer and autumn. Each level is represented by a code, for example, "1A" is the easiest and "3B" is the most difficult.
* PerevalAdded:
  > The PerevalAdded model contains information about a particular pass (pereval), including its status (new, pending, accepted, or rejected), titles, connection details, the time it was added, and associated user and coordinate information. It also links to the difficulty level through the Level model.
* Image:
  > This model is for storing image data related to a pass. It includes a data field for the image file path or URL, a title, and a foreign key to the associated PerevalAdded record.

## :open_book: Installing the project

1) Download this repository;
2) Create a virtual environment and activate it;
3) The project's external dependencies are listed in the `requirements.txt` file. This file is created using the ```pip freeze > requirements.txt``` command to ensure that   
   all necessary packages are included.
   To install these dependencies, run the following command in your terminal:
```pip install -r requirements.txt```
4) Create a database:
``` python manage.py migrate```
5) To start the server use:
   ```python manage.py runserver```

> [!NOTE]  
> The login, password and the path to the database are obtained from the environment variables (.env)

## Using Project URLs
* `pereval/` - a list of all passes and the ability to create them via an html form or json;
  > It includes filtering passes by user's email
* `pereval/<int:pk>/` - information about a particular pass by its id;
  > It includes a delete button, as well as full `(PUT)` and partial `(PATCH)` editing buttons;
* `user/` - list of all users;
* `swagger/` or `redoc/` - using swagger/redoc
  > view all passes and users, as well as their creation, editing and deletion;
* `admin/` - administrative panel
  > You need a super user to log in. To create a superuser, do the command: ``` python manage.py createsuperuser ```

## The project was also published on the Pythonanywhere host server

link :paperclip: - http://splasha.pythonanywhere.com

![4fsp6svu](https://github.com/AnastasiaGundova/Pereval/assets/145155665/17a2a9ee-849c-4b0b-a9d4-ebeb053411bf)

 `Main page`:arrow_up:

![sq9dr095](https://github.com/AnastasiaGundova/Pereval/assets/145155665/6e1f481a-7865-42f7-8f67-7c9058a2ba2d)

 `A page with all mountain passes`:arrow_up:

![image](https://github.com/AnastasiaGundova/Pereval/assets/145155665/efedf654-6a60-4b83-b717-806313764da3)

 `Creating a pass through json`:arrow_up:

![image](https://github.com/AnastasiaGundova/Pereval/assets/145155665/b1dc3d2d-fb34-4cf7-9a29-60aa296a495e)


 `The page of the successfully created pass`:arrow_up:

![image](https://github.com/AnastasiaGundova/Pereval/assets/145155665/7c627ccf-a724-4ad5-8324-132072aa097e)


   `A page with all users`:arrow_up:



