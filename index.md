---
layout: default
section: home
description: Yilei Fu is a computational genomics researcher at Baylor College of Medicine, working on long-read sequencing, DNA methylation, and genetic variation.
---
<div class="container home-content">
  <section class="home-intro">
    <h1>Yilei Fu <span class="name-chinese" lang="zh">付译磊</span></h1>
    <p class="position">Postdoctoral Associate · Human Genome Sequencing Center · Baylor College of Medicine</p>
    <p>I develop computational methods for long-read sequencing, with interests in DNA methylation, haplotype phasing, somatic variation, and rare-disease genomics. I work with <a href="https://fritzsedlazeck.github.io/">Fritz Sedlazeck</a> at Baylor College of Medicine.</p>
    <p>I received my Ph.D. in Computer Science from Rice University in 2023, advised by <a href="https://www.treangenlab.com/">Todd Treangen</a> and Fritz Sedlazeck. <a href="{{ '/about/' | relative_url }}">More about me</a>.</p>
    <div class="profile-links"><a href="{{ site.scholar_url }}">Google Scholar</a><a href="https://github.com/{{ site.github_username }}">GitHub</a><a href="{{ site.orcid_url }}">ORCID</a></div>
  </section>
  <section class="home-section" aria-labelledby="research-title">
    <h2 id="research-title">Research</h2>
    <p>My current work focuses on connecting genetic variation with the additional information carried on long DNA molecules:</p>
    <ul class="research-list"><li><strong>Cell-type-resolved variation:</strong> using methylation to connect somatic variants and tandem-repeat changes with cell types.</li><li><strong>Genetics and epigenetics:</strong> combining sequence and methylation to improve haplotype phasing and genome interpretation.</li><li><strong>All of Us methylation:</strong> studying population-scale DNA methylation, allele-specific patterns, and their relationships with genetic variation. <a href="{{ '/research/#all-of-us' | relative_url }}">Project details</a>.</li><li><strong>Rare-disease analysis:</strong> developing practical workflows for family-based long-read sequencing.</li></ul>
    <p><a href="{{ '/research/' | relative_url }}">Read more about my research</a></p>
  </section>
  <section class="home-section" aria-labelledby="selected-title">
    <div class="section-heading-inline"><h2 id="selected-title">Selected publications</h2><a href="{{ '/publications/' | relative_url }}">All publications</a></div>
    <div class="publication-list">{% assign selected = site.data.publications | where: 'selected', true %}{% for pub in selected limit:5 %}{% include publication.html pub=pub compact=true %}{% endfor %}</div>
  </section>
  <section class="home-section" aria-labelledby="software-title">
    <div class="section-heading-inline"><h2 id="software-title">Software</h2><a href="{{ '/software/' | relative_url }}">More software</a></div>
    <ul class="software-list"><li><a href="https://github.com/Fu-Yilei/SniffCell">SniffCell</a> — Cell-type-resolved variant discovery from bulk long-read sequencing.</li><li><a href="https://github.com/treangenlab/methphaser">MethPhaser</a> — Methylation-informed haplotype phasing.</li><li><a href="https://github.com/Fu-Yilei/TBAS_pipeline">TBAS</a> — Trio-barcoded adaptive sequencing analysis.</li><li><a href="https://github.com/Fu-Yilei/Vulcan">Vulcan</a> — Dual-mode long-read alignment.</li></ul>
  </section>
  <section class="home-section" aria-labelledby="notes-title">
    <div class="section-heading-inline"><h2 id="notes-title">Notes & talks</h2><a href="{{ '/notes/' | relative_url }}">All notes</a></div>
    <ul class="recent-notes">
      <li><time datetime="2026-11-19">Nov 2026</time><a href="https://www.youtube.com/watch?v=77VDKtSW33w">TBAS talk at SVAR26: cost-efficient long-read trio sequencing</a></li>
      <li><time datetime="2025-06-30">Jun 2025</time><a href="https://www.youtube.com/watch?v=Fh3-dmZdvFU">Computational analysis of DNA methylation from long-read sequencing · Labroots recording</a></li>
      <li><time datetime="2024-06-26">Jun 2024</time><a href="https://www.youtube.com/watch?v=YvzpYYDCFrk&amp;t=6s">MethPhase: methylation-based haplotype phasing · Labroots recording</a></li>
      {% assign substantive_posts = site.posts | where_exp: 'post', "post.title != 'About Yilei Fu'" %}{% for post in substantive_posts limit:3 %}<li><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: '%b %Y' }}</time><a href="{{ post.url | relative_url }}">{{ post.title }}</a></li>{% endfor %}
    </ul>
  </section>
</div>
