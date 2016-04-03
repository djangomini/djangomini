# Admin site

In Django - one of the killer features is an **admin site**.
In very short time you can create admin website to manage few Django Models.
Primary this admin site used by admin and managers.

Problems becomes when you need to create customized pages and at the same time support main website,
where users can find public information. For exaple, when you need to edit object not only by site admin,
but also by customers - it creates two wersion of website - one for internal usage, and one - for customers.

We decide that one website for all - is a better solution. First of all - design of website is the same for
all kind of users. Next - you can handle complex logic that can allow to modify the same object by different
groups of users.

### Our solution

We propose you to use extended base classes like `CreateObjectController` to avoid some mistakes when you
coding. To crete, view, edit and delete object - you need to use separate page that handled by a base Controller
with built-in logic to control certain type of operation with requested object.
