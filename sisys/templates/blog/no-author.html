{% extends 'base.html' %}
{% load static %}
{% block content %}

    <!-- Inner Banner -->
    <div class="inner-banner">
        <div class="container-fluid">
            <div class="row align-items-center">
                <div class="col-lg-7 col-md-7">
                    <div class="inner-title">
                        <h3> Author </h3>
                        <ul>
                            <li>
                                <a href="{% url 'blog_home' %}">Blog</a>
                            </li>
                            <li> Author</li>
                        </ul>
                    </div>
                </div>

                <div class="col-lg-5 col-md-5">
                    <div class="inner-img">
                        <img src="{% static 'images/inner-banner/inner-banner5.png' %}" alt="Inner Banner"/>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- Inner Banner End -->

    <!-- Blog Page Area -->
    <div class="blog-page-area pt-100 pb-70">
        <div class="container">
            <div class="row">
                <div class="col-lg-4">
                    <div class="side-bar-area pr-20">
                        <h1 style="text-align: center">
                            No Author Found...
                        </h1>

                        <div class="side-bar-widget">
                            <h3 class="title">Popular Tags</h3>
                            <ul class="side-bar-widget-tag">
                                <{% for tag in tags %}
                                <li><a href="{% url 'posts_with_tag' tag %}">{{ tag }} </a></li>
                            {% endfor %}
                            </ul>
                        </div>
                    </div>
                </div>

                <div class="col-lg-8">
                    <div class="row justify-content-center">
                        {% for post in page_obj %}
                            <div class="col-lg-6 col-md-6">
                                <div class="blog-card box-shadow">
                                    <a href="{% url 'post_details' post.id post.slug %}" class="img">
                                        <img src="{{ post.imageURL }}" alt="Blog" width="296" height="193"/>
                                    </a>
                                    <div class="content">
                                        <ul>
                                            <li>
                                                <i class="flaticon-user"></i>
                                                <a href="#">{{ name }}</a>
                                            </li>
                                            <li>
                                                <i class="flaticon-clock"></i>
                                                {{ post.created_on | date }}
                                            </li>
                                        </ul>
                                        <h3><a href="{% url 'post_details' post.id post.slug %}">{{ post.title }}</a>
                                        </h3>
                                        <a href="{% url 'post_details' post.id post.slug %}"
                                           class="default-btn two border-radius-5">Read More
                                            <i
                                                    class="flaticon-arrow-pointing-to-right"></i></a>
                                    </div>
                                </div>
                            </div>
                        {% endfor %}

                        <div class="col-lg-12 col-md-12 text-center">
                            <div class="pagination-area">
                                {% if page_obj.has_previous %}
                                    <a href="?page={{ page_obj.previous_page_number }}"
                                       class="prev page-numbers">
                                        <i class="flaticon-arrow-pointing-to-left"></i>
                                    </a>
                                {% endif %}
                                {% for i in paginator %}
                                    {% if i.number == page_obj.number %}
                                        <span class="page-numbers current"
                                              aria-current="page">{{ i.number }}</span>
                                    {% else %}
                                        <a href="{% url 'author_posts' author %}?page={{ i.number }}"
                                           class="page-numbers">{{ i.number }}</a>
                                    {% endif %}
                                {% endfor %}

                                {% if page_obj.has_next%}
                                    <a href="{% url 'author_posts' author %}?page={{ page_obj.next_page_number }}"
                                       class="next page-numbers">
                                        <i class="flaticon-arrow-pointing-to-right"></i>
                                    </a>
                                {% endif %}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- Blog Page Area End -->

{% endblock %}
