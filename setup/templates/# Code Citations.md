# Code Citations

## License: desconhecido
https://github.com/adrianoOliveiraRocha/mercadinho_online/tree/8976d30d42ba5619269671bf2ce56d4c9be64099/core/templates/core/base.html

```
item">
            <a class="nav-link" href="{% url 'logout' %}">Sair</a>
        </li>
    {% else %}
        <li class="nav-item">
            <a class="nav-link" href="{% url 'login' %}">Entrar</a>
        </li>
    {% endif %}
</ul>
```


## License: desconhecido
https://github.com/caiofall20/Agenda/tree/4a9cf5f743759f1e2e9e2561defb858391ac9f1b/Projeto/agenda/templates/agenda/_layouts/base.html

```
is_authenticated %}
        <li class="nav-item">
            <a class="nav-link" href="{% url 'logout' %}">Sair</a>
        </li>
    {% else %}
        <li class="nav-item">
            <a class="nav-link" href="{% url 'login' %}">Entrar</a>
        </li>
    {% endif %}
</ul>
```


## License: desconhecido
https://github.com/alefdantas/gastu/tree/d7a02588bdf9eeed20b484102aa5b4ad7aa2842e/polls/templates/cadastrarRestaurante.html

```
" href="{% url 'logout' %}">Sair</a>
        </li>
    {% else %}
        <li class="nav-item">
            <a class="nav-link" href="{% url 'login' %}">Entrar</a>
        </li>
    {% endif %}
</ul>
```


## License: MIT
https://github.com/DiegoBrian/Eureka/tree/27cf952b27af7fc8cfcc797dffc43a92c9a16d15/simplemooc/core/templates/base.html

```
% url 'logout' %}">Sair</a>
        </li>
    {% else %}
        <li class="nav-item">
            <a class="nav-link" href="{% url 'login' %}">Entrar</a>
        </li>
    {% endif %}
</ul>
```


## License: desconhecido
https://github.com/paulo9405/gestao_acai_django/tree/8e70858230edc6726fa8206068ea94e6522ea2a8/core/templates/core/venda_list.html

```
</a>
        </li>
    {% else %}
        <li class="nav-item">
            <a class="nav-link" href="{% url 'login' %}">Entrar</a>
        </li>
    {% endif %}
</ul>
```

<div class="container mt-2">
    {% if messages %}
        {% for message in messages %}
            <div class="alert alert-{{ message.tags }} alert-dismissible fade show" role="alert">
                {{ message }}
                <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
            </div>
        {% endfor %}
    {% endif %}
</div>

