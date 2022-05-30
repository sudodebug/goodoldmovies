countries = [{"id": "australia", "title": "Австралия", "continent": "aus"},
             {"id": "india", "title": "Индия", "continent": "asi"},
             {"id": "poland", "title": "Польша", "continent": "eur"},
             {"id": "mexico", "title": "Мексика", "continent": "amr"},
             ]

<nav>
{% for country in countries %}
  <a href="{{ country.continent }}/{{ country.id }}">{{ country.title }}</a>
{% endfor %}</nav>


<nav>
<a href="/aus/australia/">Австралия</a>
<a href="/asi/india/">Индия</a>
<a href="/eur/poland/">Польша</a>
<a href="/amr/mexico/">Мексика</a>
</nav>
