from __future__ import annotations

from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parent

ICONS = {
    "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.79 19.79 0 0 1 2.12 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.69 2.8a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.33 1.84.56 2.8.69A2 2 0 0 1 22 16.92z"/>',
    "message": '<path d="M21 15a4 4 0 0 1-4 4H8l-5 3V7a4 4 0 0 1 4-4h10a4 4 0 0 1 4 4z"/><path d="M8 9h8M8 13h5"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "arrow-left": '<path d="M19 12H5M11 18l-6-6 6-6"/>',
    "chevron": '<path d="m6 9 6 6 6-6"/>',
    "shield": '<path d="M20 13c0 5-3.5 7.5-8 9-4.5-1.5-8-4-8-9V5l8-3 8 3z"/><path d="m9 12 2 2 4-4"/>',
    "cloud": '<path d="M17.5 19H6a4 4 0 0 1-.8-7.92A6 6 0 0 1 16.7 9.1 5 5 0 0 1 17.5 19z"/>',
    "network": '<rect x="9" y="2" width="6" height="6" rx="1"/><rect x="2" y="16" width="6" height="6" rx="1"/><rect x="16" y="16" width="6" height="6" rx="1"/><path d="M12 8v4M5 16v-2h14v2"/>',
    "headset": '<path d="M4 14a8 8 0 0 1 16 0"/><path d="M18 19c0 1.7-1.3 3-3 3h-3"/><rect x="3" y="13" width="4" height="6" rx="2"/><rect x="17" y="13" width="4" height="6" rx="2"/>',
    "globe": '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 0 20M12 2a15.3 15.3 0 0 0 0 20"/>',
    "server": '<rect x="3" y="4" width="18" height="6" rx="2"/><rect x="3" y="14" width="18" height="6" rx="2"/><path d="M7 7h.01M7 17h.01M11 7h6M11 17h6"/>',
    "chart": '<path d="M3 3v18h18"/><path d="m7 16 4-5 4 3 5-7"/>',
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
    "check": '<path d="m20 6-11 11-5-5"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "map": '<polygon points="3 6 9 3 15 6 21 3 21 18 15 21 9 18 3 21"/><path d="M9 3v15M15 6v15"/>',
    "wifi": '<path d="M5 12.55a11 11 0 0 1 14.08 0M1.42 9a16 16 0 0 1 21.16 0M8.53 16.11a6 6 0 0 1 6.95 0M12 20h.01"/>',
    "search": '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/>',
    "lock": '<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
    "building": '<path d="M3 21h18M6 21V5l6-3 6 3v16M9 9h.01M9 13h.01M9 17h.01M15 9h.01M15 13h.01M15 17h.01"/>',
    "spark": '<path d="m12 3-1.7 5.3L5 10l5.3 1.7L12 17l1.7-5.3L19 10l-5.3-1.7z"/><path d="m5 3-.7 2.3L2 6l2.3.7L5 9l.7-2.3L8 6l-2.3-.7zM19 16l-.7 2.3L16 19l2.3.7L19 22l.7-2.3L22 19l-2.3-.7z"/>',
    "whatsapp": '<path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8A8.5 8.5 0 0 1 12.5 20a8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8A8.5 8.5 0 0 1 8.7 3.9a8.38 8.38 0 0 1 3.8-.9h.5A8.48 8.48 0 0 1 21 11z"/><path d="M9.2 8.4c.2-.4.4-.4.7-.4h.4c.1 0 .3 0 .4.3l.8 1.8c.1.2.1.4 0 .5l-.6.7c-.1.1-.2.3 0 .5.5.9 1.2 1.6 2.1 2.1.2.1.4.1.5 0l.8-1c.2-.2.4-.2.6-.1l1.8.9c.2.1.3.2.3.4 0 .4-.2 1.3-.7 1.8-.5.5-1.2.8-2 .6-1.2-.2-2.7-.8-4.3-2.2-1.3-1.1-2.2-2.6-2.5-3.7-.3-1 .1-1.8.5-2.2z"/>',
    "bolt": '<path d="m13 2-9 12h8l-1 8 9-12h-8z"/>',
    "route": '<circle cx="6" cy="19" r="3"/><circle cx="18" cy="5" r="3"/><path d="M6 16V8a3 3 0 0 1 3-3h6"/>',
    "mic": '<path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2M12 19v3M8 22h8"/>',
    "video": '<path d="m16 13 5 3V8l-5 3z"/><rect x="3" y="6" width="13" height="12" rx="2"/>',
    "database": '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5v7c0 1.7 4 3 9 3s9-1.3 9-3V5M3 12v7c0 1.7 4 3 9 3s9-1.3 9-3v-7"/>',
    "layers": '<polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/>',
    "sliders": '<path d="M4 21v-7M4 10V3M12 21v-9M12 8V3M20 21v-5M20 12V3M1 14h6M9 8h6M17 16h6"/>',
    "repeat": '<path d="m17 1 4 4-4 4"/><path d="M3 11V9a4 4 0 0 1 4-4h14M7 23l-4-4 4-4"/><path d="M21 13v2a4 4 0 0 1-4 4H3"/>',
    "link": '<path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>',
    "monitor": '<rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/>',
    "smartphone": '<rect x="5" y="2" width="14" height="20" rx="2"/><path d="M12 18h.01"/>',
    "file": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h8"/>',
    "filter": '<path d="M22 3H2l8 9.46V19l4 2v-8.54z"/>',
    "target": '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
    "award": '<circle cx="12" cy="8" r="6"/><path d="M15.5 13.5 17 22l-5-3-5 3 1.5-8.5"/>',
    "heart": '<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.6l-1-1a5.5 5.5 0 0 0-7.8 7.8l1 1L12 21l7.8-7.6 1-1a5.5 5.5 0 0 0 0-7.8z"/>',
    "eye": '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
    "refresh": '<path d="M23 4v6h-6M1 20v-6h6"/><path d="M3.5 9a9 9 0 0 1 14.9-3.4L23 10M1 14l4.6 4.4A9 9 0 0 0 20.5 15"/>',
    "menu": '<path d="M4 6h16M4 12h16M4 18h16"/>',
}


def svg(name: str, cls: str = "icon") -> str:
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS.get(name, ICONS["spark"])}</svg>'


def icon_box(name: str, accent: bool = False) -> str:
    extra = " icon-box--accent" if accent else ""
    return f'<span class="icon-box{extra}">{svg(name)}</span>'


SERVICES = [
    ("PABX Virtual", "pabx-virtual.html", "cloud", "Telefonia em nuvem, ramais e gestão"),
    ("PABX IP", "pabx-ip.html", "network", "Voz, vídeo e colaboração corporativa"),
    ("Omnichannel", "omnichannel.html", "message", "Todos os canais em uma plataforma"),
    ("0800 VOIP", "0800-voip.html", "phone", "Alcance nacional e atendimento gratuito"),
    ("Link Dedicado", "link-dedicado.html", "wifi", "Internet corporativa de alta performance"),
]


def linkset(depth: int) -> dict[str, str]:
    prefix = "../" if depth else ""
    service_prefix = "" if depth else "servicos/"
    return {
        "home": f"{prefix}index.html",
        "company": f"{prefix}empresa.html",
        "solutions": f"{prefix}solucoes.html",
        "blog": f"{prefix}blog.html",
        "contact": f"{prefix}contato.html",
        "assets": f"{prefix}assets/",
        "service_prefix": service_prefix,
    }


def active_class(page: str, current: str, service: bool = False) -> str:
    if service:
        return " is-active" if current == "service" or current == "solutions" else ""
    return " is-active" if current == page else ""


def header(current: str, depth: int = 0) -> str:
    l = linkset(depth)
    service_links = "\n".join(
        f'''<a class="dropdown-link" href="{l['service_prefix']}{file}">
          {icon_box(icon)}
          <span><strong>{name}</strong><small>{desc}</small></span>
        </a>'''
        for name, file, icon, desc in SERVICES
    )
    return dedent(f'''
      <a class="skip-link" href="#conteudo">Ir para o conteúdo</a>
      <div class="scroll-progress" data-scroll-progress aria-hidden="true"></div>
      <div class="topbar">
        <div class="container topbar__inner">
          <div class="topbar__items">
            <a href="tel:+551139950800" aria-label="Ligar para a D.lextel">{svg('phone')} <span>(11) 3995-0800</span></a>
            <span>Atendimento para empresas em todo o Brasil</span>
          </div>
          <div class="topbar__actions">
            <span>Plantão técnico após as 18h: opção 9</span>
            <a href="#" data-whatsapp-message="Olá, vim pelo site da D.lextel e preciso falar com a equipe.">{svg('whatsapp')} WhatsApp</a>
          </div>
        </div>
      </div>
      <header class="site-header" data-site-header>
        <div class="container header__inner">
          <a class="brand" href="{l['home']}" aria-label="D.lextel - Página inicial">
            <img src="{l['assets']}img/logo-dlextel.png" alt="D.lextel Telecomunicações" width="470" height="200">
          </a>
          <button class="nav-toggle" type="button" aria-label="Abrir menu" aria-expanded="false" aria-controls="main-navigation" data-nav-toggle><span></span></button>
          <nav class="main-nav" id="main-navigation" aria-label="Navegação principal" data-main-nav>
            <ul class="nav-list">
              <li><a class="nav-link{active_class('home', current)}" href="{l['home']}"{' aria-current="page"' if current == 'home' else ''}>Início</a></li>
              <li><a class="nav-link{active_class('company', current)}" href="{l['company']}"{' aria-current="page"' if current == 'company' else ''}>A D.lextel</a></li>
              <li class="has-dropdown" data-dropdown>
                <button class="dropdown-trigger{active_class('service', current, True)}" type="button" aria-expanded="false" data-dropdown-trigger>
                  Serviços {svg('chevron', 'nav-chevron')}
                </button>
                <div class="dropdown-menu" aria-label="Serviços D.lextel">
                  {service_links}
                  <a class="dropdown-link" href="{l['solutions']}">
                    {icon_box('layers', True)}
                    <span><strong>Ver todas as soluções</strong><small>Compare e encontre a melhor opção</small></span>
                  </a>
                </div>
              </li>
              <li><a class="nav-link{active_class('blog', current)}" href="{l['blog']}"{' aria-current="page"' if current == 'blog' else ''}>Blog</a></li>
              <li><a class="nav-link{active_class('contact', current)}" href="{l['contact']}"{' aria-current="page"' if current == 'contact' else ''}>Contato</a></li>
            </ul>
            <a class="btn btn--primary btn--sm" href="{l['contact']}">Solicitar proposta {svg('arrow')}</a>
          </nav>
        </div>
      </header>
    ''')


def footer(depth: int = 0) -> str:
    l = linkset(depth)
    service_links = "\n".join(f'<li><a href="{l["service_prefix"]}{file}">{name}</a></li>' for name, file, _, _ in SERVICES)
    return dedent(f'''
      <footer class="site-footer">
        <div class="footer-main">
          <div class="container footer-grid">
            <div class="footer-brand">
              <a href="{l['home']}" aria-label="D.lextel - Início"><img src="{l['assets']}img/logo-dlextel.png" alt="D.lextel Telecomunicações" width="470" height="200" loading="lazy"></a>
              <p>Soluções integradas de comunicação corporativa para conectar equipes, organizar o atendimento e dar mais eficiência à operação.</p>
              <span class="badge badge--dark"><span class="badge-dot"></span> Atendimento nacional</span>
            </div>
            <div>
              <h2 class="footer-title">Institucional</h2>
              <ul class="footer-links">
                <li><a href="{l['home']}">Início</a></li>
                <li><a href="{l['company']}">A D.lextel</a></li>
                <li><a href="{l['solutions']}">Soluções</a></li>
                <li><a href="{l['blog']}">Blog</a></li>
                <li><a href="{l['contact']}">Contato</a></li>
              </ul>
            </div>
            <div>
              <h2 class="footer-title">Serviços</h2>
              <ul class="footer-links">{service_links}</ul>
            </div>
            <div>
              <h2 class="footer-title">Fale com a D.lextel</h2>
              <div class="footer-contact">
                <a href="tel:+551139950800">{svg('phone')} <span><strong>(11) 3995-0800</strong><br>Comercial e atendimento</span></a>
                <a href="#" data-whatsapp-message="Olá, vim pelo site da D.lextel e gostaria de falar com um especialista.">{svg('whatsapp')} <span>Atendimento pelo WhatsApp</span></a>
                <span>{svg('clock')} <span>Plantão técnico emergencial após as 18h, opção 9</span></span>
                <span>{svg('globe')} <span>Soluções para empresas em todo o Brasil</span></span>
              </div>
            </div>
          </div>
        </div>
        <div class="footer-bottom">
          <div class="container footer-bottom__inner">
            <span>© <span data-current-year></span> D.lextel. Todos os direitos reservados.</span>
            <div class="footer-legal">
              <span>Comunicação corporativa com tecnologia, eficiência e suporte especializado.</span>
            </div>
          </div>
        </div>
      </footer>
      <a class="whatsapp-float" href="#" aria-label="Falar com a D.lextel no WhatsApp" data-whatsapp-message="Olá, vim pelo site da D.lextel e gostaria de falar com um especialista.">{svg('whatsapp')}</a>
    ''')


