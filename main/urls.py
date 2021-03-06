from django.urls import path
from django.views.generic import TemplateView, DetailView
from main import views, models


urlpatterns = [
    path(
        "product/<slug:slug>/",
        DetailView.as_view(model=models.Product,
                           template_name="product_detail.html"),
        name="product",
    ),
    path(
        "products/<slug:tag>/",
        views.ProductListView.as_view(),
        name="product",
    ),
    # path(
    #     "products/",
    #     views.ProductListView.as_view(),
    #     name="products",
    # ),
    path(
        "about-us/",
        TemplateView.as_view(template_name="about_us.html"),
        name="about_us"
    ),
    path(
        "",
        TemplateView.as_view(template_name="home.html"),
        name="home"
    ),
    path(
        "contact-us/",
        views.ContactUsView.as_view(),
        name="contact_us",
    ),
]
