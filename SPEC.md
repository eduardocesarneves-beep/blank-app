# KONEXÃO DIRETA — SPEC.md
> Documento mestre de especificação do produto. Fonte única de verdade para produto, design, desenvolvimento e compliance.
> Versão: 1.0 | Data: Março/2026 | Status: Ativo

---

## ÍNDICE

1. [Visão Geral e Posicionamento](#1-visão-geral-e-posicionamento)
2. [Identidade Visual e Design System](#2-identidade-visual-e-design-system)
3. [Arquitetura da Plataforma](#3-arquitetura-da-plataforma)
4. [Perfis de Usuário e RBAC](#4-perfis-de-usuário-e-rbac)
5. [Cadastro, KYC e Compliance](#5-cadastro-kyc-e-compliance)
6. [Redes Sociais — Enriquecimento e Parceiros](#6-redes-sociais--enriquecimento-e-parceiros)
7. [Modelo de Monetização Completo](#7-modelo-de-monetização-completo)
8. [Motor de Matching](#8-motor-de-matching)
9. [Fluxo Contratual e Anonimato](#9-fluxo-contratual-e-anonimato)
10. [Tipos de Contratação](#10-tipos-de-contratação)
11. [Minidisputa — Pregão Eletrônico Privado](#11-minidisputa--pregão-eletrônico-privado)
12. [Formulários de Demanda por Vertical](#12-formulários-de-demanda-por-vertical)
13. [Ordem de Serviço (OS)](#13-ordem-de-serviço-os)
14. [Fluxo Financeiro — Escrow, Split e NF](#14-fluxo-financeiro--escrow-split-e-nf)
15. [Acervo Técnico AEC e Relatório por IA](#15-acervo-técnico-aec-e-relatório-por-ia)
16. [Perfil Aluno-Mentorado — KD TI](#16-perfil-aluno-mentorado--kd-ti)
17. [Catálogo de Serviços por Vertical](#17-catálogo-de-serviços-por-vertical)
18. [Sistema de Disputas e Mediação](#18-sistema-de-disputas-e-mediação)
19. [Rules Engine — Antibypass e Segurança](#19-rules-engine--antibypass-e-segurança)
20. [Reputação, Score e Avaliação Bilateral](#20-reputação-score-e-avaliação-bilateral)
21. [Módulo de Notificações](#21-módulo-de-notificações)
22. [Mapa de Telas](#22-mapa-de-telas)
23. [Arquitetura Técnica](#23-arquitetura-técnica)
24. [Integrações de API](#24-integrações-de-api)
25. [Segurança e LGPD](#25-segurança-e-lgpd)
26. [Roadmap — 8 Sprints MVP](#26-roadmap--8-sprints-mvp)

---

## 1. Visão Geral e Posicionamento

### 1.1 Definição do Produto

**KONEXÃO DIRETA (KD)** é um marketplace SaaS B2B2P de governança e intermediação que conecta empresas contratantes a profissionais independentes (PF, MEI e PJ) com segurança jurídica, financeira e operacional.

> "Conexões técnicas. Negócios seguros."

A KD opera como **intermediadora de negócios** — não assume responsabilidade técnica pela execução dos serviços contratados. Seu papel é garantir governança, rastreabilidade, segurança contratual e financeira em toda a cadeia de contratação.

### 1.2 Problema Resolvido

| Lado | Dor principal |
|------|--------------|
| Empresa | Informalidade contratual, risco de inadimplência, falta de rastreabilidade, exposição jurídica trabalhista |
| Profissional | Medo de não receber, escopo mal definido, falta de proteção contratual, reputação fragmentada |
| Mercado | Contratações técnicas bilionárias operando com WhatsApp, PDF e boa fé |

### 1.3 Verticais Operacionais

| Vertical | Foco | Registro obrigatório |
|----------|------|---------------------|
| **KD AEC** | Arquitetura, Engenharia e Construção | CREA ou CAU ativo |
| **KD TI** | Tecnologia, Dados e Inteligência Artificial | MEI ou PJ ativo |
| **KD MEI** | Execução operacional e serviços de campo | MEI ativo |

### 1.4 Módulos Futuros (Fase 2)

- **UNIVERSIDADE KD** — capacitação e certificação profissional (LMS)
- **KD INFRA** — marketplace de locação de hardware e licenças de software técnico

### 1.5 Modelo de Operação

```
Empresa publica demanda
       ↓
KD faz matching curado
       ↓
Profissional aceita (ANÔNIMO)
       ↓
Minuta → Contrato assinado (ANÔNIMO)
       ↓
Empresa deposita no Escrow (Asaas)
       ↓
IDENTIDADES REVELADAS → OS gerada
       ↓
Execução por marcos
       ↓
Aprovação → Split automático (Asaas)
       ↓
NF + ART/RRT → Saque liberado
```

---

## 2. Identidade Visual e Design System

### 2.1 Paleta de Cores (extraída da logo KD)

```css
/* Cores primárias */
--kd-purple:     #7F77DD;   /* Roxo principal — logo */
--kd-purple-dark:#534AB7;   /* Roxo escuro */
--kd-blue:       #378ADD;   /* Azul principal — logo */
--kd-blue-dark:  #185FA5;   /* Azul escuro */

/* Gradiente oficial da marca */
--kd-gradient: linear-gradient(135deg, #534AB7 0%, #378ADD 100%);

/* Backgrounds */
--kd-bg-dark:    #0F0F23;   /* Fundo escuro (tema dark) */
--kd-bg-light:   #F8FAFC;   /* Fundo claro (tema light) */
--kd-surface:    #FFFFFF;   /* Cards e superfícies */

/* Semânticas */
--kd-success:    #1D9E75;
--kd-warning:    #BA7517;
--kd-danger:     #E24B4A;
--kd-info:       #185FA5;

/* Neutros */
--kd-gray-900:   #2C2C2A;
--kd-gray-600:   #5F5E5A;
--kd-gray-200:   #D3D1C7;
--kd-gray-50:    #F1EFE8;
```

### 2.2 Tipografia

```css
/* Display / Headings */
font-family: 'Space Grotesk', sans-serif;

/* Body / Interface */
font-family: 'Inter', sans-serif;

/* Código / Técnico */
font-family: 'JetBrains Mono', monospace;
```

### 2.3 Temas

- **Light**: fundo `#F8FAFC`, superfícies brancas, texto `#2C2C2A`
- **Dark**: fundo `#0F0F23`, superfícies `#1A1A2E`, texto `#F8FAFC`
- Alternância nativa — usuário escolhe; sistema respeita `prefers-color-scheme`

### 2.4 Diretrizes de Design

| Diretriz | Valor |
|----------|-------|
| Estilo | Corporate tech premium |
| Referências | Stripe, Deel, Linear, Brex |
| Border radius | 8px (componentes), 12px (cards) |
| Sombras | Apenas sombras funcionais (sem decorativas) |
| Animações | Entrada: 200ms ease-out; Saída: 150ms ease-in |
| Grid | 12 colunas, gutter 24px |
| Densidade | Dashboard executivo — limpo, orientado a dados |
| CTA principal | Gradiente `--kd-gradient` |

### 2.5 Componentes Base

- `<KdButton>` — primary (gradiente) / secondary (outline) / ghost / danger
- `<KdBadge>` — verified / bronze / silver / gold / platinum / elite / student
- `<KdCard>` — surface branca, borda 0.5px, radius 12px
- `<KdScore>` — display de score com barra de progresso e nível
- `<KdTimeline>` — linha do tempo de OS com ícones por etapa
- `<KdChat>` — chat corporativo com antibypass integrado

---

## 3. Arquitetura da Plataforma

### 3.1 Ambientes

| Ambiente | URL sugerida | Usuários |
|----------|-------------|---------|
| Site público institucional | konexaodireta.com.br | Visitantes |
| Portal Empresa | app.konexaodireta.com.br/empresa | Perfis empresa |
| Portal Profissional | app.konexaodireta.com.br/profissional | Perfis profissionais |
| Backoffice KD | admin.konexaodireta.com.br | Equipe interna KD |

### 3.2 Módulos do Sistema

```
┌─────────────────────────────────────────────────────────┐
│                    KONEXÃO DIRETA                        │
├──────────────┬──────────────┬──────────────┬────────────┤
│   Identidade │  Marketplace │   Contratação│  Financeiro│
│  Auth / KYC  │  Demandas    │  OS / Marcos │  Escrow    │
│  RBAC / LGPD │  Matching    │  Assinatura  │  Split     │
│  Redes Soc.  │  Catálogo    │  Anonimato   │  Carteira  │
├──────────────┼──────────────┼──────────────┼────────────┤
│   Reputação  │   Disputas   │  Compliance  │  Admin KD  │
│  Score       │  Mediação    │  SICAF       │  Backoffice│
│  Avaliações  │  Evidências  │  CEIS/CNEP   │  Analytics │
│  Badges      │  Penalidades │  ART/RRT     │  Auditoria │
└──────────────┴──────────────┴──────────────┴────────────┘
```

---

## 4. Perfis de Usuário e RBAC

### 4.1 Perfis Internos KD

| Perfil | Permissões principais |
|--------|-----------------------|
| `SUPER_ADMIN_KD` | Acesso total — configurações, planos, integrações, usuários |
| `OPERACAO_KD` | Curadoria de matching, supervisão de OS, mediação |
| `FINANCEIRO_KD` | Escrow, splits, saques, reconciliação, relatórios |
| `COMPLIANCE_KYC_KD` | Verificação documental, SICAF, CEIS/CNEP, aprovações |
| `SUPORTE_KD` | Tickets, FAQ, chat de suporte, visualização de OS |

### 4.2 Perfis Empresa

| Perfil | Permissões principais |
|--------|-----------------------|
| `EMPRESA_OWNER` | Acesso total à conta — plano, usuários, financeiro, demandas |
| `EMPRESA_GESTOR` | Criar demandas, acompanhar OS, aprovar marcos, ver financeiro |
| `EMPRESA_SOLICITANTE` | Criar demandas, acompanhar OS (sem acesso financeiro) |
| `EMPRESA_FINANCEIRO` | Aprovar pagamentos, liberar marcos, relatórios financeiros |
| `EMPRESA_JURIDICO` | Visualizar contratos, OS, disputas (somente leitura) |

### 4.3 Perfis Profissional

| Perfil | Permissões principais |
|--------|-----------------------|
| `PROFISSIONAL_PF` | Perfil completo — convites, OS, financeiro, acervo |
| `PROFISSIONAL_MEI` | Idem PF + CNPJ MEI vinculado |
| `PROFISSIONAL_PJ` | Idem MEI + dados empresariais |
| `ALUNO_MENTORADO` | Idem profissional + badge estudante + mentor vinculado — maior de 18 anos |
| `MENTOR_IES` | Visualização de OS do aluno, comentários técnicos (somente leitura operacional) |

### 4.4 Regras Especiais de Acesso

- Um usuário pode ter **múltiplos perfis** (ex: profissional que também contrata como empresa)
- Profissional e empresa que tenham **conflito registrado** nunca se encontram no mesmo matching
- O perfil `ALUNO_MENTORADO` exige **vinculação com IES parceira** e mentor ativo
- Menor de 18 anos: **bloqueio absoluto** em qualquer perfil profissional ou aluno

---

## 5. Cadastro, KYC e Compliance

### 5.1 Fluxo de Onboarding

```
Acessa plataforma
      ↓
Escolhe perfil: [Empresa] ou [Profissional]
      ↓
Dados básicos (nome, e-mail, senha ou OAuth social)
      ↓
[PASSO INDUZIDO] Conectar redes sociais (LinkedIn, Instagram, Facebook, TikTok, YouTube)
   — Linguagem: "Conecte suas redes e receba ofertas exclusivas de parceiros KD
     alinhadas ao seu momento profissional"
   — Botão: "Conectar e aproveitar benefícios" / Link: "Agora não"
      ↓
Upload de documentos por perfil
      ↓
Aceite de Termos de Uso + Política de Privacidade
      ↓
Status: CADASTRO_BASICO (navegação liberada, operação bloqueada)
      ↓
Análise KD (até 48h úteis)
      ↓
Status: VERIFICADO_DOCUMENTAL (operação liberada)
```

### 5.2 Documentos por Perfil

#### Empresa Contratante

| Documento | Obrigatório | Validação |
|-----------|------------|-----------|
| CNPJ | Sim | API Receita Federal (automática) |
| Contrato social / ato constitutivo | Sim | Upload PDF → OCR + análise manual KD |
| Documento representante legal (RG/CNH) | Sim | Upload + selfie com documento |
| Comprovante de endereço (≤90 dias) | Sim | Upload PDF/imagem |
| Dados bancários PJ | Sim | Validação Asaas (para escrow) |
| Consulta CEIS/CNEP | Sim | API automática (bloqueio se inidônea) |
| Consulta SICAF | Opcional | API ComprasNet/Gov.br — obrigatório no plano Licitante |
| Aceite Termos de Uso | Sim | Registro com timestamp e IP |

#### Profissional KD AEC

| Documento | Obrigatório | Validação |
|-----------|------------|-----------|
| CPF | Sim | API Receita Federal |
| CNPJ (se MEI/PJ) | Sim | API Receita Federal |
| Selfie com documento | Sim | Prova de vida — análise manual KD |
| Comprovante de endereço | Sim | Upload |
| Dados bancários | Sim | Validação Asaas |
| Registro CREA ou CAU ativo | Sim — bloqueante | Upload + validação manual KD |
| Currículo (campos guiados) | Sim | Preenchimento na plataforma |
| Acervo técnico (ARTs, RRTs, atestados) | Sim — obrigatório para operar em AEC | Upload PDF → leitura IA |
| Portfólio (imagens/links de projetos) | Opcional | Upload ou links |

#### Profissional KD TI

| Documento | Obrigatório | Validação |
|-----------|------------|-----------|
| CPF | Sim | API Receita Federal |
| CNPJ MEI ou PJ | Sim — bloqueante | API Receita Federal |
| Selfie com documento | Sim | Análise manual KD |
| Comprovante de endereço | Sim | Upload |
| Dados bancários | Sim | Validação Asaas |
| Currículo (campos guiados) | Sim | Preenchimento na plataforma |
| Portfólio (GitHub, projetos, links) | Obrigatório mínimo 1 item | Upload ou link |

#### Profissional KD MEI

| Documento | Obrigatório | Validação |
|-----------|------------|-----------|
| CPF | Sim | API Receita Federal |
| CNPJ MEI ativo | Sim — bloqueante | API Receita Federal |
| Certificado MEI | Sim | Upload + validação CNPJ |
| Selfie com documento | Sim | Análise manual KD |
| Comprovante de endereço | Sim | Upload |
| Dados bancários | Sim | Validação Asaas |
| Currículo (campos guiados) | Sim | Preenchimento na plataforma |
| Consulta SICAF (se aplicável) | Opcional | API ComprasNet |

#### Aluno-Mentorado KD TI

| Documento | Obrigatório | Observação |
|-----------|------------|-----------|
| CPF | Sim | Maior de 18 anos — validação obrigatória |
| Comprovante de matrícula na IES parceira | Sim | Upload + validação com IES |
| Dados bancários | Sim | Validação Asaas |
| Currículo simplificado | Sim | Preenchimento na plataforma |
| Vinculação com mentor (professor IES) | Sim — bloqueante | Mentor aceita o vínculo |

### 5.3 Níveis de Verificação (Selo KD)

| Nível | Critério | Acesso |
|-------|---------|--------|
| `CADASTRO_BASICO` | E-mail confirmado + dados básicos | Navegação apenas |
| `PERFIL_COMPLETO` | Todos os campos preenchidos | Sem operação |
| `VERIFICADO_DOCUMENTAL` | Documentos aprovados pela KD | Operação completa |
| `VERIFICADO_PREMIUM` | Score alto + histórico positivo + 6+ meses na plataforma | Destaque automático no ranking |
| `ELEGIVEL_SEGURO` | Verificado + critérios ViaSeg aprovados | OS com cobertura ViaSeg ativa |

### 5.4 SLA de Verificação

| Tipo | Prazo padrão | Prazo expresso (upsell) |
|------|-------------|------------------------|
| Profissional | 48h úteis | 4h úteis (R$ 79) |
| Empresa | 48h úteis | 24h úteis |
| Renovação de documentos | 24h úteis | 2h úteis |

### 5.5 Verificação SICAF

- **API**: ComprasNet / Portal de Compras do Governo Federal
- **Uso**: verificação de regularidade fiscal, trabalhista, previdenciária e qualificação técnica
- **Aplicação**:
  - Empresas contratantes que participam de licitações públicas
  - MEIs prestadores que atendem contratos públicos
  - Obrigatório no plano **Licitante**; opcional nos demais
- **Bloqueio**: empresa ou MEI com irregularidade grave no SICAF → alerta na plataforma (não bloqueia automaticamente — análise manual KD)

---

## 6. Redes Sociais — Enriquecimento e Parceiros

### 6.1 Objetivo

Enriquecer o perfil do usuário na plataforma e habilitar direcionamento de campanhas externas por parceiros do grupo KD, de forma **transparente e em conformidade com a LGPD**.

### 6.2 Redes Suportadas

| Rede | OAuth | Dados extraídos | Melhor perfil |
|------|-------|----------------|---------------|
| LinkedIn | Sim | Cargo, empresa, histórico profissional, foto, bio, conexões | Empresa, AEC, TI |
| Instagram | Sim | Posts públicos, hashtags, localização, seguidores | MEI, AEC |
| Facebook | Sim | Perfil público, páginas, grupos | Todos |
| TikTok | Sim | Vídeos públicos, categorias de conteúdo | MEI, Alunos |
| YouTube | Sim | Vídeos, categorias, descrições | TI, AEC |

### 6.3 Fluxo de Aceite — Dois Momentos

**Momento 1 — Onboarding (wizard de cadastro, passo 3):**

```
┌─────────────────────────────────────────────────────────┐
│  Potencialize seu perfil KD                             │
│                                                         │
│  Conecte suas redes sociais e tenha acesso a ofertas    │
│  exclusivas de parceiros KD alinhadas ao seu momento    │
│  profissional — materiais, ferramentas, software e      │
│  muito mais, direto para você no momento certo.         │
│                                                         │
│  [LinkedIn]  [Instagram]  [Facebook]  [TikTok]         │
│                                                         │
│  ✓ Você pode desconectar a qualquer momento             │
│  ✓ Seus dados nunca são vendidos a terceiros            │
│  ✓ Apenas parceiros credenciados KD têm acesso          │
│                                                         │
│  [Conectar e aproveitar]        [Agora não →]           │
└─────────────────────────────────────────────────────────┘
```

**Momento 2 — Dashboard vazio (empty state após cadastro):**

```
Banner persistente (dispensável, reaparece após 7 dias):

"Complete seu perfil KD — conecte suas redes e desbloqueie
 ofertas personalizadas de parceiros. Leva menos de 1 minuto."
 
[Conectar agora]  [Lembrar depois]
```

### 6.4 Conformidade LGPD

| Requisito LGPD | Implementação KD |
|----------------|-----------------|
| Finalidade informada | "Receber ofertas de parceiros KD alinhadas ao seu momento profissional" — exibido no aceite |
| Consentimento específico | Aceite separado dos Termos de Uso — checkbox próprio com timestamp e IP |
| Direito de revogação | Botão "Desconectar redes" disponível a qualquer momento nas configurações |
| Compartilhamento com terceiros | "Parceiros credenciados KD" — mencionado no aceite; lista completa disponível na Política de Privacidade |
| Portabilidade | Usuário pode solicitar exportação de todos os dados coletados via redes |
| Não obrigatoriedade | Campo opcional — plataforma funciona normalmente sem a conexão |

### 6.5 Uso dos Dados

```
Usuário conecta rede social
        ↓
KD coleta dados públicos via OAuth
        ↓
Motor de análise comportamental identifica:
  - Fase de obra (posts com fotos de execução → AEC)
  - Stack tecnológico (posts sobre linguagens → TI)
  - Tipo de serviço (vídeos de execução → MEI)
  - Momento de compra (post "iniciando obra", "comprando material")
        ↓
Segmentação enviada ao parceiro autorizado
(ex: e-commerce de materiais de construção)
        ↓
Parceiro executa campanha externa direcionada
(e-mail, anúncio, notificação — fora da plataforma KD)
```

> **Importante**: a KD não exibe anúncios dentro da plataforma. O direcionamento ocorre **fora** da plataforma KD, através dos canais do parceiro.

---

## 7. Modelo de Monetização Completo

### 7.1 Empresa — Planos de Assinatura (sem fee transacional)

| | Básico | Pro | Full | Licitante |
|--|--------|-----|------|-----------|
| **Preço/mês** | R$ 997 | R$ 1.500 | R$ 4.997 | R$ 2.997 |
| **Fee transacional** | 0% | 0% | 0% | 0% |
| **Usuários inclusos** | 2 | 3 | 3 | 3 |
| **Nichos** | 1 | 2 | 3 (todos) | AEC + 1 |
| **OS/mês** | Até 10 | Até 20 | Ilimitadas | Até 30 |
| **Matching** | Automático | Auto + curadoria | Curadoria prioritária | Curadoria prioritária |
| **Minidisputa** | Upsell | 1 inclusa/mês | Ilimitadas | 2 inclusos/mês |
| **Relatório acervo** | Não | Não | Incluso | Ilimitado |
| **SICAF integrado** | Não | Não | Não | Sim |
| **Export compliance** | Não | Não | Não | Sim |
| **Suporte** | E-mail padrão | E-mail prioritário | Dedicado | Dedicado |
| **API** | Leitura básica | Leitura avançada | Full + webhooks | Full + webhooks |

**Expansão de plano:**
- Módulo adicional (nicho extra): **R$ 1.300/mês**
- Usuário adicional: **R$ 150/mês por usuário**
- Trial recomendado: **14 dias sem custo** para novos cadastros

### 7.2 Empresa — Upsells e Minisserviços

| Serviço | Valor | Descrição |
|---------|-------|-----------|
| Minidisputa avulsa | R$ 290/evento | Pregão eletrônico — incluso no Full e Licitante |
| Urgência na demanda | R$ 149/demanda | Curadoria KD prioritária — SLA matching 4h |
| Relatório acervo técnico | R$ 49/relatório ou R$ 129/mês | Relatório IA do acervo do profissional |
| Relatório compliance fornecedor | R$ 89/relatório | Due diligence formal ESG/compliance |
| Seguro ViaSeg por OS | % sobre valor (ViaSeg) | Cobertura opcional por OS |
| Taxa de disputa | R$ 197/evento | Reembolsada se decisão favorável à empresa |

### 7.3 Profissional — Fee Progressivo por Volume

> **Zero custo até o primeiro contrato.** Fee cobrado sobre o valor bruto negociado entre empresa e profissional na OS, descontado automaticamente via split Asaas.

| Faixa acumulada (12 meses móveis) | Fee | Nível | Benefício extra |
|----------------------------------|-----|-------|----------------|
| 1ª OS (estreia) | **0%** | Iniciante | Primeiro contrato sem custo |
| R$ 0 a R$ 10.000 | **12%** | Bronze | Acesso a convites da plataforma |
| R$ 10.001 a R$ 30.000 | **10%** | Prata | Badge Prata no perfil |
| R$ 30.001 a R$ 80.000 | **8%** | Ouro | Badge Ouro + prioridade no matching |
| R$ 80.001 a R$ 200.000 | **6%** | Platinum | Platinum + destaque automático no ranking |
| Acima de R$ 200.000 | **4%** | Elite KD | Elite + gerente de conta KD dedicado |

**Regras do fee progressivo:**
- Volume calculado sobre os **últimos 12 meses móveis**
- Profissional inativo por 12 meses consecutivos retorna ao nível Bronze
- Fee aplicado sobre o **valor bruto da OS** — sem nenhuma cobrança adicional
- Plano Elite do profissional reduz o fee em **1pp extra** sobre a faixa ativa

### 7.4 Profissional — Planos de Destaque

| | Gratuito | Premium | Elite |
|--|---------|---------|-------|
| **Preço/mês** | R$ 0 | R$ 147 | R$ 297 |
| **Fee** | Progressivo normal | Progressivo normal | Progressivo −1pp extra |
| **Destaque no ranking** | Não | Sim | Sim |
| **Badge premium** | Não | Sim | Sim |
| **Convites simultâneos** | Padrão | Ampliado | Máximo |
| **KYC expresso** | Upsell | Não incluso | 1x/mês incluso |
| **Relatório acervo** | Upsell | Upsell | Incluso |
| **Acesso prioritário minidisputas** | Não | Não | Sim |
| **Suporte** | Padrão | Prioritário | Dedicado |

### 7.5 Profissional — Upsells e Minisserviços

| Serviço | Valor | Descrição |
|---------|-------|-----------|
| KYC expresso | R$ 79/solicitação | Análise documental em 4h úteis vs. 48h padrão |
| Antecipação de recebível | 1,5% a 2,5% sobre valor | Antecipa marcos aprovados antes do prazo |
| Seguro ViaSeg por OS | % sobre valor (ViaSeg) | Cobertura opcional por OS |
| Relatório de acervo avulso | R$ 49/relatório | Geração IA do acervo técnico |
| Boost de destaque avulso | R$ 39/7 dias | Posição privilegiada em categoria específica |
| Módulo aluno-mentorado | Gratuito (custo na IES) | Badge estudante + mentor vinculado |

### 7.6 Regras de Upgrade Automático

- Básico com média ≥ 10 OS/mês por 2 meses consecutivos → sugestão de upgrade para Pro
- Pro com média ≥ 20 OS/mês por 2 meses consecutivos → sugestão de upgrade para Full
- Upgrade assistido por CS com cálculo de economia
- Incentivo: **10% de desconto** na primeira mensalidade do novo plano se aceito no mês da sugestão
- Downgrade: somente aprovado com queda real de volume (evita arbitragem de fee)

---

## 8. Motor de Matching

### 8.1 Algoritmo de Sugestão

**Filtros eliminatórios (nesta ordem):**

1. Nicho compatível (AEC, TI ou MEI)
2. Subcategoria exigida (do catálogo padronizado)
3. Status `VERIFICADO_DOCUMENTAL` — somente perfis verificados recebem match
4. Localidade — apenas se demanda exigir presencial ou híbrido (PostGIS)
5. **Filtro de conflito** — par empresa-profissional com disputa registrada → descarte silencioso

**Fórmula de ranqueamento:**

```
Score_Match = (Score_Reputação × 0.40)
            + (Taxa_Conclusão × 0.30)
            + (Tempo_Resposta × 0.20)
            + (Disponibilidade × 0.10)
```

**Ajustes de posição:**
- Profissional com plano Premium ou Elite → +1 posição no ranking
- Profissional com nível Ouro, Platinum ou Elite KD → +1 posição adicional
- Profissional com Acervo Técnico completo (AEC) → +0.5 ponto no score

### 8.2 Entrega do Match

- Shortlist travada em **5 profissionais**
- Operação KD pode ajustar manualmente via backoffice antes de notificar a empresa
- Empresa **não** faz buscas abertas (protege modelo B2B, evita leilão predatório)
- Empresa vê: perfil técnico, score, especialidades, acervo resumido — **sem nome até OS**

### 8.3 Filtro de Conflito

```sql
-- Pseudo-lógica do filtro
SELECT professional_id
FROM match_candidates
WHERE NOT EXISTS (
  SELECT 1 FROM dispute_history
  WHERE company_id = :company_id
  AND professional_id = match_candidates.professional_id
  AND outcome IN ('PENALTY_APPLIED', 'BANNED', 'SETTLEMENT_WITH_PENALTY')
)
```

- O descarte é **silencioso e bilateral** — nenhuma das partes é notificada
- O profissional descartado não sabe que aquela empresa estava na demanda
- A empresa não sabe que aquele profissional existia na base para aquela demanda

---

## 9. Fluxo Contratual e Anonimato

### 9.1 Princípio do Anonimato

Identidades ficam **ocultas** desde a publicação da demanda até a confirmação do pagamento do primeiro marco no escrow.

### 9.2 Fluxo Completo (9 etapas)

| Etapa | Ação | Empresa vê | Profissional vê | Identidades |
|-------|------|-----------|----------------|-------------|
| 1 — Demanda | Empresa publica com ID anonimizado | Própria demanda | Nada | 🔒 Ocultas |
| 2 — Match | Sistema cruza conflitos e gera shortlist | Score + especialidades | Não aparece | 🔒 Ocultas |
| 3 — Shortlist | Empresa recebe até 5 perfis | Perfil técnico sem nome | Nada | 🔒 Ocultas |
| 4 — Convite | Empresa convida; profissional decide | Aguarda aceite | Escopo sem nome empresa | 🔒 Ocultas |
| 5 — Minuta | Plataforma gera minuta com dados mascarados | Dados mascarados | Dados mascarados | 🔒 Ocultas |
| 6 — Contrato | Assinatura digital com IDs mascarados | Assina com ID mascarado | Assina com ID mascarado | 🔒 Ocultas |
| 7 — Pagamento | Empresa deposita no escrow Asaas | Deposita | Confirma — aguarda OS | 🔒 Ocultas |
| **8 — OS gerada** | **DESBLOQUEIO — dados completos** | Nome + CNPJ + contatos | Nome + CNPJ + contatos | ✅ **Reveladas** |
| 9 — Execução | OS aceita — prazo inicia — chat liberado | Fluxo padrão KD | Fluxo padrão KD | ✅ Públicas |

### 9.3 Geração de Minuta e Contrato

```
Convite aceito pelo profissional
        ↓
Sistema gera MINUTA automaticamente com:
  - Objeto (escopo da demanda)
  - Partes (IDs mascarados)
  - Valor e modelo de pagamento
  - Marcos e critérios de aceite
  - Prazos
  - Cláusulas de autonomia (sem vínculo empregatício)
  - Cláusulas antibypass
  - Dispute flow
  - Regras de ART/RRT e NF
  - Política de cancelamento e multas
        ↓
Ambas as partes revisam e aprovam a minuta
        ↓
Sistema gera CONTRATO em PDF jurídico
        ↓
API de assinatura eletrônica (ClickSign / ZapSign / DocuSign)
        ↓
Contrato assinado → status OS: AGUARDANDO_PAGAMENTO
        ↓
Empresa deposita no escrow → status OS: ATIVA
        ↓
DESBLOQUEIO de identidades
```

---

## 10. Tipos de Contratação

| Modalidade | Descrição | Taxa extra |
|------------|-----------|-----------|
| Contratação direta | Empresa seleciona profissional do match diretamente | Não |
| Cotação simples | Empresa recebe shortlist e compara propostas | Não |
| **Minidisputa** | Pregão eletrônico privado — lances em tempo real | **Sim** |
| Convite selecionado | Empresa convida favorito ou profissional do histórico | Não |
| Catálogo / ATA | Contratação pelo catálogo com preço registrado | Não |

---

## 11. Minidisputa — Pregão Eletrônico Privado

> Baseada na lógica da **Lei 14.133/2021 (NLL)**, adaptada para ambiente privado B2B.
> Serviço adicional pago — taxa por evento.

### 11.1 Regras Gerais

- Mínimo de **3 profissionais habilitados** para a sessão abrir
- Taxa **não reembolsável** após abertura da sessão
- Preços **anônimos entre profissionais** — somente empresa vê o ranking ao vivo
- Cada lance deve ser **inferior ao lance anterior** do mesmo profissional
- KD **não interfere** nos valores — livre formação de preço
- Recusa do convite: **sem penalidade** de score

### 11.2 Fluxo em 5 Fases

| Fase | Ação | Gatilho de avanço |
|------|------|-------------------|
| 1 — Abertura | Empresa ativa modo minidisputa + taxa cobrada | Taxa confirmada + convites enviados (mín. 3) |
| 2 — Habilitação | Profissionais aceitam ou recusam | Mín. 3 habilitados — senão empresa amplia ou cancela |
| 3 — Lances | Sessão aberta — lances em tempo real — ranking anônimo | Prazo expirado ou empresa encerra |
| 4 — Adjudicação | Empresa analisa menor preço + score e seleciona | Empresa clica em "Adjudicar" |
| 5 — Contratação | OS gerada com valor vencedor — fluxo padrão KD | OS aceita + escrow confirmado |

### 11.3 Penalidades

| Situação | Penalidade |
|----------|-----------|
| Vencedor desiste após adjudicação | Perda de score + 2º colocado convocado automaticamente |
| Menos de 3 habilitados | Sessão não abre — empresa pode ampliar convites |
| Bypass durante a sessão | Suspensão + perda de cobertura KD |
| Cancelamento após abertura | Taxa não reembolsável |
| Lance igual ou acima do anterior | Sistema rejeita automaticamente |

---

## 12. Formulários de Demanda por Vertical

### 12.1 KD AEC — Wizard 4 Passos

**Passo 1 — Identificação e Contexto**
- Título da demanda *
- Tipo de empreendimento * (residencial uni/multifamiliar / comercial / industrial / institucional / infraestrutura / reforma / outro)
- Disciplina principal * (seleção do catálogo KD AEC)
- Disciplinas complementares (múltipla seleção)
- Fase do projeto * (estudo preliminar / anteprojeto / projeto básico / executivo / as built / legalização / fiscalização / gestão)
- Descrição do objeto * (mínimo 200 caracteres)
- Área aproximada (m²) *
- Número de pavimentos
- Padrão construtivo (simples / médio / alto / luxo)

**Passo 2 — Normas e Requisitos Técnicos**
- Normas aplicáveis (sistema sugere com base na disciplina):
  - NBR 6118 (estruturas de concreto) / NBR 6120 / NBR 8681
  - NBR 9050 (acessibilidade) — obrigatória para edificações de uso público
  - NBR 15575 (desempenho) — obrigatória para residencial
  - NBR 14653 (avaliações / PTAM)
  - Resolução CFM / RDC 50 (para saúde)
  - NR-10 / NR-12 / NR-17 (instalações)
  - ABNT NBR 5626 / 7229 / 10844 (hidrossanitário)
  - IT (Instruções Técnicas do corpo de bombeiros estadual)
  - Outro (campo livre)
- Exige ART/RRT ao contrato? * (obrigatório para AEC)
- Exige BIM? * (não / LOD 100-200 / LOD 300 / LOD 400+)
- Software exigido (campo livre)
- Exige seguro de responsabilidade técnica ViaSeg? (sim/não)

**Passo 3 — Escopo, Entregáveis e Marcos**
- Entregáveis esperados * (múltipla seleção):
  - Memoriais descritivos e calculativos
  - Plantas, cortes e elevações
  - Detalhamentos e especificações
  - Planilha orçamentária (SINAPI / SICRO / outro)
  - Cronograma físico-financeiro
  - Relatório fotográfico
  - Arquivos nativos editáveis
  - Arquivos PDF assinados
- Proposta de marcos * (wizard: descrição + valor + prazo + critério de aceite)
- Modelo de pagamento * (marcos / pacote fechado / hora / m²)
- Prazo total desejado *

**Passo 4 — Localização, Orçamento e Publicação**
- Estado e cidade *
- Modalidade * (presencial / remoto / híbrido)
- Orçamento estimado *
- Urgência * (normal / urgente — taxa adicional)
- Exigências documentais do profissional (campo livre)
- Observações jurídicas / técnicas (campo livre)
- Revisão e publicar

---

### 12.2 KD TI — Wizard 4 Passos

**Passo 1 — Identificação e Contexto**
- Título da demanda *
- Categoria principal * (dev web / mobile / dados-BI / IA-automação / infra-cloud / segurança / UX-UI / QA / suporte / gestão de produto)
- Descrição do problema ou necessidade * (mínimo 200 caracteres)
- Perfil esperado (júnior / pleno / sênior / especialista)
- Tipo de projeto * (novo / evolução de sistema / correção / consultoria / auditoria)

**Passo 2 — Requisitos Técnicos e Normas**
- Stack tecnológico esperado (campo livre)
- Conformidades obrigatórias (múltipla seleção):
  - LGPD — Lei 13.709/2018
  - ISO 27001 (segurança da informação)
  - PCI-DSS (dados de pagamento)
  - OWASP Top 10 (segurança de aplicações web)
  - WCAG 2.1 (acessibilidade digital)
  - PMBOK / Agile / Scrum (gestão)
  - Outro (campo livre)
- Exige documentação técnica? (tipo: diagrama arquitetura / manual / API docs)
- Exige testes automatizados? (não / unitários / integração / E2E)
- Exige entrega em repositório Git? (sim/não)
- Confidencialidade / NDA? *
- Exige seguro ViaSeg? (sim/não)

**Passo 3 — Escopo, Entregáveis e Marcos**
- Entregáveis esperados *:
  - Código-fonte comentado
  - Documentação técnica
  - Testes e relatórios de QA
  - Diagrama de arquitetura
  - Protótipo / mockup validado
  - Integração com ambiente de produção
  - Treinamento ou handoff
- Proposta de marcos *
- Modelo de pagamento * (marcos / hora / pacote)
- Prazo total *

**Passo 4 — Localização, Orçamento e Publicação**
- Modalidade * (remoto / presencial / híbrido)
- Estado e cidade (se presencial/híbrido)
- Orçamento estimado *
- Urgência *
- Exigências documentais adicionais
- Revisão e publicar

---

### 12.3 KD MEI — Wizard 4 Passos

**Passo 1 — Identificação e Contexto**
- Título da demanda *
- Tipo de serviço * (seleção do catálogo KD MEI)
- Descrição do serviço * (mínimo 150 caracteres)
- Tipo de local * (residencial / comercial / industrial / espaço público / obra nova / reforma)
- Área aproximada (m²) ou extensão (m / km) quando aplicável

**Passo 2 — Normas e Requisitos**
- Normas aplicáveis (sistema sugere com base no serviço):
  - NR-10 (instalações elétricas)
  - NR-12 (segurança em máquinas)
  - NR-18 (obra de construção civil)
  - NBR 5410 (instalações elétricas BT)
  - NBR 7229 / 10844 (hidrossanitário)
  - NBR 13571 / 13572 (sondagem)
  - Outro (campo livre)
- Exige EPI específico? (campo livre)
- Exige nota fiscal de serviço? * (sim — obrigatório)
- Exige seguro ViaSeg? (sim/não)

**Passo 3 — Escopo, Entregáveis e Marcos**
- Entregáveis esperados *:
  - Execução do serviço conforme escopo
  - Relatório fotográfico antes/depois
  - Laudo ou declaração de conclusão
  - ART/RRT (se exigido pelo conselho)
  - Nota fiscal de serviço
- Proposta de marcos * (ou valor único)
- Modelo de pagamento * (marcos / pacote / m² / diária)
- Prazo total *

**Passo 4 — Localização, Orçamento e Publicação**
- Estado e cidade * (obrigatório — serviço presencial)
- Endereço completo (enviado ao profissional somente após OS)
- Orçamento estimado *
- Urgência *
- Exigências adicionais
- Revisão e publicar

---

## 13. Ordem de Serviço (OS)

### 13.1 Estrutura Mínima da OS

- Identificação das partes (revelada após pagamento escrow)
- Objeto e escopo completo
- Entregáveis listados com critérios de aceite
- Marcos com valor, prazo e critério de aprovação
- Modelo de pagamento
- Cláusulas de autonomia (ausência de vínculo empregatício)
- Cláusulas antibypass
- Regras de ART/RRT e NF
- Dispute flow
- Regras de cancelamento e multas
- Seguro (se contratado)

### 13.2 Modelos de Pagamento

| Modelo | Descrição | Uso típico |
|--------|-----------|-----------|
| Por marcos | Valor dividido por etapas com critérios de aceite | Projetos AEC e TI em fases |
| Por hora | Valor por hora registrado na OS | Consultoria e suporte TI |
| Por m² | Valor por metro quadrado executado | Projetos AEC / MEI |
| Pacote fechado | Valor total por entrega completa | Jobs TI e MEI pontuais |

### 13.3 SLA de Marco e Aceite Tácito

```
Profissional entrega marco
        ↓
Status: AGUARDANDO_APROVACAO
        ↓
Empresa notificada (e-mail + in-app urgente)
        ↓
D+3: lembrete automático
D+4: segundo lembrete — alerta urgente
D+5: ACEITE TÁCITO — split automático via Asaas
```

### 13.4 Condicionantes de Saque

| Condição | Aplicação | Prazo |
|----------|-----------|-------|
| Nota Fiscal válida | Todos os nichos | D+3 e D+7: notificações; D+15: alerta crítico |
| ART/RRT válida | KD AEC obrigatório | Idem — momento de envio é decisão do profissional |

> O Conselho de Classe exige emissão da ART/RRT ao iniciar o serviço. A plataforma não obriga o timing, mas bloqueia o saque sem o documento.

### 13.5 Pausa e Cancelamento

**Pausa:**
- Empresa solicita com justificativa registrada
- Prazos congelados, escrow mantido, profissional notificado
- Registro auditável obrigatório

**Cancelamento:**

| Tipo | Penalidade | Destino do saldo |
|------|-----------|-----------------|
| Por acordo mútuo | Nenhuma | Saldo restante → empresa; marcos pagos → profissional |
| Unilateral empresa | Multa % sobre marco interrompido | Parte → profissional como indenização |
| Unilateral profissional | Multa % + redução de score | Parte → empresa como indenização |
| Por bypass comprovado | Retenção total + banimento | Conforme decisão KD e Termos de Uso |

---

## 14. Fluxo Financeiro — Escrow, Split e NF

### 14.1 Parceiro Financeiro

**Asaas** — gateway brasileiro com suporte a Pix, cartão, split de pagamento e subcontas.

### 14.2 Fluxo do Escrow

```
Empresa deposita via checkout Asaas (Pix ou Cartão)
        ↓
Asaas webhook → API KD confirma → status OS: ATIVA
        ↓
Profissional executa marcos
        ↓
Marco aprovado (ou aceite tácito D+5)
        ↓
API Asaas Split:
  ├── Fee KD → conta KD
  └── Líquido → carteira do profissional na plataforma
        ↓
NF + ART/RRT validados
        ↓
Saque liberado → transferência para conta bancária do profissional
```

### 14.3 Endpoints Asaas Principais

```http
POST /v3/customers          — criar subconta do profissional
POST /v3/payments           — gerar cobrança Pix/Cartão com split
POST /v3/transfers          — custódia manual se necessário
Webhook: POST /api/v1/webhooks/asaas — confirmar pagamento
```

### 14.4 Tributação

- Impostos são de alçada dos usuários — a plataforma **não** realiza cálculo tributário automático na V1
- A plataforma exibe informação orientativa sobre obrigações fiscais por perfil (MEI, PJ, PF)

---

## 15. Acervo Técnico AEC e Relatório por IA

### 15.1 Composição do Acervo

- ARTs e RRTs emitidas (upload PDF)
- Atestados de Capacidade Técnica de contratantes anteriores
- Certidões de Acervo Técnico (CAT) emitidas pelo CREA
- Documentos complementares de projetos relevantes

### 15.2 Leitura por IA

```
Upload do documento PDF
        ↓
OCR + extração por IA (LLM com prompt especializado)
        ↓
Campos extraídos:
  - Tipo de serviço / disciplina
  - Área (m² / km)
  - Valor do contrato
  - Localidade (estado / município)
  - Ano de execução
  - Responsabilidade técnica (autor / co-autor)
  - Número de registro (ART/RRT/CAT)
  - Norma técnica referenciada
  - Órgão contratante
        ↓
Geração do Relatório de Acervo estruturado
        ↓
Disponível para download pelo profissional
e visualização filtrada pelo contratante
```

### 15.3 Uso pelo Contratante

O contratante (empresa) pode filtrar profissionais por:
- Disciplina técnica
- Tipo de obra / empreendimento
- Porte (faixa de m² ou valor)
- Localidade de execução anterior
- Norma técnica dominada
- Ano de experiência

> Isso permite que empresas identifiquem com precisão qual profissional tem capacidade técnica comprovada para uma licitação específica.

### 15.4 Impacto no Score

- Profissional com Acervo Técnico completo recebe **+0.5 ponto** no score de matching
- Acervo com documentos vencidos ou inconsistentes → alerta no perfil

---

## 16. Perfil Aluno-Mentorado — KD TI

### 16.1 Regras

- Exclusivo para alunos matriculados em **IES parceiras da KD**
- **Obrigatório ser maior de 18 anos** — validação por CPF + data de nascimento
- Vinculação com professor-mentor ativa — obrigatório para operar
- Badge **"Estudante Mentorado"** visível para empresas em todo o perfil e shortlist
- Recebe convites, fecha OS e recebe pagamentos normalmente
- Fee progressivo aplicado normalmente (inicia em 12% na faixa Bronze)
- **Não pode atuar** em OS de alto risco técnico (laudos, perícias, fiscalização de obra)
- Mesmo conjunto de condicionantes de saque do profissional experiente (NF obrigatória)
- A decisão de contratar é sempre da empresa — com pleno conhecimento do perfil estudante

### 16.2 Papel do Mentor

- Recebe notificação a cada marco entregue pelo aluno
- Pode inserir comentários técnicos via módulo de mentoria (somente leitura operacional)
- Acesso limitado ao painel do aluno — não tem acesso financeiro
- Não recebe remuneração da KD — relação é com a IES parceira

### 16.3 Modelo Comercial com IES

- Contrato de parceria entre KD e IES — negociado caso a caso
- IES pode pagar licença de acesso ao módulo de mentoria ou revenue share sobre fees dos alunos
- Alunos acessam gratuitamente — sem mensalidade

---

## 17. Catálogo de Serviços por Vertical

### 17.1 KD AEC

| Grupo | Disciplinas | Conselho |
|-------|------------|---------|
| Arquitetura e Urbanismo | Projeto arquitetônico, interiores, urbanístico, reforma, retrofit, legalização, paisagismo | CAU |
| Eng. Civil e Estrutural | Projeto estrutural (concreto, metálico, madeira), fundações, pontes, laudos estruturais | CREA |
| Instalações Elétricas | Projeto elétrico BT/MT/AT, SPDA, QGBT, automação predial, energia solar, eficiência energética, cabeamento, CFTV | CREA |
| Instalações Hidráulicas | Hidrossanitário predial, água fria/quente, esgoto, drenagem pluvial, ETA/ETE, reúso | CREA |
| Climatização e PPCI | Climatização/AVAC, ventilação mecânica, PPCI/AVCB, sprinkler, gases especiais, NRs | CREA |
| Infraestrutura e Meio Ambiente | Projeto viário, pavimentação, terraplenagem, saneamento, EIA/RIMA, licenciamento, PGRS, barragens | CREA |
| Topografia e Geotecnia | Topografia, georreferenciamento, sondagem SPT/CPT, geotecnia, drones/levantamento aéreo, batimetria | CREA / TRT |
| Tecnologia e Gestão | Compatibilização BIM, modelagem BIM, as built, orçamento, gestão de obra, fiscalização, due diligence, PMOC, cronograma | CREA ou CAU |
| Laudos e Perícias | Laudo técnico/PTAM, perícia de engenharia, vistoria predial, inspeção de fachada, patologia, avaliação de imóveis (NBR 14653) | CREA ou CAU |

> Categoria personalizada: profissional pode solicitar inclusão de disciplina não listada via backoffice KD.

### 17.2 KD TI

Desenvolvimento web, mobile, UX/UI, dados/BI, IA/automações, infra/cloud, suporte técnico, segurança da informação, QA/testes, gestão de produto/projetos.

### 17.3 KD MEI

Eletricista, encanador, pedreiro, pintor, gesseiro, serralheiro, marceneiro, técnico em climatização, instalador, manutenção predial, limpeza técnica/pós-obra, montagem/apoio operacional, topógrafo de campo, sondagem, operador de drone.

---

## 18. Sistema de Disputas e Mediação

### 18.1 Gatilhos de Abertura

- Empresa contesta qualidade ou entrega dentro dos 5 dias úteis
- Profissional contesta cancelamento imotivado
- Obra embargada por órgão competente
- Quebra de prazo injustificada

### 18.2 Fluxo de Mediação

| Fase | Responsável | Prazo | Ação |
|------|------------|-------|------|
| Abertura | Parte solicitante | Imediato | Motivo + evidências iniciais — saldo congelado |
| Defesa | Ambas as partes | 48h | Upload: fotos, prints do chat, laudos |
| Mediação KD | Equipe KD | 5 dias úteis | Análise — KD é **mediadora**, não árbitro técnico |
| Decisão | KD (operacional) | Após mediação | Liberação, estorno ou escalamento externo |
| Escalamento | Partes (externo) | Se necessário | Saldo congelado até decisão judicial/arbitral |

> **Importante**: A KD não julga questões técnicas de engenharia ou qualidade de projeto. Em disputas técnicas profundas, o saldo permanece congelado até acordo externo assinado.
> Taxa de disputa: **R$ 197** cobrada da empresa ao abrir — reembolsada se decisão for favorável.

---

## 19. Rules Engine — Antibypass e Segurança

### 19.1 Monitoramento de Chat

- Chat liberado **somente** após OS gerada e aceita
- Interceptor NLP/Regex em **todas as mensagens** antes de persistir

**Padrões detectados e mascarados:**

```regex
# E-mail
/\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b/

# Telefone (BR)
/(\+55\s?)?(\(?\d{2}\)?\s?)(\d{4,5}[-\s]?\d{4})/

# Chave PIX (CPF/CNPJ/telefone/e-mail/aleatória)
/\b(\d{3}\.?\d{3}\.?\d{3}-?\d{2}|\d{2}\.?\d{3}\.?\d{3}\/?\d{4}-?\d{2})\b/

# Links externos
/(https?:\/\/(?!app\.konexaodireta)[^\s]+)/

# Menções a plataformas externas
/(whatsapp|telegram|instagram|linkedin|gmail|hotmail|yahoo)/i
```

**Ação ao detectar:**
1. Mensagem mascarada: `[Conteúdo retido pela moderação KD]`
2. Flag criada na tabela `audit_logs` com: user_id, message_hash, pattern_matched, timestamp
3. Notificação silenciosa ao backoffice KD para revisão

### 19.2 Penalidades por Bypass

| Nível | Critério | Penalidade |
|-------|---------|-----------|
| Advertência | 1ª ocorrência suspeita | Notificação formal + redução de score |
| Perda de cobertura | Bypass confirmado | KD se isenta de suporte e proteção da OS |
| Cancelamento de seguro | Bypass confirmado + OS segurada | Apólice ViaSeg cancelada |
| Bloqueio temporário | 2ª ocorrência confirmada | Conta suspensa por 30 dias |
| Banimento | Reincidência ou bypass com pagamento externo comprovado | Conta encerrada permanentemente |
| Retenção de saldo | Banimento + saldo em carteira | Retido para cobertura de multas contratuais |

---

## 20. Reputação, Score e Avaliação Bilateral

### 20.1 Score do Profissional (público)

| Fator | Peso | Fonte |
|-------|------|-------|
| Nota média (1-5) | 40% | Avaliações pós-OS |
| Taxa de conclusão | 30% | OS finalizadas sem disputa / total OS |
| Tempo de resposta | 20% | Média para aceitar/recusar convites |
| Disponibilidade | 10% | Atualização do calendário de disponibilidade |

**Ajustes adicionais:**
- Acervo técnico completo (AEC): +0.5 ponto
- Plano Premium ou Elite ativo: +1 posição no ranking
- Nível Ouro, Platinum ou Elite KD: +1 posição adicional

### 20.2 Score da Empresa (parcialmente público para profissionais)

Profissionais visualizam:
- Tempo médio de resposta em aprovação de marcos
- Histórico de pagamentos no prazo
- Taxa de disputas abertas / total de OS
- Índice de cancelamento unilateral

### 20.3 Avaliação Pós-OS

- **Obrigatória** para ambas as partes — desbloqueia novas ações na plataforma
- Componentes: nota 1 a 5 + comentário escrito + tags de desempenho
- Comentários são públicos e moderados
- KD remove apenas em caso de ofensa, assédio ou violação de LGPD
- Notas numéricas **não são alteradas** pela plataforma

### 20.4 Badges de Nível do Profissional

| Badge | Critério | Benefício |
|-------|---------|-----------|
| Iniciante | 1ª OS | Fee zerado |
| Bronze | Até R$ 10k | Acesso a convites |
| Prata | R$ 10k a R$ 30k | Badge Prata no perfil |
| Ouro | R$ 30k a R$ 80k | Badge Ouro + prioridade matching |
| Platinum | R$ 80k a R$ 200k | Platinum + destaque automático |
| Elite KD | Acima R$ 200k | Elite + gerente de conta dedicado |

---

## 21. Módulo de Notificações

### 21.1 Canais

| Canal | Status V1 | Tecnologia |
|-------|----------|-----------|
| E-mail | ✅ Ativo | AWS SES |
| In-app (WebSocket) | ✅ Ativo | Socket.io + NestJS |
| WhatsApp | 🔜 Fase 2 | API oficial Meta |
| Push / Web Push | 🔜 Fase 2 | Firebase FCM |
| SMS | 🔜 Fase 2 | Twilio ou similar |

### 21.2 Eventos e SLAs

| Evento | Canal | Destinatário | SLA |
|--------|-------|-------------|-----|
| KYC aprovado/reprovado | E-mail + in-app | Empresa ou profissional | Imediato |
| Matching gerado | In-app | Operação KD | Imediato |
| Convite enviado | E-mail + in-app | Profissional | Imediato |
| OS gerada | E-mail + in-app | Ambas as partes | Imediato |
| Marco entregue | E-mail urgente + in-app badge | Empresa | Imediato (inicia SLA 5 dias) |
| Lembrete marco D+3 | E-mail urgente | Empresa | D+3 após entrega |
| Lembrete marco D+4 | E-mail crítico + in-app | Empresa | D+4 |
| Aceite tácito D+5 | E-mail + in-app | Ambas as partes | D+5 — split automático |
| Disputa aberta | E-mail + in-app | KD + ambas as partes | Imediato |
| Saque processado | E-mail + in-app | Profissional | Imediato |
| Bypass detectado | In-app alerta | Usuário + backoffice KD | Imediato |
| NF/ART pendente D+3 | E-mail notificação | Profissional | D+3 após aprovação do marco |
| NF/ART pendente D+7 | E-mail urgente | Profissional | D+7 |
| NF/ART pendente D+15 | Alerta crítico + equipe KD | Profissional + KD | D+15 |
| Upgrade sugerido | E-mail + in-app | Empresa | Ao atingir gatilho de volume |
| ViaSeg (reservado) | E-mail + in-app via webhook | Ambas as partes | Conforme ViaSeg API |

---

## 22. Mapa de Telas

### 22.1 Site Público (6 telas)

| ID | Tela | Objetivo |
|----|------|---------|
| 1.1 | Home Principal | Converter visitantes — hero, vantagens, nichos, como funciona, CTA equilibrada |
| 1.2 | Para Empresas | Landing conversão empresa — vantagens, formulário rápido |
| 1.3 | Para Profissionais | Landing conversão profissional — vantagens, formulário rápido |
| 1.4 | Planos e Assinaturas | Tabela comparativa de planos empresa |
| 1.5 | Como Funciona | Passo a passo visual do fluxo completo |
| 1.6 | Segurança e Governança | Pilares: escrow, ViaSeg, compliance, mediação, LGPD |
| 1.7 | Blog / Conteúdo | SEO — artigos por vertical |
| 1.8 | Nichos de Atuação | Landing por vertical: KD AEC, KD TI, KD MEI |
| 1.9 | Cadastro / Onboarding | Wizard com bifurcação empresa/profissional + aceite redes sociais |
| 1.10 | Login / Recuperação | E-mail + OAuth (LinkedIn, Meta, Google) + 2FA |

### 22.2 Portal Empresa (15 telas)

| ID | Tela |
|----|------|
| 2.1 | Dashboard Empresa |
| 2.2 | Criar Demanda (Wizard 4 passos — por vertical) |
| 2.3 | Lista de Demandas |
| 2.4 | Detalhes da Demanda |
| 2.5 | Card Profissional (shortlist) |
| 2.6 | Perfil Profissional Completo |
| 2.7 | Ordem de Serviço |
| 2.8 | Aprovação de Marco |
| 2.9 | Financeiro Empresa |
| 2.10 | Reputação e Reviews |
| 2.11 | Configurações da Conta |
| 2.12 | Gestão de Usuários Internos |
| 2.13 | Notificações Empresa |
| 2.14 | Relatórios e Exportação |
| 2.15 | Detalhes da OS (timeline completa) |

### 22.3 Portal Profissional (12 telas)

| ID | Tela |
|----|------|
| 3.1 | Dashboard Profissional |
| 3.2 | Lista de Convites |
| 3.3 | Detalhes do Convite |
| 3.4 | Minha Conta e Perfil |
| 3.5 | Execução de OS |
| 3.6 | Financeiro Profissional |
| 3.7 | Minha Reputação |
| 3.8 | Upload de Documentos KYC |
| 3.9 | Configurações do Profissional |
| 3.10 | Envio de Nota Fiscal e ART/RRT |
| 3.11 | Notificações Profissional |
| 3.12 | Catálogo de Serviços do Perfil |
| 3.13 | Acervo Técnico (AEC) |

### 22.4 Backoffice KD (11 telas)

| ID | Tela |
|----|------|
| 4.1 | Dashboard Administrativo KD |
| 4.2 | Central de KYC / Compliance |
| 4.3 | Central de Disputas |
| 4.4 | Controle Financeiro |
| 4.5 | Matching Manual (curadoria) |
| 4.6 | Gestão de Usuários |
| 4.7 | Gestão de OS |
| 4.8 | Validação de NF e ART/RRT |
| 4.9 | Auditoria e Logs |
| 4.10 | Gestão do Catálogo |
| 4.11 | Gestão de Planos e Upgrades |

---

## 23. Arquitetura Técnica

### 23.1 Stack

| Camada | Tecnologia | Justificativa |
|--------|-----------|--------------|
| Frontend | Next.js 14 (React) + TailwindCSS | SSR/SSG, SEO, performance |
| Backend API | NestJS (Node.js + TypeScript) | DI tipada, arquitetura modular, enterprise |
| Banco de dados | PostgreSQL 15+ (AWS RDS) | Relacional + PostGIS para geolocalização |
| Cache / Filas | Redis + BullMQ | Jobs assíncronos: matching, notificações, splits |
| Storage | AWS S3 + CloudFront | Documentos, contratos, fotos — Presigned URLs |
| Auth | JWT (access + refresh) + OAuth 2.0 | Login social Meta, LinkedIn, Google |
| WebSocket | Socket.io + NestJS Gateway | Chat antibypass em tempo real |
| Infraestrutura | AWS (ECS Fargate + ALB + RDS + S3) | Escalável, gerenciado |
| CI/CD | GitHub Actions | Deploy automatizado com pipeline de testes |
| Monitoramento | Grafana + Metabase + AWS CloudWatch | Analytics, dashboards, logs |
| Assinatura eletrônica | ClickSign / ZapSign / DocuSign | API para geração e assinatura de OS |

### 23.2 Arquitetura de Aplicação

```
Modular Monolith (V1 MVP)
        ↓
Extração gradual para Microsserviços (Fase 2 / Tração)

Domínios principais:
  01_Identity    — users, companies, professionals
  02_Marketplace — needs (demandas), matches, invites
  03_Contracts   — orders (OS), milestones, signatures
  04_Ledger      — wallets, escrow_accounts, transactions
  05_Reputation  — reviews, scores, badges
  06_Compliance  — kyc_docs, audit_logs, disputes
  07_Notifications — events, channels, templates
```

### 23.3 Banco de Dados — Domínios Principais

```sql
-- 01_Identity
users (id, email, role, status, created_at)
companies (id, legal_name, cnpj, plan, sicaf_status)
professionals (user_id, niche, specialties, score, level)
professional_verifications (id, professional_id, council_type, status)
social_connections (id, user_id, network, oauth_token, consented_at)

-- 02_Marketplace
demands (id, company_id, title, niche, status, budget)
demand_matches (demand_id, professional_id, status, score_at_match)
conflict_registry (id, company_id, professional_id, dispute_id, created_at)

-- 03_Contracts
orders (id, demand_id, company_id, professional_id, status, total_value)
milestones (id, order_id, description, value, due_date, status)
contracts (id, order_id, pdf_s3_key, signed_at, provider)

-- 04_Ledger
wallets (id, user_id, available_balance, held_balance)
escrow_accounts (id, order_id, asaas_id, amount, status)
transactions (id, from_user, to_user, amount, type, asaas_ref)

-- 05_Reputation
reviews (id, order_id, reviewer_id, target_id, score, comment)
audit_logs (id, user_id, action, entity, timestamp, ip)

-- 06_Compliance
kyc_documents (id, user_id, doc_type, s3_key, status, reviewed_by)
disputes (id, order_id, opened_by, reason, status, resolution)
bypass_flags (id, order_id, user_id, pattern, masked_content, timestamp)
```

---

## 24. Integrações de API

| Integração | Finalidade | Status V1 |
|-----------|-----------|----------|
| **Asaas** | Escrow, split, subcontas, Pix, cartão, webhooks | ✅ Prioritária |
| **AWS SES** | Envio de e-mails transacionais e notificações | ✅ Prioritária |
| **OAuth Meta** | Login social Facebook/Instagram | ✅ Prioritária |
| **OAuth LinkedIn** | Login social + enriquecimento de perfil | ✅ Prioritária |
| **OAuth Google** | Login social complementar | ✅ Prioritária |
| **Receita Federal** | Validação CNPJ + CPF | ✅ Prioritária |
| **CEIS / CNEP** | Consulta de inidoneidade | ✅ Prioritária |
| **ClickSign / ZapSign** | Assinatura eletrônica de OS e contratos | ✅ Prioritária |
| **PostGIS (PostgreSQL)** | Geolocalização para matching presencial | ✅ Prioritária |
| **SICAF (ComprasNet)** | Verificação cadastral governo federal | ✅ Plano Licitante |
| **ViaSeg** | Seguro por OS — cotação e emissão de apólice | 🔜 Caminho previsto (API ainda não disponível) |
| **OAuth TikTok** | Login social + enriquecimento | 🔜 Fase 2 |
| **OAuth YouTube** | Enriquecimento de perfil | 🔜 Fase 2 |
| **Firebase FCM** | Push notifications mobile/web | 🔜 Fase 2 |
| **WhatsApp Business API** | Notificações via WhatsApp | 🔜 Fase 2 |
| **KD Open API** | API pública monetizada para parceiros/ERPs | 🔜 Fase 2 |
| **Universidade KD** | LMS integrado | 🔜 Fase 2 |
| **KD Infra** | Marketplace de locação | 🔜 Fase 2 |

---

## 25. Segurança e LGPD

### 25.1 Proteção de Dados

| Camada | Implementação |
|--------|--------------|
| Dados em repouso | Criptografia AES-256 no RDS e S3 para PII (CPF, CNPJ, dados bancários) |
| Dados em trânsito | TLS 1.3 em todas as conexões |
| Acesso a arquivos | S3 privado + Presigned URLs com expiração curta (15 min) |
| Autenticação | JWT (access token 15min + refresh token 7 dias) + 2FA para operações financeiras |
| Auditoria | Log imutável de toda ação de pagamento, alteração de contrato, acesso a documentos |

### 25.2 Conformidade LGPD

| Requisito | Implementação |
|-----------|--------------|
| Consentimento explícito | Termos de Uso + aceite de redes sociais com timestamp e IP |
| Finalidade informada | Descrita no aceite de cada categoria de dado |
| Direito de acesso | Exportação de dados disponível nas configurações |
| Direito ao esquecimento | Solicitação via suporte — dados anonimizados (não deletados por obrigação fiscal) |
| DPO | Responsável de proteção de dados designado internamente |
| Relatório de impacto | RIPD produzido antes do go-live |
| Redes sociais | Aceite específico separado dos Termos — revogável a qualquer momento |

---

## 26. Roadmap — 8 Sprints MVP (16 semanas)

| Sprint | Período | Foco | Entregas principais |
|--------|---------|------|-------------------|
| **Sprint 1** | Sem. 1-2 | Setup e Identidade | AWS + PostgreSQL + Redis + Next.js + NestJS; Login e-mail + OAuth (Meta, LinkedIn, Google); JWT + RBAC; Landing page institucional |
| **Sprint 2** | Sem. 3-4 | KYC, Perfis e Painéis | Fluxo KYC (upload → S3 → análise); Integração Receita Federal + CEIS; Dashboard vazio empresa e profissional; Backoffice triagem documental; Currículo e Acervo Técnico (upload) |
| **Sprint 3** | Sem. 5-6 | Demandas e Catálogo | Wizard de criação de demanda (3 verticais); CRUD demandas com regras de visibilidade; Tela de convites profissional; Catálogo de serviços por vertical; Aceite de redes sociais (onboarding + dashboard) |
| **Sprint 4** | Sem. 7-8 | Motor de Matching | Algoritmo de ranqueamento com PostGIS; Filtro de conflito no matching; Moderação manual KD (backoffice); Card do profissional na shortlist; Leitura IA do Acervo Técnico (AEC) |
| **Sprint 5** | Sem. 9-10 | OS, Anonimato e Chat | Geração de OS com anonimato; Minuta e contrato digital (ClickSign/ZapSign); WebSocket chat com engine antibypass; Filtro NLP/Regex completo; Desbloqueio de identidades pós-pagamento |
| **Sprint 6** | Sem. 11-12 | Escrow, Asaas e Marcos | Integração Asaas (subcontas, Pix, cartão); Escrow por OS; Aprovação de marcos (empresa); Temporizador SLA 5 dias + aceite tácito; Split automático (fee KD + carteira profissional); NF e ART/RRT como condicionantes de saque |
| **Sprint 7** | Sem. 13-14 | Disputas, Reputação e Minidisputa | Fluxo de disputa completo (evidências, mediação, decisão); Congelamento de escrow em disputa; Avaliação bilateral pós-OS; Cálculo e recálculo de score; Fluxo completo de Minidisputa (5 fases); Badges de nível por volume |
| **Sprint 8** | Sem. 15-16 | QA, Dashboards e Deploy | Dashboards completos (empresa, profissional, KD, financeiro); Testes E2E (cadastro → demanda → match → OS → pagamento); Grafana + Metabase sobre PostgreSQL; Deploy AWS (ECS + CloudFront + Route53); Onboarding de early adopters |

---

## Appendix A — Glossário

| Termo | Definição |
|-------|-----------|
| OS | Ordem de Serviço — contrato operacional gerado pela plataforma após aceite mútuo |
| Marco | Etapa de entrega dentro de uma OS com valor, prazo e critério de aceite definidos |
| Escrow | Custódia financeira — valor depositado e retido até aprovação do marco |
| Split | Divisão automática do valor: fee KD + líquido profissional |
| Match | Sugestão de profissionais gerada pelo algoritmo para uma demanda |
| Shortlist | Lista de até 5 profissionais sugeridos para uma demanda |
| Aceite tácito | Aprovação automática de marco por decurso de prazo (D+5 sem manifestação da empresa) |
| Bypass | Tentativa de contratação ou pagamento fora da plataforma |
| Acervo técnico | Conjunto de ARTs, RRTs e atestados que comprovam a capacidade técnica do profissional AEC |
| ATA | Ata de Registro de Preços — modelo de contratação por catálogo com preço previamente registrado |
| KYC | Know Your Customer — processo de verificação documental e identidade |
| SICAF | Sistema de Cadastramento Unificado de Fornecedores — base do governo federal |
| CEIS | Cadastro de Empresas Inidôneas e Suspensas |
| CNEP | Cadastro Nacional de Empresas Punidas |
| ART | Anotação de Responsabilidade Técnica (CREA) |
| RRT | Registro de Responsabilidade Técnica (CAU) |
| NLL | Nova Lei de Licitações — Lei 14.133/2021 |
| IES | Instituição de Ensino Superior |
| GMV | Gross Merchandise Volume — volume total transacionado na plataforma |
| MRR | Monthly Recurring Revenue — receita recorrente mensal |
| LTV | Lifetime Value — valor total gerado por um cliente ao longo do relacionamento |
| LGPD | Lei Geral de Proteção de Dados — Lei 13.709/2018 |

---

## Appendix B — Decisões de Produto Registradas

| Data | Decisão | Racional |
|------|---------|---------|
| Mar/2026 | Asaas como gateway financeiro (vs. ViaBank) | API brasileira, suporte a Pix/cartão, split nativo, KYC básico de subconta |
| Mar/2026 | Anonimato até confirmação de pagamento no escrow | Segurança jurídica bilateral — partes com conflito nunca se encontram |
| Mar/2026 | Fee progressivo por volume (profissional) | Incentivo ao crescimento na plataforma — quanto mais trabalha, menos paga |
| Mar/2026 | Empresa paga mensalidade — profissional paga fee (sem mensalidade até 1ª OS) | Reduz barreira de entrada do profissional — cresce na base antes de pagar |
| Mar/2026 | Acervo técnico AEC lido por IA | Diferencial para licitações — extração estruturada de ARTs/RRTs/atestados |
| Mar/2026 | Aceite de redes sociais em dois momentos (onboarding + dashboard) | Maximiza conversão — segundo momento captura quem pulou no primeiro |
| Mar/2026 | Redes sociais: aceite transparente com finalidade declarada (LGPD) | Evita autuação ANPD — "parceiros credenciados KD" declarado no aceite |
| Mar/2026 | Plano Licitante (R$ 2.997/mês) | Nicho específico de alto LTV — empresas que participam de licitações públicas |
| Mar/2026 | Filtro de conflito silencioso no matching | Mantém qualidade operacional sem expor histórico de disputas |
| Mar/2026 | Minidisputa baseada na NLL 14.133/2021 | Credibilidade jurídica — livre formação de preço sem tabelamento |
| Mar/2026 | Aluno-mentorado com mesmas condicionantes do profissional | Mesma governança — o que muda é currículo, experiência e valor negociado |
| Mar/2026 | Universidade KD e KD Infra na Fase 2 | MVP focado no core — espaço reservado na home ("em breve") |

---

*KONEXÃO DIRETA — Documento gerado em Março/2026*
*Para dúvidas sobre este SPEC, contate o time de produto KD.*