def page_shell(*, title: str, description: str, canonical: str, current: str, content: str, depth: int = 0, extra_scripts: str = "", schema: str = "") -> str:
    l = linkset(depth)
    return dedent(f'''<!doctype html>
    <html lang="pt-BR" class="no-js">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>{title}</title>
      <meta name="description" content="{description}">
      <meta name="theme-color" content="#032b47">
      <meta name="robots" content="index,follow,max-image-preview:large">
      <link rel="canonical" href="{canonical}">
      <meta property="og:locale" content="pt_BR">
      <meta property="og:type" content="website">
      <meta property="og:title" content="{title}">
      <meta property="og:description" content="{description}">
      <meta property="og:url" content="{canonical}">
      <meta property="og:site_name" content="D.lextel Telecomunicações">
      <meta property="og:image" content="https://dlextel.com.br/wp-content/uploads/2021/01/cropped-logo-1.png">
      <meta name="twitter:card" content="summary_large_image">
      <link rel="icon" type="image/png" href="{l['assets']}img/favicon.png">
      <link rel="apple-touch-icon" href="{l['assets']}img/apple-touch-icon.png">
      <link rel="preconnect" href="https://fonts.googleapis.com">
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
      <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Manrope:wght@600;700;800&display=swap" rel="stylesheet">
      <link rel="stylesheet" href="{l['assets']}css/style.css">
      <script>document.documentElement.classList.remove('no-js');</script>
      {schema}
    </head>
    <body>
      <noscript><div class="no-js-note">Ative o JavaScript para usar o menu, as animações, o blog integrado e o formulário guiado.</div></noscript>
      {header(current, depth)}
      <main id="conteudo">{content}</main>
      {footer(depth)}
      <script src="{l['assets']}js/main.js" defer></script>
      {extra_scripts}
    </body>
    </html>
    ''')


def section_head(eyebrow: str, title: str, text: str, center: bool = False) -> str:
    center_class = " section-head--center" if center else ""
    return f'''<div class="section-head{center_class}" data-reveal>
      <span class="eyebrow">{eyebrow}</span>
      <h2>{title}</h2>
      <p>{text}</p>
    </div>'''


def cta_banner(depth: int = 0, title: str = "Pronto para modernizar a comunicação da sua empresa?", text: str = "Converse com um especialista da D.lextel e receba uma orientação inicial sobre a solução mais adequada para sua operação.", message: str = "Olá, vim pelo site da D.lextel e gostaria de solicitar uma avaliação da comunicação da minha empresa.") -> str:
    l = linkset(depth)
    return dedent(f'''
      <section class="section section--sm">
        <div class="container">
          <div class="cta-banner" data-reveal>
            <div class="cta-banner__grid">
              <div>
                <span class="eyebrow">Converse com a equipe</span>
                <h2>{title}</h2>
                <p>{text}</p>
              </div>
              <div class="stack">
                <a class="btn btn--primary" href="#" data-whatsapp-message="{message}">{svg('whatsapp')} Falar no WhatsApp</a>
                <a class="btn btn--ghost-light" href="{l['contact']}">Solicitar contato {svg('arrow')}</a>
              </div>
            </div>
          </div>
        </div>
      </section>
    ''')


def testimonials(depth: int = 0) -> str:
    l = linkset(depth)
    slides = [
        ("cliente-sawary.webp", "Sawary Jeans", "A modernização com PABX IP, 0800 e VoIP trouxe uma economia relatada de 70%, além de mais controle e visibilidade sobre as ligações.", "Soluções integradas de comunicação"),
        ("cliente-central-embalagens.webp", "Central de Embalagens", "A migração da telefonia analógica para o PABX Virtual e o uso do softphone ajudaram a manter as equipes administrativa e comercial conectadas no trabalho remoto.", "PABX Virtual e mobilidade"),
        ("cliente-ambiente-brasil.webp", "Ambiente Brasil Engenharia", "Com PABX Virtual e aplicativo móvel, a empresa relatou melhora na qualidade, redução das filas de recepção e economia de 55% nas ligações.", "Telefonia em nuvem"),
    ]
    rendered = []
    for idx, (image, name, quote, context) in enumerate(slides):
        rendered.append(f'''
          <article class="testimonial-slide" data-slider-slide aria-hidden="{'false' if idx == 0 else 'true'}">
            <div class="testimonial-brand"><img src="{l['assets']}img/{image}" alt="{name}" width="360" height="360" loading="lazy"></div>
            <div class="testimonial-content">
              <span class="quote-mark" aria-hidden="true">“</span>
              <blockquote>{quote}</blockquote>
              <div class="testimonial-meta"><strong>{name}</strong><span>{context}</span></div>
            </div>
          </article>
        ''')
    return dedent(f'''
      <section class="section section--soft">
        <div class="container">
          {section_head('Experiências reais', 'Empresas que evoluíram sua comunicação com a D.lextel', 'Depoimentos do site atual, reorganizados para destacar os impactos percebidos pelos clientes.', True)}
          <div data-testimonial-slider data-reveal>
            <div class="testimonial-shell"><div class="testimonial-track" data-slider-track>{''.join(rendered)}</div></div>
            <div class="slider-controls">
              <div class="slider-dots" data-slider-dots aria-label="Selecionar depoimento"></div>
              <div class="slider-arrows">
                <button class="slider-btn" type="button" aria-label="Depoimento anterior" data-slider-prev>{svg('arrow-left')}</button>
                <button class="slider-btn" type="button" aria-label="Próximo depoimento" data-slider-next>{svg('arrow')}</button>
              </div>
            </div>
          </div>
          <p class="note text-center" style="margin-top:1rem">Percentuais e resultados foram relatados pelos próprios clientes no site atual e podem variar conforme cada operação.</p>
        </div>
      </section>
    ''')


def partners(depth: int = 0) -> str:
    l = linkset(depth)
    return dedent(f'''
      <section class="section section--sm">
        <div class="container">
          {section_head('Ecossistema tecnológico', 'Parcerias que fortalecem nossas soluções', 'Tecnologias e fabricantes reconhecidos para construir projetos confiáveis, escaláveis e alinhados às necessidades de cada empresa.', True)}
          <div class="partners-panel" data-reveal>
            <img src="{l['assets']}img/parceiros.webp" alt="Parceiros D.lextel: Khomp, AWS, 3CX Partner, VoIP Group e Yealink" width="1359" height="222" loading="lazy">
          </div>
        </div>
      </section>
    ''')


def faq(items: list[tuple[str, str]]) -> str:
    rendered = []
    for index, (question, answer) in enumerate(items):
        aid = f"faq-answer-{index+1}"
        rendered.append(f'''
          <article class="faq-item" data-faq-item>
            <button class="faq-question" type="button" aria-expanded="false" aria-controls="{aid}" data-faq-button>
              <span>{question}</span><span class="faq-plus" aria-hidden="true"></span>
            </button>
            <div class="faq-answer" id="{aid}"><div class="faq-answer__inner"><div class="faq-answer__content"><p>{answer}</p></div></div></div>
          </article>
        ''')
    return f'<div class="faq-list">{"".join(rendered)}</div>'


def inner_hero(*, depth: int, eyebrow: str, title: str, lead: str, breadcrumb: str, visual: str, message: str) -> str:
    l = linkset(depth)
    return dedent(f'''
      <section class="inner-hero">
        <canvas class="network-canvas" data-network-canvas aria-hidden="true"></canvas>
        <div class="container inner-hero__grid">
          <div class="inner-hero__content" data-reveal="left">
            <nav class="breadcrumbs" aria-label="Navegação estrutural"><span><a href="{l['home']}">Início</a></span><span>{breadcrumb}</span></nav>
            <span class="eyebrow">{eyebrow}</span>
            <h1>{title}</h1>
            <p class="inner-hero__lead">{lead}</p>
            <div class="hero__actions">
              <a class="btn btn--primary" href="#" data-whatsapp-message="{message}">{svg('whatsapp')} Falar com especialista</a>
              <a class="btn btn--ghost-light" href="#detalhes">Conhecer a solução {svg('arrow')}</a>
            </div>
          </div>
          <div data-reveal="right">{visual}</div>
        </div>
      </section>
    ''')


