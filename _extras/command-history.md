---
layout: page
title: "Command History"
permalink: /command-history/
---

{% include base_path.html %}

<script>
  window.onload = function() {
    var lesson_episodes = [
    {% for episode in site.episodes %}
    "{{ episode.url }}"{% unless forloop.last %},{% endunless %}
    {% endfor %}
    ];

    var xmlHttp = [];  /* Required since we are going to query every episode.*/
    for (i=0; i < lesson_episodes.length; i++) {
      xmlHttp[i] = new XMLHttpRequest();
      xmlHttp[i].episode = lesson_episodes[i];  /* To enable use this later.*/
      xmlHttp[i].onreadystatechange = function() {

        if (this.readyState == 4 && this.status == 200) {
          var parser = new DOMParser();
          var htmlDoc = parser.parseFromString(this.responseText,"text/html");
          var htmlDocArticle = htmlDoc.getElementsByTagName("article")[0];

          var article_here = document.getElementById(this.episode);

          var cblocks = htmlDocArticle. querySelectorAll('div.highlighter-rouge');
      //     window.alert(cblocks.length)

          if (cblocks.length > 0) {
            // var htext = htmlDocArticle.getElementsByTagName("div")[0].innerHTML;

            var htext = htmlDocArticle.getElementsByTagName("h1")[0].innerHTML;

            var htitle = document.createElement('h2');
            htitle.innerHTML = htext;
            article_here.appendChild(htitle);
            var cblock_num = 0;
            for (let cblock of cblocks) {
              cblock_num++;

              //var title = document.createElement('p');
              //title.innerHTML = "<strong>Figure " + cblock_num + ".</strong> "
              //                + cblock.alt;
            var bnum = document.createElement('p');
            bnum.innerHTML = cblock_num;
               
                  
              //article_here.appendChild(bnum);
              article_here.appendChild(cblock);
               
              if (cblock_num < cblocks.code_block) {
                var hr = document.createElement('hr');
                article_here.appendChild(hr);
              }
            }
          }
        }
      }
      episode_url = "{{ relative_root_path }}" + lesson_episodes[i];
      xmlHttp[i].open("GET", episode_url);
      xmlHttp[i].send(null);
    }
  }
</script>
{% comment %}
Create anchor for each one of the episodes.
{% endcomment %}
{% for episode in site.episodes %}
<article id="{{ episode.url }}" class="figures"></article>
{% endfor %}

{% include links.md %}


<!-- 
{% for post in site.snippets %}
{{ post.path | inspect }}
{% endfor %} -->

<!-- {% include {{ site.snippets }}/scheduler/runtime-exceeded-output.snip %} -->
