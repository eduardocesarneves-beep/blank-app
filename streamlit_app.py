"""
KONEXÃO DIRETA (KD) - Portal Principal
Função: Este arquivo serve como o ponto de entrada principal da plataforma KD, 
integrando os portais de Empresa, Profissional e Backoffice conforme definido no SPEC.md.
Responsável por gerenciar a navegação, autenticação básica e a interface do usuário 
utilizando o framework Streamlit.
"""

import streamlit as st

# Configuração da página seguindo o Design System (SPEC.md 2.0)
st.set_page_config(
    page_title="Konexão Direta (KD)",
    page_icon="🔗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização básica seguindo a paleta de cores (SPEC.md 2.1)
st.markdown("""
    <style>
    :root {
        --kd-purple: #7F77DD;
        --kd-blue: #378ADD;
        --kd-gradient: linear-gradient(135deg, #534AB7 0%, #378ADD 100%);
    }
    .main-title {
        background: var(--kd-gradient);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        font-size: 3rem;
    }
    </style>
""", unsafe_allow_html=True)

def show_home():
    st.markdown('<h1 class="main-title">Konexão Direta (KD)</h1>', unsafe_allow_html=True)
    st.subheader("Conexões técnicas. Negócios seguros.")
    
    st.write("""
    **KONEXÃO DIRETA (KD)** é um marketplace SaaS B2B2P de governança e intermediação que conecta 
    empresas contratantes a profissionais independentes (PF, MEI e PJ) com segurança jurídica, 
    financeira e operacional.
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 🏗️ KD AEC")
        st.write("Arquitetura, Engenharia e Construção.")
    with col2:
        st.markdown("### 💻 KD TI")
        st.write("Tecnologia, Dados e IA.")
    with col3:
        st.markdown("### 🛠️ KD MEI")
        st.write("Execução operacional e serviços de campo.")

def show_portal_empresa():
    st.header("🏢 Portal Empresa")
    st.info("Status: Em desenvolvimento (Sprint 2)")
    
    tabs = st.tabs(["Dashboard", "Criar Demanda", "Minhas Demandas", "Financeiro"])
    
    with tabs[0]:
        st.write("Visão geral das suas contratações e demandas ativas.")
    with tabs[1]:
        st.write("Formulário para publicação de novas demandas técnicas.")
    with tabs[2]:
        st.write("Acompanhamento de matches e ordens de serviço.")
    with tabs[3]:
        st.write("Gestão de pagamentos e escrow (Asaas).")

def show_portal_profissional():
    st.header("👷 Portal Profissional")
    st.info("Status: Em desenvolvimento (Sprint 2)")
    
    tabs = st.tabs(["Dashboard", "Convites", "Minhas OS", "Financeiro", "Perfil & KYC"])
    
    with tabs[0]:
        st.write("Resumo de ganhos, reputação e convites pendentes.")
    with tabs[1]:
        st.write("Novas oportunidades de trabalho recebidas via matching.")
    with tabs[2]:
        st.write("Gestão de execução de serviços e entrega de marcos.")
    with tabs[3]:
        st.write("Carteira, saques e notas fiscais.")
    with tabs[4]:
        st.write("Verificação documental e acervo técnico.")

def show_backoffice():
    st.header("⚙️ Backoffice KD")
    st.warning("Acesso restrito à equipe interna.")
    
    tabs = st.tabs(["Compliance/KYC", "Matching Manual", "Disputas", "Financeiro Geral"])
    
    with tabs[0]:
        st.write("Análise de documentos e aprovação de perfis.")
    with tabs[1]:
        st.write("Curadoria de matches entre empresas e profissionais.")
    with tabs[2]:
        st.write("Mediação de conflitos e análise de evidências.")
    with tabs[3]:
        st.write("Monitoramento de transações e splits.")

# Navegação Lateral
st.sidebar.image("https://via.placeholder.com/150x50?text=KD+LOGO", use_container_width=True)
st.sidebar.title("Navegação")
page = st.sidebar.selectbox(
    "Selecione o Portal:",
    ["Home", "Portal Empresa", "Portal Profissional", "Backoffice KD"]
)

# Renderização da Página
if page == "Home":
    show_home()
elif page == "Portal Empresa":
    show_portal_empresa()
elif page == "Portal Profissional":
    show_portal_profissional()
elif page == "Backoffice KD":
    show_backoffice()

# Rodapé
st.sidebar.markdown("---")
st.sidebar.caption("KD v1.0 | Março 2026")