# ---------- Home ----------
def home_page() -> str:
    solution_cards = [
        ("cloud", "PABX Virtual", "Telefonia em nuvem para organizar chamadas, habilitar ramais no celular e no computador e acompanhar a operação com mais controle.", "servicos/pabx-virtual.html"),
        ("network", "PABX IP", "Comunicação por voz, vídeo e chat sobre a rede de dados, com mobilidade, integrações e recursos corporativos avançados.", "servicos/pabx-ip.html"),
        ("message", "Omnichannel", "WhatsApp, telefonia, e-mail, chat e redes sociais centralizados para sua equipe atender sem perder o histórico do cliente.", "servicos/omnichannel.html"),
        ("phone", "0800 VOIP", "Um número nacional e gratuito para quem liga, conectado à sua central de atendimento, URA, equipes e ramais.", "servicos/0800-voip.html"),
        ("wifi", "Link Dedicado", "Conectividade corporativa via fibra, com velocidade simétrica, baixa latência, monitoramento NOC e opção Lan to Lan.", "servicos/link-dedicado.html"),
    ]
    cards = []
    for idx, (icon, title, text, url) in enumerate(solution_cards):
        cards.append(f'''
          <article class="card solution-card card-grid-line" data-reveal data-reveal-delay="{min(idx+1,5)}">
            {icon_box(icon)}<h3>{title}</h3><p>{text}</p>
            <a class="btn btn--link" href="{url}">Ver detalhes {svg('arrow')}</a>
          </article>
        ''')

    need_tabs = [
        ("calls", "phone", "Não perder ligações", "PABX Virtual"),
        ("channels", "message", "Centralizar canais", "Omnichannel"),
        ("national", "globe", "Atender todo o Brasil", "0800 VOIP"),
        ("internet", "wifi", "Melhorar conectividade", "Link Dedicado"),
        ("integration", "link", "Integrar sistemas", "PABX + API"),
    ]
    tabs = "".join(f'''<button class="need-tab{' is-active' if i == 0 else ''}" type="button" role="tab" data-need-tab="{key}">{svg(icon)}<strong>{label}</strong><span>›</span></button>''' for i, (key, icon, label, _) in enumerate(need_tabs))
    panels_data = {
        "calls": ("Organize o fluxo de chamadas e reduza oportunidades perdidas", "Distribua ligações por filas, departamentos e horários. Atenda pelo celular ou computador, acompanhe chamadas perdidas e mantenha uma comunicação profissional mesmo com equipes remotas.", "PABX Virtual", "servicos/pabx-virtual.html", ["URA e filas de atendimento", "Softphone e ramal móvel", "Gravações e relatórios"]),
        "channels": ("Um histórico único para todos os canais de atendimento", "Reúna WhatsApp, voz, e-mail, chat e redes sociais em uma plataforma com filas, transferências, protocolos, automações, auditoria e relatórios.", "Omnichannel", "servicos/omnichannel.html", ["Caixa de entrada unificada", "Automação e inteligência artificial", "Dashboards de operação"]),
        "national": ("Facilite o contato com clientes em qualquer região do país", "Disponibilize um número 0800 exclusivo e direcione as chamadas para sua central, URA, PABX, aplicativo ou equipes distribuídas.", "0800 VOIP", "servicos/0800-voip.html", ["Número único nacional", "Chamadas simultâneas", "Integração com a central"]),
        "internet": ("Garanta performance para aplicações críticas da empresa", "Tenha link dedicado em fibra, velocidade full duplex, baixa latência e monitoramento contínuo para sustentar voz, cloud, videoconferência e sistemas corporativos.", "Link Dedicado", "servicos/link-dedicado.html", ["Velocidade simétrica", "NOC 24x7x365", "Lan to Lan e MPLS"]),
        "integration": ("Conecte telefonia, CRM e processos internos", "Use APIs e integrações para identificar clientes, registrar chamadas, anexar gravações e automatizar fluxos entre a comunicação e os sistemas da empresa.", "PABX integrado", "servicos/pabx-virtual.html", ["Integração com CRM", "Microsoft Teams", "WhatsApp e sistemas internos"]),
    }
    panels = []
    for i, (key, _) in enumerate([(x[0], x) for x in need_tabs]):
        title, text, result, url, bullets = panels_data[key]
        panels.append(f'''
          <div class="need-panel{' is-active' if i == 0 else ''}" role="tabpanel" data-need-panel="{key}"{' hidden' if i else ''}>
            <span class="eyebrow">Diagnóstico rápido</span><h3>{title}</h3><p>{text}</p>
            <ul class="check-list">{''.join(f'<li>{b}</li>' for b in bullets)}</ul>
            <div class="need-result"><div><strong>Solução indicada: {result}</strong><span>Conheça recursos, aplicações e benefícios.</span></div><a class="btn btn--brand btn--sm" href="{url}">Explorar {svg('arrow')}</a></div>
          </div>
        ''')

    blog_cards = [
        ("Omnichannel", "16 de abril de 2025", "Omnichannel: o que é, como funciona e exemplos práticos", "Entenda como integrar os canais e manter o contexto do cliente durante toda a jornada.", "https://dlextel.com.br/omnichannel-o-que-e/"),
        ("Gestão de telecom", "14 de abril de 2025", "Redução de custos em telecomunicações", "Estratégias para revisar a operação, modernizar a telefonia e ganhar eficiência.", "https://dlextel.com.br/reducao-de-custos/"),
        ("Telefonia VoIP", "11 de abril de 2025", "O que é VoIP e como essa tecnologia funciona", "Conheça as aplicações da telefonia pela internet no ambiente corporativo.", "https://dlextel.com.br/o-que-e-voip/"),
    ]
    blog_html = "".join(f'''
      <article class="blog-card" data-reveal data-reveal-delay="{i+1}">
        <a class="blog-card__media" href="{url}" target="_blank" rel="noopener noreferrer"><span class="blog-card__placeholder"><span>{svg('file')} Conteúdo D.lextel</span></span></a>
        <div class="blog-card__body"><div class="blog-card__meta"><span>{cat}</span><span>•</span><time>{date}</time></div><h3><a href="{url}" target="_blank" rel="noopener noreferrer">{title}</a></h3><p>{excerpt}</p><a class="btn btn--link" href="{url}" target="_blank" rel="noopener noreferrer">Ler artigo {svg('arrow')}</a></div>
      </article>'''
      for i, (cat, date, title, excerpt, url) in enumerate(blog_cards)
    )

    content = dedent(f'''
      <section class="hero">
        <canvas class="network-canvas" data-network-canvas aria-hidden="true"></canvas>
        <div class="container hero__grid">
          <div class="hero__content" data-reveal="left">
            <span class="eyebrow">Comunicação corporativa integrada</span>
            <h1>Toda a comunicação da sua empresa. <span class="text-accent">Conectada.</span></h1>
            <p class="hero__lead">PABX Virtual, Telefonia VoIP, Omnichannel, 0800 e conectividade corporativa em projetos pensados para reduzir custos, aumentar a produtividade e melhorar o atendimento.</p>
            <div class="hero__actions">
              <a class="btn btn--primary" href="#" data-whatsapp-message="Olá, vim pelo site da D.lextel e gostaria de avaliar as soluções para minha empresa.">{svg('whatsapp')} Falar com especialista</a>
              <a class="btn btn--ghost-light" href="solucoes.html">Conhecer soluções {svg('arrow')}</a>
            </div>
            <ul class="hero__trust"><li>Atendimento nacional</li><li>Projetos personalizados</li><li>Suporte especializado</li></ul>
          </div>
          <div class="hero-visual" data-reveal="right">
            <span class="hero-visual__glow"></span>
            <img class="hero-device" src="assets/img/pabx-virtual-voip.webp" alt="Soluções D.lextel em computador, celulares e telefone IP" width="613" height="477">
            <div class="floating-card floating-card--one"><span class="status-dot"></span><span><strong>Operação conectada</strong><small>Voz, chat e canais digitais</small></span></div>
            <div class="floating-card floating-card--two"><span class="signal-bars"><i></i><i></i><i></i><i></i></span><span><strong>Mais controle</strong><small>Relatórios em tempo real</small></span></div>
            <div class="floating-card floating-card--three">{icon_box('shield', True)}<span><strong>Comunicação segura</strong><small>Cloud e suporte técnico</small></span></div>
          </div>
        </div>
        <a class="hero-scroll" href="#solucoes">Descubra</a>
      </section>
      <div class="trust-strip">
        <div class="container trust-strip__inner">
          <div class="trust-item">{icon_box('globe')}<span><strong>Atendimento nacional</strong><small>Soluções para todo o Brasil</small></span></div>
          <div class="trust-item">{icon_box('shield')}<span><strong>Empresa licenciada</strong><small>Atuação informada junto à Anatel</small></span></div>
          <div class="trust-item">{icon_box('sliders')}<span><strong>Projeto sob medida</strong><small>Plano conforme sua operação</small></span></div>
          <div class="trust-item">{icon_box('headset')}<span><strong>Suporte especializado</strong><small>Da implantação à evolução</small></span></div>
        </div>
      </div>

      <section class="section" id="solucoes">
        <div class="container">
          {section_head('Portfólio completo', 'Soluções para cada etapa da comunicação da sua empresa', 'Telefonia, atendimento e conectividade trabalhando de forma integrada — com flexibilidade para acompanhar o crescimento da operação.', True)}
          <div class="grid-5">{''.join(cards)}</div>
        </div>
      </section>

      <section class="section section--soft">
        <div class="container">
          {section_head('Encontre o melhor caminho', 'Comece pelo desafio da sua empresa', 'Selecione o cenário que mais se aproxima da sua necessidade para entender qual solução pode gerar mais impacto.', False)}
          <div class="need-selector" data-need-selector data-reveal>
            <div class="need-tabs" role="tablist" aria-label="Necessidades de comunicação">{tabs}</div>
            <div class="need-panels">{''.join(panels)}</div>
          </div>
        </div>
      </section>

      <section class="section" id="integracao">
        <div class="container integration-grid">
          <div class="integration-copy" data-reveal="left">
            <span class="eyebrow">Comunicação unificada</span>
            <h2>Uma infraestrutura central para conectar pessoas, canais e sistemas</h2>
            <p class="lead">A D.lextel reúne voz, atendimento digital, mobilidade, conectividade e integrações para que sua equipe trabalhe com menos ruído e mais contexto.</p>
            <ul class="check-list">
              <li>Ramais no telefone IP, celular, computador e Microsoft Teams</li>
              <li>WhatsApp, chat, e-mail, voz e redes sociais em um só fluxo</li>
              <li>Integrações com CRM, banco de dados e sistemas internos</li>
              <li>Relatórios, gravações, filas, protocolos e acompanhamento em tempo real</li>
            </ul>
            <a class="btn btn--brand" href="solucoes.html" style="margin-top:1.5rem">Ver arquitetura de soluções {svg('arrow')}</a>
          </div>
          <div class="integration-visual" aria-label="Diagrama de comunicação integrada" data-reveal="right">
            <span class="integration-line integration-line--1"></span><span class="integration-line integration-line--2"></span><span class="integration-line integration-line--3"></span><span class="integration-line integration-line--4"></span><span class="integration-line integration-line--5"></span><span class="integration-line integration-line--6"></span>
            <div class="integration-core"><span><strong>D.lextel</strong><br><small>Comunicação integrada</small></span></div>
            <div class="integration-node integration-node--1">{svg('phone')}<strong>Telefonia</strong></div>
            <div class="integration-node integration-node--2">{svg('message')}<strong>WhatsApp e chat</strong></div>
            <div class="integration-node integration-node--3">{svg('database')}<strong>CRM e sistemas</strong></div>
            <div class="integration-node integration-node--4">{svg('wifi')}<strong>Conectividade</strong></div>
            <div class="integration-node integration-node--5">{svg('chart')}<strong>Relatórios</strong></div>
            <div class="integration-node integration-node--6">{svg('users')}<strong>Equipes</strong></div>
          </div>
        </div>
      </section>

      <section class="section section--brand">
        <div class="container">
          {section_head('Infraestrutura para crescer', 'Tecnologia, alcance e acompanhamento da operação', 'Recursos que sustentam uma comunicação corporativa mais previsível, escalável e preparada para o dia a dia.', True)}
          <div class="stats-grid" data-reveal>
            <div class="stat"><span class="stat__value" data-counter="100" data-suffix="%">0%</span><span class="stat__label">da velocidade contratada no Link Dedicado full duplex</span></div>
            <div class="stat"><span class="stat__value" data-counter="24" data-suffix="×7">0</span><span class="stat__label">monitoramento contínuo pelo NOC</span></div>
            <div class="stat"><span class="stat__value" data-counter="5">0</span><span class="stat__label">frentes de solução em um único portfólio</span></div>
            <div class="stat"><span class="stat__value" data-counter="1">0</span><span class="stat__label">parceiro para integrar comunicação e conectividade</span></div>
          </div>
        </div>
      </section>

      <section class="section">
        <div class="container split">
          <div class="split__media" data-reveal="left">
            <img src="assets/img/business-meeting.webp" alt="Profissionais analisando um projeto corporativo" width="1024" height="683" loading="lazy">
            <div class="split__floating"><strong>Projeto consultivo</strong><span>Entendimento, desenho, implantação e suporte.</span></div>
          </div>
          <div data-reveal="right">
            <span class="eyebrow">Sobre a D.lextel</span>
            <h2>Comunicação inteligente para o crescimento do seu negócio</h2>
            <p class="lead">A D.lextel é uma provedora de soluções integradas de comunicação corporativa, com foco em PABX em nuvem, Telefonia VoIP, Omnichannel, 0800 e conectividade.</p>
            <p>O trabalho combina consultoria, projeto personalizado e suporte técnico para conectar empresas e pessoas com mais eficiência, controle e flexibilidade.</p>
            <ul class="check-list"><li>Equipe técnica qualificada e certificada</li><li>Soluções flexíveis e escaláveis</li><li>Atendimento próximo em todas as etapas</li></ul>
            <a class="btn btn--brand" href="empresa.html" style="margin-top:1.5rem">Conhecer a D.lextel {svg('arrow')}</a>
          </div>
        </div>
      </section>

      <section class="section section--blue">
        <div class="container">
          {section_head('Como trabalhamos', 'Da necessidade à operação, com acompanhamento em cada etapa', 'Um processo consultivo para reduzir riscos, organizar a implantação e construir uma solução que acompanhe a empresa.', True)}
          <div class="process-grid">
            <article class="process-card" data-reveal><h3>Diagnóstico</h3><p>Entendimento do cenário, dos canais, da equipe e dos principais gargalos.</p></article>
            <article class="process-card" data-reveal data-reveal-delay="1"><h3>Projeto</h3><p>Definição da arquitetura, dos recursos, integrações e plano de implantação.</p></article>
            <article class="process-card" data-reveal data-reveal-delay="2"><h3>Implantação</h3><p>Configuração, testes, portabilidade quando necessária e orientação à equipe.</p></article>
            <article class="process-card" data-reveal data-reveal-delay="3"><h3>Evolução</h3><p>Suporte especializado, acompanhamento e ajustes conforme a operação cresce.</p></article>
          </div>
        </div>
      </section>

      {testimonials(0)}
      {partners(0)}

      <section class="section section--soft">
        <div class="container">
          <div class="section-head" data-reveal><span class="eyebrow">Conteúdo e tendências</span><h2>Novidades no Blog D.lextel</h2><p>Guias e análises para ajudar empresas a tomar decisões melhores sobre telefonia, atendimento e conectividade.</p></div>
          <div class="blog-grid">{blog_html}</div>
          <div class="text-center" style="margin-top:2rem"><a class="btn btn--brand" href="blog.html">Acessar todos os conteúdos {svg('arrow')}</a></div>
        </div>
      </section>
      {cta_banner(0)}
    ''')

    schema = dedent('''
      <script type="application/ld+json">
      {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "D.lextel Telecomunicações",
        "url": "https://dlextel.com.br/",
        "logo": "https://dlextel.com.br/wp-content/uploads/2021/01/cropped-logo-1.png",
        "telephone": "+55 11 3995-0800",
        "areaServed": "BR",
        "description": "Soluções integradas de comunicação corporativa, PABX Virtual, VoIP, Omnichannel, 0800 e Link Dedicado."
      }
      </script>
    ''')
    return page_shell(
        title="D.lextel | PABX Virtual, Omnichannel, 0800 e Link Dedicado",
        description="Comunicação corporativa integrada com PABX Virtual, Telefonia VoIP, Omnichannel, 0800 e Link Dedicado para empresas em todo o Brasil.",
        canonical="https://dlextel.com.br/",
        current="home",
        content=content,
        schema=schema,
    )


