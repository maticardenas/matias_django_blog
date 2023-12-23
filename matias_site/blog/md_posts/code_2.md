# Dockerfile

## Example of Dockerfile Content


```bash
FROM python:3.11-alpine3.15

LABEL maintainer="cardenasmatias.1990@gmail.com"

ENV PYTHONUNBUFFERED 1

RUN apk update && apk add gcc && apk add g++ && apk add libffi-dev \
   && apk add bash && apk add vim

WORKDIR /usr/football_api

COPY ./football_api ./
COPY poetry.lock pyproject.toml ./

EXPOSE 8000

RUN pip install poetry
RUN poetry install -vvv --no-root

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
```

![img_1.png](../../md_posts/img_1.png)

## Example of Python code


```python
class Post(models.Model):
    author = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE
    )  # linking the user as author, as website is only intended to be used by me
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self) -> None:
        """When I hit the 'publish' button I will set the publish date to now()"""
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
```