"""Defines URL patterns for blog_app."""

from django.urls import path

from . import views

app_name = "blog_app"
urlpatterns = [
    # Home page.
    path("", views.home, name="home"),

    # Show all topics.
    path("topics/", views.topics, name="topics"),

    # Detail page for a single topic.
    path("topics/<int:topic_id>/", views.topic, name="topic"),

    # Page for adding a new topic.
    path("new_topic/", views.new_topic, name="new_topic"),

    # Page for adding a new post.
    path("new_post/<int:topic_id>/", views.new_post, name="new_post"),

    # Page for editing an post.
    path("edit_post/<int:post_id>/", views.edit_post, name="edit_post")
]