# ---------- Company ----------
def company_page() -> str:
    visual = '''<div class="inner-visual"><span class="inner-visual__orb"></span><div class="inner-visual__frame"><img src="assets/img/business-meeting.webp" alt="Equipe em reunião de projeto corporativo" width="1024" height="683"></div></div>'''
    content = inner_hero(depth=0, eyebrow="Tecnologia com proximidade", title="Conectamos empresas e pessoas com eficiência, inovação e suporte", lead="A D.lextel desenvolve projetos de comunicação corporativa que integram telefonia, atendimento digital e conectividade em uma operação mais simples de administrar.", breadcrumb="A D.lextel", visual=visual, message="Olá, quero conhecer melhor a D.lextel e entender como a empresa pode apoiar nosso projeto de comunicação.")
    content += dedent(f'''
      <section class="section" id="detalhes">
        <div class="container split">
          <div data-reveal="left">
            <span class="eyebrow">Quem somos</span>
            <h2>Uma parceira para transformar a comunicação da sua empresa</h2>
            <p class="lead">A D.lextel é especializada em PABX Virtual em nuvem, Telefonia VoIP, Plataforma Omnichannel, números 0800 e conectividade corporativa.</p>
            <p>O objetivo é conectar pessoas e negócios de forma inteligente, reunindo tecnologias de comunicação e atendimento em projetos flexíveis, seguros e escaláveis.</p>
            <p>Com atuação consultiva, a equipe busca compreender as particularidades de cada cliente para combinar desempenho, confiabilidade, mobilidade e suporte especializado.</p>
          </div>
          <div class="timeline" data-reveal="right">
            <article class="timeline-item"><h3>Entendimento do negócio</h3><p>Levantamento do cenário, dos canais, da estrutura e dos objetivos da empresa.</p></article>
            <article class="timeline-item"><h3>Arquitetura personalizada</h3><p>Combinação de recursos de voz, atendimento, internet e integrações.</p></article>
            <article class="timeline-item"><h3>Implantação acompanhada</h3><p>Configuração, testes e orientação para que a transição aconteça com segurança.</p></article>
            <article class="timeline-item"><h3>Suporte e evolução</h3><p>Acompanhamento técnico para ajustar a solução conforme novas necessidades surgem.</p></article>
          </div>
        </div>
      </section>

      <section class="section section--soft">
        <div class="container">
          {section_head('Direção da empresa', 'Missão, visão e valores que orientam cada projeto', 'Tecnologia só gera valor quando vem acompanhada de transparência, responsabilidade e compromisso com a operação do cliente.', True)}
          <div class="grid-3">
            <article class="card mv-card" data-reveal>{icon_box('target', True)}<h3>Missão</h3><p>Conectar empresas e pessoas por meio de soluções inteligentes em comunicação corporativa, com tecnologia, qualidade e suporte especializado.</p></article>
            <article class="card mv-card" data-reveal data-reveal-delay="1">{icon_box('eye')}<h3>Visão</h3><p>Ser referência nacional em PABX Virtual, Telefonia VoIP e Omnichannel, reconhecida pela inovação, confiabilidade e excelência no atendimento.</p></article>
            <article class="card mv-card" data-reveal data-reveal-delay="2">{icon_box('heart')}<h3>Valores</h3><p>Transparência, ética, responsabilidade, inovação contínua, colaboração, respeito às pessoas e foco em resultados sustentáveis.</p></article>
          </div>
        </div>
      </section>

      <section class="section">
        <div class="container service-showcase">
          <div data-reveal="left">
            <span class="eyebrow">Suporte especializado</span>
            <h2>Uma equipe que acompanha sua operação, não apenas a instalação</h2>
            <p class="lead">O atendimento técnico faz parte da solução: da definição do projeto ao suporte cotidiano, com orientação para aproveitar melhor os recursos contratados.</p>
            <div class="grid-2" style="margin-top:1.5rem">
              <article class="card">{icon_box('users')}<h3>Equipe qualificada</h3><p>Profissionais preparados para entender ambientes corporativos e necessidades de atendimento.</p></article>
              <article class="card">{icon_box('headset')}<h3>Atendimento próximo</h3><p>Suporte para configurações, dúvidas, ajustes e evolução da operação.</p></article>
              <article class="card">{icon_box('shield')}<h3>Confiabilidade</h3><p>Projetos com foco em disponibilidade, segurança e continuidade da comunicação.</p></article>
              <article class="card">{icon_box('refresh')}<h3>Evolução contínua</h3><p>Soluções escaláveis que podem acompanhar novas equipes, canais e integrações.</p></article>
            </div>
          </div>
          <div class="service-showcase__media service-showcase__media--contain" data-reveal="right"><img src="assets/img/suporte-premium.webp" alt="Ilustração de suporte técnico remoto" width="500" height="350" loading="lazy"></div>
        </div>
      </section>

      <section class="section section--brand">
        <div class="container">
          {section_head('Por que D.lextel', 'Um portfólio integrado para reduzir complexidade', 'Telefonia, atendimento e conectividade podem ser planejados como partes da mesma estratégia — com um parceiro que conhece toda a arquitetura.', True)}
          <div class="grid-4">
            <article class="card card--dark" data-reveal>{icon_box('layers', True)}<h3>Soluções integradas</h3><p>Voz, canais digitais, internet, 0800 e integrações em uma visão única.</p></article>
            <article class="card card--dark" data-reveal data-reveal-delay="1">{icon_box('sliders', True)}<h3>Flexibilidade</h3><p>Recursos e módulos selecionados conforme o porte e a operação.</p></article>
            <article class="card card--dark" data-reveal data-reveal-delay="2">{icon_box('globe', True)}<h3>Alcance nacional</h3><p>Atendimento a empresas de diferentes regiões do Brasil.</p></article>
            <article class="card card--dark" data-reveal data-reveal-delay="3">{icon_box('award', True)}<h3>Compromisso técnico</h3><p>Consultoria, implantação e suporte orientados à qualidade do serviço.</p></article>
          </div>
        </div>
      </section>
      {testimonials(0)}
      {partners(0)}
      {cta_banner(0, 'Vamos construir uma comunicação mais eficiente para sua empresa?', 'Apresente seu cenário à equipe da D.lextel e receba uma recomendação inicial de arquitetura e serviços.', 'Olá, quero conversar sobre um projeto de comunicação corporativa com a D.lextel.')}
    ''')
    return page_shell(title="A D.lextel | Comunicação corporativa e telecomunicações", description="Conheça a D.lextel, provedora de soluções integradas de comunicação corporativa, telefonia VoIP, Omnichannel, 0800 e conectividade.", canonical="https://dlextel.com.br/quem-somos/", current="company", content=content)


# ---------- Solutions ----------
def solutions_page() -> str:
    visual = '''<div class="inner-visual"><span class="inner-visual__orb"></span><div class="inner-visual__frame inner-visual__frame--contain"><img src="assets/img/integracoes.webp" alt="Integrações entre WhatsApp, Microsoft Teams, CRM e sistemas internos" width="760" height="674"></div></div>'''
    cards_data = [
        ("01", "cloud", "PABX Virtual", "Organize o atendimento e leve os ramais para a nuvem, com mobilidade, gravações, filas, relatórios e integrações.", ["URA e fluxos", "Softphone", "Relatórios e gravações"], "servicos/pabx-virtual.html"),
        ("02", "network", "PABX IP", "Use a rede de dados para voz, vídeo e colaboração, com flexibilidade para diferentes portes e estruturas.", ["Voz e videoconferência", "Roteamento inteligente", "CRM e aplicativos"], "servicos/pabx-ip.html"),
        ("03", "message", "Omnichannel", "Centralize os canais digitais e de voz para dar contexto à equipe e continuidade à experiência do cliente.", ["Caixa unificada", "Automação e IA", "Auditoria e dashboards"], "servicos/omnichannel.html"),
        ("04", "phone", "0800 VOIP", "Ofereça um canal nacional gratuito para quem liga e conecte o número à sua central, URA e equipes.", ["Número exclusivo", "Ligações simultâneas", "Portabilidade"], "servicos/0800-voip.html"),
        ("05", "wifi", "Link Dedicado", "Sustente aplicações críticas com fibra, velocidade full duplex, baixa latência e monitoramento NOC.", ["10 Mbps a 10 Gbps", "NOC 24x7x365", "Lan to Lan/MPLS"], "servicos/link-dedicado.html"),
    ]
    cards = "".join(f'''
      <article class="card solution-overview-card" data-reveal data-reveal-delay="{min(i+1,5)}">
        <span class="solution-overview-card__number">{num}</span>
        <div>{icon_box(icon)}<h3 style="margin-top:1.3rem">{title}</h3><p>{text}</p><ul class="check-list">{''.join(f'<li>{x}</li>' for x in bullets)}</ul></div>
        <a class="btn btn--brand" href="{url}">Ver solução {svg('arrow')}</a>
      </article>'''
      for i, (num, icon, title, text, bullets, url) in enumerate(cards_data)
    )
    content = inner_hero(depth=0, eyebrow="Portfólio D.lextel", title="Soluções integradas para comunicação, atendimento e conectividade", lead="Escolha uma solução específica ou combine diferentes frentes em um projeto único, desenhado para a realidade da sua empresa.", breadcrumb="Soluções", visual=visual, message="Olá, gostaria de entender quais soluções D.lextel são mais indicadas para minha empresa.")
    content += dedent(f'''
      <section class="section" id="detalhes">
        <div class="container">
          {section_head('Escolha por objetivo', 'Cinco frentes para modernizar a comunicação da empresa', 'Cada serviço tem uma função clara e pode ser combinado aos demais para ampliar produtividade, controle e experiência do cliente.', True)}
          <div class="grid-3">{cards}</div>
        </div>
      </section>

      <section class="section section--soft">
        <div class="container">
          {section_head('Comparativo rápido', 'Qual solução atende melhor cada necessidade?', 'Use a tabela como ponto de partida. O desenho final depende do porte, dos canais, da infraestrutura e dos objetivos da operação.', False)}
          <div class="compare-wrap" data-reveal>
            <table class="compare-table">
              <thead><tr><th>Solução</th><th>Principal objetivo</th><th>Indicada para</th><th>Recursos de destaque</th></tr></thead>
              <tbody>
                <tr><td>PABX Virtual</td><td>Organizar telefonia e ramais na nuvem</td><td>Equipes presenciais, híbridas ou remotas</td><td>URA, filas, softphone, gravação, relatórios e integrações</td></tr>
                <tr><td>PABX IP</td><td>Unificar voz, vídeo e colaboração sobre IP</td><td>PMEs, corporações e call centers</td><td>Roteamento, videoconferência, mobilidade e CRM</td></tr>
                <tr><td>Omnichannel</td><td>Centralizar canais e histórico do cliente</td><td>Atendimento, vendas, suporte e contact center</td><td>WhatsApp, voz, e-mail, redes sociais, automação e IA</td></tr>
                <tr><td>0800 VOIP</td><td>Criar um canal nacional gratuito para quem liga</td><td>SAC, televendas, ouvidoria e suporte</td><td>Número exclusivo, URA, simultaneidade e portabilidade</td></tr>
                <tr><td>Link Dedicado</td><td>Garantir conectividade corporativa previsível</td><td>Operações críticas, cloud, voz e filiais</td><td>Fibra, full duplex, NOC, baixa latência e Lan to Lan</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>

      <section class="section">
        <div class="container split">
          <div data-reveal="left">
            <span class="eyebrow">Combinação inteligente</span>
            <h2>Mais resultado quando as soluções trabalham juntas</h2>
            <p class="lead">A telefonia depende de conectividade; o atendimento precisa de histórico; o 0800 ganha eficiência com URA, filas e relatórios. A integração evita silos e simplifica a gestão.</p>
            <ul class="check-list"><li>PABX + Omnichannel para unir voz e mensageria</li><li>0800 + PABX para distribuir chamadas com inteligência</li><li>Link Dedicado + Cloud para garantir performance</li><li>API + CRM para registrar interações e automatizar processos</li></ul>
          </div>
          <div class="service-showcase__media service-showcase__media--contain" data-reveal="right"><img src="assets/img/pabx-virtual-voip.webp" alt="Ecossistema de telefonia D.lextel" width="613" height="477" loading="lazy"></div>
        </div>
      </section>

      <section class="section section--brand">
        <div class="container">
          {section_head('Projeto consultivo', 'Como escolher sem complicar', 'A equipe D.lextel ajuda a transformar objetivos de negócio em uma arquitetura de comunicação clara, dimensionada e escalável.', True)}
          <div class="process-grid">
            <article class="process-card" data-reveal><h3>Mapeie os canais</h3><p>Telefonia, WhatsApp, chat, e-mail, redes sociais, internet e sistemas.</p></article>
            <article class="process-card" data-reveal data-reveal-delay="1"><h3>Entenda os volumes</h3><p>Usuários, ramais, chamadas, atendimentos, unidades e horários de pico.</p></article>
            <article class="process-card" data-reveal data-reveal-delay="2"><h3>Defina prioridades</h3><p>Economia, mobilidade, qualidade, experiência, gestão ou continuidade.</p></article>
            <article class="process-card" data-reveal data-reveal-delay="3"><h3>Desenhe a evolução</h3><p>Implante o essencial e deixe a solução pronta para novos módulos.</p></article>
          </div>
        </div>
      </section>

      <section class="section section--soft">
        <div class="container container--narrow">
          {section_head('Dúvidas frequentes', 'Antes de escolher sua solução', 'Respostas iniciais para orientar a avaliação do projeto.', True)}
          {faq([
            ('É possível contratar mais de uma solução?', 'Sim. O portfólio foi pensado para integração. PABX, Omnichannel, 0800 e conectividade podem fazer parte da mesma arquitetura.'),
            ('A D.lextel atende empresas fora de São Paulo?', 'O site atual informa atuação em todo o Brasil, com projetos personalizados para empresas de diferentes regiões.'),
            ('É necessário trocar toda a infraestrutura?', 'Nem sempre. A equipe avalia o ambiente atual, os equipamentos, os links e os sistemas para definir o melhor caminho de migração.'),
            ('As soluções podem crescer junto com a empresa?', 'Sim. A proposta é trabalhar com recursos escaláveis, adicionando ramais, usuários, canais, módulos e integrações conforme a operação evolui.'),
            ('Como recebo uma proposta?', 'Preencha o formulário guiado ou chame no WhatsApp. A equipe fará um levantamento inicial antes de dimensionar a solução.'),
          ])}
        </div>
      </section>
      {cta_banner(0, 'Não sabe por onde começar?', 'Conte o principal desafio da sua empresa. A equipe D.lextel ajuda a identificar a combinação de soluções mais adequada.', 'Olá, preciso de ajuda para escolher a melhor solução D.lextel para minha empresa.')}
    ''')
    return page_shell(title="Soluções D.lextel | PABX, Omnichannel, 0800 e conectividade", description="Compare PABX Virtual, PABX IP, Omnichannel, 0800 VOIP e Link Dedicado e encontre a melhor arquitetura para sua empresa.", canonical="https://dlextel.com.br/solucoes/", current="solutions", content=content)


