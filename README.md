# D.lextel — reconstrução institucional v1

Primeira versão funcional do novo site da D.lextel, desenvolvida em HTML5, CSS e JavaScript puros. O projeto não depende de npm, frameworks ou etapa de compilação para funcionar.

## O que está incluído

### Cinco páginas principais

- `index.html` — Home
- `empresa.html` — A D.lextel
- `solucoes.html` — visão geral das soluções
- `blog.html` — Blog integrado ao WordPress
- `contato.html` — contato com diagnóstico guiado

### Cinco páginas individuais de serviço

- `servicos/pabx-virtual.html`
- `servicos/pabx-ip.html`
- `servicos/omnichannel.html`
- `servicos/0800-voip.html`
- `servicos/link-dedicado.html`

### Recursos implementados

- Layout responsivo para desktop, tablet e celular.
- Identidade visual baseada na marca D.lextel: azul, amarelo e branco.
- Menu fixo, dropdown de serviços e navegação móvel lateral.
- Animações discretas de entrada, contadores, canvas tecnológico no Hero e microinterações.
- Seletor de necessidade na Home para orientar o visitante até a solução mais adequada.
- Carrossel de depoimentos com os relatos já usados no site atual.
- Seção de parceiros com Khomp, AWS, 3CX, VoIP Group e Yealink.
- FAQs interativas.
- Botões e atalho flutuante para o WhatsApp `+55 11 3995-0800`.
- Formulário em três etapas, com validação, resumo da solicitação e armazenamento temporário do rascunho no navegador.
- SEO básico: títulos, descriptions, canonical, Open Graph, favicon e Schema.org.
- Acessibilidade básica: navegação por teclado, ARIA, foco visível, link para pular ao conteúdo e respeito à preferência de movimento reduzido.

## Como visualizar

A forma mais simples é extrair o ZIP e abrir `index.html`. Para testar o Blog e reproduzir melhor o comportamento de um servidor, use um servidor local.

No Linux, macOS ou WSL:

```bash
cd dlextel-site-v1
python3 -m http.server 8000
```

Depois acesse no navegador:

```text
http://localhost:8000/
```

No Windows, também é possível usar a extensão **Live Server** do Visual Studio Code.

## Blog integrado ao WordPress

A página `blog.html` consulta automaticamente:

```text
https://dlextel.com.br/wp-json/wp/v2/posts
```

Assim, os posts atuais e futuros podem aparecer no novo layout sem serem cadastrados novamente. Quando a API não responde, a página mostra uma seleção local de artigos como fallback.

A lógica fica em:

```text
assets/js/blog.js
```

Para manter os artigos no mesmo domínio e preservar SEO, a versão final deve manter o WordPress responsável pelo Blog ou converter este layout em um tema/template WordPress.

## Formulário de contato

Nesta primeira versão, o envio abre o WhatsApp da D.lextel com um resumo preenchido pelo visitante. Isso deixa o formulário funcional sem depender de servidor, plugin ou serviço externo.

A lógica fica em:

```text
assets/js/contact.js
```

Também existe suporte a um endpoint futuro. Antes de carregar `contact.js`, defina:

```html
<script>
  window.DLEXTEL_FORM_ENDPOINT = "https://seu-endpoint.com/contato";
</script>
```

O endpoint deve aceitar uma requisição `POST` em JSON. Sem essa configuração, o fallback pelo WhatsApp continua ativo.

## Estrutura do projeto

```text
dlextel-site-v1/
├── index.html
├── empresa.html
├── solucoes.html
├── blog.html
├── contato.html
├── servicos/
│   ├── pabx-virtual.html
│   ├── pabx-ip.html
│   ├── omnichannel.html
│   ├── 0800-voip.html
│   └── link-dedicado.html
├── assets/
│   ├── css/style.css
│   ├── js/main.js
│   ├── js/blog.js
│   ├── js/contact.js
│   └── img/
├── deploy/
├── preview/
├── robots.txt
├── sitemap.xml
├── QA-REPORT.json
└── build_site.py
```

## Antes de publicar em produção

É importante confirmar internamente:

1. autorização para manter os nomes, logos, depoimentos e percentuais relatados pelos clientes;
2. informações de licença/outorga da Anatel que poderão ser publicadas;
3. especificações comerciais e técnicas, como capacidades, prazos e cobertura;
4. funcionamento atual do plantão técnico após as 18h pela opção 9;
5. dados institucionais, endereço, e-mails e redes sociais que ainda não foram enviados;
6. Política de Privacidade e Termos adequados à LGPD;
7. URLs finais, redirecionamentos 301 e canonical antes da troca do site;
8. otimização final de imagens reais, prints dos sistemas e fotos que ainda serão enviados.

## Publicação no WordPress

Há dois caminhos recomendados:

### Opção 1 — transformar o layout em tema WordPress

É a melhor opção para preservar Blog, administração, URLs, SEO e futuras atualizações. Os HTMLs viram templates PHP e o CSS/JS pode ser reaproveitado praticamente sem mudanças.

### Opção 2 — páginas estáticas com WordPress apenas no Blog

É possível manter os HTMLs como páginas institucionais e o WordPress numa rota ou subdiretório. Nesse caso, servidor, rewrites, canonical e sitemap precisam ser configurados com cuidado.

O arquivo `deploy/apache-rewrites.example.txt` contém apenas uma referência inicial. Ele não deve substituir o `.htaccess` do WordPress sem revisão.

## Qualidade e testes

Foram realizados testes automatizados em desktop e celular para:

- carregamento das 10 páginas;
- ausência de overflow horizontal;
- menu móvel e dropdown;
- seletor de soluções;
- carrossel;
- FAQs;
- formulário completo;
- fallback do Blog;
- links de WhatsApp;
- existência de arquivos, IDs e âncoras locais;
- sintaxe dos arquivos JavaScript.

O resultado detalhado está em `QA-REPORT.json`.
