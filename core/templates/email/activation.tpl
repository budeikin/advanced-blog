{% extends "mail_templated/base.tpl" %}

{% block subject %}
Activation 
{% endblock %}

{% block body %}
http://127.0.0.1:8000/account/api/v1/activation/confirm/{{token}}
{% endblock %}