# ---------- Blog ----------
def blog_page() -> str:
    visual = '''<div class="inner-visual"><span class="inner-visual__orb"></span><div class="inner-visual__frame"><img src="assets/img/atendimento.webp" alt="Equipe de atendimento corporativo" width="500" height="350"></div></div>'''
    content = inner_hero(depth=0, eyebrow="Conhecimento para empresas", title="Blog com inovação e tendências em telecomunicações", lead="Guias, análises e conteúdos sobre telefonia IP, VoIP, Omnichannel, gestão de atendimento, conectividade e redução de custos.", breadcrumb="Blog", visual=visual, message="Olá, li um conteúdo no blog da D.lextel e gostaria de falar com um especialista.")
    content += dedent(f'''
      <section class="section" id="detalhes">
        <div class="container">
          {section_head('Conteúdo integrado', 'Artigos do WordPress em um novo layout', 'Esta página consulta o blog atual pela API do WordPress. Novos artigos publicados continuam aparecendo automaticamente.', False)}
          <div class="blog-toolbar" data-reveal>
            <div class="search-field">{svg('search')}<input type="search" placeholder="Pesquisar no blog: PABX, VoIP, Omnichannel..." aria-label="Pesquisar artigos" data-blog-search></div>
            <button class="btn btn--brand" type="button" data-blog-search-button>Pesquisar {svg('search')}</button>
          </div>
          <div class="blog-status" aria-live="polite" data-blog-status>Carregando artigos...</div>
          <div class="blog-grid" data-blog-grid></div>
          <div class="blog-pagination">
            <button class="btn btn--ghost btn--sm" type="button" data-blog-prev>{svg('arrow-left')} Anterior</button>
            <span class="note" data-blog-page>Página 1</span>
            <button class="btn btn--ghost btn--sm" type="button" data-blog-next>Próxima {svg('arrow')}</button>
          </div>
        </div>
      </section>

      <section class="section section--soft">
        <div class="container">
          {section_head('Linhas editoriais', 'Informação para decisões melhores em comunicação', 'Explore os principais temas que orientam a transformação da telefonia e do atendimento nas empresas.', True)}
          <div class="grid-4">
            <article class="card" data-reveal>{icon_box('network')}<h3>Telefonia IP e VoIP</h3><p>Conceitos, aplicações, migração, equipamentos, mobilidade e recursos corporativos.</p></article>
            <article class="card" data-reveal data-reveal-delay="1">{icon_box('message')}<h3>Atendimento Omnichannel</h3><p>Integração de canais, automação, experiência do cliente e gestão de equipes.</p></article>
            <article class="card" data-reveal data-reveal-delay="2">{icon_box('chart')}<h3>Gestão e economia</h3><p>Estratégias para reduzir desperdícios, monitorar indicadores e melhorar processos.</p></article>
            <article class="card" data-reveal data-reveal-delay="3">{icon_box('wifi')}<h3>Conectividade</h3><p>Link Dedicado, estabilidade, baixa latência, cloud e continuidade da operação.</p></article>
          </div>
        </div>
      </section>
      {cta_banner(0, 'Transforme informação em um projeto para sua empresa', 'Depois de conhecer as possibilidades, converse com a equipe D.lextel para avaliar o cenário real da sua operação.', 'Olá, acompanhei o blog da D.lextel e gostaria de solicitar uma consultoria inicial.')}
    ''')
    scripts = '<script src="assets/js/blog.js" defer></script>'
    return page_shell(title="Blog D.lextel | Telefonia, VoIP, PABX e Omnichannel", description="Conteúdos sobre telefonia IP, VoIP, PABX Virtual, Omnichannel, atendimento, conectividade e gestão de telecomunicações.", canonical="https://dlextel.com.br/blog/", current="blog", content=content, extra_scripts=scripts)


# ---------- Contact ----------
def contact_page() -> str:
    visual = '''<div class="inner-visual"><span class="inner-visual__orb"></span><div class="inner-visual__frame"><img src="assets/img/atendimento.webp" alt="Profissional de atendimento D.lextel" width="500" height="350"></div></div>'''
    choices = [
        ("PABX Virtual", "Ramais, URA, filas, softphone e gestão em nuvem", "cloud"),
        ("PABX IP", "Voz, vídeo e colaboração sobre a rede de dados", "network"),
        ("Omnichannel", "WhatsApp, voz, e-mail e canais em uma plataforma", "message"),
        ("0800 VOIP", "Número nacional integrado à central de atendimento", "phone"),
        ("Link Dedicado", "Conectividade corporativa via fibra e monitoramento", "wifi"),
        ("Ainda não sei", "Quero ajuda para identificar a solução", "spark"),
    ]
    choice_html = "".join(f'''
      <div class="choice"><input type="radio" name="servico" value="{name}" id="servico-{i}"><label for="servico-{i}">{icon_box(icon)}<span><strong>{name}</strong><small>{desc}</small></span></label></div>
    ''' for i, (name, desc, icon) in enumerate(choices, 1))
    content = inner_hero(depth=0, eyebrow="Fale com a equipe", title="Conte sua necessidade e receba uma orientação inicial", lead="Use o formulário guiado para organizar as informações do projeto. Ao final, a solicitação pode ser encaminhada diretamente para o WhatsApp da D.lextel.", breadcrumb="Contato", visual=visual, message="Olá, gostaria de falar com a equipe comercial da D.lextel.")
    content += dedent(f'''
      <section class="section section--soft" id="detalhes">
        <div class="container contact-layout">
          <aside class="contact-aside" data-reveal="left">
            <div class="contact-card">{icon_box('phone', True)}<div><strong>Telefone comercial</strong><a href="tel:+551139950800">(11) 3995-0800</a></div></div>
            <div class="contact-card">{icon_box('whatsapp')}<div><strong>WhatsApp</strong><a href="#" data-whatsapp-message="Olá, vim pela página de contato da D.lextel.">Iniciar conversa</a></div></div>
            <div class="contact-card">{icon_box('clock')}<div><strong>Plantão emergencial</strong><span>Após as 18h, ligue para o mesmo número e selecione a opção 9.</span></div></div>
            <div class="card card--dark"><span class="eyebrow">Atendimento nacional</span><h3>Projetos para empresas em todo o Brasil</h3><p>Telefonia, atendimento e conectividade com desenho personalizado para cada operação.</p></div>
          </aside>
          <div class="wizard" data-reveal="right">
            <div class="wizard__header"><div class="wizard__header-top"><strong>Diagnóstico inicial D.lextel</strong><span data-form-step-label>Etapa 1 de 3</span></div><div class="wizard__progress"><div class="wizard__progress-bar" data-form-progress></div></div></div>
            <div class="wizard__body" data-wizard-body>
              <form data-contact-form novalidate>
                <div class="honeypot" aria-hidden="true"><label>Não preencha <input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
                <section class="form-step is-active" data-form-step>
                  <h2>Qual solução mais se aproxima do seu objetivo?</h2><p>Não precisa ter certeza. Essa seleção serve apenas para direcionar a conversa.</p>
                  <div class="choice-grid">{choice_html}<div class="field-error" data-field-error style="grid-column:1/-1"></div></div>
                  <div class="wizard__actions"><span></span><button class="btn btn--brand" type="button" data-form-next>Continuar {svg('arrow')}</button></div>
                </section>
                <section class="form-step" data-form-step hidden>
                  <h2>Conte um pouco sobre a operação</h2><p>Essas informações ajudam a equipe a preparar uma conversa mais objetiva.</p>
                  <div class="form-grid">
                    <div class="form-group form-group--full"><label for="objetivo">Principal objetivo *</label><select id="objetivo" name="objetivo" required><option value="">Selecione</option><option>Reduzir custos de telefonia</option><option>Organizar chamadas e ramais</option><option>Centralizar canais de atendimento</option><option>Melhorar a experiência do cliente</option><option>Garantir conectividade e estabilidade</option><option>Integrar telefonia com CRM ou sistemas</option><option>Outro objetivo</option></select><span class="field-error" data-field-error></span></div>
                    <div class="form-group"><label for="empresa">Nome da empresa *</label><input id="empresa" name="empresa" type="text" autocomplete="organization" required><span class="field-error" data-field-error></span></div>
                    <div class="form-group"><label for="porte">Porte ou tamanho da equipe *</label><select id="porte" name="porte" required><option value="">Selecione</option><option>Até 10 pessoas</option><option>11 a 50 pessoas</option><option>51 a 200 pessoas</option><option>201 a 500 pessoas</option><option>Mais de 500 pessoas</option><option>Prefiro explicar na conversa</option></select><span class="field-error" data-field-error></span></div>
                    <div class="form-group form-group--full"><label for="mensagem">Detalhes do cenário</label><textarea id="mensagem" name="mensagem" maxlength="600" placeholder="Ex.: temos três unidades, usamos telefonia analógica e queremos integrar o atendimento ao WhatsApp..."></textarea><span class="char-count" data-char-count>0/600</span></div>
                  </div>
                  <div class="wizard__actions"><button class="btn btn--ghost" type="button" data-form-prev>{svg('arrow-left')} Voltar</button><button class="btn btn--brand" type="button" data-form-next>Continuar {svg('arrow')}</button></div>
                </section>
                <section class="form-step" data-form-step hidden>
                  <h2>Como a equipe pode falar com você?</h2><p>Confira o resumo e informe seus dados de contato.</p>
                  <div class="form-summary" data-form-summary></div>
                  <div class="form-grid">
                    <div class="form-group"><label for="nome">Seu nome *</label><input id="nome" name="nome" type="text" autocomplete="name" required><span class="field-error" data-field-error></span></div>
                    <div class="form-group"><label for="telefone">Telefone/WhatsApp *</label><input id="telefone" name="telefone" type="tel" inputmode="tel" autocomplete="tel" placeholder="(11) 99999-9999" required><span class="field-error" data-field-error></span></div>
                    <div class="form-group form-group--full"><label for="email">E-mail profissional *</label><input id="email" name="email" type="email" autocomplete="email" required><span class="field-error" data-field-error></span></div>
                  </div>
                  <label class="form-consent"><input type="checkbox" name="consentimento" value="sim" required><span>Autorizo a D.lextel a utilizar os dados informados exclusivamente para responder a esta solicitação e realizar o contato comercial.</span><span class="field-error" data-field-error></span></label>
                  <p class="field-error" data-form-global-error aria-live="polite"></p>
                  <div class="wizard__actions"><button class="btn btn--ghost" type="button" data-form-prev>{svg('arrow-left')} Voltar</button><button class="btn btn--primary" type="submit">Enviar pelo WhatsApp {svg('whatsapp')}</button></div>
                </section>
              </form>
            </div>
            <div class="form-success" data-form-success><span class="form-success__icon">{svg('check')}</span><h2 tabindex="-1">Solicitação preparada</h2><p>O WhatsApp foi aberto com o resumo do seu projeto. Envie a mensagem para concluir o contato com a equipe D.lextel.</p><a class="btn btn--brand" href="#" data-whatsapp-message="Olá, vim pelo formulário do site da D.lextel e preciso concluir meu atendimento.">{svg('whatsapp')} Abrir WhatsApp novamente</a></div>
          </div>
        </div>
      </section>

      <section class="section">
        <div class="container container--narrow">
          {section_head('Antes de falar conosco', 'Dúvidas rápidas sobre o atendimento', 'O primeiro contato serve para entender o cenário e direcionar a conversa para a solução mais adequada.', True)}
          {faq([
            ('A avaliação inicial tem custo?', 'O site atual apresenta a solicitação de orçamento e a conversa inicial como sem compromisso. A proposta comercial depende do dimensionamento do projeto.'),
            ('Posso falar com a D.lextel pelo WhatsApp?', 'Sim. O telefone e WhatsApp informado é +55 11 3995-0800.'),
            ('A D.lextel atende em todo o Brasil?', 'Sim. O site atual informa atuação nacional com soluções personalizadas para empresas.'),
            ('Quais dados ajudam a preparar uma proposta?', 'Número de usuários ou ramais, unidades, canais utilizados, volume de chamadas ou atendimentos, sistemas que precisam ser integrados e principais objetivos.'),
            ('Como funciona o suporte fora do horário?', 'O site atual informa plantão técnico emergencial após as 18h pelo telefone (11) 3995-0800, opção 9.'),
          ])}
        </div>
      </section>
    ''')
    scripts = '<script src="assets/js/contact.js" defer></script>'
    return page_shell(title="Contato D.lextel | Solicite uma avaliação", description="Fale com a D.lextel pelo telefone ou WhatsApp e solicite uma avaliação para PABX, Omnichannel, 0800 ou Link Dedicado.", canonical="https://dlextel.com.br/contato/", current="contact", content=content, extra_scripts=scripts)


# ---------- Service shared ----------
def service_benefit_strip(items: list[tuple[str, str, str]]) -> str:
    return '<div class="benefit-strip" data-reveal>' + ''.join(f'<div class="benefit-item">{svg(icon)}<strong>{title}</strong><span>{text}</span></div>' for icon, title, text in items) + '</div>'


def feature_cards(items: list[tuple[str, str, str]]) -> str:
    return '<div class="grid-4">' + ''.join(f'<article class="card feature-card" data-reveal data-reveal-delay="{min(i+1,4)}">{icon_box(icon)}<h3>{title}</h3><p>{text}</p></article>' for i, (icon, title, text) in enumerate(items)) + '</div>'


def service_testimonial(depth: int = 1) -> str:
    l = linkset(depth)
    return dedent(f'''
      <section class="section section--soft">
        <div class="container split">
          <div class="split__media" data-reveal="left"><img src="{l['assets']}img/cliente-sawary.webp" alt="Sawary Jeans" width="360" height="360" loading="lazy" style="object-fit:contain;background:#fff"></div>
          <div data-reveal="right"><span class="eyebrow">Caso relatado no site atual</span><h2>Mais controle sobre a comunicação e redução de custos</h2><p class="lead">A Sawary Jeans relata que a combinação de PABX IP, 0800 e Telefonia VoIP modernizou a infraestrutura e gerou economia de 70% no custo total.</p><p>O depoimento também destaca melhoria no gerenciamento, no monitoramento das ligações e na qualidade do atendimento da D.lextel.</p><p class="note">Resultados informados pelo cliente e sujeitos às características de cada operação.</p></div>
        </div>
      </section>
    ''')


# ---------- PABX Virtual ----------
def pabx_virtual_page() -> str:
    visual = dedent('''
      <div class="service-hero-media">
        <img class="service-hero-image" src="../assets/img/pabx-virtual-voip.webp" alt="PABX Virtual em computadores, smartphones e telefone IP" width="613" height="477">
        <div class="service-mini-stat service-mini-stat--top"><strong>Cloud</strong><span>Implantação flexível</span></div>
        <div class="service-mini-stat service-mini-stat--bottom"><strong>Em qualquer lugar</strong><span>Celular, computador ou telefone IP</span></div>
      </div>
    ''')
    features = [
        ("route", "URA e fluxos inteligentes", "Menus automáticos, horários e direcionamento para departamentos, filas ou ramais."),
        ("smartphone", "Softphone e Web Client", "Atenda no celular ou computador sem perder a identidade profissional da empresa."),
        ("users", "Filas e distribuição automática", "Organize grupos, reduza chamadas perdidas e equilibre o atendimento entre a equipe."),
        ("mic", "Gravação de chamadas", "Mais controle para qualidade, treinamento, segurança e acompanhamento dos atendimentos."),
        ("chart", "Relatórios e monitoramento", "Acompanhe chamadas atendidas, perdidas, tempo de espera e desempenho da operação."),
        ("message", "Integração com WhatsApp", "Centralize o relacionamento e mantenha o histórico de conversas organizado."),
        ("video", "Integração com Microsoft Teams", "Use o Teams como telefone corporativo para chamadas internas e externas."),
        ("database", "CRM, API e sistemas", "Identifique clientes, registre chamadas, associe gravações e crie automações."),
    ]
    content = inner_hero(depth=1, eyebrow="Telefonia em nuvem", title="PABX Virtual para atender melhor, trabalhar de qualquer lugar e ganhar controle", lead="Substitua limitações da telefonia tradicional por uma central moderna, flexível e preparada para equipes presenciais, remotas ou híbridas.", breadcrumb="PABX Virtual", visual=visual, message="Olá, gostaria de receber informações sobre o PABX Virtual da D.lextel.")
    content += dedent(f'''
      <section class="section" id="detalhes"><div class="container">{service_benefit_strip([
        ('phone','Menos chamadas perdidas','Filas, grupos e distribuição automática.'),
        ('chart','Mais controle','Relatórios, gravações e acompanhamento.'),
        ('smartphone','Mobilidade','Ramais no celular, computador ou telefone IP.'),
        ('sliders','Escalabilidade','Adicione usuários e recursos conforme a empresa cresce.'),
      ])}</div></section>

      <section class="section section--soft">
        <div class="container split">
          <div data-reveal="left"><span class="eyebrow">Problema resolvido</span><h2>Pare de perder ligações e de pagar por uma estrutura que não acompanha sua empresa</h2><p class="lead">O PABX Virtual organiza o atendimento, reduz dependência de linhas físicas e permite que a equipe continue conectada em diferentes locais.</p><ul class="check-list"><li>Distribuição automática por filas e departamentos</li><li>Atendimento com o mesmo número em diferentes dispositivos</li><li>Visibilidade sobre chamadas e desempenho da equipe</li><li>Integrações para reduzir tarefas manuais</li></ul></div>
          <div class="service-showcase__media service-showcase__media--contain" data-reveal="right"><img src="../assets/img/pabx-virtual-voip.webp" alt="Ecossistema do PABX Virtual D.lextel" width="613" height="477" loading="lazy"></div>
        </div>
      </section>

      <section class="section"><div class="container">{section_head('Recursos da solução', 'Uma central completa para a telefonia corporativa', 'Configure fluxos, habilite mobilidade e acompanhe a operação em uma plataforma preparada para diferentes cenários.', True)}{feature_cards(features)}</div></section>

      <section class="section section--blue">
        <div class="container service-showcase">
          <div class="service-showcase__media" data-reveal="left"><img src="../assets/img/integracoes.webp" alt="Integrações do PABX Virtual com WhatsApp, Teams, CRM e sistemas" width="760" height="674" loading="lazy"></div>
          <div data-reveal="right"><span class="eyebrow">Integrações</span><h2>Transforme a telefonia em parte dos processos da empresa</h2><p class="lead">Com integrações e API, o PABX pode conversar com o CRM, bancos de dados, WhatsApp, Microsoft Teams e sistemas internos.</p><ul class="check-list"><li>Identificação automática do cliente ao receber chamadas</li><li>Registro de ligações e gravações no CRM</li><li>Automação de tarefas e fluxos personalizados</li><li>Integração com ferramentas próprias ou de terceiros</li></ul></div>
        </div>
      </section>

      <section class="section section--brand">
        <div class="container"><div class="section-head section-head--center" data-reveal><span class="eyebrow">Modelo de implantação</span><h2>Nuvem ou On-Premises?</h2><p>A escolha depende da política interna, da infraestrutura, do nível de controle desejado e da forma de trabalho da equipe.</p></div>
          <div class="compare-cards">
            <article class="compare-card is-featured" data-reveal><span class="badge badge--dark">Mais flexível</span><h3>PABX em nuvem</h3><ul class="check-list check-list--light"><li>Implantação mais rápida</li><li>Menor investimento inicial</li><li>Ideal para equipes remotas e híbridas</li><li>Escalabilidade simples</li></ul><a class="btn btn--primary" href="#" data-whatsapp-message="Olá, gostaria de avaliar um PABX em nuvem com a D.lextel.">Avaliar modelo cloud</a></article>
            <article class="compare-card" data-reveal data-reveal-delay="1"><span class="badge">Controle local</span><h3>PABX On-Premises</h3><ul class="check-list"><li>Infraestrutura instalada no ambiente da empresa</li><li>Dados e controle local</li><li>Adequação a políticas internas específicas</li><li>Projeto dimensionado para o cenário existente</li></ul><a class="btn btn--brand" href="#" data-whatsapp-message="Olá, gostaria de avaliar um PABX On-Premises com a D.lextel.">Avaliar modelo local</a></article>
          </div>
        </div>
      </section>

      <section class="section"><div class="container">{section_head('Aplicações', 'Para empresas que precisam de mobilidade sem perder profissionalismo', 'A solução se adapta ao tamanho da equipe, ao volume de chamadas e à necessidade de integração.', True)}
        <div class="grid-4"><article class="card application-card" data-reveal>{icon_box('building')}<strong>Escritórios e serviços</strong><p>Atendimento organizado por áreas, horários e profissionais.</p></article><article class="card application-card" data-reveal data-reveal-delay="1">{icon_box('users')}<strong>Equipes remotas</strong><p>Ramais ativos no celular ou computador, em qualquer lugar.</p></article><article class="card application-card" data-reveal data-reveal-delay="2">{icon_box('headset')}<strong>Centrais de atendimento</strong><p>Filas, grupos, gravações e indicadores de desempenho.</p></article><article class="card application-card" data-reveal data-reveal-delay="3">{icon_box('layers')}<strong>Empresas em crescimento</strong><p>Expansão de usuários e recursos sem reconstruir toda a estrutura.</p></article></div>
      </div></section>

      <section class="section section--soft"><div class="container container--narrow">{section_head('Dúvidas frequentes', 'PABX Virtual na prática', 'Pontos importantes antes de planejar a migração.', True)}{faq([
        ('O que é PABX Virtual?', 'É uma central telefônica baseada em nuvem que organiza chamadas, ramais, filas, URA e outros recursos sem depender de um equipamento PABX tradicional em cada local.'),
        ('Posso atender pelo celular e computador?', 'Sim. A solução pode utilizar aplicativo softphone e Web Client, mantendo o ramal corporativo em diferentes dispositivos.'),
        ('É possível manter o número atual?', 'A viabilidade depende do tipo de número e da operadora atual. A equipe avalia a portabilidade e o desenho da migração.'),
        ('O PABX integra com CRM?', 'Sim. O site atual informa integrações com CRM, banco de dados e sistemas internos por meio de API aberta.'),
        ('A solução funciona para equipes híbridas?', 'Sim. Esse é um dos principais cenários, pois os ramais podem acompanhar o colaborador dentro ou fora do escritório.'),
      ])}</div></section>
      {service_testimonial(1)}
      {cta_banner(1, 'Organize sua telefonia com PABX Virtual', 'Fale com a D.lextel para avaliar ramais, números, fluxos de atendimento, integrações e o modelo de implantação.', 'Olá, gostaria de solicitar uma proposta de PABX Virtual para minha empresa.')}
    ''')
    return page_shell(title="PABX Virtual D.lextel | Telefonia em nuvem para empresas", description="PABX Virtual com URA, filas, softphone, gravação, relatórios e integrações para empresas presenciais, remotas ou híbridas.", canonical="https://dlextel.com.br/PABX-virtual/", current="service", content=content, depth=1)


# ---------- PABX IP ----------
def pabx_ip_page() -> str:
    visual = dedent('''
      <div class="inner-visual"><span class="inner-visual__orb"></span><div class="inner-visual__frame"><img src="../assets/img/business-meeting.webp" alt="Equipe corporativa usando soluções de comunicação IP" width="1024" height="683"></div><div class="service-mini-stat service-mini-stat--top"><strong>Voz + Vídeo</strong><span>Colaboração sobre IP</span></div></div>
    ''')
    features = [
        ("route", "Roteamento inteligente", "Direcione chamadas para ramais, grupos ou dispositivos móveis e evite perder contatos importantes."),
        ("mic", "Gravação de chamadas", "Registre chamadas para treinamento, qualidade, auditoria e acompanhamento da operação."),
        ("video", "Videoconferências", "Realize reuniões com vídeo, compartilhamento de conteúdo e colaboração entre equipes remotas."),
        ("users", "Grupos de atendimento", "Organize departamentos e distribua chamadas para reduzir espera e melhorar a experiência."),
        ("smartphone", "APP e Web Client", "Trabalhe de qualquer lugar com voz, vídeo e chat corporativo em dispositivos conectados."),
        ("headset", "Módulo recepcionista", "Visualize status, transfira chamadas e registre recados com mais agilidade."),
        ("database", "Integração com CRM", "Conecte chamadas a dados do cliente e mantenha registros associados à operação."),
        ("shield", "Segurança e gestão", "Administre usuários, permissões, regras e recursos com uma visão centralizada."),
    ]
    content = inner_hero(depth=1, eyebrow="Comunicação sobre IP", title="PABX IP para voz, vídeo, mobilidade e colaboração corporativa", lead="Utilize a rede de dados para realizar e receber chamadas, conectar unidades e habilitar recursos avançados de comunicação para empresas de todos os portes.", breadcrumb="PABX IP", visual=visual, message="Olá, gostaria de informações sobre a solução PABX IP da D.lextel.")
    content += dedent(f'''
      <section class="section" id="detalhes"><div class="container">{service_benefit_strip([
        ('chart','Redução de custos','Aproveitamento da rede IP e chamadas mais eficientes.'),
        ('sliders','Escalabilidade','Adicione ou remova ramais conforme a demanda.'),
        ('link','Integração','Conecte telefonia a aplicativos e sistemas de negócio.'),
        ('smartphone','Mobilidade','Acesse ramais em diferentes locais e dispositivos.'),
      ])}</div></section>

      <section class="section section--soft"><div class="container split">
        <div data-reveal="left"><span class="eyebrow">Entenda a tecnologia</span><h2>O que é PABX IP?</h2><p class="lead">É um sistema de telefonia que transmite voz por protocolo de internet, utilizando a rede de dados em vez de depender exclusivamente de linhas telefônicas físicas.</p><p>Essa arquitetura permite mais flexibilidade para equipes distribuídas, integração com aplicativos, administração centralizada e expansão de ramais com menos complexidade.</p><ul class="check-list"><li>Chamadas internas entre unidades e colaboradores</li><li>Ramais acessíveis com conexão à internet</li><li>Recursos de voz, vídeo e chat</li><li>Integração com ferramentas corporativas</li></ul></div>
        <div class="service-showcase__media" data-reveal="right"><img src="../assets/img/business-meeting.webp" alt="Reunião corporativa com colaboração entre equipes" width="1024" height="683" loading="lazy"></div>
      </div></section>

      <section class="section"><div class="container">{section_head('Funcionalidades', 'Recursos para uma operação conectada e produtiva', 'Do atendimento telefônico à colaboração entre equipes, o PABX IP amplia a capacidade de comunicação da empresa.', True)}{feature_cards(features)}</div></section>

      <section class="section section--brand"><div class="container">{section_head('Cenários de uso', 'Uma solução versátil para diferentes estruturas', 'O desenho muda de acordo com o porte, o volume de chamadas, as unidades e os sistemas que precisam ser conectados.', True)}
        <div class="grid-4"><article class="card card--dark" data-reveal>{icon_box('building', True)}<h3>Pequenas e médias empresas</h3><p>Comunicação profissional, fácil de administrar e preparada para crescer.</p></article><article class="card card--dark" data-reveal data-reveal-delay="1">{icon_box('layers', True)}<h3>Grandes corporações</h3><p>Gestão de muitos ramais, unidades e integrações em uma arquitetura central.</p></article><article class="card card--dark" data-reveal data-reveal-delay="2">{icon_box('headset', True)}<h3>Call centers</h3><p>Roteamento, gravação, grupos e relatórios para operações de atendimento.</p></article><article class="card card--dark" data-reveal data-reveal-delay="3">{icon_box('globe', True)}<h3>Equipes distribuídas</h3><p>Mobilidade para colaboradores e escritórios em diferentes localidades.</p></article></div>
      </div></section>

      <section class="section"><div class="container">{section_head('Recursos operacionais', 'Atendimento, mobilidade e produtividade no mesmo ambiente', 'Uma seleção dos recursos descritos no site atual para apoiar diferentes fluxos corporativos.', False)}
        <div class="grid-3"><article class="card" data-reveal><h3>URA de atendimento</h3><p>Menus que direcionam clientes para o departamento ou ramal adequado.</p></article><article class="card" data-reveal data-reveal-delay="1"><h3>Ligações entre unidades</h3><p>Comunicação interna pela rede IP para reduzir custos e aproximar equipes.</p></article><article class="card" data-reveal data-reveal-delay="2"><h3>Chamadas completas</h3><p>Transferência direta ou assistida, captura, desvio e roteamento por número.</p></article><article class="card" data-reveal><h3>Áudios personalizados</h3><p>Mensagens por horário, status, departamentos e música de espera.</p></article><article class="card" data-reveal data-reveal-delay="1"><h3>Áudio e videoconferência</h3><p>Reuniões com recursos de colaboração e gravação.</p></article><article class="card" data-reveal data-reveal-delay="2"><h3>Status da equipe</h3><p>Mais agilidade para recepção, transferências e recados.</p></article></div>
      </div></section>

      <section class="section section--soft"><div class="container container--narrow">{section_head('Dúvidas frequentes', 'Planejando um PABX IP', 'Respostas para começar a avaliação técnica e comercial.', True)}{faq([
        ('Qual a diferença entre PABX IP e PABX tradicional?', 'O PABX IP utiliza a rede de dados e protocolo IP, habilitando mobilidade, integrações e administração mais flexível do que uma estrutura baseada apenas em linhas físicas.'),
        ('O PABX IP funciona para grandes empresas?', 'Sim. O site atual o apresenta para PMEs, grandes corporações, call centers e equipes remotas, com dimensionamento adequado a cada cenário.'),
        ('É possível fazer videoconferências?', 'Sim. A solução descrita inclui chamadas de áudio, vídeo e recursos de colaboração.'),
        ('Posso usar o ramal fora do escritório?', 'Sim. Aplicativos softphone e Web Client permitem acessar a comunicação em locais com conexão adequada.'),
        ('Preciso de uma boa internet?', 'Sim. Qualidade de voz e vídeo depende de conectividade, configuração de rede e dimensionamento. A D.lextel também oferece Link Dedicado para operações críticas.'),
      ])}</div></section>
      {service_testimonial(1)}
      {cta_banner(1, 'Leve voz, vídeo e colaboração para a rede IP', 'Converse com a D.lextel para dimensionar ramais, unidades, integrações, equipamentos e conectividade.', 'Olá, gostaria de solicitar uma proposta para PABX IP.')}
    ''')
    return page_shell(title="PABX IP D.lextel | Voz, vídeo e colaboração para empresas", description="PABX IP com voz, vídeo, softphone, roteamento, gravação, grupos de atendimento e integração para empresas de todos os portes.", canonical="https://dlextel.com.br/pabx-ip/", current="service", content=content, depth=1)


# ---------- Omnichannel ----------
def omnichannel_page() -> str:
    visual = dedent('''
      <div class="omni-visual">
        <div class="omni-window">
          <div class="omni-sidebar"><i class="is-active">CX</i><i>WA</i><i>VOZ</i><i>MAIL</i><i>IA</i></div>
          <div class="omni-main">
            <div class="omni-inboxes"><h4>Caixa unificada</h4><div class="omni-contact"><span class="omni-avatar">AS</span><span><strong>Ana Souza</strong><small>Preciso de ajuda com meu pedido...</small></span></div><div class="omni-contact"><span class="omni-avatar">CM</span><span><strong>Carlos Mendes</strong><small>Gostaria de falar com vendas...</small></span></div><div class="omni-contact"><span class="omni-avatar">LP</span><span><strong>Larissa Prado</strong><small>Atendimento iniciado pelo WhatsApp</small></span></div></div>
            <div class="omni-chat"><h4>Atendimento #4821</h4><div class="message">Olá! Comecei o contato pelo WhatsApp e preciso continuar por aqui.</div><div class="message message--out">Perfeito. Já temos seu histórico e vamos dar sequência sem repetir as informações.</div><div class="channel-pills"><span class="channel-pill">WhatsApp</span><span class="channel-pill">Voz</span><span class="channel-pill">E-mail</span><span class="channel-pill">Instagram</span><span class="channel-pill">Chat</span></div></div>
          </div>
        </div>
      </div>
    ''')
    plan_features = {
        "Plano Chat": ["Chatbot", "Caixa de entrada unificada", "Filas e transferências", "Tickets e protocolos", "Histórico e acompanhamento", "Dashboard e relatórios", "Pesquisa de satisfação", "Campanhas", "Auditoria e IA"],
        "Plano Voz": ["PABX completo", "Discador automático", "URA reversa e callback", "Gravação de chamadas", "Dados do cliente na tela", "Protocolos e tabulação", "Dashboard em tempo real", "Pesquisa de satisfação", "Auditoria e IA"],
        "Omnichannel": ["Atendimento em chat e voz", "E-mail e canais digitais", "Disparo de voz e WhatsApp", "Histórico unificado", "Tickets e protocolos", "Discador, URA e callback", "Dashboards e relatórios", "Automação e auditoria", "Inteligência artificial"],
    }
    plan_cards = []
    for i, (name, feats) in enumerate(plan_features.items()):
        featured = name == "Omnichannel"
        plan_cards.append(f'''
          <article class="plan-card{' is-featured' if featured else ''}" data-reveal data-reveal-delay="{i+1}"><span class="badge{' badge--dark' if featured else ''}">{'Solução completa' if featured else 'Módulo especializado'}</span><h3>{name}</h3><p>{'Integre canais de voz e digitais em uma jornada única.' if featured else 'Recursos direcionados para a operação de ' + ('mensageria digital.' if name == 'Plano Chat' else 'telefonia e contact center.')}</p><ul class="check-list{' check-list--light' if featured else ''}">{''.join(f'<li>{x}</li>' for x in feats)}</ul><a class="btn {'btn--primary' if featured else 'btn--brand'}" href="#" data-whatsapp-message="Olá, gostaria de informações sobre o {name} Omnichannel da D.lextel.">Solicitar informações</a></article>
        ''')
    features = [
        ("message", "Caixa de entrada unificada", "Organize WhatsApp, Facebook, Instagram, Telegram, e-mail, chat e outras interações em um único ambiente."),
        ("phone", "Discador e URA Reversa", "Automatize contatos, roteie chamadas e configure menus para aumentar a produtividade da equipe."),
        ("layers", "Módulos flexíveis", "Combine PABX, mensageria, automação e canais conforme a realidade da operação."),
        ("route", "Filas e transferências", "Distribua atendimentos por equipes, competências, prioridades e disponibilidade."),
        ("file", "Tickets e protocolos", "Crie registros rastreáveis e mantenha o histórico associado a cada cliente."),
        ("chart", "Dashboards e relatórios", "Acompanhe volumes, tempos, desempenho, satisfação e indicadores em tempo real."),
        ("spark", "Automação e IA", "Reduza tarefas repetitivas, direcione demandas e acelere respostas."),
        ("shield", "Auditoria e segurança", "Mantenha visibilidade sobre as interações e aplique controles para proteger os dados."),
    ]
    content = inner_hero(depth=1, eyebrow="Atendimento integrado", title="Omnichannel para atender em todos os canais sem perder o contexto do cliente", lead="Centralize voz, WhatsApp, e-mail, chat e redes sociais em uma plataforma escalável, com automação, relatórios, filas e histórico unificado.", breadcrumb="Omnichannel", visual=visual, message="Olá, gostaria de conhecer a Plataforma Omnichannel da D.lextel.")
    content += dedent(f'''
      <section class="section" id="detalhes"><div class="container">{service_benefit_strip([
        ('message','Atendimento unificado','Todos os canais e históricos em uma interface.'),
        ('spark','Automação inteligente','Fluxos que reduzem tarefas repetitivas.'),
        ('chart','Gestão em tempo real','Dashboards, auditoria e indicadores.'),
        ('sliders','Módulos flexíveis','Recursos combinados conforme sua necessidade.'),
      ])}</div></section>

      <section class="section section--soft"><div class="container">{section_head('Planos e módulos', 'Escolha a composição que faz sentido para a operação', 'Comece por chat, voz ou combine tudo em uma experiência Omnichannel completa.', True)}<div class="plan-grid">{''.join(plan_cards)}</div></div></section>

      <section class="section"><div class="container">{section_head('Funcionalidades', 'Uma plataforma para organizar, automatizar e acompanhar o atendimento', 'Recursos para reduzir silos, dar contexto à equipe e melhorar a continuidade da experiência do cliente.', True)}{feature_cards(features)}</div></section>

      <section class="section section--brand"><div class="container split">
        <div data-reveal="left"><span class="eyebrow">Experiência contínua</span><h2>O cliente troca de canal. O contexto continua.</h2><p class="lead">Com os canais conectados, a equipe visualiza o histórico e evita que o cliente repita as mesmas informações a cada novo contato.</p><ul class="check-list check-list--light"><li>Atendimento por chat e voz</li><li>WhatsApp e campanhas</li><li>E-mail e redes sociais</li><li>Telefonia, discador e URA</li><li>Dados do cliente e protocolos</li></ul></div>
        <div class="omni-visual" data-reveal="right"><div class="omni-window"><div class="omni-sidebar"><i class="is-active">CX</i><i>WA</i><i>VOZ</i><i>MAIL</i><i>IA</i></div><div class="omni-main"><div class="omni-inboxes"><h4>Atendimentos</h4><div class="omni-contact"><span class="omni-avatar">01</span><span><strong>WhatsApp</strong><small>Fila comercial</small></span></div><div class="omni-contact"><span class="omni-avatar">02</span><span><strong>Telefonia</strong><small>Suporte técnico</small></span></div></div><div class="omni-chat"><h4>Visão do cliente</h4><div class="message">Histórico de conversas, ligações, tickets e protocolos.</div><div class="message message--out">Atendimento transferido com contexto completo.</div><div class="channel-pills"><span class="channel-pill">Chatbot</span><span class="channel-pill">SLA</span><span class="channel-pill">IA</span><span class="channel-pill">Relatórios</span></div></div></div></div></div>
      </div></section>

      <section class="section section--soft"><div class="container container--narrow">{section_head('Dúvidas frequentes', 'Plataforma Omnichannel', 'Entenda como a solução pode entrar na sua operação.', True)}{faq([
        ('O que é uma plataforma Omnichannel?', 'É uma solução que integra canais como telefone, WhatsApp, e-mail, redes sociais e chat em um sistema único, preservando o histórico e o contexto do cliente.'),
        ('Posso contratar apenas chat ou apenas voz?', 'Sim. O site atual apresenta planos Chat, Voz e Omnichannel, permitindo escolher módulos conforme a necessidade.'),
        ('Quais canais podem ser centralizados?', 'A solução descrita inclui voz, WhatsApp, e-mail, chat, Facebook, Instagram, Telegram e outros canais, conforme o projeto e as integrações disponíveis.'),
        ('A plataforma possui automação e inteligência artificial?', 'Sim. O site atual lista chatbot, automações, auditoria e inteligência artificial entre os recursos.'),
        ('A implementação é rápida?', 'O prazo varia com a complexidade, os canais, as integrações e o volume da operação. A D.lextel informa trabalhar para reduzir o impacto durante a implantação.'),
        ('A plataforma considera a LGPD?', 'O site atual informa uso de criptografia, protocolos de segurança e atenção às normas de proteção de dados. A configuração e os processos internos também devem ser avaliados em cada projeto.'),
      ])}</div></section>
      {testimonials(1)}
      {cta_banner(1, 'Centralize seus canais com Omnichannel', 'Converse com a D.lextel sobre usuários, canais, filas, automações, integrações e indicadores de atendimento.', 'Olá, gostaria de solicitar uma demonstração da Plataforma Omnichannel.')}
    ''')
    return page_shell(title="Omnichannel D.lextel | Atendimento integrado em todos os canais", description="Plataforma Omnichannel para centralizar WhatsApp, voz, e-mail, chat e redes sociais com automação, filas, protocolos, IA e relatórios.", canonical="https://dlextel.com.br/omnichannel/", current="service", content=content, depth=1)


# ---------- 0800 ----------
def voip_0800_page() -> str:
    visual = dedent('''
      <div class="number-visual"><div class="number-visual__circle"><span><strong>0800</strong><span>Atendimento nacional conectado à sua empresa</span></span></div></div>
    ''')
    features = [
        ("route", "URA de atendimento", "Direcione chamadas para áreas, filas ou ramais com menus personalizados."),
        ("message", "Integração com WhatsApp Business", "Combine atendimento por voz e mensagens em uma estratégia mais completa."),
        ("users", "Atendimento diferenciado", "Distribua chamadas entre equipes e organize os fluxos conforme a operação."),
        ("globe", "Número único nacional", "Ofereça um canal fácil de divulgar e acessível para clientes em todo o Brasil."),
        ("repeat", "Chamadas simultâneas", "Dimensione a capacidade de atendimento conforme os volumes e horários de pico."),
        ("phone", "Gratuito para quem liga", "A empresa contratante assume o custo e facilita o contato do público."),
        ("link", "Entrega via SIP", "Integre o número a PABX, gateway, ATA ou aplicativo compatível."),
        ("refresh", "Portabilidade", "Leve um número existente para a D.lextel após análise e documentação."),
    ]
    content = inner_hero(depth=1, eyebrow="Alcance e credibilidade", title="0800 VOIP: conveniência para o cliente e presença nacional para sua empresa", lead="Disponibilize um canal gratuito para quem liga e direcione as chamadas para sua central de atendimento, equipes, URA, PABX ou aplicativo.", breadcrumb="0800 VOIP", visual=visual, message="Olá, gostaria de receber informações sobre o 0800 VOIP da D.lextel.")
    content += dedent(f'''
      <section class="section" id="detalhes"><div class="container">{service_benefit_strip([
        ('globe','Presença nacional','Um número único para clientes de todo o Brasil.'),
        ('phone','Mais acessibilidade','A ligação é gratuita para quem entra em contato.'),
        ('route','Centralização','Direcione chamadas para sua estrutura de atendimento.'),
        ('award','Credibilidade','Fortaleça a percepção de uma operação profissional.'),
      ])}</div></section>

      <section class="section section--soft"><div class="container split">
        <div data-reveal="left"><span class="eyebrow">Canal de relacionamento</span><h2>Um número pensado para SAC, vendas, ouvidoria e suporte</h2><p class="lead">O 0800 aproxima clientes, fornecedores e colaboradores, ao mesmo tempo em que centraliza as chamadas na estrutura definida pela empresa.</p><ul class="check-list"><li>SAC e atendimento ao consumidor</li><li>Televendas e geração de oportunidades</li><li>Ouvidoria e canais institucionais</li><li>Suporte técnico e pós-venda</li><li>Contato com fornecedores e equipes</li></ul></div>
        <div class="number-visual" data-reveal="right"><div class="number-visual__circle"><span><strong>0800</strong><span>Um canal gratuito, eficiente e disponível em todo o Brasil</span></span></div></div>
      </div></section>

      <section class="section"><div class="container">{section_head('Vantagens', 'Uma solução completa para atendimento 0800', 'Conecte o número aos recursos de telefonia e organize a forma como as chamadas chegam à equipe.', True)}{feature_cards(features)}</div></section>

      <section class="section section--brand"><div class="container">{section_head('Como funciona', 'Do número nacional ao ramal que atende o cliente', 'A arquitetura pode entregar as chamadas pela internet para diferentes dispositivos e centrais, conforme o projeto.', True)}
        <div class="process-grid"><article class="process-card" data-reveal><h3>Contratação</h3><p>Definição de número novo ou análise de portabilidade de um número existente.</p></article><article class="process-card" data-reveal data-reveal-delay="1"><h3>Configuração</h3><p>Criação da conta, regras, URA, filas, horários e destinos de atendimento.</p></article><article class="process-card" data-reveal data-reveal-delay="2"><h3>Entrega SIP</h3><p>Registro em PABX, gateway, ATA ou aplicativo, conforme a arquitetura.</p></article><article class="process-card" data-reveal data-reveal-delay="3"><h3>Operação</h3><p>Chamadas distribuídas para equipes, unidades ou ramais definidos.</p></article></div>
      </div></section>

      <section class="section"><div class="container service-showcase">
        <div data-reveal="left"><span class="eyebrow">Continuidade</span><h2>Planeje redundância para manter o atendimento disponível</h2><p class="lead">Como o 0800 VOIP utiliza conectividade, uma operação crítica deve considerar links redundantes e alternativas de atendimento móvel.</p><ul class="check-list"><li>Mais de um link de internet quando necessário</li><li>Roteamento alternativo de chamadas</li><li>Atendimento pelo celular em cenários de contingência</li><li>Dimensionamento de simultaneidade e picos</li></ul></div>
        <div class="service-showcase__media service-showcase__media--contain" data-reveal="right"><img src="../assets/img/pabx-virtual-voip.webp" alt="0800 integrado ao PABX e aos dispositivos da empresa" width="613" height="477" loading="lazy"></div>
      </div></section>

      <section class="section section--soft"><div class="container container--narrow">{section_head('Dúvidas frequentes', 'Contratação e portabilidade do 0800', 'Informações do site atual para orientar os próximos passos.', True)}{faq([
        ('Posso portar um número 0800 existente?', 'Sim, mediante consulta de viabilidade e envio de documentos que comprovem a titularidade, como CNPJ ou CPF e a última fatura, além da autorização necessária.'),
        ('Qual o prazo de portabilidade?', 'O site atual informa prazo estimado de 5 a 15 dias úteis após a documentação e a análise de viabilidade.'),
        ('Quanto tempo leva para ativar um número novo?', 'O site atual informa prazo de até 72 horas após assinatura e validação, sujeito às condições do projeto.'),
        ('Como a chamada é entregue?', 'A ligação pode ser entregue por uma conta SIP registrada em PABX, gateway, ATA ou aplicativo.'),
        ('O que acontece se a internet cair?', 'É recomendável planejar redundância de conectividade e rotas alternativas. Também pode ser possível atender pelo ramal no celular usando outra conexão.'),
        ('A ligação é gratuita para quem liga?', 'Sim. No modelo 0800, o custo é assumido pela empresa contratante, tornando a ligação gratuita para o originador.'),
      ])}</div></section>
      {service_testimonial(1)}
      {cta_banner(1, 'Crie um canal 0800 para sua empresa', 'Fale com a D.lextel para avaliar número novo, portabilidade, URA, capacidade simultânea e integração com sua central.', 'Olá, gostaria de solicitar uma proposta de 0800 VOIP.')}
    ''')
    return page_shell(title="0800 VOIP D.lextel | Número nacional para empresas", description="Número 0800 VOIP integrado a PABX, URA e equipes, com alcance nacional, portabilidade e atendimento gratuito para quem liga.", canonical="https://dlextel.com.br/empresa-0800/", current="service", content=content, depth=1)


# ---------- Link Dedicado ----------
def link_dedicado_page() -> str:
    visual = dedent(f'''
      <div class="fiber-visual">
        <span class="fiber-link fiber-link--1"></span><span class="fiber-link fiber-link--2"></span><span class="fiber-link fiber-link--3"></span><span class="fiber-link fiber-link--4"></span><span class="fiber-link fiber-link--5"></span>
        <span class="fiber-node fiber-node--core">{svg('server')}</span><span class="fiber-node fiber-node--1">{svg('cloud')}</span><span class="fiber-node fiber-node--2">{svg('building')}</span><span class="fiber-node fiber-node--3">{svg('phone')}</span><span class="fiber-node fiber-node--4">{svg('database')}</span><span class="fiber-node fiber-node--5">{svg('users')}</span>
      </div>
    ''')
    features = [
        ("bolt", "Alta capacidade", "Opções descritas no site atual de 10 Mbps a 10 Gbps para diferentes perfis de operação."),
        ("clock", "Ativação planejada", "O site informa ativação a partir de 10 dias úteis, conforme viabilidade e projeto."),
        ("globe", "Presença nacional", "Pontos de presença em hubs de tráfego e atendimento a diferentes regiões."),
        ("wifi", "Baixa latência", "Conexões diretas e rotas otimizadas para aplicações corporativas e conteúdo."),
        ("eye", "Monitoramento contínuo", "Supervisão 24x7x365 pelo NOC, com suporte de engenharia e manutenção em campo."),
        ("repeat", "Full duplex", "Upload e download com velocidade simétrica e garantia da capacidade contratada."),
        ("shield", "Estabilidade", "Conectividade pensada para aplicações críticas, voz, cloud e sistemas."),
        ("link", "Lan to Lan", "Interconexão privada entre matriz, filiais, datacenters ou ambientes em nuvem."),
    ]
    content = inner_hero(depth=1, eyebrow="Conectividade corporativa", title="Link Dedicado e Lan to Lan para mais performance, estabilidade e controle", lead="Internet corporativa via fibra com velocidade full duplex, baixa latência, monitoramento contínuo e opções para conectar unidades e ambientes críticos.", breadcrumb="Link Dedicado", visual=visual, message="Olá, gostaria de receber informações sobre Link Dedicado da D.lextel.")
    content += dedent(f'''
      <section class="section" id="detalhes"><div class="container">{service_benefit_strip([
        ('repeat','100% full duplex','Velocidade simétrica conforme a capacidade contratada.'),
        ('eye','NOC 24x7x365','Monitoramento contínuo da conectividade.'),
        ('bolt','Baixa latência','Performance para cloud, voz e sistemas críticos.'),
        ('link','Lan to Lan','Conexão privada entre unidades e datacenters.'),
      ])}</div></section>

      <section class="section section--soft"><div class="container split">
        <div data-reveal="left"><span class="eyebrow">Internet corporativa</span><h2>Conectividade dimensionada para a operação, não para o consumo doméstico</h2><p class="lead">O Link Dedicado oferece uma conexão exclusiva e previsível para sustentar telefonia IP, videoconferência, sistemas em nuvem, transferência de dados e atendimento digital.</p><ul class="check-list"><li>Velocidade simétrica de upload e download</li><li>Monitoramento e suporte especializado</li><li>Menor variação de desempenho</li><li>Planejamento de redundância e continuidade</li></ul></div>
        <div class="fiber-visual" data-reveal="right"><span class="fiber-link fiber-link--1"></span><span class="fiber-link fiber-link--2"></span><span class="fiber-link fiber-link--3"></span><span class="fiber-link fiber-link--4"></span><span class="fiber-link fiber-link--5"></span><span class="fiber-node fiber-node--core">{svg('server')}</span><span class="fiber-node fiber-node--1">{svg('cloud')}</span><span class="fiber-node fiber-node--2">{svg('building')}</span><span class="fiber-node fiber-node--3">{svg('phone')}</span><span class="fiber-node fiber-node--4">{svg('database')}</span><span class="fiber-node fiber-node--5">{svg('users')}</span></div>
      </div></section>

      <section class="section"><div class="container">{section_head('Diferenciais', 'Conexão para operações que não podem depender de instabilidade', 'Recursos descritos no site atual para entregar capacidade, visibilidade e suporte à infraestrutura da empresa.', True)}{feature_cards(features)}</div></section>

      <section class="section section--brand"><div class="container">
        <div class="split"><div data-reveal="left"><span class="eyebrow">Capacidade escalável</span><h2>De 10 Mbps a 10 Gbps</h2><p class="lead">A capacidade ideal depende do número de usuários, aplicações, tráfego, unidades, serviços em nuvem e criticidade da operação.</p><p>O dimensionamento deve considerar consumo atual, picos, crescimento e redundância — não apenas a velocidade nominal.</p><a class="btn btn--primary" href="#" data-whatsapp-message="Olá, preciso dimensionar a capacidade de Link Dedicado para minha empresa.">Dimensionar meu link {svg('arrow')}</a></div>
          <div class="card card--dark" data-reveal="right"><h3>O que avaliar</h3><ul class="check-list check-list--light"><li>Quantidade de usuários e dispositivos</li><li>Telefonia IP e videoconferências</li><li>Sistemas em cloud e backups</li><li>Unidades, datacenters e acessos remotos</li><li>Requisitos de disponibilidade</li><li>Plano de contingência</li></ul></div></div>
      </div></section>

      <section class="section"><div class="container service-showcase">
        <div data-reveal="left"><span class="eyebrow">Lan to Lan / Transporte IP</span><h2>Interconexão privada entre matriz, filiais, datacenters e cloud</h2><p class="lead">O Lan to Lan é uma conexão ponto a ponto que permite tráfego direto entre localidades, com uma arquitetura privada baseada em fibra e roteamento MPLS.</p><ul class="check-list"><li>Integração de redes entre unidades</li><li>Tráfego corporativo com maior controle</li><li>Conexão com datacenters e plataformas cloud</li><li>Performance e segurança para aplicações internas</li></ul></div>
        <div class="service-showcase__media service-showcase__media--contain" data-reveal="right"><img src="../assets/img/integracoes.webp" alt="Conectividade entre unidades, sistemas e cloud" width="760" height="674" loading="lazy"></div>
      </div></section>

      <section class="section section--soft"><div class="container container--narrow">{section_head('Dúvidas frequentes', 'Link Dedicado e Lan to Lan', 'Pontos iniciais para avaliar conectividade corporativa.', True)}{faq([
        ('Qual a diferença entre Link Dedicado e internet comum?', 'O Link Dedicado é dimensionado para uso corporativo, com capacidade exclusiva, velocidade simétrica e acompanhamento técnico mais estruturado.'),
        ('O que significa full duplex?', 'Significa que upload e download podem operar com a mesma capacidade contratada, importante para cloud, backups, voz e videoconferência.'),
        ('Quais velocidades estão disponíveis?', 'O site atual informa links de 10 Mbps a 10 Gbps, sujeitos à análise de viabilidade e ao projeto.'),
        ('O serviço possui monitoramento?', 'Sim. O site atual informa supervisão 24x7x365 pelo NOC, com suporte de engenharia e manutenção em campo.'),
        ('O que é Lan to Lan?', 'É uma interconexão privada ponto a ponto para transportar tráfego entre matriz, filiais, datacenters ou ambientes em nuvem.'),
        ('Quanto tempo leva para ativar?', 'O site atual menciona ativação a partir de 10 dias úteis. O prazo real depende da viabilidade, da região e da infraestrutura necessária.'),
      ])}</div></section>
      {testimonials(1)}
      {cta_banner(1, 'Garanta conectividade para as aplicações críticas', 'Solicite uma análise de viabilidade e dimensionamento para Link Dedicado, redundância ou Lan to Lan.', 'Olá, gostaria de solicitar uma análise de viabilidade para Link Dedicado.')}
    ''')
    return page_shell(title="Link Dedicado D.lextel | Internet corporativa e Lan to Lan", description="Link Dedicado via fibra com velocidade full duplex, NOC 24x7x365, baixa latência e Lan to Lan para empresas.", canonical="https://dlextel.com.br/link-dedicado/", current="service", content=content, depth=1)


PAGES = {
    "index.html": home_page,
    "empresa.html": company_page,
    "solucoes.html": solutions_page,
    "blog.html": blog_page,
    "contato.html": contact_page,
    "servicos/pabx-virtual.html": pabx_virtual_page,
    "servicos/pabx-ip.html": pabx_ip_page,
    "servicos/omnichannel.html": omnichannel_page,
    "servicos/0800-voip.html": voip_0800_page,
    "servicos/link-dedicado.html": link_dedicado_page,
}


def build() -> None:
    for relative, builder in PAGES.items():
        path = ROOT / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(builder(), encoding="utf-8")
        print(f"generated {relative}")


if __name__ == "__main__":
    build()
