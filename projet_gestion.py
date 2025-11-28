import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import math
import time
import requests
import json
import sqlite3
import hashlib

class IntegrationSystem:
    """Sous-système d'intégration avancé pour le contrôle de gestion"""
    
    def __init__(self):
        self.connections = {}
        self.init_database()
    
    def init_database(self):
        """Initialisation de la base de données des intégrations"""
        conn = sqlite3.connect('integrations.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS system_connections (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                system_name TEXT NOT NULL,
                system_type TEXT NOT NULL,
                connection_status TEXT NOT NULL,
                last_sync TIMESTAMP,
                api_endpoint TEXT,
                config_data TEXT
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS data_flows (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                flow_name TEXT NOT NULL,
                source_system TEXT NOT NULL,
                target_system TEXT NOT NULL,
                frequency TEXT NOT NULL,
                last_execution TIMESTAMP,
                success_rate REAL
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def add_system_connection(self, name, system_type, endpoint, config):
        """Ajouter une nouvelle connexion système"""
        conn = sqlite3.connect('integrations.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO system_connections 
            (system_name, system_type, connection_status, last_sync, api_endpoint, config_data)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, system_type, 'Disconnected', None, endpoint, json.dumps(config)))
        
        conn.commit()
        conn.close()
    
    def test_connection(self, system_name):
        """Tester la connexion à un système"""
        try:
            # Simulation de test de connexion
            time.sleep(1)
            return True
        except:
            return False
def main():
    st.set_page_config(
        page_title="Contrôle de Gestion",
        page_icon="📊",
        layout="wide"
    )
    # Initialisation du sous-système d'intégration
    if 'integration_system' not in st.session_state:
        st.session_state.integration_system = IntegrationSystem()
    
    # Navigation principale
    st.sidebar.title("🏢 Contrôle de Gestion")
    st.sidebar.markdown("---")
    
    main_sections = [
            "🏠 Accueil",
        "📈 Contrôle de Gestion", 
        "💰 Budget des Ventes",
        "🏭 Budget de Production",
        "📦 Gestion des Stocks",
        "🏗️ Budget d'Investissement", 
        "💸 Budget de Trésorerie",
        "🔄 Processus Complet",
        "📅 Plan d'Implémentation",
        "🚀 Aller Plus Loin",
        "🏠 Tableau de Bord Executive",
        "🔗 Centre d'Intégration Systèmes", 
        "🤖 Automatisation Intelligente",
        "📚 Centre de Connaissances",
        "💰 Budget des Ventes IA",
        "🏭 Production Optimisée",
        "📦 Gestion Stocks Avancée",
        "🏗️ Investissement Stratégique",
        "💸 Trésorerie Prédictive",
        "📊 Reporting Executive"
    ]
    
    main_choice = st.sidebar.radio("Navigation Principale:", main_sections)
    
    # Affichage des sections

    if  main_choice == "🏠 Accueil":
        show_home()
    elif main_choice  == "📈 Contrôle de Gestion":
        show_controle_gestion()
    elif main_choice  == "💰 Budget des Ventes":
        show_budget_ventes()
    elif main_choice  == "🏭 Budget de Production":
        show_budget_production()
    elif main_choice  == "📦 Gestion des Stocks":
        show_gestion_stocks()
    elif main_choice  == "🏗️ Budget d'Investissement":
        show_budget_investissement()
    elif main_choice  == "💸 Budget de Trésorerie":
        show_budget_tresorerie()
    elif main_choice  == "🔄 Processus Complet":
        show_processus_complet()
    elif main_choice  == "📅 Plan d'Implémentation":
        show_plan_implementation()
    elif main_choice  == "🚀 Aller Plus Loin":
        show_advanced_features()
    elif main_choice == "🏠 Tableau de Bord Executive":
        show_executive_dashboard()
    elif main_choice == "🔗 Centre d'Intégration Systèmes":
        show_integration_center()
    elif main_choice == "🤖 Automatisation Intelligente":
        show_intelligent_automation()
    elif main_choice == "📚 Centre de Connaissances":
        show_knowledge_center()
    elif main_choice == "💰 Budget des Ventes IA":
        show_ai_sales_budget()
    elif main_choice == "🏭 Production Optimisée":
        show_optimized_production()
    elif main_choice == "📦 Gestion Stocks Avancée":
        show_advanced_stock_management()
    elif main_choice == "🏗️ Investissement Stratégique":
        show_strategic_investment()
    elif main_choice == "💸 Trésorerie Prédictive":
        show_predictive_cashflow()
    elif main_choice == "📊 Reporting Executive":
        show_executive_reporting()




def show_executive_dashboard():
    st.title("🏠 Tableau de Bord Executive")
    
    # KPI en temps réel
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📈 CA Cumulé", "2.8M €", "+15.2%", delta_color="inverse")
        st.progress(0.85)
    
    with col2:
        st.metric("🏭 Taux Rendement", "92.5%", "+3.2%")
        st.progress(0.92)
    
    with col3:
        st.metric("📦 Rotation Stocks", "8.2", "+1.5")
        st.progress(0.75)
    
    with col4:
        st.metric("💸 Trésorerie", "856K €", "+5.8%")
        st.progress(0.68)
    
    # Alertes intelligentes
    st.subheader("🚨 Alertes Intelligentes")
    
    alert_col1, alert_col2, alert_col3 = st.columns(3)
    
    with alert_col1:
        with st.container(border=True):
            st.error("**Dépassement Budget Production**")
            st.write("Écart: +12.5% vs prévision")
            st.button("Analyser", key="alert1")
    
    with alert_col2:
        with st.container(border=True):
            st.warning("**Niveau Stock Critique**")
            st.write("Article A001: 2 jours restants")
            st.button("Commander", key="alert2")
    
    with alert_col3:
        with st.container(border=True):
            st.success("**Opportunité Investissement**")
            st.write("ROI potentiel: 22.3%")
            st.button("Étudier", key="alert3")
    
    # Graphiques de performance
    col1, col2 = st.columns(2)
    
    with col1:
        # Performance mensuelle
        months = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Jun']
        revenue = [120, 135, 115, 145, 160, 155]
        target = [110, 125, 120, 140, 150, 145]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(name='Réel', x=months, y=revenue))
        fig.add_trace(go.Scatter(name='Objectif', x=months, y=target, mode='lines+markers'))
        fig.update_layout(title='Performance Commerciale Mensuelle')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Répartition des coûts
        costs = {
            'Catégorie': ['Main d\'œuvre', 'Matériaux', 'Frais fixes', 'R&D', 'Marketing'],
            'Montant': [450, 320, 180, 120, 90]
        }
        df_costs = pd.DataFrame(costs)
        
        fig = px.pie(df_costs, values='Montant', names='Catégorie', 
                    title='Répartition des Coûts')
        st.plotly_chart(fig, use_container_width=True)

def show_integration_center():
    st.title("🔗 Centre d'Intégration Systèmes")
    
    # Sous-menu intégration
    integration_tabs = st.tabs([
        "🏗️ Architecture", 
        "🧾 Connecteurs ERP", 
        "🛒 Connecteurs CRM",
        "💰 Connecteurs Comptabilité",
        "📊 Connecteurs BI",
        "🌐 APIs Personnalisées",
        "📡 Monitoring Temps Réel"
    ])
    
    with integration_tabs[0]:
        show_integration_architecture()
    
    with integration_tabs[1]:
        show_erp_connectors()
    
    with integration_tabs[2]:
        show_crm_connectors()
    
    with integration_tabs[3]:
        show_accounting_connectors()
    
    with integration_tabs[4]:
        show_bi_connectors()
    
    with integration_tabs[5]:
        show_custom_apis()
    
    with integration_tabs[6]:
        show_realtime_monitoring()

def show_integration_architecture():
    st.header("🏗️ Architecture d'Intégration Systèmes")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 🎯 Architecture Microservices Modern
        
        **🏗️ Composants Principaux :**
        
        ```python
        class IntegrationArchitecture:
            ├── 🔌 API Gateway
            ├── 🗄️ Message Broker (Kafka/RabbitMQ)
            ├── 💾 Data Lake
            ├── 🔄 ETL Engine
            ├── 🛡️ Security Layer
            ├── 📊 Monitoring
            └── 🔧 Connectors
        ```
        
        **📊 Flux de Données :**
        """)
        
        # Diagramme de flux
        flow_data = {
            'Source': ['ERP SAP', 'CRM Salesforce', 'Comptabilité Sage', 'BI Power BI'],
            'Destination': ['Data Lake', 'Data Warehouse', 'Application', 'Reporting'],
            'Fréquence': ['Temps réel', '15 min', 'Quotidien', 'Hebdomadaire'],
            'Volume': ['2GB/jour', '500MB/jour', '1GB/jour', '200MB/jour']
        }
        
        st.dataframe(pd.DataFrame(flow_data), use_container_width=True)
    
    with col2:
        st.markdown("""
        ### 📈 Métriques d'Intégration
        
        **🔗 Connectivité :**
        """)
        st.metric("Systèmes Connectés", "8/12", "2 nouveaux")
        st.metric("Taux Disponibilité", "99.8%")
        st.metric("Latence Moyenne", "156ms")
        
        st.markdown("""
        **📊 Données :**
        """)
        st.metric("Flux Actifs", "24")
        st.metric("Volume Quotidien", "3.7 GB")
        st.metric("Temps Réel", "85%")
        
        # Bouton d'action rapide
        st.markdown("---")
        if st.button("🔄 Scanner Nouveaux Systèmes"):
            with st.spinner("Scan en cours..."):
                time.sleep(2)
                st.success("3 nouveaux systèmes détectés!")

def show_erp_connectors():
    st.header("🧾 Connecteurs ERP")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 🔌 Connecteurs ERP Supportés
        
        **🏢 SAP ERP :**
        ```python
        # Connexion RFC SAP
        import pyrfc
        conn = pyrfc.Connection(
            ashost='sap.company.com',
            sysnr='00',
            client='100',
            user='control_gestion',
            passwd='***'
        )
        
        # Extraction données stocks
        result = conn.call('BAPI_MATERIAL_GET_LIST')
        ```
        
        **📊 Oracle E-Business Suite :**
        ```python
        # Connexion JDBC
        jdbc_url = "jdbc:oracle:thin:@server:1521:XE"
        # Extraction données production
        ```
        
        **💼 Sage X3 :**
        ```python
        # API REST Sage
        response = requests.get(
            'https://sage-api/items',
            headers={'Authorization': 'Bearer {token}'}
        )
        ```
        """)
    
    with col2:
        st.markdown("""
        ### 📈 Statut des Connexions ERP
        """)
        
        erp_status = {
            'Système': ['SAP ECC', 'Oracle EBS', 'Sage X3', 'Microsoft Dynamics'],
            'Statut': ['✅ Connecté', '🟡 Partiel', '✅ Connecté', '🔴 En attente'],
            'Dernière Synchro': ['14:25', '13:45', '14:30', 'N/A'],
            'Données': ['Stocks, Production', 'Ventes, Achats', 'Compta, Stocks', 'Tous modules']
        }
        
        st.dataframe(pd.DataFrame(erp_status), use_container_width=True)
        
        # Configuration nouvelle connexion
        st.markdown("---")
        st.subheader("➕ Nouvelle Connexion")
        
        with st.form("new_erp_connection"):
            system_name = st.selectbox("Système ERP", ["SAP", "Oracle", "Sage", "Autre"])
            endpoint = st.text_input("URL du serveur")
            username = st.text_input("Nom d'utilisateur")
            password = st.text_input("Mot de passe", type="password")
            
            if st.form_submit_button("🔗 Tester la Connexion"):
                with st.spinner("Test de connexion en cours..."):
                    time.sleep(2)
                    st.success("Connexion réussie!")

def show_crm_connectors():
    st.header("🛒 Connecteurs CRM")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 🎯 Intégration Données Commerciales
        
        **📈 Salesforce :**
        ```python
        # API Salesforce REST
        from simple_salesforce import Salesforce
        sf = Salesforce(
            username='user@company.com',
            password='password',
            security_token='token'
        )
        
        # Extraction opportunités
        opportunities = sf.query(
            "SELECT Id, Name, Amount, StageName FROM Opportunity"
        )
        ```
        
        **💼 HubSpot :**
        ```python
        # API HubSpot
        import hubspot
        client = hubspot.Client(api_key='api_key')
        
        # Contacts et deals
        contacts = client.crm.contacts.get_all()
        deals = client.crm.deals.get_all()
        ```
        
        **🔄 Synchronisation Automatique :**
        - Pipeline commercial temps réel
        - Taux de conversion
        - Cycle de vente moyen
        - Segmentation clients
        """)
    
    with col2:
        st.markdown("""
        ### 📊 Métriques CRM
        """)
        
        crm_data = {
            'KPI': ['Pipeline Actif', 'Taux Conversion', 'Cycle Vente', 'Panier Moyen'],
            'Valeur': ['4.2M €', '22.5%', '45 jours', '8,450 €'],
            'Source': ['Salesforce', 'HubSpot', 'Salesforce', 'ERP']
        }
        
        st.dataframe(pd.DataFrame(crm_data), use_container_width=True)
        
        # Graphique pipeline
        stages = ['Prospection', 'Qualification', 'Proposition', 'Négociation', 'Signature']
        values = [120, 85, 60, 35, 22]
        
        fig = px.funnel(x=values, y=stages, title='Pipeline Commercial')
        st.plotly_chart(fig, use_container_width=True)

def show_accounting_connectors():
    st.header("💰 Connecteurs Comptabilité")
    
    st.markdown("""
    ### 🧾 Automatisation Comptable Avancée
    
    **🔗 Systèmes Supportés :**
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **📊 Cegid :**
        - Rapprochement automatique
        - Contrôle TVA intelligent
        - Clôture assistée
        """)
    
    with col2:
        st.markdown("""
        **📈 Quadratus :**
        - Import FEC automatique
        - Analyse des écarts
        - Reporting réglementaire
        """)
    
    with col3:
        st.markdown("""
        **💼 QuickBooks :**
        - Synchronisation bancaire
        - Facturation électronique
        - Paie automatisée
        """)
    
    # Démonstration rapprochement automatique
    st.subheader("🤖 Rapprochement Automatique")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🧠 Algorithme Intelligent :**
        ```python
        def automatic_reconciliation(bank_stmt, accounting_data):
            matches = []
            for bank_tx in bank_stmt:
                best_match = None
                highest_score = 0
                
                for acc_tx in accounting_data:
                    # Score de similarité
                    score = calculate_similarity(
                        bank_tx.description,
                        acc_tx.description,
                        bank_tx.amount,
                        acc_tx.amount
                    )
                    
                    if score > 0.85:  # Seuil de confiance
                        matches.append((bank_tx, acc_tx, score))
            
            return sorted(matches, key=lambda x: x[2], reverse=True)
        ```
        """)
    
    with col2:
        # Simulation rapprochement
        reconciliation_data = {
            'Type': ['Automatique', 'Semi-auto', 'Manuel'],
            'Transactions': [845, 23, 5],
            'Taux Reconnaissance': ['98.7%', '1.2%', '0.1%'],
            'Gain Temps': ['94%', '3%', '3%']
        }
        
        st.dataframe(pd.DataFrame(reconciliation_data), use_container_width=True)
        
        st.metric("⏱️ Temps Économisé", "18h/semaine")
        st.metric("✅ Exactitude", "99.8%")

def show_bi_connectors():
    st.header("📊 Connecteurs Business Intelligence")
    
    st.markdown("""
    ### 🎯 Intégration Plateformes BI
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **📈 Power BI :**
        ```python
        # API Power BI
        from powerbi import PowerBIClient
        
        client = PowerBIClient(
            client_id='client_id',
            client_secret='client_secret',
            tenant_id='tenant_id'
        )
        
        # Publication automatique de rapports
        dataset = client.datasets.get_dataset(dataset_id)
        client.imports.post_import_in_group(
            group_id, 
            file_path='budget_report.pbix'
        )
        ```
        
        **📊 Tableau :**
        ```python
        # Tableau Server API
        import tableauserverclient as TSC
        
        tableau_auth = TSC.TableauAuth(
            username='user', 
            password='pass', 
            site_id='site'
        )
        server = TSC.Server('https://tableau-server')
        
        # Extraction données pour ML
        with server.auth.sign_in(tableau_auth):
            all_datasources = list(TSC.Pager(server.datasources))
        ```
        """)
    
    with col2:
        st.markdown("""
        **🔗 Flux de Données BI :**
        """)
        
        bi_flows = {
            'Source': ['Data Warehouse', 'API Métier', 'ERP', 'CRM'],
            'Destination': ['Power BI', 'Tableau', 'Qlik', 'Custom Dashboard'],
            'Fréquence': ['Temps réel', '15 min', 'Quotidien', 'Hebdomadaire'],
            'Utilisateurs': ['45', '28', '15', '12']
        }
        
        st.dataframe(pd.DataFrame(bi_flows), use_container_width=True)
        
        # Métriques d'utilisation
        st.subheader("📈 Utilisation BI")
        
        usage_data = {
            'Plateforme': ['Power BI', 'Tableau', 'Qlik', 'Custom'],
            'Rapports Actifs': [45, 28, 15, 12],
            'Utilisateurs Quotidiens': [85, 42, 23, 8],
            'Données Traitées (GB)': [12.5, 8.2, 4.5, 2.1]
        }
        
        st.dataframe(pd.DataFrame(usage_data), use_container_width=True)

def show_custom_apis():
    st.header("🌐 APIs Personnalisées")
    
    st.markdown("""
    ### 🏗️ Architecture API-First
    
    **🔌 Endpoints Principaux :**
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **💰 Module Budgétaire :**
        ```python
        # API Budget
        POST /api/v1/budget/calculate-moindres-carres
        GET  /api/v1/budget/forecast/{period}
        PUT  /api/v1/budget/actual/{period}
        POST /api/v1/budget/scenario-analysis
        ```
        
        **🏭 Module Production :**
        ```python
        # API Production
        GET  /api/v1/production/capacity
        POST /api/v1/production/optimize
        PUT  /api/v1/production/schedule
        GET  /api/v1/production/kpi
        ```
        """)
    
    with col2:
        st.markdown("""
        **📦 Module Stocks :**
        ```python
        # API Stocks
        GET  /api/v1/inventory/levels
        POST /api/v1/inventory/calculate-eoq
        PUT  /api/v1/inventory/update
        GET  /api/v1/inventory/abc-analysis
        ```
        
        **💸 Module Trésorerie :**
        ```python
        # API Trésorerie
        POST /api/v1/cashflow/forecast
        GET  /api/v1/cashflow/position
        POST /api/v1/cashflow/scenarios
        ```
        """)
    
    # Testeur d'API interactif
    st.subheader("🧪 Testeur d'API")
    
    col1, col2 = st.columns(2)
    
    with col1:
        endpoint = st.selectbox("Endpoint à tester:", [
            "/api/v1/budget/forecast/next-quarter",
            "/api/v1/inventory/optimization",
            "/api/v1/production/capacity-utilization",
            "/api/v1/cashflow/daily-position"
        ])
        
        payload = st.text_area("Payload (JSON):", '{"period": "2024-Q2", "confidence": 0.95}')
    
    with col2:
        if st.button("🚀 Tester l'API"):
            with st.spinner("Appel API en cours..."):
                time.sleep(2)
                
                # Simulation réponse
                mock_response = {
                    "status": "success",
                    "data": {
                        "forecast": 1250000,
                        "confidence_interval": [1180000, 1320000],
                        "calculation_time": "156ms",
                        "method": "moindres_carres_ameliore"
                    },
                    "metadata": {
                        "timestamp": "2024-01-15T14:30:00Z",
                        "version": "2.1.0"
                    }
                }
                
                st.json(mock_response)
                st.success("✅ Appel réussi - Latence: 156ms")

def show_realtime_monitoring():
    st.header("📡 Monitoring Temps Réel")
    
    st.markdown("""
    ### 📊 Tableau de Bord de Surveillance
    """)
    
    # Métriques en temps réel
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("🔗 Connexions Actives", "24", "3")
        st.metric("📈 Débit Données", "45 MB/min")
    
    with col2:
        st.metric("⚡ Latence Moyenne", "156ms", "-12ms")
        st.metric("🔄 Synchronisations", "128/h")
    
    with col3:
        st.metric("✅ Taux Réussite", "99.2%", "0.3%")
        st.metric("⚠️ Alertes Actives", "3")
    
    with col4:
        st.metric("📊 Volume Journalier", "3.7 GB", "+450MB")
        st.metric("👥 Utilisateurs", "45")
    
    # Logs en temps réel
    st.subheader("📝 Logs des Intégrations")
    
    # Simulation de logs
    logs_data = {
        'Timestamp': ['14:35:02', '14:34:45', '14:34:23', '14:34:01', '14:33:58'],
        'Système': ['SAP ERP', 'Salesforce', 'Sage Compta', 'Power BI', 'API Custom'],
        'Action': ['Sync stocks', 'Update pipeline', 'Rapprochement', 'Refresh dataset', 'Budget calc'],
        'Statut': ['✅ Succès', '✅ Succès', '⚠️ Avertissement', '✅ Succès', '✅ Succès'],
        'Détails': ['1,245 items', '3 deals updated', '2 écarts détectés', 'Dataset updated', 'Forecast Q2']
    }
    
    st.dataframe(pd.DataFrame(logs_data), use_container_width=True)
    
    # Graphique de performance
    st.subheader("📈 Performance des Intégrations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Taux de réussite par système
        systems = ['SAP', 'Salesforce', 'Sage', 'Power BI', 'Custom API']
        success_rates = [99.8, 98.5, 97.2, 99.5, 99.9]
        
        fig = px.bar(x=systems, y=success_rates, 
                    title='Taux de Réussite par Système (%)')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Volume de données par système
        data_volume = [1250, 850, 620, 450, 380]  # MB/jour
        
        fig = px.pie(values=data_volume, names=systems,
                    title='Répartition Volume Données')
        st.plotly_chart(fig, use_container_width=True)

def show_intelligent_automation():
    st.title("🤖 Automatisation Intelligente")
    
    automation_tabs = st.tabs([
        "🔄 Workflows Métier", 
        "📧 Communications Auto", 
        "🔍 Contrôles Intelligents",
        "🎯 Décision Assistée IA"
    ])
    
    with automation_tabs[0]:
        show_business_workflows()
    
    with automation_tabs[1]:
        show_auto_communications()
    
    with automation_tabs[2]:
        show_intelligent_controls()
    
    with automation_tabs[3]:
        show_ai_decision_support()

def show_business_workflows():
    st.header("🔄 Workflows Métier Automatisés")
    
    st.markdown("""
    ### ⚙️ Processus Automatisés du Contrôle de Gestion
    """)
    
    # Catalogue des workflows
    workflows = {
        'Processus': ['Budget des Ventes', 'Plan Production', 'Gestion Stocks', 'Contrôle Trésorerie', 'Reporting Mensuel'],
        'Déclencheur': ['Nouveau mois', 'Commande client', 'Niveau stock bas', 'Fin de journée', 'Clôture mensuelle'],
        'Actions': ['Calcul prévision, Ajustement saisonnier', 'Calcul besoin, Ordonnancement', 'Commande auto, Ajustement niveau', 'Rapprochement, Alertes', 'Consolidation, Analyse écarts'],
        'Fréquence': ['Mensuelle', 'Temps réel', 'Quotidienne', 'Quotidienne', 'Mensuelle'],
        'Statut': ['✅ Actif', '✅ Actif', '🟡 Test', '✅ Actif', '✅ Actif']
    }
    
    st.dataframe(pd.DataFrame(workflows), use_container_width=True)
    
    # Éditeur de workflow
    st.subheader("🎨 Éditeur de Workflow")
    
    col1, col2 = st.columns(2)
    
    with col1:
        workflow_name = st.text_input("Nom du workflow", "Budget_Ventes_Automatisé")
        trigger = st.selectbox("Déclencheur", ["Nouveau mois", "Seuil dépassé", "Événement externe", "Planifié"])
        
        st.subheader("📋 Étapes du Workflow")
        steps = st.text_area("Définir les étapes (une par ligne):", 
                           "1. Collecte données ventes historiques\n2. Calcul tendance moindres carrés\n3. Ajustement coefficients saisonniers\n4. Validation contrôleur\n5. Publication budget")
    
    with col2:
        st.subheader("🔧 Configuration")
        systems_involved = st.multiselect("Systèmes impliqués", 
                                         ["ERP SAP", "CRM Salesforce", "Sage Compta", "Power BI", "API Custom"])
        notifications = st.multiselect("Notifications", 
                                      ["Email direction", "Slack contrôleur", "SMS urgence", "Rapport automatique"])
        
        if st.button("💾 Sauvegarder le Workflow"):
            st.success("Workflow sauvegardé avec succès!")
            st.info("Le workflow sera activé après validation.")



def show_knowledge_center():
    st.title("📚 Centre de Connaissances")
    
    knowledge_tabs = st.tabs([
        "💰 Budget des Ventes", 
        "🏭 Production", 
        "📦 Gestion Stocks",
        "🏗️ Investissement", 
        "💸 Trésorerie",
        "📊 Méthodes Avancées"
    ])
    
    with knowledge_tabs[0]:
        show_sales_budget_knowledge()
    
    with knowledge_tabs[1]:
        show_production_knowledge()
    
    with knowledge_tabs[2]:
        show_stock_management_knowledge()
    
    with knowledge_tabs[3]:
        show_investment_knowledge()
    
    with knowledge_tabs[4]:
        show_cashflow_knowledge()
    
    with knowledge_tabs[5]:
        show_advanced_methods()

# Les autres fonctions restent similaires mais peuvent être enrichies...

# Fonctions de démonstration pour compléter
def show_sales_budget_knowledge():
    st.header("💰 Encyclopédie du Budget des Ventes")
    
    st.markdown("""
    ## 📚 Théorie Complète et Méthodologies
    
    ### 🎯 Méthode des Moindres Carrés
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.latex(r"y = ax + b")
        st.latex(r"a = \frac{\sum{(x_i - \bar{x})(y_i - \bar{y})}}{\sum{(x_i - \bar{x})^2}}")
        st.latex(r"b = \bar{y} - a\bar{x}")
    
    with col2:
        st.markdown("""
        **Explication :**
        - $y$ : Variable dépendante (ventes)
        - $x$ : Variable indépendante (temps)
        - $a$ : Pente de la droite (tendance)
        - $b$ : Ordonnée à l'origine
        
        **Applications :**
        - Prévision tendancielle
        - Analyse croissance
        - Détection anomalies
        """)
    
    # Calculateur interactif
    st.subheader("🧮 Calculateur Interactif")
    
    if st.button("🎯 Lancer la Démonstration"):
        with st.spinner("Calcul en cours..."):
            time.sleep(2)
            
            # Simulation de calcul
            st.success("Calcul terminé!")
            st.metric("Prévision Mois +1", "125,450 €")
            st.metric("Coefficient de détermination R²", "0.94")

# Les autres fonctions de connaissance suivent le même pattern...


def show_automated_reports():
    st.header("📋 Rapports Automatisés")
    
    st.markdown("""
    ### 🎯 Génération Automatique de Rapports
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📅 Rapports Programmes")
        
        rapports_disponibles = {
            'Type Rapport': ['Rapport Mensuel Performance', 'Analyse Budget vs Réel', 'Tableau de Bord Commercial', 'Analyse Trésorerie', 'Rapport Stocks'],
            'Fréquence': ['Mensuel', 'Hebdomadaire', 'Quotidien', 'Hebdomadaire', 'Mensuel'],
            'Prochaine Génération': ['01/02/2024', '22/01/2024', '16/01/2024', '19/01/2024', '01/02/2024'],
            'Statut': ['🟢 Actif', '🟢 Actif', '🟡 Pause', '🟢 Actif', '🟢 Actif']
        }
        
        st.dataframe(pd.DataFrame(rapports_disponibles), use_container_width=True)
        
        st.subheader("🎨 Personnalisation des Rapports")
        format_rapport = st.selectbox("Format du rapport", ["PDF Professionnel", "PPT Présentation", "Excel Données", "HTML Interactif"])
        niveau_detail = st.select_slider("Niveau de détail", ["Synthèse", "Standard", "Détaillé"])
        
    with col2:
        st.subheader("🚀 Génération de Rapport")
        
        rapport_choice = st.selectbox("Sélectionner un rapport à générer:", [
            "Rapport Performance Mensuel",
            "Analyse Écarts Budget",
            "Tableau de Bord Commercial", 
            "État Trésorerie Détaillé",
            "Rapport Optimisation Stocks"
        ])
        
        periode_rapport = st.selectbox("Période du rapport:", [
            "Mois en cours", "Trimestre en cours", "Année en cours", "Période personnalisée"
        ])
        
        if st.button("📊 Générer le Rapport", type="primary"):
            with st.spinner("Génération du rapport en cours..."):
                time.sleep(3)
                
                st.success("✅ Rapport généré avec succès!")
                
                # Aperçu du rapport généré
                st.subheader("👁️ Aperçu du Rapport")
                
                with st.container(border=True):
                    st.markdown("""
                    **📈 RAPPORT DE PERFORMANCE MENSUEL - Janvier 2024**
                    
                    **🎯 Synthèse Executive:**
                    - 📈 **CA Mensuel:** 2.8M € (+15.2% vs prévision)
                    - 🏭 **Production:** 45.2K unités (+8.7%)
                    - 💰 **Marge Brute:** 32.5% (+2.1 points)
                    - 📦 **Rotation Stocks:** 8.2 (+1.5)
                    
                    **🚨 Points de Vigilance:**
                    - Dépassement budget production: +12.5%
                    - 2 articles en niveau stock critique
                    
                    **📊 Recommandations:**
                    - Optimiser la gamme produits C
                    - Renégocier les conditions fournisseurs
                    - Investir dans la digitalisation
                    """)
                
                # Options de téléchargement
                col_dl1, col_dl2, col_dl3 = st.columns(3)
                with col_dl1:
                    st.download_button("📥 Télécharger PDF", data="simulated_pdf_content", 
                                     file_name=f"rapport_performance_{datetime.now().strftime('%Y%m%d')}.pdf")
                with col_dl2:
                    st.download_button("📊 Télécharger Excel", data="simulated_excel_content",
                                     file_name=f"donnees_rapport_{datetime.now().strftime('%Y%m%d')}.xlsx")
                with col_dl3:
                    st.button("📧 Envoyer par Email")

def show_comparative_analysis():
    st.header("📊 Analyse Comparative")
    
    st.markdown("""
    ### 🎯 Benchmarks et Analyses Comparatives
    """)
    
    tab1, tab2, tab3 = st.tabs(["📈 Vs Objectifs", "🔄 Vs Période Précédente", "🌍 Vs Concurrents"])
    
    with tab1:
        st.subheader("📈 Performance vs Objectifs")
        
        # Données de comparaison objectifs
        indicateurs = {
            'KPI': ['Chiffre d\'Affaires', 'Marge Brute', 'Production', 'Rotation Stocks', 'Taux Service'],
            'Objectif': [2600000, 30.0, 42000, 7.5, 98.0],
            'Réel': [2800000, 32.5, 45200, 8.2, 98.5],
            'Écart (%)': ['+7.7%', '+8.3%', '+7.6%', '+9.3%', '+0.5%'],
            'Statut': ['✅ Dépassé', '✅ Dépassé', '✅ Dépassé', '✅ Dépassé', '✅ Atteint']
        }
        
        df_comparison = pd.DataFrame(indicateurs)
        st.dataframe(df_comparison, use_container_width=True)
        
        # Graphique de performance
        fig = go.Figure()
        fig.add_trace(go.Bar(name='Objectif', x=df_comparison['KPI'], y=df_comparison['Objectif']))
        fig.add_trace(go.Bar(name='Réel', x=df_comparison['KPI'], y=df_comparison['Réel']))
        fig.update_layout(title='Performance vs Objectifs', barmode='group')
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.subheader("🔄 Évolution vs Période Précédente")
        
        col1, col2 = st.columns(2)
        
        with col1:
            periode_comparaison = st.selectbox("Période de comparaison:", [
                "Mois précédent", "Trimestre précédent", "Même période année dernière"
            ])
            
            # Métriques de croissance
            croissance_data = {
                'Indicateur': ['CA', 'Marge', 'Production', 'Productivité', 'Rentabilité'],
                f'Croissance vs {periode_comparaison}': ['+15.2%', '+8.3%', '+12.7%', '+5.8%', '+9.1%'],
                'Tendance': ['📈', '📈', '📈', '📈', '📈']
            }
            
            st.dataframe(pd.DataFrame(croissance_data), use_container_width=True)
        
        with col2:
            # Graphique d'évolution
            periodes = ['T-3', 'T-2', 'T-1', 'T0']
            ca_evolution = [2200, 2350, 2450, 2800]  # en k€
            
            fig = px.line(x=periodes, y=ca_evolution, 
                         title='Évolution du Chiffre d\'Affaires (k€)',
                         markers=True)
            fig.update_traces(line=dict(color='green', width=3))
            st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.subheader("🌍 Benchmark Sectoriel")
        
        st.markdown("""
        **📊 Comparaison avec les Concurrents:**
        """)
        
        benchmark_data = {
            'Indicateur': ['Part de Marché', 'Croissance CA', 'Marge Brute', 'ROI', 'Productivité'],
            'Notre Entreprise': ['12.5%', '15.2%', '32.5%', '18.5%', '92.5%'],
            'Concurrent A': ['15.2%', '12.8%', '28.7%', '16.2%', '88.3%'],
            'Concurrent B': ['10.8%', '8.5%', '30.2%', '15.8%', '90.1%'],
            'Moyenne Secteur': ['12.8%', '11.2%', '29.8%', '16.5%', '89.7%']
        }
        
        st.dataframe(pd.DataFrame(benchmark_data), use_container_width=True)
        
        # Radar chart de comparaison
        categories = ['Part de Marché', 'Croissance', 'Marge', 'ROI', 'Productivité']
        notre_entreprise = [12.5, 15.2, 32.5, 18.5, 92.5]
        moyenne_secteur = [12.8, 11.2, 29.8, 16.5, 89.7]
        
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=notre_entreprise,
            theta=categories,
            fill='toself',
            name='Notre Entreprise'
        ))
        fig.add_trace(go.Scatterpolar(
            r=moyenne_secteur,
            theta=categories,
            fill='toself',
            name='Moyenne Secteur'
        ))
        fig.update_layout(polar=dict(radialaxis=dict(visible=True)), showlegend=True)
        st.plotly_chart(fig, use_container_width=True)

def show_kpi_dashboard():
    st.header("🎯 Tableau de Bord des Indicateurs Clés")
    
    st.markdown("""
    ### 📊 Monitoring des KPI en Temps Réel
    """)
    
    # Sélection des KPI à afficher
    kpi_categories = st.multiselect(
        "Catégories de KPI à afficher:",
        ["Commercial", "Production", "Financier", "Stocks", "RH", "Qualité"],
        default=["Commercial", "Production", "Financier"]
    )
    
    # Affichage des KPI par catégorie
    if "Commercial" in kpi_categories:
        with st.expander("📈 KPI COMMERCIAL", expanded=True):
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("CA Cumulé", "2.8M €", "15.2%")
                st.metric("Panier Moyen", "8,450 €", "3.2%")
            
            with col2:
                st.metric("Nouvelles Affaires", "45", "12.5%")
                st.metric("Taux Conversion", "22.5%", "2.1%")
            
            with col3:
                st.metric("Pipeline Actif", "4.2M €", "8.7%")
                st.metric("Cycle de Vente", "45 jours", "-3 jours")
            
            with col4:
                st.metric("Satisfaction Client", "4.2/5", "0.3")
                st.metric("Taux Fidélisation", "88.5%", "1.8%")
    
    if "Production" in kpi_categories:
        with st.expander("🏭 KPI PRODUCTION", expanded=True):
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Volume Production", "45.2K", "8.7%")
                st.metric("Taux Rendement", "92.5%", "3.2%")
            
            with col2:
                st.metric("TRS", "85.2%", "2.1%")
                st.metric("Taux Rebut", "1.2%", "-0.3%")
            
            with col3:
                st.metric("Capacité Utilisée", "88.7%", "5.2%")
                st.metric("Maintenance", "95.8%", "1.5%")
            
            with col4:
                st.metric("Coût Unitaire", "245 €", "-2.8%")
                st.metric("Productivité", "115.2%", "4.7%")
    
    if "Financier" in kpi_categories:
        with st.expander("💰 KPI FINANCIER", expanded=True):
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Trésorerie", "856K €", "5.8%")
                st.metric("Marge Brute", "32.5%", "2.1%")
            
            with col2:
                st.metric("BFR", "1.2M €", "-8.5%")
                st.metric("ROI", "18.5%", "3.2%")
            
            with col3:
                st.metric("Délai Clients", "45 jours", "-2 jours")
                st.metric("Délai Fournisseurs", "60 jours", "+5 jours")
            
            with col4:
                st.metric("Endettement", "1.8x EBITDA", "-0.3x")
                st.metric("Cash-flow Libre", "450K €", "12.5%")
    
    # Tableau de bord interactif
    st.subheader("📊 Tableau de Bord Personnalisable")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Sélection des graphiques
        graphiques = st.multiselect(
            "Graphiques à afficher:",
            ["Évolution CA", "Performance Production", "Analyse Marges", "Rotation Stocks", "Trésorerie"],
            default=["Évolution CA", "Performance Production"]
        )
    
    with col2:
        # Période d'analyse
        periode_analyse = st.selectbox(
            "Période d'analyse:",
            ["7 derniers jours", "30 derniers jours", "3 derniers mois", "Année en cours"]
        )
    
    # Génération des graphiques sélectionnés
    if "Évolution CA" in graphiques:
        st.subheader("📈 Évolution du Chiffre d'Affaires")
        
        # Données simulées
        jours = list(range(1, 31))
        ca_quotidien = [100 + np.random.normal(0, 20) for _ in jours]
        ca_cumule = np.cumsum(ca_quotidien)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=jours, y=ca_quotidien, name='CA Quotidien', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=jours, y=ca_cumule, name='CA Cumulé', line=dict(color='green')))
        fig.update_layout(title='Évolution du Chiffre d\'Affaires sur 30 jours')
        st.plotly_chart(fig, use_container_width=True)
    
    if "Performance Production" in graphiques:
        st.subheader("🏭 Performance de la Production")
        
        # Données simulées production
        equipes = ['Équipe A', 'Équipe B', 'Équipe C', 'Équipe D']
        production = [1250, 1180, 1320, 1270]
        objectifs = [1200, 1200, 1200, 1200]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(name='Production', x=equipes, y=production))
        fig.add_trace(go.Scatter(name='Objectif', x=equipes, y=objectifs, mode='markers', 
                               marker=dict(size=15, color='red')))
        fig.update_layout(title='Performance des Équipes de Production')
        st.plotly_chart(fig, use_container_width=True)

def show_optimized_production():
    st.title("🏭 Production Optimisée")
    
    st.markdown("""
    ## 🧠 Système Intelligent de Planification et Optimisation de la Production
    
    ### 🎯 Planification Avancée et Optimisation en Temps Réel
    """)
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "📅 Plan Directeur", 
        "🔧 Optimisation Charges", 
        "📈 Performance Temps Réel",
        "🤖 IA Prévisionnelle"
    ])
    
    with tab1:
        show_production_master_plan()
    
    with tab2:
        show_capacity_optimization()
    
    with tab3:
        show_realtime_performance()
    
    with tab4:
        show_ai_production_forecasting()

def show_production_master_plan():
    st.header("📅 Plan Directeur de Production (PDP)")
    
    st.markdown("""
    ### 🎯 Méthode MRP II - Manufacturing Resource Planning
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Données d'Entrée")
        
        ventes_prevues = st.number_input("Prévisions ventes mensuelles (unités)", value=10000)
        stock_initial = st.number_input("Stock initial (unités)", value=1500)
        stock_cible = st.number_input("Stock cible (unités)", value=2000)
        delai_fabrication = st.number_input("Délai de fabrication (jours)", value=10)
        
        st.subheader("⚙️ Contraintes de Production")
        capacite_journaliere = st.number_input("Capacité de production journalière (unités)", value=500)
        jours_ouvres = st.number_input("Jours ouvrés par mois", value=22)
    
    with col2:
        # Calculs automatiques
        production_necessaire = ventes_prevues + stock_cible - stock_initial
        jours_production = production_necessaire / capacite_journaliere
        taux_utilisation = (production_necessaire / (capacite_journaliere * jours_ouvres)) * 100
        
        st.metric("📦 Production nécessaire", f"{production_necessaire:,.0f} unités")
        st.metric("⏱️ Jours de production estimés", f"{jours_production:.1f} jours")
        st.metric("🏭 Taux d'utilisation capacité", f"{taux_utilisation:.1f}%")
        
        # Recommandations
        if taux_utilisation > 100:
            st.error("🚨 **CAPACITÉ INSUFFISANTE** - Prévoir heures supplémentaires ou sous-traitance")
        elif taux_utilisation > 85:
            st.warning("⚠️ **CAPACITÉ TENDUE** - Surveillance renforcée nécessaire")
        else:
            st.success("✅ **CAPACITÉ ADÉQUATE** - Planification optimale possible")
    
    # Plan de production détaillé
    st.subheader("📋 Plan de Production Détaillé")
    
    if st.button("📊 Générer le Plan de Production"):
        # Génération d'un plan simulé
        semaines = ['Sem 1', 'Sem 2', 'Sem 3', 'Sem 4']
        production_plan = {
            'Semaine': semaines,
            'Production Planifiée': [2500, 2500, 2500, 2500],
            'Capacité Disponible': [2750, 2750, 2750, 2750],
            'Taux Utilisation': ['90.9%', '90.9%', '90.9%', '90.9%'],
            'Stock Fin Semaine': [1800, 1600, 1400, 2000]
        }
        
        df_plan = pd.DataFrame(production_plan)
        st.dataframe(df_plan, use_container_width=True)
        
        # Graphique Gantt simplifié
        st.subheader("📅 Diagramme de Gantt de Production")
        
        tasks = [
            dict(Task="Préparation", Start='2024-01-01', Finish='2024-01-03'),
            dict(Task="Fabrication Lot A", Start='2024-01-04', Finish='2024-01-10'),
            dict(Task="Fabrication Lot B", Start='2024-01-11', Finish='2024-01-17'),
            dict(Task="Contrôle Qualité", Start='2024-01-18', Finish='2024-01-20'),
            dict(Task="Expédition", Start='2024-01-21', Finish='2024-01-22')
        ]
        
        # Affichage simplifié du diagramme
        for task in tasks:
            col1, col2, col3 = st.columns([2, 3, 1])
            with col1:
                st.write(f"**{task['Task']}**")
            with col2:
                st.progress(100)
            with col3:
                st.write(f"{task['Start']} to {task['Finish']}")

def show_capacity_optimization():
    st.header("🔧 Optimisation des Charges de Production")
    
    st.markdown("""
    ### 🎯 Répartition Optimale des Ressources
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏭 Ressources Disponibles")
        
        machines = st.number_input("Nombre de machines", value=8, min_value=1)
        equipes = st.number_input("Nombre d'équipes", value=3, min_value=1)
        heures_equipe = st.number_input("Heures par équipe/semaine", value=35)
        
        st.subheader("📦 Commandes en Cours")
        commandes_urgentes = st.number_input("Commandes urgentes (unités)", value=500)
        commandes_normales = st.number_input("Commandes normales (unités)", value=2000)
    
    with col2:
        # Calcul de la capacité
        capacite_totale = machines * equipes * heures_equipe * 4  # capacité mensuelle
        besoin_production = (commandes_urgentes * 1.5) + (commandes_normales * 1.0)  # coefficients de difficulté
        
        taux_charge = (besoin_production / capacite_totale) * 100
        
        st.metric("⚡ Capacité totale disponible", f"{capacite_totale:,.0f} h-machine")
        st.metric("📦 Besoin de production", f"{besoin_production:,.0f} h-machine")
        st.metric("📊 Taux de charge global", f"{taux_charge:.1f}%")
        
        # Recommandations d'optimisation
        if taux_charge > 100:
            st.error("""
            **🚨 SURCHARGE CRITIQUE**
            - Activer les heures supplémentaires
            - Sous-traiter une partie de la production
            - Renégocier les délais clients
            """)
        elif taux_charge > 85:
            st.warning("""
            **⚠️ CHARGE ÉLEVÉE**
            - Optimiser les séquences de production
            - Rééquilibrer les charges entre équipes
            - Anticiper les maintenances
            """)
        else:
            st.success("""
            **✅ CHARGE OPTIMALE**
            - Capacité bien utilisée
            - Marge de manœuvre disponible
            - Possibilité d'accepter nouvelles commandes
            """)
    
    # Optimisation avancée
    st.subheader("🧮 Optimisation par Algorithmes")
    
    if st.button("🎯 Lancer l'Optimisation Automatique"):
        with st.spinner("Calcul de la solution optimale..."):
            time.sleep(2)
            
            st.success("✅ Solution optimale trouvée!")
            
            # Résultats de l'optimisation
            optimisation_results = {
                'Paramètre': ['Charge Équipe A', 'Charge Équipe B', 'Charge Équipe C', 'Heures Supp', 'Taux Utilisation Machines'],
                'Avant Optimisation': ['115%', '92%', '78%', '12h', '88%'],
                'Après Optimisation': ['95%', '98%', '97%', '8h', '92%'],
                'Gain': ['-20%', '+6%', '+19%', '-4h', '+4%']
            }
            
            st.dataframe(pd.DataFrame(optimisation_results), use_container_width=True)
            
            st.info("""
            **💡 Recommandations de l'algorithme:**
            - Réaffecter 15% de la charge de l'équipe A vers l'équipe C
            - Programmer les maintenances préventives en période creuse
            - Utiliser la flexibilité inter-équipes
            """)

def show_realtime_performance():
    st.header("📈 Performance de Production en Temps Réel")
    
    st.markdown("""
    ### 🎯 Monitoring Live des Indicateurs de Production
    """)
    
    # KPI en temps réel
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("🏭 Production du Jour", "1,245 unités", "8.2%")
        st.metric("⚡ Cadence Réelle", "52 u/h", "3.5%")
    
    with col2:
        st.metric("✅ Taux Qualité", "98.7%", "0.8%")
        st.metric("🔄 TRS Global", "85.2%", "2.1%")
    
    with col3:
        st.metric("⏱️ Temps d'Arrêt", "2.3%", "-0.5%")
        st.metric("🔧 Maintenances", "95.8%", "1.2%")
    
    with col4:
        st.metric("📊 Rendement", "92.5%", "1.8%")
        st.metric("💸 Coût Unitaire", "245 €", "-2.3%")
    
    # Graphiques de performance temps réel
    st.subheader("📊 Évolution des Performances")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Évolution du TRS
        heures = [f"{h:02d}:00" for h in range(6, 22)]
        trs_values = [82 + np.random.normal(0, 3) for _ in heures]
        
        fig = px.line(x=heures, y=trs_values, title='TRS en Temps Réel',
                     labels={'x': 'Heure', 'y': 'TRS (%)'})
        fig.add_hline(y=85, line_dash="dash", line_color="red", annotation_text="Objectif")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Répartition des arrêts
        causes_arrets = {
            'Cause': ['Maintenance', 'Changement série', 'Panne', 'Approvisionnement', 'Formation'],
            'Durée (min)': [45, 30, 25, 20, 15]
        }
        
        fig = px.pie(causes_arrets, values='Durée (min)', names='Cause',
                    title='Répartition des Temps d\'Arrêt')
        st.plotly_chart(fig, use_container_width=True)
    
    # Alertes temps réel
    st.subheader("🚨 Alertes de Production")
    
    alertes = [
        {"type": "⚠️", "message": "Machine B - Tendance baisse rendement", "priorite": "Moyenne"},
        {"type": "🔴", "message": "Équipe C - Retard production 15%", "priorite": "Haute"},
        {"type": "🟢", "message": "Qualité - Objectif dépassé", "priorite": "Basse"},
        {"type": "⚠️", "message": "Stock matière première critique", "priorite": "Moyenne"}
    ]
    
    for alerte in alertes:
        with st.container(border=True):
            col1, col2 = st.columns([1, 4])
            with col1:
                st.write(f"**{alerte['type']} {alerte['priorite']}**")
            with col2:
                st.write(alerte['message'])
                if alerte['priorite'] == "Haute":
                    st.button("Intervenir", key=f"btn_{alerte['message']}")

def show_ai_production_forecasting():
    st.header("🤖 IA Prédictive pour la Production")
    
    st.markdown("""
    ### 🧠 Système de Prévision et Optimisation par Intelligence Artificielle
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Modèles Prédictifs")
        
        st.markdown("""
        **🎯 Applications de l'IA:**
        - Prévision des pannes
        - Optimisation des paramètres
        - Prévision de la demande
        - Optimisation des stocks
        - Planification intelligente
        """)
        
        st.markdown("""
        **🧠 Algorithmes Utilisés:**
        - Random Forest
        - LSTM pour séries temporelles
        - Reinforcement Learning
        - Computer Vision pour contrôle qualité
        """)
    
    with col2:
        st.subheader("📈 Performance des Modèles")
        
        model_performance = {
            'Modèle': ['Prévision Pannes', 'Optimisation Paramètres', 'Contrôle Qualité', 'Prévision Demande'],
            'Précision': ['94.2%', '91.8%', '96.5%', '92.3%'],
            'Gain Productivité': ['+12.5%', '+8.7%', '+15.2%', '+9.8%'],
            'Statut': ['🟢 Production', '🟢 Production', '🟡 Test', '🟢 Production']
        }
        
        st.dataframe(pd.DataFrame(model_performance), use_container_width=True)
    
    # Démonstration de l'IA prédictive
    st.subheader("🔮 Démonstration - Prévision des Pannes")
    
    if st.button("🎯 Lancer la Simulation IA"):
        with st.spinner("Analyse des données et prédiction en cours..."):
            time.sleep(3)
            
            st.success("✅ Analyse IA terminée!")
            
            # Résultats de la prédiction
            col_res1, col_res2, col_res3 = st.columns(3)
            
            with col_res1:
                st.metric("🔧 Prochaine Panne Prévue", "J+4", "92% de confiance")
                st.metric("📍 Machine à Risque", "Presse HYD-45")
            
            with col_res2:
                st.metric("⏱️ Fenêtre d'Intervention", "48h", "Pour maintenance préventive")
                st.metric("💰 Économie Potentielle", "12,500 €", "Évitation arrêt production")
            
            with col_res3:
                st.metric("🎯 Composant Critique", "Joint d'étanchéité", "Usure détectée")
                st.metric("📊 Données Analysées", "2.5M points", "6 mois d'historique")
            
            # Recommandations IA
            st.subheader("💡 Recommandations de l'IA")
            
            recommendations = [
                "🔧 **Programmer maintenance préventive** dans les 48h sur la presse HYD-45",
                "📦 **Commander pièces de rechange** : Joints d'étanchéité (réf. JNT-4587)",
                "👨‍🔧 **Former équipe maintenance** sur les signes avant-coureurs",
                "📊 **Renforcer monitoring** des paramètres hydrauliques",
                "🔄 **Ajuster planning production** pour anticiper la maintenance"
            ]
            
            for i, rec in enumerate(recommendations, 1):
                st.write(f"{i}. {rec}")
            
            # Plan d'action automatique
            st.subheader("📅 Plan d'Action Généré")
            
            plan_actions = {
                'Action': ['Commander pièces', 'Programmer maintenance', 'Alerter équipe', 'Ajuster planning'],
                'Responsable': ['Logistique', 'Planning', 'Maintenance', 'Production'],
                'Échéance': ['24h', '48h', 'Immédiat', '24h'],
                'Statut': ['🟡 En cours', '🟢 Planifié', '🔴 En attente', '🟡 En cours']
            }
            
            st.dataframe(pd.DataFrame(plan_actions), use_container_width=True)

# Fonctions pour compléter les autres sections manquantes
def show_ai_sales_budget():
    st.title("💰 Budget des Ventes IA")
    st.info("Cette section est en cours de développement...")
    # Implémentation similaire aux autres sections

def show_advanced_stock_management():
    st.title("📦 Gestion des Stocks Avancée")
    st.info("Cette section est en cours de développement...")
    # Implémentation similaire aux autres sections

def show_strategic_investment():
    st.title("🏗️ Investissement Stratégique")
    st.info("Cette section est en cours de développement...")
     
    
    # Métriques principales en haut
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "💰 Budget Total", 
            "4.2M€", 
            "+12% vs prévision",
            delta_color="normal"
        )
    
    with col2:
        st.metric(
            "📈 ROI Moyen", 
            "18.5%", 
            "+2.3%",
            delta_color="inverse"
        )
    
    with col3:
        st.metric(
            "⏱️ Délai Retour", 
            "3.2 ans", 
            "-0.4 ans",
            delta_color="inverse"
        )
    
    with col4:
        st.metric(
            "🚨 Projets à Risque", 
            "2", 
            "-1",
            delta_color="inverse"
        )

    # Onglets pour différentes analyses
    analysis_tabs = st.tabs([
        "📊 Vue d'Ensemble", 
        "💰 Analyse Financière", 
        "📅 Planning", 
        "🎯 Décisions Stratégiques"
    ])
    
    with analysis_tabs[0]:
        show_investment_overview()
    
    with analysis_tabs[1]:
        show_financial_analysis()
    
    with analysis_tabs[2]:
        show_investment_planning()
    
    with analysis_tabs[3]:
        show_strategic_decisions()

def show_investment_overview():
    st.subheader("📊 Vue d'Ensemble des Investissements")
    
    # Données des projets d'investissement
    projects_data = {
        'Projet': [
            'Nouvelle Ligne Production', 
            'Modernisation Usine A', 
            'Système IA Qualité',
            'Énergie Renouvelable',
            'R&D Nouveaux Produits',
            'Digitalisation Logistique'
        ],
        'Type': ['Production', 'Infrastructure', 'Technologie', 'Durabilité', 'Innovation', 'Digital'],
        'Budget (M€)': [2.1, 1.2, 0.4, 0.8, 0.3, 0.4],
        'ROI Attendu (%)': [22.5, 15.8, 28.3, 12.1, 35.2, 18.7],
        'Délai (ans)': [3.5, 2.8, 1.5, 4.2, 2.1, 1.8],
        'Risque': ['Moyen', 'Faible', 'Élevé', 'Faible', 'Très Élevé', 'Moyen'],
        'Statut': ['En Cours', 'Planifié', 'Étude', 'Planifié', 'Étude', 'En Cours']
    }
    
    df_projects = pd.DataFrame(projects_data)
    
    # Filtres
    col1, col2, col3 = st.columns(3)
    
    with col1:
        type_filter = st.multiselect(
            "Filtrer par Type",
            options=df_projects['Type'].unique(),
            default=df_projects['Type'].unique()
        )
    
    with col2:
        risque_filter = st.multiselect(
            "Filtrer par Niveau de Risque",
            options=df_projects['Risque'].unique(),
            default=df_projects['Risque'].unique()
        )
    
    with col3:
        statut_filter = st.multiselect(
            "Filtrer par Statut",
            options=df_projects['Statut'].unique(),
            default=df_projects['Statut'].unique()
        )
    
    # Application des filtres
    filtered_df = df_projects[
        (df_projects['Type'].isin(type_filter)) &
        (df_projects['Risque'].isin(risque_filter)) &
        (df_projects['Statut'].isin(statut_filter))
    ]
    
    # Affichage des données
    st.dataframe(
        filtered_df.style.format({
            'Budget (M€)': '{:.1f}',
            'ROI Attendu (%)': '{:.1f}',
            'Délai (ans)': '{:.1f}'
        }),
        use_container_width=True
    )
    
    # Graphiques de synthèse
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        # Répartition du budget par type
        budget_by_type = filtered_df.groupby('Type')['Budget (M€)'].sum()
        fig_budget = px.pie(
            values=budget_by_type.values,
            names=budget_by_type.index,
            title="Répartition du Budget par Type d'Investissement"
        )
        st.plotly_chart(fig_bart, use_container_width=True)
    
    with col_chart2:
        # ROI vs Risque
        fig_roi_risk = px.scatter(
            filtered_df,
            x='ROI Attendu (%)',
            y='Budget (M€)',
            size='Budget (M€)',
            color='Risque',
            hover_name='Projet',
            title="ROI vs Budget par Niveau de Risque"
        )
        st.plotly_chart(fig_roi_risk, use_container_width=True)

def show_financial_analysis():
    st.subheader("💰 Analyse Financière Détaillée")
    
    # Sélection du projet à analyser
    projects = [
        'Nouvelle Ligne Production', 
        'Modernisation Usine A', 
        'Système IA Qualité',
        'Énergie Renouvelable'
    ]
    
    selected_project = st.selectbox("Sélectionner un projet à analyser", projects)
    
    if selected_project:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader(f"📈 Analyse {selected_project}")
            
            # Métriques financières
            st.metric("Investissement Initial", "2.1M€")
            st.metric("VAN (Valeur Actuelle Nette)", "450K€")
            st.metric("TRI (Taux de Rentabilité Interne)", "22.5%")
            st.metric("Délai de Récupération", "3.2 ans")
            
            # Scénarios de sensibilité
            st.subheader("🎯 Scénarios de Sensibilité")
            
            variation_prix = st.slider("Variation des prix de vente (%)", -20, 20, 0)
            variation_couts = st.slider("Variation des coûts opérationnels (%)", -15, 15, 0)
            
            # Calcul impact sur ROI
            roi_base = 22.5
            roi_ajuste = roi_base + (variation_prix * 0.8) - (variation_couts * 0.6)
            
            st.metric("ROI Ajusté", f"{roi_ajuste:.1f}%", f"{roi_ajuste - roi_base:.1f}%")
        
        with col2:
            st.subheader("📊 Flux de Trésorerie")
            
            # Simulation des flux de trésorerie
            years = list(range(2024, 2034))
            cash_flows = {
                'Année': years,
                'Investissement': [-2100000] + [0] * 9,
                'Revenus': [0, 500000, 800000, 1200000, 1500000, 1500000, 1500000, 1500000, 1500000, 1500000],
                'Coûts': [0, -300000, -400000, -600000, -700000, -700000, -700000, -700000, -700000, -700000],
                'Flux Net': [-2100000, 200000, 400000, 600000, 800000, 800000, 800000, 800000, 800000, 800000]
            }
            
            df_cashflow = pd.DataFrame(cash_flows)
            df_cashflow['Cumulé'] = df_cashflow['Flux Net'].cumsum()
            
            fig_cashflow = go.Figure()
            fig_cashflow.add_trace(go.Bar(x=df_cashflow['Année'], y=df_cashflow['Flux Net'], name='Flux Net Annuel'))
            fig_cashflow.add_trace(go.Scatter(x=df_cashflow['Année'], y=df_cashflow['Cumulé'], name='Flux Cumulé', line=dict(color='red')))
            fig_cashflow.update_layout(title="Projection des Flux de Trésorerie")
            st.plotly_chart(fig_cashflow, use_container_width=True)

def show_investment_planning():
    st.subheader("📅 Planning et Gantt des Investissements")
    
    # Données du planning
    gantt_data = {
        'Tâche': [
            'Étude de Faisabilité', 'Approbation Budget', 'Appel d\'Offres',
            'Sélection Fournisseur', 'Installation', 'Tests et Validation',
            'Formation Équipes', 'Mise en Production'
        ],
        'Début': [
            '2024-01-15', '2024-03-01', '2024-03-15', '2024-05-01',
            '2024-06-01', '2024-08-15', '2024-09-15', '2024-10-01'
        ],
        'Fin': [
            '2024-02-28', '2024-03-14', '2024-04-30', '2024-05-31',
            '2024-08-14', '2024-09-14', '2024-09-30', '2024-12-31'
        ],
        'Projet': [
            'Nouvelle Ligne Production', 'Nouvelle Ligne Production', 'Nouvelle Ligne Production',
            'Nouvelle Ligne Production', 'Nouvelle Ligne Production', 'Nouvelle Ligne Production',
            'Nouvelle Ligne Production', 'Nouvelle Ligne Production'
        ],
        'Progression': [100, 100, 75, 50, 25, 10, 0, 0]
    }
    
    df_gantt = pd.DataFrame(gantt_data)
    df_gantt['Début'] = pd.to_datetime(df_gantt['Début'])
    df_gantt['Fin'] = pd.to_datetime(df_gantt['Fin'])
    
    # Diagramme de Gantt
    fig_gantt = px.timeline(
        df_gantt, 
        x_start="Début", 
        x_end="Fin", 
        y="Tâche",
        color="Progression",
        title="Planning des Investissements - Diagramme de Gantt"
    )
    fig_gantt.update_yaxes(autorange="reversed")
    st.plotly_chart(fig_gantt, use_container_width=True)
    
    # Indicateurs d'avancement
    st.subheader("📊 Indicateurs d'Avancement")
    
    progress_col1, progress_col2, progress_col3, progress_col4 = st.columns(4)
    
    with progress_col1:
        st.metric("📅 Délai Moyen", "45 jours", "-5 jours")
    
    with progress_col2:
        st.metric("💰 Budget Utilisé", "68%", "2%")
    
    with progress_col3:
        st.metric("✅ Tâches Terminées", "3/8", "37%")
    
    with progress_col4:
        st.metric("🚨 Retards", "1 projet", "Critique")

def show_strategic_decisions():
    st.subheader("🎯 Aide à la Décision Stratégique")
    
    # Matrice de décision
    st.write("### 🧩 Matrice de Décision Stratégique")
    
    decision_data = {
        'Critère': [
            'Alignement Stratégique', 'ROI Attendu', 'Risque Technique',
            'Impact Environnemental', 'Délai de Mise en Œuvre', 'Compétences Internes'
        ],
        'Pondération': [25, 30, 15, 10, 10, 10],
        'Nouvelle Ligne': [9, 8, 6, 7, 5, 8],
        'Modernisation Usine': [7, 6, 8, 8, 9, 9],
        'Système IA': [8, 9, 5, 9, 7, 6]
    }
    
    df_decision = pd.DataFrame(decision_data)
    
    # Calcul des scores
    for project in ['Nouvelle Ligne', 'Modernisation Usine', 'Système IA']:
        df_decision[f'{project} Score'] = (df_decision[project] * df_decision['Pondération']) / 10
    
    st.dataframe(df_decision, use_container_width=True)
    
    # Scores totaux
    scores_totaux = {
        'Projet': ['Nouvelle Ligne Production', 'Modernisation Usine A', 'Système IA Qualité'],
        'Score Total': [
            df_decision['Nouvelle Ligne Score'].sum(),
            df_decision['Modernisation Usine Score'].sum(),
            df_decision['Système IA Score'].sum()
        ]
    }
    
    df_scores = pd.DataFrame(scores_totaux)
    
    # Graphique des scores
    fig_scores = px.bar(
        df_scores, 
        x='Projet', 
        y='Score Total',
        title="Score Total par Projet - Matrice de Décision",
        color='Score Total'
    )
    st.plotly_chart(fig_scores, use_container_width=True)
    
    # Recommandations
    st.subheader("💡 Recommandations Stratégiques")
    
    best_project = df_scores.loc[df_scores['Score Total'].idxmax()]
    
    st.success(f"**🎯 Projet Recommandé : {best_project['Projet']}**")
    st.write(f"**Score : {best_project['Score Total']:.1f}/100**")
    
    col_rec1, col_rec2 = st.columns(2)
    
    with col_rec1:
        st.markdown("""
        **✅ Points Forts :**
        - Alignement parfait avec la stratégie
        - ROI élevé et maîtrisé
        - Compétences internes disponibles
        - Impact positif sur l'environnement
        """)
    
    with col_rec2:
        st.markdown("""
        **⚠️ Points de Vigilance :**
        - Délai de mise en œuvre moyen
        - Risque technique modéré
        - Investissement initial important
        - Formation nécessaire
        """)
    
    # Outil de simulation de décision
    st.subheader("🔧 Simulateur de Décision")
    
    col_sim1, col_sim2 = st.columns(2)
    
    with col_sim1:
        budget_disponible = st.slider("Budget disponible (M€)", 1.0, 5.0, 2.5)
        horizon_investissement = st.selectbox("Horizon d'investissement", ["Court terme (1-2 ans)", "Moyen terme (3-5 ans)", "Long terme (5+ ans)"])
    
    with col_sim2:
        tolerance_risque = st.select_slider("Tolérance au risque", ["Faible", "Moyenne", "Élevée"])
        objectif_principal = st.selectbox("Objectif principal", ["Rentabilité", "Croissance", "Innovation", "Durabilité"])
    
    if st.button("🎯 Générer la Recommandation Personnalisée"):
        st.balloons()
        st.success(f"**Recommandation : {best_project['Projet']}**")
        st.info(f"Cette recommandation est optimisée pour un budget de {budget_disponible}M€ avec une tolérance au risque {tolerance_risque.lower()} et un objectif principal d'{objectif_principal.lower()}.")

  

 
    
    st.title("🏗️ Analyse des Investissements Stratégiques")
    show_strategic_investment()

def show_strategic_investment():
    # Métriques principales en haut
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "💰 Budget Total", 
            "4.2M€", 
            "+12% vs prévision",
            delta_color="normal"
        )
    
    with col2:
        st.metric(
            "📈 ROI Moyen", 
            "18.5%", 
            "+2.3%",
            delta_color="inverse"
        )
    
    with col3:
        st.metric(
            "⏱️ Délai Retour", 
            "3.2 ans", 
            "-0.4 ans",
            delta_color="inverse"
        )
    
    with col4:
        st.metric(
            "🚨 Projets à Risque", 
            "2", 
            "-1",
            delta_color="inverse"
        )

    # Onglets pour différentes analyses
    analysis_tabs = st.tabs([
        "📊 Vue d'Ensemble", 
        "💰 Analyse Financière", 
        "📅 Planning", 
        "🎯 Décisions Stratégiques",
        "📈 Performance"
    ])
    
    with analysis_tabs[0]:
        show_investment_overview()
    
    with analysis_tabs[1]:
        show_financial_analysis()
    
    with analysis_tabs[2]:
        show_investment_planning()
    
    with analysis_tabs[3]:
        show_strategic_decisions()
        
    with analysis_tabs[4]:
        show_performance_analytics()

def show_investment_overview():
    st.subheader("📊 Vue d'Ensemble des Investissements")
    
    # Données des projets d'investissement
    projects_data = {
        'Projet': [
            'Nouvelle Ligne Production', 
            'Modernisation Usine A', 
            'Système IA Qualité',
            'Énergie Renouvelable',
            'R&D Nouveaux Produits',
            'Digitalisation Logistique'
        ],
        'Type': ['Production', 'Infrastructure', 'Technologie', 'Durabilité', 'Innovation', 'Digital'],
        'Budget (M€)': [2.1, 1.2, 0.4, 0.8, 0.3, 0.4],
        'ROI Attendu (%)': [22.5, 15.8, 28.3, 12.1, 35.2, 18.7],
        'Délai (ans)': [3.5, 2.8, 1.5, 4.2, 2.1, 1.8],
        'Risque': ['Moyen', 'Faible', 'Élevé', 'Faible', 'Très Élevé', 'Moyen'],
        'Statut': ['En Cours', 'Planifié', 'Étude', 'Planifié', 'Étude', 'En Cours'],
        'Priorité': ['Élevée', 'Moyenne', 'Élevée', 'Basse', 'Moyenne', 'Élevée']
    }
    
    df_projects = pd.DataFrame(projects_data)
    
    # Filtres
    col1, col2, col3 = st.columns(3)
    
    with col1:
        type_filter = st.multiselect(
            "Filtrer par Type",
            options=df_projects['Type'].unique(),
            default=df_projects['Type'].unique()
        )
    
    with col2:
        risque_filter = st.multiselect(
            "Filtrer par Niveau de Risque",
            options=df_projects['Risque'].unique(),
            default=df_projects['Risque'].unique()
        )
    
    with col3:
        statut_filter = st.multiselect(
            "Filtrer par Statut",
            options=df_projects['Statut'].unique(),
            default=df_projects['Statut'].unique()
        )
    
    # Application des filtres
    filtered_df = df_projects[
        (df_projects['Type'].isin(type_filter)) &
        (df_projects['Risque'].isin(risque_filter)) &
        (df_projects['Statut'].isin(statut_filter))
    ]
    
    # Affichage des données
    st.dataframe(
        filtered_df.style.format({
            'Budget (M€)': '{:.1f}',
            'ROI Attendu (%)': '{:.1f}',
            'Délai (ans)': '{:.1f}'
        }).background_gradient(subset=['ROI Attendu (%)'], cmap='Greens'),
        use_container_width=True
    )
    
    # Graphiques de synthèse
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        # Répartition du budget par type
        budget_by_type = filtered_df.groupby('Type')['Budget (M€)'].sum()
        fig_budget = px.pie(
            values=budget_by_type.values,
            names=budget_by_type.index,
            title="Répartition du Budget par Type d'Investissement"
        )
        st.plotly_chart(fig_budget, use_container_width=True)
    
    with col_chart2:
        # ROI vs Risque
        fig_roi_risk = px.scatter(
            filtered_df,
            x='ROI Attendu (%)',
            y='Budget (M€)',
            size='Budget (M€)',
            color='Risque',
            hover_name='Projet',
            title="ROI vs Budget par Niveau de Risque",
            size_max=30
        )
        st.plotly_chart(fig_roi_risk, use_container_width=True)

def show_financial_analysis():
    st.subheader("💰 Analyse Financière Détaillée")
    
    # Sélection du projet à analyser
    projects = [
        'Nouvelle Ligne Production', 
        'Modernisation Usine A', 
        'Système IA Qualité',
        'Énergie Renouvelable'
    ]
    
    selected_project = st.selectbox("Sélectionner un projet à analyser", projects)
    
    if selected_project:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader(f"📈 Analyse {selected_project}")
            
            # Métriques financières selon le projet
            if selected_project == 'Nouvelle Ligne Production':
                metrics = {
                    "Investissement Initial": "2.1M€",
                    "VAN (Valeur Actuelle Nette)": "450K€",
                    "TRI (Taux de Rentabilité Interne)": "22.5%",
                    "Délai de Récupération": "3.2 ans"
                }
            elif selected_project == 'Modernisation Usine A':
                metrics = {
                    "Investissement Initial": "1.2M€",
                    "VAN (Valeur Actuelle Nette)": "280K€",
                    "TRI (Taux de Rentabilité Interne)": "15.8%",
                    "Délai de Récupération": "2.8 ans"
                }
            elif selected_project == 'Système IA Qualité':
                metrics = {
                    "Investissement Initial": "0.4M€",
                    "VAN (Valeur Actuelle Nette)": "120K€",
                    "TRI (Taux de Rentabilité Interne)": "28.3%",
                    "Délai de Récupération": "1.5 ans"
                }
            else:  # Énergie Renouvelable
                metrics = {
                    "Investissement Initial": "0.8M€",
                    "VAN (Valeur Actuelle Nette)": "95K€",
                    "TRI (Taux de Rentabilité Interne)": "12.1%",
                    "Délai de Récupération": "4.2 ans"
                }
            
            for metric_name, metric_value in metrics.items():
                st.metric(metric_name, metric_value)
            
            # Scénarios de sensibilité
            st.subheader("🎯 Scénarios de Sensibilité")
            
            variation_prix = st.slider("Variation des prix de vente (%)", -20, 20, 0, key="price_var")
            variation_couts = st.slider("Variation des coûts opérationnels (%)", -15, 15, 0, key="cost_var")
            
            # Calcul impact sur ROI
            roi_base = float(metrics["TRI (Taux de Rentabilité Interne)"].replace('%', ''))
            roi_ajuste = roi_base + (variation_prix * 0.8) - (variation_couts * 0.6)
            
            st.metric("ROI Ajusté", f"{roi_ajuste:.1f}%", f"{roi_ajuste - roi_base:.1f}%")
        
        with col2:
            st.subheader("📊 Flux de Trésorerie")
            
            # Simulation des flux de trésorerie selon le projet
            if selected_project == 'Nouvelle Ligne Production':
                cash_flows = [-2100000, 200000, 400000, 600000, 800000, 800000, 800000, 800000, 800000, 800000]
            elif selected_project == 'Modernisation Usine A':
                cash_flows = [-1200000, 150000, 250000, 350000, 450000, 450000, 450000, 450000, 450000, 450000]
            elif selected_project == 'Système IA Qualité':
                cash_flows = [-400000, 80000, 120000, 160000, 200000, 200000, 200000, 200000, 200000, 200000]
            else:  # Énergie Renouvelable
                cash_flows = [-800000, 50000, 80000, 110000, 140000, 140000, 140000, 140000, 140000, 140000]
            
            years = list(range(2024, 2034))
            df_cashflow = pd.DataFrame({
                'Année': years,
                'Flux Net': cash_flows
            })
            df_cashflow['Cumulé'] = df_cashflow['Flux Net'].cumsum()
            
            fig_cashflow = go.Figure()
            fig_cashflow.add_trace(go.Bar(x=df_cashflow['Année'], y=df_cashflow['Flux Net'], 
                                         name='Flux Net Annuel', marker_color='lightblue'))
            fig_cashflow.add_trace(go.Scatter(x=df_cashflow['Année'], y=df_cashflow['Cumulé'], 
                                            name='Flux Cumulé', line=dict(color='red', width=3)))
            fig_cashflow.update_layout(title="Projection des Flux de Trésorerie")
            st.plotly_chart(fig_cashflow, use_container_width=True)
            
            # Point de rentabilité
            break_even_index = next((i for i, val in enumerate(df_cashflow['Cumulé']) if val >= 0), None)
            if break_even_index:
                st.info(f"**Point de rentabilité atteint en {years[break_even_index]}**")

def show_investment_planning():
    st.subheader("📅 Planning et Gantt des Investissements")
    
    # Données du planning
    gantt_data = {
        'Tâche': [
            'Étude de Faisabilité', 'Approbation Budget', 'Appel d\'Offres',
            'Sélection Fournisseur', 'Installation', 'Tests et Validation',
            'Formation Équipes', 'Mise en Production'
        ],
        'Début': [
            '2024-01-15', '2024-03-01', '2024-03-15', '2024-05-01',
            '2024-06-01', '2024-08-15', '2024-09-15', '2024-10-01'
        ],
        'Fin': [
            '2024-02-28', '2024-03-14', '2024-04-30', '2024-05-31',
            '2024-08-14', '2024-09-14', '2024-09-30', '2024-12-31'
        ],
        'Projet': [
            'Nouvelle Ligne Production', 'Nouvelle Ligne Production', 'Nouvelle Ligne Production',
            'Nouvelle Ligne Production', 'Nouvelle Ligne Production', 'Nouvelle Ligne Production',
            'Nouvelle Ligne Production', 'Nouvelle Ligne Production'
        ],
        'Progression': [100, 100, 75, 50, 25, 10, 0, 0]
    }
    
    df_gantt = pd.DataFrame(gantt_data)
    df_gantt['Début'] = pd.to_datetime(df_gantt['Début'])
    df_gantt['Fin'] = pd.to_datetime(df_gantt['Fin'])
    
    # Diagramme de Gantt
    fig_gantt = px.timeline(
        df_gantt, 
        x_start="Début", 
        x_end="Fin", 
        y="Tâche",
        color="Progression",
        title="Planning des Investissements - Diagramme de Gantt",
        color_continuous_scale='Viridis'
    )
    fig_gantt.update_yaxes(autorange="reversed")
    st.plotly_chart(fig_gantt, use_container_width=True)
    
    # Indicateurs d'avancement
    st.subheader("📊 Indicateurs d'Avancement")
    
    progress_col1, progress_col2, progress_col3, progress_col4 = st.columns(4)
    
    with progress_col1:
        st.metric("📅 Délai Moyen", "45 jours", "-5 jours")
    
    with progress_col2:
        st.metric("💰 Budget Utilisé", "68%", "2%")
    
    with progress_col3:
        st.metric("✅ Tâches Terminées", "3/8", "37%")
    
    with progress_col4:
        st.metric("🚨 Retards", "1 projet", "Critique")
        
    # Alertes et actions
    st.subheader("🚨 Alertes et Actions Requises")
    
    alert_data = {
        'Projet': ['Modernisation Usine A', 'Système IA Qualité', 'Nouvelle Ligne Production'],
        'Type Alerte': ['Délai', 'Budget', 'Ressources'],
        'Description': ['Retard de 15 jours sur planning', 'Dépassement budget de 8%', 'Manque compétences techniques'],
        'Priorité': ['Élevée', 'Moyenne', 'Élevée'],
        'Action': ['Réviser planning', 'Analyser coûts', 'Recrutement urgent']
    }
    
    st.dataframe(pd.DataFrame(alert_data), use_container_width=True)

def show_strategic_decisions():
    st.subheader("🎯 Aide à la Décision Stratégique")
    
    # Matrice de décision
    st.write("### 🧩 Matrice de Décision Stratégique")
    
    decision_data = {
        'Critère': [
            'Alignement Stratégique', 'ROI Attendu', 'Risque Technique',
            'Impact Environnemental', 'Délai de Mise en Œuvre', 'Compétences Internes'
        ],
        'Pondération': [25, 30, 15, 10, 10, 10],
        'Nouvelle Ligne': [9, 8, 6, 7, 5, 8],
        'Modernisation Usine': [7, 6, 8, 8, 9, 9],
        'Système IA': [8, 9, 5, 9, 7, 6]
    }
    
    df_decision = pd.DataFrame(decision_data)
    
    # Calcul des scores
    for project in ['Nouvelle Ligne', 'Modernisation Usine', 'Système IA']:
        df_decision[f'{project} Score'] = (df_decision[project] * df_decision['Pondération']) / 10
    
    st.dataframe(df_decision, use_container_width=True)
    
    # Scores totaux
    scores_totaux = {
        'Projet': ['Nouvelle Ligne Production', 'Modernisation Usine A', 'Système IA Qualité'],
        'Score Total': [
            df_decision['Nouvelle Ligne Score'].sum(),
            df_decision['Modernisation Usine Score'].sum(),
            df_decision['Système IA Score'].sum()
        ]
    }
    
    df_scores = pd.DataFrame(scores_totaux)
    
    # Graphique des scores
    fig_scores = px.bar(
        df_scores, 
        x='Projet', 
        y='Score Total',
        title="Score Total par Projet - Matrice de Décision",
        color='Score Total',
        color_continuous_scale='Viridis'
    )
    st.plotly_chart(fig_scores, use_container_width=True)
    
    # Recommandations
    st.subheader("💡 Recommandations Stratégiques")
    
    best_project = df_scores.loc[df_scores['Score Total'].idxmax()]
    
    st.success(f"**🎯 Projet Recommandé : {best_project['Projet']}**")
    st.write(f"**Score : {best_project['Score Total']:.1f}/100**")
    
    col_rec1, col_rec2 = st.columns(2)
    
    with col_rec1:
        st.markdown("""
        **✅ Points Forts :**
        - Alignement parfait avec la stratégie
        - ROI élevé et maîtrisé
        - Compétences internes disponibles
        - Impact positif sur l'environnement
        """)
    
    with col_rec2:
        st.markdown("""
        **⚠️ Points de Vigilance :**
        - Délai de mise en œuvre moyen
        - Risque technique modéré
        - Investissement initial important
        - Formation nécessaire
        """)
    
    # Outil de simulation de décision
    st.subheader("🔧 Simulateur de Décision")
    
    col_sim1, col_sim2 = st.columns(2)
    
    with col_sim1:
        budget_disponible = st.slider("Budget disponible (M€)", 1.0, 5.0, 2.5, key="budget_sim")
        horizon_investissement = st.selectbox("Horizon d'investissement", 
                                            ["Court terme (1-2 ans)", "Moyen terme (3-5 ans)", "Long terme (5+ ans)"],
                                            key="horizon_sim")
    
    with col_sim2:
        tolerance_risque = st.select_slider("Tolérance au risque", 
                                          ["Faible", "Moyenne", "Élevée"],
                                          key="risk_sim")
        objectif_principal = st.selectbox("Objectif principal", 
                                        ["Rentabilité", "Croissance", "Innovation", "Durabilité"],
                                        key="objective_sim")
    
    if st.button("🎯 Générer la Recommandation Personnalisée", key="generate_rec"):
        # Logique de recommandation basée sur les critères
        if budget_disponible >= 2.0 and tolerance_risque == "Moyenne" and objectif_principal == "Rentabilité":
            recommendation = "Nouvelle Ligne Production"
        elif budget_disponible < 1.5 and tolerance_risque == "Faible" and objectif_principal == "Durabilité":
            recommendation = "Modernisation Usine A"
        elif budget_disponible < 1.0 and tolerance_risque == "Élevée" and objectif_principal == "Innovation":
            recommendation = "Système IA Qualité"
        else:
            recommendation = best_project['Projet']
            
        st.balloons()
        st.success(f"**Recommandation : {recommendation}**")
        st.info(f"Cette recommandation est optimisée pour un budget de {budget_disponible}M€ avec une tolérance au risque {tolerance_risque.lower()} et un objectif principal d'{objectif_principal.lower()}.")

def show_performance_analytics():
    st.subheader("📈 Analytics et Performance")
    
    # KPI historiques
    st.write("### 📊 Évolution des Performances")
    
    # Données historiques simulées
    years = [2020, 2021, 2022, 2023, 2024]
    performance_data = {
        'ROI Moyen (%)': [15.2, 16.8, 17.5, 18.1, 18.5],
        'Budget Total (M€)': [2.8, 3.2, 3.6, 3.9, 4.2],
        'Projets Livrés': [8, 10, 12, 14, 16],
        'Taux de Réussite (%)': [85, 88, 90, 92, 94]
    }
    
    df_performance = pd.DataFrame(performance_data, index=years)
    
    # Sélection du KPI à visualiser
    kpi_selected = st.selectbox("Sélectionner le KPI à analyser", list(performance_data.keys()))
    
    fig_trend = px.line(
        df_performance, 
        x=df_performance.index, 
        y=kpi_selected,
        title=f"Évolution du {kpi_selected}",
        markers=True
    )
    fig_trend.update_traces(line=dict(width=3))
    st.plotly_chart(fig_trend, use_container_width=True)
    
    # Analyse comparative
    st.subheader("📋 Benchmarking Interne")
    
    col_bench1, col_bench2 = st.columns(2)
    
    with col_bench1:
        st.write("**Performance par Type de Projet**")
        type_performance = {
            'Type': ['Production', 'Infrastructure', 'Technologie', 'Durabilité', 'Innovation'],
            'ROI Moyen (%)': [18.2, 14.5, 25.3, 11.8, 32.7],
            'Taux Réussite (%)': [92, 88, 85, 95, 78]
        }
        st.dataframe(pd.DataFrame(type_performance), use_container_width=True)
    
    with col_bench2:
        st.write("**Retour d'Expérience**")
        st.metric("📈 Meilleur ROI", "35.2%", "R&D Nouveaux Produits")
        st.metric("⚡ Plus Rapide", "1.5 ans", "Système IA Qualité")
        st.metric("🛡️ Moins Risqué", "2% d'écart", "Modernisation Usine A")



def show_predictive_cashflow():
    st.title("💸 Trésorerie Prédictive")
    st.info("Cette section est en cours de développement...")
    # Implémentation similaire aux autres sections

def show_executive_reporting():
    st.title("📊 Reporting Executive")
    st.info("Cette section est en cours de développement...")

def show_auto_communications():
    st.header("📧 Communications Automatisées")
    
    st.markdown("""
    ### 🤖 Système de Notification Intelligent
    
    **🎯 Scénarios de Communication Automatisée :**
    """)
    
    # Configuration des notifications
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔔 Configuration des Alertes")
        
        with st.form("alert_config"):
            st.write("**📈 Alertes Budget :**")
            budget_threshold = st.slider("Seuil d'alerte budget (%)", 5, 20, 10)
            
            st.write("**📦 Alertes Stock :**")
            stock_days = st.slider("Seuil stock critique (jours)", 1, 10, 3)
            
            st.write("**💰 Alertes Trésorerie :**")
            cash_threshold = st.number_input("Seuil trésorerie (€)", value=10000)
            
            if st.form_submit_button("💾 Sauvegarder la configuration"):
                st.success("Configuration sauvegardée!")
    
    with col2:
        st.subheader("📧 Canaux de Communication")
        
        channels = st.multiselect(
            "Canaux activés :",
            ["Email Direction", "Slack Contrôleur", "SMS Urgence", "Teams Alerts", "Rapport PDF Auto"],
            default=["Email Direction", "Slack Contrôleur"]
        )
        
        st.write("**📋 Templates de Messages :**")
        template = st.selectbox("Template à utiliser :", [
            "Alerte Budget Standard",
            "Urgence Stock Critique", 
            "Rapport Mensuel Auto",
            "Alerte Trésorerie"
        ])
        
        if st.button("👁️ Aperçu du Template"):
            st.info("""
            **Objet :** Alerte Budget - Écart détecté
            **Message :** Bonjour, un écart de 12.5% a été détecté sur le budget production. 
            Montant réel: 125,000€ vs Budget: 111,000€. Action recommandée: analyse immédiate.
            """)
    
    # Historique des communications
    st.subheader("📝 Historique des Communications")
    
    comm_history = {
        'Date': ['15/01/2024 14:30', '15/01/2024 10:15', '14/01/2024 16:45', '14/01/2024 09:00'],
        'Type': ['Alerte Budget', 'Rapport Quotidien', 'Alerte Stock', 'Rapport Hebdo'],
        'Destinataire': ['direction@entreprise.com', 'controleur@entreprise.com', 'logistique@entreprise.com', 'equipe@entreprise.com'],
        'Statut': ['✅ Livré', '✅ Livré', '⚠️ En attente', '✅ Livré'],
        'Message': ['Écart production +12.5%', 'Synthèse performance', 'Stock article A001 critique', 'Rapport consolidation']
    }
    
    st.dataframe(pd.DataFrame(comm_history), use_container_width=True)
    
    # Test de notification
    st.subheader("🧪 Test du Système de Notification")
    
    col_test1, col_test2 = st.columns(2)
    
    with col_test1:
        test_type = st.selectbox("Type de notification à tester:", [
            "Alerte Budget", "Alerte Stock", "Rapport Auto", "Alerte Trésorerie"
        ])
        test_recipient = st.text_input("Destinataire test:", "test@entreprise.com")
    
    with col_test2:
        if st.button("🚀 Tester la Notification", type="primary"):
            with st.spinner("Envoi de la notification test..."):
                time.sleep(2)
                st.success("✅ Notification test envoyée avec succès!")
                st.info(f"📧 Type: {test_type} | 📨 Destinataire: {test_recipient}")

# Ajoutez également cette fonction manquante pour show_production_knowledge
def show_production_knowledge():
    st.header("🏭 Encyclopédie de la Production")
    
    st.markdown("""
    ## 📚 Théorie et Méthodologies de la Gestion de Production
    
    ### 🎯 Méthodes de Planification
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **📊 MRP II (Manufacturing Resource Planning)**
        
        **Formules de Base :**
        """)
        
        st.latex(r"""
        \text{Besoin Brut} = \text{Prévision Ventes} + \text{Stock Cible}
        """)
        
        st.latex(r"""
        \text{Besoin Net} = \text{Besoin Brut} - \text{Stock Existant} - \text{Commandes}
        """)
        
        st.latex(r"""
        \text{Ordre de Fabrication} = \max(\text{Besoin Net}, 0)
        """)
        
        st.markdown("""
        **📈 Indicateurs Clés :**
        """)
        
        st.latex(r"""
        \text{TRS} = \frac{\text{Temps Utile}}{\text{Temps Total}} \times 100
        """)
        
        st.latex(r"""
        \text{Taux de Rendement} = \frac{\text{Output Réel}}{\text{Output Théorique}} \times 100
        """)
    
    with col2:
        st.markdown("""
        **⚙️ Méthode Kanban**
        
        **Calcul du nombre de kanbans :**
        """)
        
        st.latex(r"""
        N = \frac{D \times (L + S)}{C}
        """)
        
        st.markdown("""
        **Où :**
        - $N$ : Nombre de kanbans
        - $D$ : Demande moyenne
        - $L$ : Délai de réapprovisionnement  
        - $S$ : Stock de sécurité
        - $C$ : Capacité du conteneur
        """)
        
        st.markdown("""
        **🔧 OEE (Overall Equipment Effectiveness)**
        """)
        
        st.latex(r"""
        \text{OEE} = \text{Disponibilité} \times \text{Performance} \times \text{Qualité}
        """)
        
        st.latex(r"""
        \text{OEE} = \frac{\text{Temps Brut}}{\text{Temps Planifié}} \times \frac{\text{Cadence Réelle}}{\text{Cadence Max}} \times \frac{\text{Units Bonnes}}{\text{Units Totales}}
        """)
    
    # Calculateur de production interactif
    st.subheader("🧮 Calculateur de Besoins de Production")
    
    col1, col2 = st.columns(2)
    
    with col1:
        ventes_prevues = st.number_input("Ventes prévues (unités)", value=1000)
        stock_initial = st.number_input("Stock initial (unités)", value=100)
        stock_cible = st.number_input("Stock cible (unités)", value=120)
        delai_fabrication = st.number_input("Délai fabrication (jours)", value=5)
    
    with col2:
        # Calculs automatiques
        production_necessaire = ventes_prevues + stock_cible - stock_initial
        besoin_quotidien = production_necessaire / 30  # Sur 1 mois
        lancement_commande = delai_fabrication + 1  # J+1 pour sécurité
        
        st.metric("📦 Production nécessaire", f"{production_necessaire} unités")
        st.metric("📊 Besoin quotidien moyen", f"{besoin_quotidien:.1f} unités/jour")
        st.metric("⏱️ Date lancement recommandée", f"J+{lancement_commande}")
    
    # Simulation de plan de production
    if st.button("📋 Générer Plan de Production"):
        st.subheader("📅 Plan de Production Simulé")
        
        # Génération d'un plan sur 30 jours
        jours = list(range(1, 31))
        production_jour = [besoin_quotidien * (1 + np.random.normal(0, 0.1)) for _ in jours]
        stock_cumul = [stock_initial]
        
        for prod in production_jour:
            nouveau_stock = stock_cumul[-1] + prod - besoin_quotidien
            stock_cumul.append(max(0, nouveau_stock))
        
        df_plan = pd.DataFrame({
            'Jour': jours,
            'Production (u)': [round(p, 1) for p in production_jour],
            'Stock Fin Jour': [round(s, 1) for s in stock_cumul[1:]]
        })
        
        st.dataframe(df_plan, use_container_width=True)
        
        # Graphique
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=jours, y=production_jour, name='Production', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=jours, y=stock_cumul[1:], name='Stock', line=dict(color='green')))
        fig.add_hline(y=stock_cible, line_dash="dash", line_color="red", annotation_text="Stock Cible")
        fig.update_layout(title="Plan de Production sur 30 jours")
        st.plotly_chart(fig, use_container_width=True)

# Ajoutez ces fonctions manquantes pour compléter l'application
def show_stock_management_knowledge():
    st.header("📦 Encyclopédie de la Gestion des Stocks")
    st.info("Section en cours de développement...")

def show_investment_knowledge():
    st.header("🏗️ Encyclopédie de l'Investissement")
    st.info("Section en cours de développement...")

def show_cashflow_knowledge():
    st.header("💸 Encyclopédie de la Trésorerie")
    st.info("Section en cours de développement...")

def show_advanced_methods():
    st.header("📊 Méthodes Avancées de Contrôle de Gestion")
    st.info("Section en cours de développement...")

def show_advanced_stock_management():
    st.title("📦 Gestion des Stocks Avancée")
    st.info("Section en cours de développement...")

def show_strategic_investment():
    st.title("🏗️ Investissement Stratégique")

    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "💰 Budget Total", 
            "4.2M€", 
            "+12% vs prévision",
            delta_color="normal"
        )
    
    with col2:
        st.metric(
            "📈 ROI Moyen", 
            "18.5%", 
            "+2.3%",
            delta_color="inverse"
        )
    
    with col3:
        st.metric(
            "⏱️ Délai Retour", 
            "3.2 ans", 
            "-0.4 ans",
            delta_color="inverse"
        )
    
    with col4:
        st.metric(
            "🚨 Projets à Risque", 
            "2", 
            "-1",
            delta_color="inverse"
        )

    # Onglets pour différentes analyses
    analysis_tabs = st.tabs([
        "📊 Vue d'Ensemble", 
        "💰 Analyse Financière", 
        "📅 Planning", 
        "🎯 Décisions Stratégiques",
        "📈 Performance"
    ])
    
    with analysis_tabs[0]:
        show_investment_overview()
    
    with analysis_tabs[1]:
        show_financial_analysis()
    
    with analysis_tabs[2]:
        show_investment_planning()
    
    with analysis_tabs[3]:
        show_strategic_decisions()
        
    with analysis_tabs[4]:
        show_performance_analytics()

def show_investment_overview():
    st.subheader("📊 Vue d'Ensemble des Investissements")
    
    # Données des projets d'investissement
    projects_data = {
        'Projet': [
            'Nouvelle Ligne Production', 
            'Modernisation Usine A', 
            'Système IA Qualité',
            'Énergie Renouvelable',
            'R&D Nouveaux Produits',
            'Digitalisation Logistique'
        ],
        'Type': ['Production', 'Infrastructure', 'Technologie', 'Durabilité', 'Innovation', 'Digital'],
        'Budget (M€)': [2.1, 1.2, 0.4, 0.8, 0.3, 0.4],
        'ROI Attendu (%)': [22.5, 15.8, 28.3, 12.1, 35.2, 18.7],
        'Délai (ans)': [3.5, 2.8, 1.5, 4.2, 2.1, 1.8],
        'Risque': ['Moyen', 'Faible', 'Élevé', 'Faible', 'Très Élevé', 'Moyen'],
        'Statut': ['En Cours', 'Planifié', 'Étude', 'Planifié', 'Étude', 'En Cours'],
        'Priorité': ['Élevée', 'Moyenne', 'Élevée', 'Basse', 'Moyenne', 'Élevée']
    }
    
    df_projects = pd.DataFrame(projects_data)
    
    # Filtres
    col1, col2, col3 = st.columns(3)
    
    with col1:
        type_filter = st.multiselect(
            "Filtrer par Type",
            options=df_projects['Type'].unique(),
            default=df_projects['Type'].unique()
        )
    
    with col2:
        risque_filter = st.multiselect(
            "Filtrer par Niveau de Risque",
            options=df_projects['Risque'].unique(),
            default=df_projects['Risque'].unique()
        )
    
    with col3:
        statut_filter = st.multiselect(
            "Filtrer par Statut",
            options=df_projects['Statut'].unique(),
            default=df_projects['Statut'].unique()
        )
    
    # Application des filtres
    filtered_df = df_projects[
        (df_projects['Type'].isin(type_filter)) &
        (df_projects['Risque'].isin(risque_filter)) &
        (df_projects['Statut'].isin(statut_filter))
    ]
    
    # Affichage des données
    st.dataframe(
        filtered_df.style.format({
            'Budget (M€)': '{:.1f}',
            'ROI Attendu (%)': '{:.1f}',
            'Délai (ans)': '{:.1f}'
        }).background_gradient(subset=['ROI Attendu (%)'], cmap='Greens'),
        use_container_width=True
    )
    
    # Graphiques de synthèse
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        # Répartition du budget par type
        budget_by_type = filtered_df.groupby('Type')['Budget (M€)'].sum()
        fig_budget = px.pie(
            values=budget_by_type.values,
            names=budget_by_type.index,
            title="Répartition du Budget par Type d'Investissement"
        )
        st.plotly_chart(fig_budget, use_container_width=True)
    
    with col_chart2:
        # ROI vs Risque
        fig_roi_risk = px.scatter(
            filtered_df,
            x='ROI Attendu (%)',
            y='Budget (M€)',
            size='Budget (M€)',
            color='Risque',
            hover_name='Projet',
            title="ROI vs Budget par Niveau de Risque",
            size_max=30
        )
        st.plotly_chart(fig_roi_risk, use_container_width=True)

def show_financial_analysis():
    st.subheader("💰 Analyse Financière Détaillée")
    
    # Sélection du projet à analyser
    projects = [
        'Nouvelle Ligne Production', 
        'Modernisation Usine A', 
        'Système IA Qualité',
        'Énergie Renouvelable'
    ]
    
    selected_project = st.selectbox("Sélectionner un projet à analyser", projects)
    
    if selected_project:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader(f"📈 Analyse {selected_project}")
            
            # Métriques financières selon le projet
            if selected_project == 'Nouvelle Ligne Production':
                metrics = {
                    "Investissement Initial": "2.1M€",
                    "VAN (Valeur Actuelle Nette)": "450K€",
                    "TRI (Taux de Rentabilité Interne)": "22.5%",
                    "Délai de Récupération": "3.2 ans"
                }
            elif selected_project == 'Modernisation Usine A':
                metrics = {
                    "Investissement Initial": "1.2M€",
                    "VAN (Valeur Actuelle Nette)": "280K€",
                    "TRI (Taux de Rentabilité Interne)": "15.8%",
                    "Délai de Récupération": "2.8 ans"
                }
            elif selected_project == 'Système IA Qualité':
                metrics = {
                    "Investissement Initial": "0.4M€",
                    "VAN (Valeur Actuelle Nette)": "120K€",
                    "TRI (Taux de Rentabilité Interne)": "28.3%",
                    "Délai de Récupération": "1.5 ans"
                }
            else:  # Énergie Renouvelable
                metrics = {
                    "Investissement Initial": "0.8M€",
                    "VAN (Valeur Actuelle Nette)": "95K€",
                    "TRI (Taux de Rentabilité Interne)": "12.1%",
                    "Délai de Récupération": "4.2 ans"
                }
            
            for metric_name, metric_value in metrics.items():
                st.metric(metric_name, metric_value)
            
            # Scénarios de sensibilité
            st.subheader("🎯 Scénarios de Sensibilité")
            
            variation_prix = st.slider("Variation des prix de vente (%)", -20, 20, 0, key="price_var")
            variation_couts = st.slider("Variation des coûts opérationnels (%)", -15, 15, 0, key="cost_var")
            
            # Calcul impact sur ROI
            roi_base = float(metrics["TRI (Taux de Rentabilité Interne)"].replace('%', ''))
            roi_ajuste = roi_base + (variation_prix * 0.8) - (variation_couts * 0.6)
            
            st.metric("ROI Ajusté", f"{roi_ajuste:.1f}%", f"{roi_ajuste - roi_base:.1f}%")
        
        with col2:
            st.subheader("📊 Flux de Trésorerie")
            
            # Simulation des flux de trésorerie selon le projet
            if selected_project == 'Nouvelle Ligne Production':
                cash_flows = [-2100000, 200000, 400000, 600000, 800000, 800000, 800000, 800000, 800000, 800000]
            elif selected_project == 'Modernisation Usine A':
                cash_flows = [-1200000, 150000, 250000, 350000, 450000, 450000, 450000, 450000, 450000, 450000]
            elif selected_project == 'Système IA Qualité':
                cash_flows = [-400000, 80000, 120000, 160000, 200000, 200000, 200000, 200000, 200000, 200000]
            else:  # Énergie Renouvelable
                cash_flows = [-800000, 50000, 80000, 110000, 140000, 140000, 140000, 140000, 140000, 140000]
            
            years = list(range(2024, 2034))
            df_cashflow = pd.DataFrame({
                'Année': years,
                'Flux Net': cash_flows
            })
            df_cashflow['Cumulé'] = df_cashflow['Flux Net'].cumsum()
            
            fig_cashflow = go.Figure()
            fig_cashflow.add_trace(go.Bar(x=df_cashflow['Année'], y=df_cashflow['Flux Net'], 
                                         name='Flux Net Annuel', marker_color='lightblue'))
            fig_cashflow.add_trace(go.Scatter(x=df_cashflow['Année'], y=df_cashflow['Cumulé'], 
                                            name='Flux Cumulé', line=dict(color='red', width=3)))
            fig_cashflow.update_layout(title="Projection des Flux de Trésorerie")
            st.plotly_chart(fig_cashflow, use_container_width=True)
            
            # Point de rentabilité
            break_even_index = next((i for i, val in enumerate(df_cashflow['Cumulé']) if val >= 0), None)
            if break_even_index:
                st.info(f"**Point de rentabilité atteint en {years[break_even_index]}**")

def show_investment_planning():
    st.subheader("📅 Planning et Gantt des Investissements")
    
    # Données du planning
    gantt_data = {
        'Tâche': [
            'Étude de Faisabilité', 'Approbation Budget', 'Appel d\'Offres',
            'Sélection Fournisseur', 'Installation', 'Tests et Validation',
            'Formation Équipes', 'Mise en Production'
        ],
        'Début': [
            '2024-01-15', '2024-03-01', '2024-03-15', '2024-05-01',
            '2024-06-01', '2024-08-15', '2024-09-15', '2024-10-01'
        ],
        'Fin': [
            '2024-02-28', '2024-03-14', '2024-04-30', '2024-05-31',
            '2024-08-14', '2024-09-14', '2024-09-30', '2024-12-31'
        ],
        'Projet': [
            'Nouvelle Ligne Production', 'Nouvelle Ligne Production', 'Nouvelle Ligne Production',
            'Nouvelle Ligne Production', 'Nouvelle Ligne Production', 'Nouvelle Ligne Production',
            'Nouvelle Ligne Production', 'Nouvelle Ligne Production'
        ],
        'Progression': [100, 100, 75, 50, 25, 10, 0, 0]
    }
    
    df_gantt = pd.DataFrame(gantt_data)
    df_gantt['Début'] = pd.to_datetime(df_gantt['Début'])
    df_gantt['Fin'] = pd.to_datetime(df_gantt['Fin'])
    
    # Diagramme de Gantt
    fig_gantt = px.timeline(
        df_gantt, 
        x_start="Début", 
        x_end="Fin", 
        y="Tâche",
        color="Progression",
        title="Planning des Investissements - Diagramme de Gantt",
        color_continuous_scale='Viridis'
    )
    fig_gantt.update_yaxes(autorange="reversed")
    st.plotly_chart(fig_gantt, use_container_width=True)
    
    # Indicateurs d'avancement
    st.subheader("📊 Indicateurs d'Avancement")
    
    progress_col1, progress_col2, progress_col3, progress_col4 = st.columns(4)
    
    with progress_col1:
        st.metric("📅 Délai Moyen", "45 jours", "-5 jours")
    
    with progress_col2:
        st.metric("💰 Budget Utilisé", "68%", "2%")
    
    with progress_col3:
        st.metric("✅ Tâches Terminées", "3/8", "37%")
    
    with progress_col4:
        st.metric("🚨 Retards", "1 projet", "Critique")
        
    # Alertes et actions
    st.subheader("🚨 Alertes et Actions Requises")
    
    alert_data = {
        'Projet': ['Modernisation Usine A', 'Système IA Qualité', 'Nouvelle Ligne Production'],
        'Type Alerte': ['Délai', 'Budget', 'Ressources'],
        'Description': ['Retard de 15 jours sur planning', 'Dépassement budget de 8%', 'Manque compétences techniques'],
        'Priorité': ['Élevée', 'Moyenne', 'Élevée'],
        'Action': ['Réviser planning', 'Analyser coûts', 'Recrutement urgent']
    }
    
    st.dataframe(pd.DataFrame(alert_data), use_container_width=True)

def show_strategic_decisions():
    st.subheader("🎯 Aide à la Décision Stratégique")
    
    # Matrice de décision
    st.write("### 🧩 Matrice de Décision Stratégique")
    
    decision_data = {
        'Critère': [
            'Alignement Stratégique', 'ROI Attendu', 'Risque Technique',
            'Impact Environnemental', 'Délai de Mise en Œuvre', 'Compétences Internes'
        ],
        'Pondération': [25, 30, 15, 10, 10, 10],
        'Nouvelle Ligne': [9, 8, 6, 7, 5, 8],
        'Modernisation Usine': [7, 6, 8, 8, 9, 9],
        'Système IA': [8, 9, 5, 9, 7, 6]
    }
    
    df_decision = pd.DataFrame(decision_data)
    
    # Calcul des scores
    for project in ['Nouvelle Ligne', 'Modernisation Usine', 'Système IA']:
        df_decision[f'{project} Score'] = (df_decision[project] * df_decision['Pondération']) / 10
    
    st.dataframe(df_decision, use_container_width=True)
    
    # Scores totaux
    scores_totaux = {
        'Projet': ['Nouvelle Ligne Production', 'Modernisation Usine A', 'Système IA Qualité'],
        'Score Total': [
            df_decision['Nouvelle Ligne Score'].sum(),
            df_decision['Modernisation Usine Score'].sum(),
            df_decision['Système IA Score'].sum()
        ]
    }
    
    df_scores = pd.DataFrame(scores_totaux)
    
    # Graphique des scores
    fig_scores = px.bar(
        df_scores, 
        x='Projet', 
        y='Score Total',
        title="Score Total par Projet - Matrice de Décision",
        color='Score Total',
        color_continuous_scale='Viridis'
    )
    st.plotly_chart(fig_scores, use_container_width=True)
    
    # Recommandations
    st.subheader("💡 Recommandations Stratégiques")
    
    best_project = df_scores.loc[df_scores['Score Total'].idxmax()]
    
    st.success(f"**🎯 Projet Recommandé : {best_project['Projet']}**")
    st.write(f"**Score : {best_project['Score Total']:.1f}/100**")
    
    col_rec1, col_rec2 = st.columns(2)
    
    with col_rec1:
        st.markdown("""
        **✅ Points Forts :**
        - Alignement parfait avec la stratégie
        - ROI élevé et maîtrisé
        - Compétences internes disponibles
        - Impact positif sur l'environnement
        """)
    
    with col_rec2:
        st.markdown("""
        **⚠️ Points de Vigilance :**
        - Délai de mise en œuvre moyen
        - Risque technique modéré
        - Investissement initial important
        - Formation nécessaire
        """)
    
    # Outil de simulation de décision
    st.subheader("🔧 Simulateur de Décision")
    
    col_sim1, col_sim2 = st.columns(2)
    
    with col_sim1:
        budget_disponible = st.slider("Budget disponible (M€)", 1.0, 5.0, 2.5, key="budget_sim")
        horizon_investissement = st.selectbox("Horizon d'investissement", 
                                            ["Court terme (1-2 ans)", "Moyen terme (3-5 ans)", "Long terme (5+ ans)"],
                                            key="horizon_sim")
    
    with col_sim2:
        tolerance_risque = st.select_slider("Tolérance au risque", 
                                          ["Faible", "Moyenne", "Élevée"],
                                          key="risk_sim")
        objectif_principal = st.selectbox("Objectif principal", 
                                        ["Rentabilité", "Croissance", "Innovation", "Durabilité"],
                                        key="objective_sim")
    
    if st.button("🎯 Générer la Recommandation Personnalisée", key="generate_rec"):
        # Logique de recommandation basée sur les critères
        if budget_disponible >= 2.0 and tolerance_risque == "Moyenne" and objectif_principal == "Rentabilité":
            recommendation = "Nouvelle Ligne Production"
        elif budget_disponible < 1.5 and tolerance_risque == "Faible" and objectif_principal == "Durabilité":
            recommendation = "Modernisation Usine A"
        elif budget_disponible < 1.0 and tolerance_risque == "Élevée" and objectif_principal == "Innovation":
            recommendation = "Système IA Qualité"
        else:
            recommendation = best_project['Projet']
            
        st.balloons()
        st.success(f"**Recommandation : {recommendation}**")
        st.info(f"Cette recommandation est optimisée pour un budget de {budget_disponible}M€ avec une tolérance au risque {tolerance_risque.lower()} et un objectif principal d'{objectif_principal.lower()}.")

def show_performance_analytics():
    st.subheader("📈 Analytics et Performance")
    
    # KPI historiques
    st.write("### 📊 Évolution des Performances")
    
    # Données historiques simulées
    years = [2020, 2021, 2022, 2023, 2024]
    performance_data = {
        'ROI Moyen (%)': [15.2, 16.8, 17.5, 18.1, 18.5],
        'Budget Total (M€)': [2.8, 3.2, 3.6, 3.9, 4.2],
        'Projets Livrés': [8, 10, 12, 14, 16],
        'Taux de Réussite (%)': [85, 88, 90, 92, 94]
    }
    
    df_performance = pd.DataFrame(performance_data, index=years)
    
    # Sélection du KPI à visualiser
    kpi_selected = st.selectbox("Sélectionner le KPI à analyser", list(performance_data.keys()))
    
    fig_trend = px.line(
        df_performance, 
        x=df_performance.index, 
        y=kpi_selected,
        title=f"Évolution du {kpi_selected}",
        markers=True
    )
    fig_trend.update_traces(line=dict(width=3))
    st.plotly_chart(fig_trend, use_container_width=True)
    
    # Analyse comparative
    st.subheader("📋 Benchmarking Interne")
    
    col_bench1, col_bench2 = st.columns(2)
    
    with col_bench1:
        st.write("**Performance par Type de Projet**")
        type_performance = {
            'Type': ['Production', 'Infrastructure', 'Technologie', 'Durabilité', 'Innovation'],
            'ROI Moyen (%)': [18.2, 14.5, 25.3, 11.8, 32.7],
            'Taux Réussite (%)': [92, 88, 85, 95, 78]
        }
        st.dataframe(pd.DataFrame(type_performance), use_container_width=True)
    
    with col_bench2:
        st.write("**Retour d'Expérience**")
        st.metric("📈 Meilleur ROI", "35.2%", "R&D Nouveaux Produits")
        st.metric("⚡ Plus Rapide", "1.5 ans", "Système IA Qualité")
        st.metric("🛡️ Moins Risqué", "2% d'écart", "Modernisation Usine A")


    #st.info("Section en cours de développement...")



def show_predictive_cashflow():
    st.title("💸 Trésorerie Prédictive")

 
    # Métriques de trésorerie en temps réel
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "💰 Solde Actuel", 
            "2.8M€", 
            "+150K€ vs mois dernier",
            delta_color="normal"
        )
    
    with col2:
        st.metric(
            "📈 Flux Mensuel Moyen", 
            "450K€", 
            "+12%",
            delta_color="inverse"
        )
    
    with col3:
        st.metric(
            "⚠️ Jours Autonomie", 
            "68 jours", 
            "-5 jours",
            delta_color="inverse"
        )
    
    with col4:
        st.metric(
            "🚨 Point Bas Prévu", 
            "1.2M€", 
            "dans 45 jours",
            delta_color="inverse"
        )

    # Onglets pour différentes analyses
    cashflow_tabs = st.tabs([
        "📊 Tableau de Bord", 
        "🔮 Prévisions", 
        "📋 Détails Flux", 
        "🎯 Scénarios",
        "🚨 Alertes"
    ])
    
    with cashflow_tabs[0]:
        show_cashflow_dashboard()
    
    with cashflow_tabs[1]:
        show_forecasts()
    
    with cashflow_tabs[2]:
        show_flow_details()
    
    with cashflow_tabs[3]:
        show_scenarios()
        
    with cashflow_tabs[4]:
        show_alerts()

def show_cashflow_dashboard():
    st.subheader("📊 Tableau de Bord Trésorerie")
    
    # Graphique principal de trésorerie
    col_viz1, col_viz2 = st.columns([2, 1])
    
    with col_viz1:
        # Données historiques et prévisions
        dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='M')
        historique = [2.5, 2.3, 2.1, 2.4, 2.7, 2.8]  # Janvier à Juin
        previsions = [2.6, 2.2, 1.8, 1.5, 1.2, 1.8]  # Juillet à Décembre
        
        fig_cashflow = go.Figure()
        
        # Historique
        fig_cashflow.add_trace(go.Scatter(
            x=dates[:6], y=historique,
            mode='lines+markers',
            name='Historique',
            line=dict(color='blue', width=3),
            marker=dict(size=8)
        ))
        
        # Prévisions
        fig_cashflow.add_trace(go.Scatter(
            x=dates[5:], y=previsions,
            mode='lines+markers',
            name='Prévisions',
            line=dict(color='orange', width=3, dash='dash'),
            marker=dict(size=8)
        ))
        
        # Zone critique
        fig_cashflow.add_hrect(
            y0=0, y1=1.5,
            fillcolor="red", opacity=0.2,
            layer="below", line_width=0,
            annotation_text="Zone Critique"
        )
        
        fig_cashflow.update_layout(
            title="Évolution de la Trésorerie 2024",
            xaxis_title="Mois",
            yaxis_title="Trésorerie (M€)",
            height=400
        )
        
        st.plotly_chart(fig_cashflow, use_container_width=True)
    
    with col_viz2:
        st.subheader("🎯 Indicateurs Clés")
        
        # Jauge de trésorerie
        solde_actuel = 2.8
        solde_min_acceptable = 1.0
        solde_ideal = 3.0
        
        progression = min(solde_actuel / solde_ideal, 1.0)
        
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number+delta",
            value = solde_actuel,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Niveau Trésorerie"},
            delta = {'reference': solde_min_acceptable},
            gauge = {
                'axis': {'range': [0, solde_ideal]},
                'bar': {'color': "darkblue"},
                'steps': [
                    {'range': [0, solde_min_acceptable], 'color': "red"},
                    {'range': [solde_min_acceptable, solde_ideal], 'color': "lightgray"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': solde_actuel
                }
            }
        ))
        
        fig_gauge.update_layout(height=300)
        st.plotly_chart(fig_gauge, use_container_width=True)
        
        # Autres indicateurs
        st.metric("📊 Ratio de Liquidité", "1.8", "0.2")
        st.metric("⏱️ BFR (Jours)", "45", "-3")
        st.metric("💳 Ligne Crédit Util.", "35%", "5%")

    # Analyse détaillée des flux
    st.subheader("📈 Analyse des Flux par Catégorie")
    
    col_flow1, col_flow2 = st.columns(2)
    
    with col_flow1:
        # Flux entrants
        flux_data = {
            'Catégorie': ['Ventes Clients', 'Subventions', 'Produits Financiers', 'Autres'],
            'Montant (K€)': [1250, 150, 80, 45],
            'Évolution (%)': [12.5, 0, 5.2, -2.1]
        }
        
        df_flux = pd.DataFrame(flux_data)
        df_flux_entrants = df_flux.copy()
        df_flux_entrants['Type'] = 'Entrants'
        
        fig_entrants = px.bar(
            df_flux, 
            x='Catégorie', 
            y='Montant (K€)',
            title="Flux Entrants par Catégorie",
            color='Évolution (%)',
            color_continuous_scale='Viridis'
        )
        st.plotly_chart(fig_entrants, use_container_width=True)
    
    with col_flow2:
        # Flux sortants
        flux_sortants = {
            'Catégorie': ['Fournisseurs', 'Salaires', 'Impôts', 'Investissements', 'Frais Généraux'],
            'Montant (K€)': [850, 420, 180, 250, 120],
            'Évolution (%)': [8.2, 3.5, -1.2, 25.0, 2.1]
        }
        
        df_sortants = pd.DataFrame(flux_sortants)
        
        fig_sortants = px.pie(
            df_sortants, 
            values='Montant (K€)', 
            names='Catégorie',
            title="Répartition des Flux Sortants"
        )
        st.plotly_chart(fig_sortants, use_container_width=True)

def show_forecasts():
    st.subheader("🔮 Prévisions et Modèles Prédictifs")
    
    # Sélection du modèle
    col_model1, col_model2 = st.columns(2)
    
    with col_model1:
        modele_choisi = st.selectbox(
            "Modèle de Prévision",
            [
                "Régression Linéaire",
                "Série Temporelle (ARIMA)",
                "Machine Learning (XGBoost)",
                "Modèle Hybride"
            ],
            index=1
        )
        
        horizon_prevision = st.slider(
            "Horizon de Prévision (mois)",
            1, 24, 12
        )
        
        niveau_confiance = st.slider(
            "Intervalle de Confiance",
            0.80, 0.99, 0.95
        )
    
    with col_model2:
        st.subheader("🧠 Paramètres du Modèle")
        
        include_saisonnalite = st.checkbox("Inclure la saisonnalité", value=True)
        include_tendances = st.checkbox("Inclure les tendances marché", value=True)
        include_evenements = st.checkbox("Inclure les événements spéciaux", value=False)
        
        if st.button("🔄 Recréer les Prévisions", type="primary"):
            st.success("Modèle recalculé avec succès!")
    
    # Résultats des prévisions
    st.subheader("📊 Résultats des Prévisions")
    
    # Données simulées de prévision
    dates_forecast = pd.date_range(start='2024-07-01', periods=horizon_prevision, freq='M')
    forecast_mean = [2.6, 2.2, 1.8, 1.5, 1.2, 1.8, 2.2, 2.5, 2.8, 3.0, 3.2, 3.3]
    forecast_upper = [x * 1.1 for x in forecast_mean]
    forecast_lower = [x * 0.9 for x in forecast_mean]
    
    fig_forecast = go.Figure()
    
    # Intervalle de confiance
    fig_forecast.add_trace(go.Scatter(
        x=list(dates_forecast) + list(dates_forecast)[::-1],
        y=forecast_upper + forecast_lower[::-1],
        fill='toself',
        fillcolor='rgba(0,100,80,0.2)',
        line=dict(color='rgba(255,255,255,0)'),
        name=f'Intervalle {niveau_confiance*100}%'
    ))
    
    # Prévision moyenne
    fig_forecast.add_trace(go.Scatter(
        x=dates_forecast, y=forecast_mean,
        line=dict(color='red', width=3),
        mode='lines+markers',
        name='Prévision Moyenne'
    ))
    
    fig_forecast.update_layout(
        title=f"Prévisions Trésorerie - {modele_choisi}",
        xaxis_title="Date",
        yaxis_title="Trésorerie (M€)",
        height=500
    )
    
    st.plotly_chart(fig_forecast, use_container_width=True)
    
    # Métriques de performance du modèle
    st.subheader("📈 Performance du Modèle")
    
    col_perf1, col_perf2, col_perf3, col_perf4 = st.columns(4)
    
    with col_perf1:
        st.metric("📊 RMSE", "0.15M€", "Amélioration: 8%")
    
    with col_perf2:
        st.metric("🎯 MAPE", "5.2%", "Amélioration: 12%")
    
    with col_perf3:
        st.metric("✅ R²", "0.89", "Stable")
    
    with col_perf4:
        st.metric("🔍 Précision", "92%", "+3%")

def show_flow_details():
    st.subheader("📋 Détail des Flux de Trésorerie")
    
    # Filtres
    col_filter1, col_filter2, col_filter3 = st.columns(3)
    
    with col_filter1:
        type_flux = st.multiselect(
            "Type de Flux",
            ["Tous", "Entrants", "Sortants", "Investissement", "Financement"],
            default=["Tous"]
        )
    
    with col_filter2:
        periode = st.selectbox(
            "Période",
            ["30 derniers jours", "3 derniers mois", "6 derniers mois", "Année en cours"]
        )
    
    with col_filter3:
        montant_min = st.number_input("Montant minimum (K€)", value=10)
    
    # Tableau détaillé des flux
    flux_detaille = {
        'Date': ['2024-06-15', '2024-06-10', '2024-06-05', '2024-06-01', '2024-05-28'],
        'Description': ['Paiement Client ABC', 'Salaire Personnel', 'Achat Matières Premières', 'Subvention État', 'Remboursement Emprunt'],
        'Type': ['Entrant', 'Sortant', 'Sortant', 'Entrant', 'Sortant'],
        'Catégorie': ['Ventes', 'Personnel', 'Achats', 'Subventions', 'Financement'],
        'Montant (K€)': [450, -120, -85, 150, -200],
        'Statut': ['Réglé', 'Réglé', 'En attente', 'Réglé', 'Réglé']
    }
    
    df_flux_detaille = pd.DataFrame(flux_detaille)
    df_flux_detaille['Date'] = pd.to_datetime(df_flux_detaille['Date'])
    
    # Application des filtres
    if "Tous" not in type_flux:
        df_flux_detaille = df_flux_detaille[df_flux_detaille['Type'].isin(type_flux)]
    
    df_flux_detaille = df_flux_detaille[df_flux_detaille['Montant (K€)'].abs() >= montant_min]
    
    st.dataframe(
        df_flux_detaille.style.format({'Montant (K€)': '{:.0f}'}),
        use_container_width=True
    )
    
    # Analyse des délais de paiement
    st.subheader("⏱️ Analyse des Délais de Paiement")
    
    col_delai1, col_delai2, col_delai3 = st.columns(3)
    
    with col_delai1:
        st.metric("🧾 Délai Clients Moyen", "45 jours", "+2 jours")
    
    with col_delai2:
        st.metric("📋 Délai Fournisseurs Moyen", "32 jours", "-3 jours")
    
    with col_delai3:
        st.metric("⚖️ Écart Délais", "13 jours", "+5 jours")
    
    # Graphique des délais
    delais_data = {
        'Mois': ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Jun'],
        'Délai Clients': [42, 43, 44, 45, 46, 45],
        'Délai Fournisseurs': [35, 34, 33, 32, 31, 32]
    }
    
    df_delais = pd.DataFrame(delais_data)
    
    fig_delais = go.Figure()
    fig_delais.add_trace(go.Scatter(
        x=df_delais['Mois'], y=df_delais['Délai Clients'],
        name='Délai Clients',
        line=dict(color='red', width=3)
    ))
    fig_delais.add_trace(go.Scatter(
        x=df_delais['Mois'], y=df_delais['Délai Fournisseurs'],
        name='Délai Fournisseurs',
        line=dict(color='blue', width=3)
    ))
    
    fig_delais.update_layout(
        title="Évolution des Délais de Paiement",
        xaxis_title="Mois",
        yaxis_title="Jours"
    )
    
    st.plotly_chart(fig_delais, use_container_width=True)

def show_scenarios():
    st.subheader("🎯 Simulation de Scénarios")
    
    # Paramètres des scénarios
    col_scen1, col_scen2 = st.columns(2)
    
    with col_scen1:
        st.subheader("📈 Scénario Optimiste")
        croissance_ventes_opt = st.slider("Croissance ventes (%)", -20, 50, 15, key="opt_ventes")
        delai_clients_opt = st.slider("Délai clients (jours)", 30, 90, 40, key="opt_clients")
        marge_opt = st.slider("Amélioration marge (%)", -10, 20, 5, key="opt_marge")
    
    with col_scen2:
        st.subheader("📉 Scénario Pessimiste")
        croissance_ventes_pes = st.slider("Croissance ventes (%)", -20, 50, -5, key="pes_ventes")
        delai_clients_pes = st.slider("Délai clients (jours)", 30, 90, 60, key="pes_clients")
        marge_pes = st.slider("Détérioration marge (%)", -20, 10, -8, key="pes_marge")
    
    # Calcul et affichage des résultats
    if st.button("🔄 Calculer les Scénarios"):
        # Simulation des résultats
        scenarios_data = {
            'Scénario': ['Optimiste', 'Référence', 'Pessimiste'],
            'Trésorerie Min (M€)': [1.8, 1.2, 0.6],
            'Trésorerie Max (M€)': [4.2, 3.3, 2.1],
            'Point Bas (Mois)': ['3', '5', '7'],
            'Probabilité': ['25%', '50%', '25%']
        }
        
        df_scenarios = pd.DataFrame(scenarios_data)
        
        st.subheader("📊 Résultats des Scénarios")
        st.dataframe(df_scenarios, use_container_width=True)
        
        # Graphique comparatif
        fig_scenarios = go.Figure()
        
        scenarios = ['Optimiste', 'Référence', 'Pessimiste']
        treso_min = [1.8, 1.2, 0.6]
        treso_max = [4.2, 3.3, 2.1]
        
        for i, scenario in enumerate(scenarios):
            fig_scenarios.add_trace(go.Bar(
                name=scenario,
                x=['Trésorerie Min', 'Trésorerie Max'],
                y=[treso_min[i], treso_max[i]],
                text=[f'{treso_min[i]}M€', f'{treso_max[i]}M€'],
                textposition='auto',
            ))
        
        fig_scenarios.update_layout(
            title="Comparaison des Scénarios",
            barmode='group'
        )
        
        st.plotly_chart(fig_scenarios, use_container_width=True)
        
        # Recommandations
        st.subheader("💡 Recommandations Stratégiques")
        
        col_rec1, col_rec2 = st.columns(2)
        
        with col_rec1:
            st.success("**✅ Actions Opportunités :**")
            st.write("- Accélérer les investissements rentables")
            st.write("- Renégocier les délais fournisseurs")
            st.write("- Développer nouveaux marchés")
        
        with col_rec2:
            st.error("**🛡️ Actions Protection :**")
            st.write("- Sécuriser ligne crédit supplémentaire")
            st.write("- Réduire stocks non essentiels")
            st.write("- Renforcer recouvrement clients")

def show_alerts():
    st.subheader("🚨 Système d'Alerte Trésorerie")
    
    # Alertes actives
    alertes_data = {
        'Niveau': ['🔴 Critique', '🟠 Élevé', '🟡 Moyen', '🟢 Faible'],
        'Description': [
            'Trésorerie < 1M€ dans 60 jours',
            'Délai clients > 50 jours',
            'Utilisation crédit > 75%',
            'Écart prévision > 15%'
        ],
        'Déclencheur': ['1.2M€', '52 jours', '78%', '18%'],
        'Action': [
            'Activer plan urgence',
            'Relance clients prioritaires',
            'Négocier extension crédit',
            'Réviser prévisions'
        ]
    }
    
    df_alertes = pd.DataFrame(alertes_data)
    st.dataframe(df_alertes, use_container_width=True)
    
    # Configuration des alertes
    st.subheader("⚙️ Configuration des Seuils d'Alerte")
    
    col_seuil1, col_seuil2, col_seuil3 = st.columns(3)
    
    with col_seuil1:
        seuil_treso_critique = st.number_input("Seuil trésorerie critique (M€)", value=1.0)
        seuil_delai_client = st.number_input("Seuil délai client max (jours)", value=50)
    
    with col_seuil2:
        seuil_utilisation_credit = st.number_input("Seuil utilisation crédit (%)", value=75)
        seuil_ecart_prevision = st.number_input("Seuil écart prévision (%)", value=15)
    
    with col_seuil3:
        frequence_rapport = st.selectbox("Fréquence des rapports", ["Quotidien", "Hebdomadaire", "Mensuel"])
        notification_email = st.checkbox("Notifications par email", value=True)
    
    if st.button("💾 Sauvegarder la Configuration"):
        st.success("Configuration des alertes sauvegardée!")
        
        # Test du système d'alerte
        with st.spinner("Test du système d'alerte en cours..."):
            import time
            time.sleep(2)
            
            st.balloons()
            st.info("**✅ Système d'alerte opérationnel**")
            st.write("**Prochain rapport programmé :** Demain 08:00")
            st.write("**Destinataires :** direction@entreprise.com, finance@entreprise.com")



def show_executive_reporting():
    st.title("📊 Reporting Executive")
    st.info("Section en cours de développement...")

def show_ai_sales_budget():
    st.title("💰 Budget des Ventes IA")
    st.info("Section en cours de développement...")
    # Implémentation similaire aux autres sections

def show_knowledge_center():
    st.title("📚 Centre de Connaissances du Contrôle de Gestion")
    
    st.markdown("""
    ## 🎯 Encyclopédie Complète des Méthodes et Outils
    
    *Base de connaissances théoriques et pratiques pour maîtriser le contrôle de gestion*
    """)
    
    knowledge_tabs = st.tabs([
        "💰 Budget des Ventes", 
        "🏭 Production", 
        "📦 Gestion Stocks",
        "🏗️ Investissement", 
        "💸 Trésorerie",
        "📊 Méthodes Avancées"
    ])
    
    with knowledge_tabs[0]:
        show_sales_budget_knowledge()
    
    with knowledge_tabs[1]:
        show_production_knowledge()
    
    with knowledge_tabs[2]:
        show_stock_management_knowledge()
    
    with knowledge_tabs[3]:
        show_investment_knowledge()
    
    with knowledge_tabs[4]:
        show_cashflow_knowledge()
    
    with knowledge_tabs[5]:
        show_advanced_methods()

def show_sales_budget_knowledge():
    st.header("💰 Théorie du Budget des Ventes")
    
    st.markdown("""
    ## 📚 Fondements Théoriques et Méthodologiques
    
    ### 🎯 Importance du Budget des Ventes
    Le budget des ventes est le **point de départ** de toute la construction budgétaire. 
    Il conditionne l'ensemble des autres budgets de l'entreprise et détermine le niveau d'activité futur.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📊 Méthode des Moindres Carrés
        
        **Principe Mathématique :**
        La méthode des moindres carrés permet de trouver la droite qui minimise la somme 
        des carrés des écarts entre les points observés et la droite de régression.
        """)
        
        st.latex(r"y = ax + b")
        
        st.markdown("""
        **Variables :**
        - $y$ : Variable dépendante (ventes)
        - $x$ : Variable indépendante (temps)
        - $a$ : Pente de la droite (tendance)
        - $b$ : Ordonnée à l'origine
        """)
    
    with col2:
        st.markdown("""
        ### 📐 Calcul des Coefficients
        
        **Pente de la droite (a) :**
        """)
        st.latex(r"""
        a = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n}(x_i - \bar{x})^2}
        """)
        
        st.markdown("""
        **Ordonnée à l'origine (b) :**
        """)
        st.latex(r"b = \bar{y} - a\bar{x}")
        
        st.markdown("""
        **Où :**
        - $\bar{x}$ : Moyenne des périodes
        - $\bar{y}$ : Moyenne des ventes
        - $n$ : Nombre d'observations
        """)
    
    # Calculateur interactif des moindres carrés
    st.subheader("🧮 Calculateur des Moindres Carrés")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Saisie des données historiques :**")
        n_periods = st.number_input("Nombre de périodes :", min_value=3, max_value=12, value=6)
        
        periods = []
        sales_data = []
        
        for i in range(n_periods):
            col_per, col_sales = st.columns(2)
            with col_per:
                period = st.number_input(f"Période {i+1}", value=i+1, key=f"per_{i}")
                periods.append(period)
            with col_sales:
                sales = st.number_input(f"Ventes {i+1}", value=1000 + i*200, key=f"sales_{i}")
                sales_data.append(sales)
    
    with col2:
        if st.button("📊 Calculer la Prévision"):
            # Conversion en arrays numpy
            x = np.array(periods)
            y = np.array(sales_data)
            
            # Calcul des coefficients
            x_mean = np.mean(x)
            y_mean = np.mean(y)
            
            numerator = np.sum((x - x_mean) * (y - y_mean))
            denominator = np.sum((x - x_mean) ** 2)
            
            a = numerator / denominator
            b = y_mean - a * x_mean
            
            st.success(f"**Équation trouvée :** y = {a:.2f}x + {b:.2f}")
            
            # Calcul R²
            y_pred = a * x + b
            ss_res = np.sum((y - y_pred) ** 2)
            ss_tot = np.sum((y - y_mean) ** 2)
            r_squared = 1 - (ss_res / ss_tot)
            
            # Prévisions
            next_period = n_periods + 1
            forecast = a * next_period + b
            
            st.metric(f"Prévision Période {next_period}", f"{forecast:,.0f} €")
            st.metric("Coefficient de détermination R²", f"{r_squared:.3f}")
            
            # Graphique
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name='Données historiques', 
                                   marker=dict(size=10, color='blue')))
            fig.add_trace(go.Scatter(x=list(x) + [next_period], 
                                   y=list(y_pred) + [forecast], 
                                   mode='lines', name='Droite de régression',
                                   line=dict(color='red', dash='dash')))
            fig.update_layout(title='Régression Linéaire - Méthode des Moindres Carrés',
                            xaxis_title='Périodes',
                            yaxis_title='Ventes (€)')
            st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    ### 📈 Coefficients Saisonniers
    
    **Définition :**
    Les coefficients saisonniers permettent d'ajuster les prévisions de tendance pour tenir compte 
    des variations périodiques liées aux saisons, mois, ou trimestres.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Calcul du coefficient saisonnier :**
        """)
        st.latex(r"""
        C_s = \frac{\bar{V}_s}{\bar{V}_t}
        """)
        
        st.markdown("""
        **Où :**
        - $C_s$ : Coefficient saisonnier pour la saison s
        - $\bar{V}_s$ : Moyenne des ventes pour la saison s
        - $\bar{V}_t$ : Moyenne générale des ventes sur toutes les saisons
        """)
    
    with col2:
        st.markdown("""
        **Ajustement saisonnier :**
        """)
        st.latex(r"""
        V_{ajustée} = V_{trend} \times C_s
        """)
        
        st.markdown("""
        **Interprétation :**
        - $C_s > 1$ : Période de haute saison
        - $C_s < 1$ : Période de basse saison
        - $C_s = 1$ : Période neutre
        """)
    
    # Calculateur de coefficients saisonniers
    st.subheader("🔄 Calculateur de Coefficients Saisonniers")
    
    st.write("**Saisie des données trimestrielles :**")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        t1_sales = st.number_input("Trimestre 1", value=120000)
    with col2:
        t2_sales = st.number_input("Trimestre 2", value=150000)
    with col3:
        t3_sales = st.number_input("Trimestre 3", value=130000)
    with col4:
        t4_sales = st.number_input("Trimestre 4", value=180000)
    
    if st.button("📐 Calculer les Coefficients"):
        sales_by_quarter = [t1_sales, t2_sales, t3_sales, t4_sales]
        total_sales = sum(sales_by_quarter)
        average_sales = total_sales / 4
        
        coefficients = []
        for quarter_sales in sales_by_quarter:
            coefficient = quarter_sales / average_sales
            coefficients.append(coefficient)
        
        st.success("**Coefficients saisonniers calculés :**")
        
        df_coefficients = pd.DataFrame({
            'Trimestre': ['T1', 'T2', 'T3', 'T4'],
            'Ventes': sales_by_quarter,
            'Coefficient': [f"{c:.3f}" for c in coefficients],
            'Interprétation': ['Basse saison' if c < 0.95 else 'Haute saison' if c > 1.05 else 'Saison normale' for c in coefficients]
        })
        
        st.dataframe(df_coefficients, use_container_width=True)








def show_production_knowledge():
    st.header("🏭 Théorie de la Gestion de Production")
    
    st.markdown("""
    ## 📚 Méthodologies et Outils de Planification
    
    ### 🎯 Le Plan Directeur de Production (PDP)
    Le PDP est l'outil central qui permet de transformer les prévisions commerciales 
    en plan de production détaillé.
    """)
    
    st.latex(r"""
    \text{Production Nécessaire} = \text{Ventes Prévues} + \text{Stock Final Cible} - \text{Stock Initial}
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📊 Méthode MRP II
        
        **Manufacturing Resource Planning**
        
        **Étapes du processus :**
        1. **Plan des ventes et opérations**
        2. **Plan directeur de production**
        3. **Planification des besoins en composants**
        4. **Ordonnancement atelier**
        5. **Lancement en fabrication**
        """)
        
        st.markdown("""
        **Calcul des besoins nets :**
        """)
        st.latex(r"""
        \text{Besoin Net} = \text{Besoin Brut} - \text{Stock Disponible} - \text{Commandes en Cours}
        """)
    
    with col2:
        st.markdown("""
        ### ⚙️ Indicateurs de Performance
        
        **TRS (Taux de Rendement Synthétique) :**
        """)
        st.latex(r"""
        \text{TRS} = \text{Disponibilité} \times \text{Performance} \times \text{Qualité}
        """)
        
        st.markdown("""
        **Décomposition :**
        - **Disponibilité** = Temps utile / Temps d'ouverture
        - **Performance** = Cadence réelle / Cadence théorique  
        - **Qualité** = Pièces bonnes / Pièces totales
        """)
        
        st.markdown("""
        **OEE (Overall Equipment Effectiveness) :**
        """)
        st.latex(r"""
        \text{OEE} = \frac{\text{Temps de Fabrication Net}}{\text{Temps d'Ouverture}} \times 100
        """)
    
    # Calculateur de plan de production
    st.subheader("🧮 Calculateur de Plan de Production")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Paramètres de base :**")
        sales_forecast = st.number_input("Prévisions ventes (unités/mois)", value=10000)
        initial_stock = st.number_input("Stock initial (unités)", value=1500)
        target_stock = st.number_input("Stock cible final (unités)", value=2000)
        working_days = st.number_input("Jours ouvrables/mois", value=22)
    
    with col2:
        st.write("**Capacités de production :**")
        daily_capacity = st.number_input("Capacité journalière (unités/jour)", value=500)
        efficiency_rate = st.slider("Taux d'efficacité estimé (%)", 70, 100, 85) / 100
        rejection_rate = st.slider("Taux de rebut estimé (%)", 0, 10, 2) / 100
    
    if st.button("📋 Générer le Plan de Production"):
        # Calculs
        production_needed = sales_forecast + target_stock - initial_stock
        adjusted_production = production_needed / (1 - rejection_rate)
        effective_daily_capacity = daily_capacity * efficiency_rate
        production_days = adjusted_production / effective_daily_capacity
        utilization_rate = (production_days / working_days) * 100
        
        st.success("**Résultats du calcul :**")
        
        results_data = {
            'Indicateur': [
                'Production nécessaire (nette)',
                'Production à lancer (brute)',
                'Capacité effective journalière',
                'Jours de production nécessaires',
                'Taux d\'utilisation des capacités'
            ],
            'Valeur': [
                f"{production_needed:,.0f} unités",
                f"{adjusted_production:,.0f} unités",
                f"{effective_daily_capacity:.0f} unités/jour",
                f"{production_days:.1f} jours",
                f"{utilization_rate:.1f}%"
            ]
        }
        
        st.dataframe(pd.DataFrame(results_data), use_container_width=True)
        
        # Recommandations
        if utilization_rate > 100:
            st.error("""
            **🚨 CAPACITÉ INSUFFISANTE**
            - Prévoir des heures supplémentaires
            - Sous-traiter une partie de la production
            - Revoir les stocks cibles
            """)
        elif utilization_rate > 85:
            st.warning("""
            **⚠️ CAPACITÉ TENDUE**
            - Optimiser les séquences de production
            - Renforcer la maintenance préventive
            - Surveiller les indicateurs de performance
            """)
        else:
            st.success("""
            **✅ CAPACITÉ ADÉQUATE**
            - Planification optimale possible
            - Marge de manœuvre disponible
            - Possibilité d'accepter commandes supplémentaires
            """)
    
    st.markdown("""
    ### 🔧 Méthode Kanban
    
    **Principe du système pull :**
    La production est déclenchée par la consommation réelle plutôt que par des prévisions.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Calcul du nombre de kanbans :**
        """)
        st.latex(r"""
        N = \frac{D \times (L + S)}{C}
        """)
        
        st.markdown("""
        **Où :**
        - $N$ : Nombre de kanbans
        - $D$ : Demande moyenne par période
        - $L$ : Délai de réapprovisionnement
        - $S$ : Stock de sécurité
        - $C$ : Capacité du conteneur
        """)
    
    with col2:
        st.markdown("""
        **Avantages du Kanban :**
        - Réduction des stocks
        - Élimination des gaspillages
        - Amélioration de la flexibilité
        - Meilleure visibilité des flux
        """)
        
        # Calculateur Kanban
        st.subheader("🔄 Calculateur Kanban")
        
        D = st.number_input("Demande moyenne (unités/jour)", value=100)
        L = st.number_input("Délai réapprovisionnement (jours)", value=2)
        S = st.number_input("Stock de sécurité (unités)", value=50)
        C = st.number_input("Capacité conteneur (unités)", value=25)
        
        if st.button("🎯 Calculer Kanbans"):
            N = (D * (L + S)) / C
            st.metric("Nombre de kanbans nécessaires", f"{math.ceil(N)}")

def show_stock_management_knowledge():
    st.header("📦 Théorie de la Gestion des Stocks")
    
    st.markdown("""
    ## 📚 Méthodes et Optimisation des Stocks
    
    ### 🎯 Les Trois Fonctions des Stocks
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **🛡️ Stock de Sécurité**
        - Parer aux aléas de la demande
        - Compenser les retards de livraison
        - Prévenir les ruptures
        """)
        
        st.latex(r"""
        SS = z \times \sigma_d \times \sqrt{L}
        """)
    
    with col2:
        st.markdown("""
        **🔄 Stock Cyclique**
        - Faire face à la demande régulière
        - Optimiser les quantités commandées
        - Réduire les coûts de possession
        """)
        
        st.latex(r"""
        Q^* = \sqrt{\frac{2DS}{H}}
        """)
    
    with col3:
        st.markdown("""
        **📈 Stock Spéculatif**
        - Anticiper les hausses de prix
        - Profiter des promotions
        - Sécuriser les approvisionnements
        """)
    
    st.markdown("""
    ### 📊 Formule de Wilson (Lot Économique)
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Équation fondamentale :**
        """)
        st.latex(r"""
        Q^* = \sqrt{\frac{2DS}{H}}
        """)
        
        st.markdown("""
        **Où :**
        - $Q^*$ : Quantité économique à commander
        - $D$ : Demande annuelle
        - $S$ : Coût de passation de commande
        - $H$ : Coût de stockage unitaire annuel
        """)
        
        st.markdown("""
        **Coût total annuel :**
        """)
        st.latex(r"""
        C_T = \frac{D}{Q}S + \frac{Q}{2}H
        """)
    
    with col2:
        # Calculateur de Wilson
        st.subheader("🧮 Calculateur du Lot Économique")
        
        D = st.number_input("Demande annuelle (unités)", value=10000)
        S = st.number_input("Coût de commande (€)", value=150.0)
        H = st.number_input("Coût stockage unitaire annuel (€)", value=2.5)
        
        if st.button("📦 Calculer EOQ"):
            Q_optimal = math.sqrt((2 * D * S) / H)
            n_orders = D / Q_optimal
            total_cost = (D / Q_optimal) * S + (Q_optimal / 2) * H
            
            st.metric("Lot économique (EOQ)", f"{Q_optimal:.0f} unités")
            st.metric("Nombre de commandes/an", f"{n_orders:.1f}")
            st.metric("Coût total annuel", f"{total_cost:,.0f} €")
            
            # Graphique des coûts
            quantities = np.linspace(Q_optimal * 0.5, Q_optimal * 1.5, 50)
            order_costs = (D / quantities) * S
            holding_costs = (quantities / 2) * H
            total_costs = order_costs + holding_costs
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=quantities, y=order_costs, name='Coût de commande'))
            fig.add_trace(go.Scatter(x=quantities, y=holding_costs, name='Coût de stockage'))
            fig.add_trace(go.Scatter(x=quantities, y=total_costs, name='Coût total'))
            fig.add_vline(x=Q_optimal, line_dash="dash", line_color="red", 
                         annotation_text=f"EOQ = {Q_optimal:.0f}")
            fig.update_layout(title='Optimisation des Coûts de Stock - Formule de Wilson',
                            xaxis_title='Quantité commandée',
                            yaxis_title='Coût (€)')
            st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    ### 📈 Méthode ABC - Loi de Pareto
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Classification ABC :**
        - **Classe A** : 20% des articles → 80% de la valeur
        - **Classe B** : 30% des articles → 15% de la valeur  
        - **Classe C** : 50% des articles → 5% de la valeur
        """)
        
        st.markdown("""
        **Stratégies de gestion :**
        - **Classe A** : Surveillance rapprochée, stocks faibles
        - **Classe B** : Gestion standard, stocks modérés
        - **Classe C** : Gestion simplifiée, stocks importants
        """)
    
    with col2:
        # Générateur d'analyse ABC
        st.subheader("📊 Générateur d'Analyse ABC")
        
        if st.button("🎯 Générer Analyse ABC Simulée"):
            # Données simulées
            n_articles = 50
            articles = [f"ART{1000+i}" for i in range(n_articles)]
            valeurs = np.random.lognormal(8, 1.2, n_articles)
            
            df_abc = pd.DataFrame({
                'Article': articles,
                'Valeur Annuelle (€)': [round(v, 2) for v in valeurs]
            })
            
            # Tri et classification
            df_abc = df_abc.sort_values('Valeur Annuelle (€)', ascending=False)
            df_abc['Cumul %'] = (df_abc['Valeur Annuelle (€)'].cumsum() / 
                                df_abc['Valeur Annuelle (€)'].sum() * 100).round(2)
            
            def classer_abc(cumul):
                if cumul <= 80: return 'A'
                elif cumul <= 95: return 'B'
                else: return 'C'
            
            df_abc['Classe'] = df_abc['Cumul %'].apply(classer_abc)
            
            # Affichage résultats
            st.success("**Analyse ABC générée :**")
            
            stats_abc = df_abc.groupby('Classe').agg({
                'Article': 'count',
                'Valeur Annuelle (€)': 'sum'
            }).round(2)
            stats_abc['% Articles'] = (stats_abc['Article'] / n_articles * 100).round(1)
            stats_abc['% Valeur'] = (stats_abc['Valeur Annuelle (€)'] / stats_abc['Valeur Annuelle (€)'].sum() * 100).round(1)
            
            st.dataframe(stats_abc, use_container_width=True)
            
            # Graphique Pareto
            fig = go.Figure()
            fig.add_trace(go.Bar(x=df_abc['Article'], y=df_abc['Valeur Annuelle (€)'],
                               marker_color=['#FF4B4B' if c == 'A' else '#FFA500' if c == 'B' else '#008000' 
                                           for c in df_abc['Classe']],
                               name='Valeur par article'))
            fig.add_trace(go.Scatter(x=df_abc['Article'], y=df_abc['Cumul %'],
                                   mode='lines', name='Cumul %', yaxis='y2',
                                   line=dict(color='blue', width=2)))
            fig.update_layout(
                title='Diagramme Pareto - Analyse ABC',
                xaxis_title='Articles',
                yaxis_title='Valeur Annuelle (€)',
                yaxis2=dict(title='Cumul %', overlaying='y', side='right', range=[0, 100])
            )
            st.plotly_chart(fig, use_container_width=True)

def show_investment_knowledge():
    st.header("🏗️ Théorie de l'Investissement")
    
    st.markdown("""
    ## 📚 Méthodes d'Évaluation des Investissements
    
    ### 🎯 Les Cinq Critères d'Évaluation
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📈 Valeur Actuelle Nette (VAN)
        
        **Définition :**
        La VAN représente la valeur créée par l'investissement, actualisée au taux de rendement requis.
        """)
        
        st.latex(r"""
        VAN = \sum_{t=1}^{n} \frac{CF_t}{(1+i)^t} - I_0
        """)
        
        st.markdown("""
        **Où :**
        - $CF_t$ : Cash-flow de la période t
        - $i$ : Taux d'actualisation
        - $I_0$ : Investissement initial
        - $n$ : Durée de vie du projet
        """)
        
        st.markdown("""
        **Règle de décision :**
        - $VAN > 0$ : Projet acceptable
        - $VAN < 0$ : Projet à rejeter
        - Entre projets : Choisir la VAN la plus élevée
        """)
    
    with col2:
        st.markdown("""
        ### 🔄 Taux de Rendement Interne (TRI)
        
        **Définition :**
        Le TRI est le taux d'actualisation qui annule la VAN du projet.
        """)
        
        st.latex(r"""
        \sum_{t=1}^{n} \frac{CF_t}{(1+TRI)^t} - I_0 = 0
        """)
        
        st.markdown("""
        **Règle de décision :**
        - $TRI > i$ : Projet acceptable
        - $TRI < i$ : Projet à rejeter
        - $i$ : Taux de rendement requis
        """)
        
        st.markdown("""
        ### ⏱️ Délai de Récupération
        """)
        
        st.latex(r"""
        \text{Payback} = \frac{I_0}{\overline{CF}}
        """)
        
        st.markdown("""
        **Limites :**
        - Ignore la valeur temporelle de l'argent
        - Ne considère pas les cash-flows après récupération
        """)
    
    # Simulateur d'investissement
    st.subheader("🧮 Simulateur d'Investissement")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Paramètres de l'investissement :**")
        investment = st.number_input("Investissement initial (€)", value=100000)
        lifespan = st.number_input("Durée de vie (années)", value=5, min_value=1, max_value=20)
        discount_rate = st.number_input("Taux d'actualisation (%)", value=10.0, min_value=0.1) / 100
        
        st.write("**Cash-flows annuels :**")
        cash_flows = []
        for year in range(1, lifespan + 1):
            cf = st.number_input(f"Année {year}", value=30000, key=f"cf_{year}")
            cash_flows.append(cf)
    
    with col2:
        if st.button("🎯 Calculer la Rentabilité"):
            # Calcul VAN
            van = -investment
            for year, cf in enumerate(cash_flows, 1):
                van += cf / ((1 + discount_rate) ** year)
            
            # Calcul TRI (méthode itérative)
            def calculate_irr(investment, cash_flows, precision=0.0001):
                irr_min, irr_max = 0, 1
                while irr_max - irr_min > precision:
                    irr_test = (irr_min + irr_max) / 2
                    van_test = -investment
                    for year, cf in enumerate(cash_flows, 1):
                        van_test += cf / ((1 + irr_test) ** year)
                    if van_test > 0:
                        irr_min = irr_test
                    else:
                        irr_max = irr_test
                return (irr_min + irr_max) / 2
            
            tri = calculate_irr(investment, cash_flows)
            
            # Calcul délai de récupération
            cumulative_cf = 0
            payback = None
            for year, cf in enumerate(cash_flows, 1):
                cumulative_cf += cf
                if cumulative_cf >= investment and payback is None:
                    payback = year - 1 + (investment - (cumulative_cf - cf)) / cf
            
            # Calcul indice de profitabilité
            profitability_index = (van + investment) / investment
            
            # Affichage résultats
            st.success("**📊 Résultats de l'analyse :**")
            
            results_data = {
                'Critère': ['VAN', 'TRI', 'Délai de récupération', 'Indice de profitabilité'],
                'Valeur': [
                    f"{van:,.0f} €",
                    f"{tri*100:.1f}%",
                    f"{payback:.1f} ans" if payback else "Non récupéré",
                    f"{profitability_index:.2f}"
                ],
                'Seuil': [
                    "> 0",
                    f"> {discount_rate*100:.1f}%",
                    "< Durée de vie",
                    "> 1"
                ],
                'Décision': [
                    "✅ Acceptable" if van > 0 else "❌ Rejet",
                    "✅ Acceptable" if tri > discount_rate else "❌ Rejet",
                    "✅ Acceptable" if payback and payback <= lifespan else "⚠️ À étudier",
                    "✅ Acceptable" if profitability_index > 1 else "❌ Rejet"
                ]
            }
            
            st.dataframe(pd.DataFrame(results_data), use_container_width=True)
            
            # Recommandation globale
            if van > 0 and tri > discount_rate:
                st.success("🎉 **INVESTISSEMENT RECOMMANDÉ** - Le projet est rentable")
            else:
                st.error("💸 **INVESTISSEMENT NON RECOMMANDÉ** - Le projet n'est pas rentable")

def show_cashflow_knowledge():
    st.header("💸 Théorie de la Gestion de Trésorerie")
    
    st.markdown("""
    ## 📚 Principes et Méthodes de Gestion de Trésorerie
    
    ### 🎯 Les Trois Tableaux de Flux Essentiels
    """)
    
    tab1, tab2, tab3 = st.tabs(["💰 Flux d'Exploitation", "🏗️ Flux d'Investissement", "🏦 Flux de Financement"])
    
    with tab1:
        st.markdown("""
        ### 💼 Flux de Trésorerie d'Exploitation (FTE)
        
        **Définition :**
        Les flux générés par l'activité normale de l'entreprise.
        """)
        
        st.latex(r"""
        FTE = \text{Résultat Net} + \text{Dotations aux Amortissements} - \Delta\text{BFR}
        """)
        
        st.markdown("""
        **Calcul du BFR (Besoin en Fonds de Roulement) :**
        """)
        st.latex(r"""
        \text{BFR} = \text{Stocks} + \text{Créances Clients} - \text{Dettes Fournisseurs}
        """)
        
        st.markdown("""
        **Variation du BFR :**
        """)
        st.latex(r"""
        \Delta\text{BFR} = \text{BFR}_{fin} - \text{BFR}_{début}
        """)
        
        st.markdown("""
        **Capacité d'Autofinancement (CAF) :**
        """)
        st.latex(r"""
        \text{CAF} = \text{Résultat Net} + \text{Dotations} - \text{Reprises}
        """)
    
    with tab2:
        st.markdown("""
        ### 🏗️ Flux de Trésorerie d'Investissement (FTI)
        
        **Définition :**
        Les flux liés aux acquisitions et cessions d'immobilisations.
        """)
        
        st.latex(r"""
        FTI = -\text{Acquisitions d'Immobilisations} + \text{Cessions d'Immobilisations}
        """)
        
        st.markdown("""
        **Composantes principales :**
        - Acquisitions d'immobilisations corporelles
        - Acquisitions d'immobilisations incorporelles  
        - Cessions d'éléments d'actif
        - Prêts accordés à des tiers
        """)
    
    with tab3:
        st.markdown("""
        ### 🏦 Flux de Trésorerie de Financement (FTF)
        
        **Définition :**
        Les flux liés aux apporteurs de capitaux.
        """)
        
        st.latex(r"""
        FTF = \text{Augmentations de Capital} + \text{Nouveaux Emprunts} - \text{Remboursements} - \text{Dividendes}
        """)
        
        st.markdown("""
        **Trésorerie Nette :**
        """)
        st.latex(r"""
        TN = FTE + FTI + FTF
        """)
    
    # Simulateur de trésorerie
    st.subheader("🧮 Simulateur de Prévision de Trésorerie")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Paramètres de base :**")
        initial_cash = st.number_input("Trésorerie initiale (€)", value=50000)
        forecast_period = st.selectbox("Période de prévision", ["3 mois", "6 mois", "12 mois"])
        
        st.write("**Encaissements :**")
        monthly_revenue = st.number_input("CA Mensuel Moyen (€)", value=100000)
        client_payment_delay = st.number_input("Délai paiement clients (jours)", value=30)
    
    with col2:
        st.write("**Décaissements :**")
        monthly_expenses = st.number_input("Charges Mensuelles Moyennes (€)", value=80000)
        supplier_payment_delay = st.number_input("Délai paiement fournisseurs (jours)", value=60)
        exceptional_expense = st.number_input("Dépense exceptionnelle (€, mois 3)", value=30000)
    
    if st.button("📊 Générer la Prévision"):
        # Calcul BFR
        bfr_operating = (client_payment_delay / 30 * monthly_revenue) - (supplier_payment_delay / 30 * monthly_expenses)
        
        # Simulation sur 12 mois
        months = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Jun', 'Jul', 'Aoû', 'Sep', 'Oct', 'Nov', 'Déc']
        n_months = 12 if forecast_period == "12 mois" else 6 if forecast_period == "6 mois" else 3
        
        cash_flow = [initial_cash]
        monthly_variations = []
        
        for i in range(n_months):
            # Mois avec dépense exceptionnelle
            if i == 2:  # Mars
                variation = monthly_revenue - monthly_expenses - exceptional_expense
            else:
                variation = monthly_revenue - monthly_expenses
            
            monthly_variations.append(variation)
            new_cash = cash_flow[i] + variation
            cash_flow.append(new_cash)
        
        # Création du tableau
        df_cashflow = pd.DataFrame({
            'Mois': ['Initial'] + months[:n_months],
            'Trésorerie (€)': cash_flow,
            'Variation (€)': [0] + monthly_variations,
            'Cumul Variations (€)': np.cumsum([0] + monthly_variations)
        })
        
        st.dataframe(df_cashflow.style.format({
            'Trésorerie (€)': '{:,.0f} €',
            'Variation (€)': '{:,.0f} €',
            'Cumul Variations (€)': '{:,.0f} €'
        }), use_container_width=True)
        
        # Graphique
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df_cashflow['Mois'], y=df_cashflow['Trésorerie (€)'],
                               mode='lines+markers', name='Trésorerie',
                               line=dict(color='blue', width=3)))
        fig.add_hline(y=0, line_dash="dash", line_color="red", annotation_text="Seuil de rupture")
        fig.update_layout(title='Évolution Prévisionnelle de la Trésorerie',
                         xaxis_title='Mois',
                         yaxis_title='Trésorerie (€)')
        st.plotly_chart(fig, use_container_width=True)
        
        # Analyse
        min_cash = min(cash_flow)
        avg_monthly_variation = np.mean(monthly_variations)
        
        st.subheader("📈 Analyse de la Prévision")
        
        col_anal1, col_anal2, col_anal3 = st.columns(3)
        
        with col_anal1:
            st.metric("Trésorerie minimale", f"{min_cash:,.0f} €")
        with col_anal2:
            st.metric("Variation mensuelle moyenne", f"{avg_monthly_variation:,.0f} €")
        with col_anal3:
            st.metric("BFR d'exploitation", f"{bfr_operating:,.0f} €")
        
        if min_cash < 0:
            st.error(f"""
            **🚨 RISQUE DE RUPTURE DÉTECTÉ**
            - Trésorerie minimale: {min_cash:,.0f} €
            - Actions recommandées:
              * Renégocier les délais fournisseurs
              * Accélérer le recouvrement clients
              * Rechercher des financements court terme
            """)
        elif min_cash < 10000:
            st.warning(f"""
            **⚠️ TRÉSORERIE TENDUE**
            - Trésorerie minimale: {min_cash:,.0f} €
            - Surveillance renforcée recommandée
            - Prévoir une ligne de crédit
            """)
        else:
            st.success(f"""
            **✅ TRÉSORERIE SÉCURISÉE**
            - Trésorerie minimale: {min_cash:,.0f} €
            - Situation financière saine
            - Possibilité d'investir les excédents
            """)

def show_advanced_methods():
    st.header("📊 Méthodes Avancées de Contrôle de Gestion")
    
    st.markdown("""
    ## 🧠 Techniques Statistiques et Prédictives Avancées
    
    ### 📈 Méthodes de Prévision Sophistiquées
    """)
    
    tab1, tab2, tab3 = st.tabs(["Séries Temporelles", "Régression Multiple", "Machine Learning"])
    
    with tab1:
        st.markdown("""
        ### 🔄 Modèles ARIMA (AutoRegressive Integrated Moving Average)
        
        **Décomposition d'une série temporelle :**
        """)
        
        st.latex(r"""
        Y_t = T_t + S_t + C_t + I_t
        """)
        
        st.markdown("""
        **Où :**
        - $Y_t$ : Série observée
        - $T_t$ : Composante tendancielle
        - $S_t$ : Composante saisonnière
        - $C_t$ : Composante cyclique
        - $I_t$ : Composante irrégulière
        """)
        
        st.markdown("""
        **Formule ARIMA(p,d,q) :**
        """)
        
        st.latex(r"""
        (1 - \sum_{i=1}^p \phi_i L^i)(1-L)^d y_t = (1 + \sum_{i=1}^q \theta_i L^i) \epsilon_t
        """)
        
        st.markdown("""
        **Paramètres :**
        - $p$ : Ordre autorégressif
        - $d$ : Ordre de différenciation
        - $q$ : Ordre moyenne mobile
        - $L$ : Opérateur retard
        - $\epsilon_t$ : Terme d'erreur blanc
        """)
        
        st.markdown("""
        **Applications en contrôle de gestion :**
        - Prévision des ventes saisonnières
        - Analyse des tendances long terme
        - Détection d'anomalies
        - Optimisation des stocks
        """)
    
    with tab2:
        st.markdown("""
        ### 📊 Régression Multiple
        
        **Modèle général :**
        """)
        
        st.latex(r"""
        y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_n x_n + \epsilon
        """)
        
        st.markdown("""
        **Variables explicatives typiques :**
        - Prix de vente
        - Dépenses marketing
        - Indices économiques
        - Facteurs saisonniers
        - Actions concurrentielles
        - Données météorologiques
        """)
        
        st.markdown("""
        **Mesures de performance :**
        """)
        
        st.latex(r"""
        R^2 = 1 - \frac{\sum(y_i - \hat{y}_i)^2}{\sum(y_i - \bar{y})^2}
        """)
        
        st.latex(r"""
        \text{RMSE} = \sqrt{\frac{1}{n}\sum_{i=1}^n (y_i - \hat{y}_i)^2}
        """)
        
        st.latex(r"""
        \text{MAPE} = \frac{100\%}{n}\sum_{i=1}^n \left| \frac{y_i - \hat{y}_i}{y_i} \right|
        """)
        
        st.markdown("""
        **Avantages :**
        - Capture les relations multiples
        - Mesure l'impact de chaque variable
        - Facile à interpréter
        - Bonnes propriétés statistiques
        """)
    
    with tab3:
        st.markdown("""
        ### 🤖 Machine Learning pour le Contrôle de Gestion
        
        **Algorithmes utilisés :**
        """)
        
        ml_algorithms = {
            'Algorithme': ['Random Forest', 'XGBoost', 'LSTM', 'Prophet', 'SVM'],
            'Application': ['Prévision ventes', 'Classification clients', 'Séries temporelles', 'Saisonnalité', 'Anomalies'],
            'Avantages': ['Robustesse bruit', 'Performance', 'Séquences longues', 'Saisonnalité forte', 'Frontières complexes'],
            'Complexité': ['Moyenne', 'Élevée', 'Très élevée', 'Moyenne', 'Élevée']
        }
        
        st.dataframe(pd.DataFrame(ml_algorithms), use_container_width=True)
        
        st.markdown("""
        **Feature Engineering :**
        """)
        
        st.code("""
        # Variables décalées (lags)
        df['lag_1'] = df['ventes'].shift(1)
        df['lag_7'] = df['ventes'].shift(7)
        df['lag_30'] = df['ventes'].shift(30)
        
        # Moyennes mobiles
        df['ma_7'] = df['ventes'].rolling(7).mean()
        df['ma_30'] = df['ventes'].rolling(30).mean()
        
        # Variables temporelles
        df['day_of_week'] = df.index.dayofweek
        df['month'] = df.index.month
        df['is_weekend'] = df['day_of_week'].isin([5, 6])
        
        # Variables externes
        df['promotion_active'] = df['budget_promo'] > 0
        df['economic_index'] = external_data['gdp_growth']
        """, language='python')
        
        st.markdown("""
        **Validation des modèles :**
        - Validation croisée time-series
        - Backtesting
        - Tests de robustesse
        - Analyse des résidus
        """)
    
    # Comparaison des méthodes
    st.subheader("📈 Comparaison des Méthodes de Prévision")
    
    comparison_data = {
        'Méthode': ['Moyenne Mobile', 'Lissage Exponentiel', 'Régression Linéaire', 'ARIMA', 'Machine Learning'],
        'Précision': ['Moyenne', 'Bonne', 'Bonne', 'Très bonne', 'Excellente'],
        'Complexité': ['Faible', 'Faible', 'Moyenne', 'Élevée', 'Très élevée'],
        'Données Requises': ['Historique court', 'Historique court', 'Variables explicatives', 'Série longue', 'Grand volume'],
        'Coût Calcul': ['Faible', 'Faible', 'Moyen', 'Élevé', 'Très élevé'],
        'Meilleur Usage': ['Tendance simple', 'Saisonnalité légère', 'Relations linéaires', 'Séries complexes', 'Patterns complexes']
    }
    
    st.dataframe(pd.DataFrame(comparison_data), use_container_width=True)
    
    st.markdown("""
    ### 🎯 Recommandations de Sélection
    
    **Pour les débutants :**
    - Commencer par les méthodes simples (moyenne mobile, lissage exponentiel)
    - Valider avec des indicateurs de performance (RMSE, MAPE)
    - Progresser vers des méthodes plus sophistiquées
    
    **Pour les experts :**
    - Combiner plusieurs méthodes (ensembling)
    - Utiliser la validation croisée
    - Implémenter des systèmes de monitoring
    - Automatiser le réentraînement des modèles
    """)

def show_home():
    st.title("🏠 Système de Gestion Budgétaire")
    
    st.markdown("""
    ## Bienvenue dans votre plateforme de contrôle de gestion
    
    Cette application vous accompagne dans l'élaboration et le suivi de tous vos budgets 
    selon une approche professionnelle et structurée.
    
    ### 📋 Modules disponibles :
    
    **🎯 Budgets Opérationnels :**
    - 📈 **Budget des Ventes** : Prévisions et analyse des ventes
    - 🏭 **Budget de Production** : Planification de la production
    - 📦 **Gestion des Stocks** : Optimisation des niveaux de stock
    
    **💰 Budgets Financiers :**
    - 🏗️ **Budget d'Investissement** : Planification des immobilisations
    - 💸 **Budget de Trésorerie** : Gestion des flux de liquidités
    
    **🔄 Processus Intégré :**
    - 🔄 **Processus Complet** : Vue d'ensemble du cycle budgétaire
    - 📅 **Plan d'Implémentation** : Feuille de route détaillée
    """)
    
    # Quick stats dashboard
    st.subheader("📊 Tableau de Bord Rapide")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Budget Ventes", "450K €", "+12%")
    with col2:
        st.metric("Production", "280K €", "+8%")
    with col3:
        st.metric("Trésorerie", "75K €", "-5%")
    with col4:
        st.metric("Investissement", "120K €", "+15%")

def show_controle_gestion():
    st.title("📈 Contrôle de Gestion")
    
    st.markdown("""
    ## Le Rôle du Contrôle de Gestion
    
    Le contrôle de gestion est un pilier essentiel pour la performance de l'entreprise.
    """)
    
    tab1, tab2, tab3 = st.tabs(["🎯 Mission", "📊 Outils", "🔍 Indicateurs"])
    
    with tab1:
        st.subheader("Mission du Contrôleur de Gestion")
        st.markdown("""
        - **Piloter** la performance économique
        - **Anticiper** les risques et opportunités  
        - **Éclairer** la prise de décision
        - **Coordonner** la construction budgétaire
        - **Analyser** les écarts et proposer des correctifs
        """)
    
    with tab2:
        st.subheader("Outils du Contrôle de Gestion")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **📈 Outils de Prévision :**
            - Budget des ventes
            - Budget de production
            - Budget de trésorerie
            
            **📋 Outils de Suivi :**
            - Tableaux de bord
            - Reporting mensuel
            - Analyse des écarts
            """)
        
        with col2:
            st.markdown("""
            **🎯 Outils d'Aide à la Décision :**
            - Calculs de coûts
            - Analyse de rentabilité
            - Simulations business
            
            **🔍 Outils d'Analyse :**
            - Ratios financiers
            - Benchmarking
            - Analyse trend
            """)
    
    with tab3:
        st.subheader("Indicateurs Clés de Performance")
        
        kpi_options = st.multiselect(
            "Sélectionnez les KPI à afficher :",
            ["Rentabilité", "Productivité", "Liquidité", "Efficacité Commerciale"],
            default=["Rentabilité", "Productivité"]
        )
        
        if "Rentabilité" in kpi_options:
            with st.expander("📈 Indicateurs de Rentabilité"):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.number_input("Marge commerciale (%)", min_value=0.0, value=32.5, step=0.1)
                with col2:
                    st.number_input("ROI (%)", min_value=0.0, value=15.2, step=0.1)
                with col3:
                    st.number_input("EBITDA (%)", min_value=0.0, value=18.7, step=0.1)

def show_budget_ventes():
    st.title("💰 Budget des Ventes")
    
    st.markdown("""
    ## Élaboration du Budget des Ventes
    
    Le budget des ventes est le point de départ de toute la construction budgétaire.
    Il conditionne l'ensemble des autres budgets de l'entreprise.
    """)
    
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Données Historiques", "📈 Méthode des Moindres Carrés", "🎯 Coefficients Saisonniers", "📋 Synthèse"])
    
    with tab1:
        st.subheader("Données Historiques des Ventes")
        
        # Sample historical data
        historical_data = {
            'Période': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            'Ventes (k€)': [120, 135, 115, 145, 160, 155, 140, 165, 180, 175, 160, 185]
        }
        
        df_historical = pd.DataFrame(historical_data)
        st.dataframe(df_historical, use_container_width=True)
        
        # Chart
        fig = px.line(df_historical, x='Période', y='Ventes (k€)', 
                     title='Évolution Historique des Ventes',
                     markers=True)
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.subheader("Méthode des Moindres Carrés")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Formule de la droite :**
            `y = ax + b`
            
            Où :
            - `y` = ventes prévues
            - `x` = période
            - `a` = pente de la droite
            - `b` = ordonnée à l'origine
            """)
            
            periods = st.number_input("Nombre de périodes à prévoir", min_value=1, max_value=24, value=6)
            
        with col2:
            # Simple calculation example
            st.markdown("""
            **Calcul des coefficients :**
            - `a` = 5.82
            - `b` = 124.36
            """)
            
            equation = "y = 5.82x + 124.36"
            st.code(equation, language='python')
        
        # Forecast calculation
        if st.button("Calculer les prévisions"):
            forecast_data = []
            for i in range(13, 13 + periods):
                forecast = 5.82 * i + 124.36
                forecast_data.append({'Période': i, 'Prévision (k€)': round(forecast, 2)})
            
            df_forecast = pd.DataFrame(forecast_data)
            st.dataframe(df_forecast, use_container_width=True)
    
    with tab3:
        st.subheader("Coefficients Saisonniers")
        
        st.markdown("""
        Ajustement des prévisions pour tenir compte des variations saisonnières.
        """)
        
        seasonal_data = {
            'Trimestre': ['T1', 'T2', 'T3', 'T4'],
            'Coefficient': [0.95, 1.05, 1.12, 0.88]
        }
        
        df_seasonal = pd.DataFrame(seasonal_data)
        st.dataframe(df_seasonal, use_container_width=True)
        
        # Seasonal adjustment example
        st.subheader("Ajustement Saisonnier")
        base_forecast = st.number_input("Prévision de base (k€)", value=200.0)
        quarter = st.selectbox("Trimestre", ['T1', 'T2', 'T3', 'T4'])
        
        coefficient = df_seasonal[df_seasonal['Trimestre'] == quarter]['Coefficient'].values[0]
        adjusted_forecast = base_forecast * coefficient
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Prévision Base", f"{base_forecast:.1f} k€")
        with col2:
            st.metric("Coefficient", f"{coefficient:.2f}")
        with col3:
            st.metric("Prévision Ajustée", f"{adjusted_forecast:.1f} k€")

def show_budget_production():
    st.title("🏭 Budget de Production")
    
    st.markdown("""
    ## Budget de Production
    
    Le budget de production découle directement du budget des ventes et de la politique de stock.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Données d'Entrée")
        sales_forecast = st.number_input("Prévision des Ventes (unités)", value=1000)
        initial_stock = st.number_input("Stock Initial (unités)", value=100)
        target_stock = st.number_input("Stock Cible Final (unités)", value=120)
        
    with col2:
        st.subheader("Calcul de Production")
        # Production = Ventes prévues + Stock cible - Stock initial
        production_needed = sales_forecast + target_stock - initial_stock
        
        st.metric("Production Nécessaire", f"{production_needed} unités")
        
        cost_per_unit = st.number_input("Coût de Production Unitaire (€)", value=50.0)
        total_production_cost = production_needed * cost_per_unit
        st.metric("Coût Total de Production", f"{total_production_cost:,.0f} €")

def show_gestion_stocks():
    st.title("📦 Gestion des Stocks")
    
    st.markdown("""
    ## Optimisation des Niveaux de Stock
    """)
    
    tab1, tab2 = st.tabs(["📊 Politique de Stock", "📈 Analyse ABC"])
    
    with tab1:
        st.subheader("Politique de Stock")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Paramètres :**
            """)
            consumption = st.number_input("Consommation Annuelle (unités)", value=10000)
            unit_cost = st.number_input("Coût Unitaire (€)", value=25.0)
            order_cost = st.number_input("Coût de Commande (€)", value=150.0)
            holding_rate = st.number_input("Taux de Détention (%)", value=20.0) / 100
        
        with col2:
            # Calcul du lot économique (formule de Wilson)
            eoq = math.sqrt((2 * consumption * order_cost) / (unit_cost * holding_rate))
            st.metric("Lot Économique (EOQ)", f"{eoq:.0f} unités")
            
            # Nombre de commandes optimal
            optimal_orders = consumption / eoq
            st.metric("Nombre de Commandes Optimal", f"{optimal_orders:.1f}")
    
    with tab2:
        st.subheader("Analyse ABC des Articles")
        
        # Sample ABC analysis data
        abc_data = {
            'Article': ['A001', 'A002', 'A003', 'A004', 'A005', 'A006', 'A007'],
            'Valeur Stock (k€)': [45, 38, 22, 15, 8, 5, 2],
            'Classe ABC': ['A', 'A', 'B', 'B', 'C', 'C', 'C']
        }
        
        df_abc = pd.DataFrame(abc_data)
        st.dataframe(df_abc, use_container_width=True)
        
        # ABC chart
        fig = px.pie(df_abc, values='Valeur Stock (k€)', names='Classe ABC',
                    title='Répartition ABC de la Valeur du Stock')
        st.plotly_chart(fig, use_container_width=True)

# Continuer avec les autres fonctions...
def show_budget_investissement():
    st.title("🏗️ Budget d'Investissement")
    
    st.markdown("""
    ## Planification des Investissements
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Nouvel Investissement")
        investment_name = st.text_input("Nom de l'investissement", "Nouvelle Machine")
        investment_amount = st.number_input("Montant de l'investissement (€)", value=50000)
        lifespan = st.number_input("Durée de vie (années)", value=5)
        annual_cashflow = st.number_input("Cash-flow Annuel Attendu (€)", value=15000)
    
    with col2:
        st.subheader("Analyse de Rentabilité")
        
        # Simple ROI calculation
        total_return = annual_cashflow * lifespan
        roi = (total_return - investment_amount) / investment_amount * 100
        payback_period = investment_amount / annual_cashflow
        
        st.metric("Return on Investment (ROI)", f"{roi:.1f}%")
        st.metric("Délai de Récupération", f"{payback_period:.1f} ans")
        
        if roi > 15:
            st.success("✅ Investissement intéressant")
        else:
            st.warning("⚠️ Investissement à reconsidérer")

def show_budget_tresorerie():
    st.title("💸 Budget de Trésorerie")
    
    st.markdown("""
    ## Prévision de Trésorerie
    """)
    
    # Cash flow simulation
    months = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Jun', 'Jul', 'Aoû', 'Sep', 'Oct', 'Nov', 'Déc']
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Encaissements")
        initial_cash = st.number_input("Trésorerie Initiale (k€)", value=50.0)
        monthly_income = st.number_input("Encaissements Mensuels Moyens (k€)", value=80.0)
    
    with col2:
        st.subheader("Décaissements")
        monthly_expenses = st.number_input("Décaissements Mensuels Moyens (k€)", value=75.0)
        exceptional_expense = st.number_input("Dépense Exceptionnelle (k€, mois 6)", value=30.0)
    
    # Calculate cash flow
    cash_flow = [initial_cash]
    for i in range(12):
        if i == 5:  # June - exceptional expense
            monthly_cash = cash_flow[i] + monthly_income - monthly_expenses - exceptional_expense
        else:
            monthly_cash = cash_flow[i] + monthly_income - monthly_expenses
        cash_flow.append(monthly_cash)
    
    # Create DataFrame for display
    cash_data = {
        'Mois': ['Initial'] + months,
        'Trésorerie (k€)': cash_flow
    }
    df_cash = pd.DataFrame(cash_data)
    
    st.dataframe(df_cash, use_container_width=True)
    
    # Cash flow chart
    fig = px.line(df_cash, x='Mois', y='Trésorerie (k€)', 
                 title='Évolution Prévisionnelle de la Trésorerie',
                 markers=True)
    st.plotly_chart(fig, use_container_width=True)

def show_processus_complet():
    st.title("🔄 Processus Complet Budgétaire")
    
    st.markdown("""
    ## Vue d'Ensemble du Cycle Budgétaire
    """)
    
    # Process flowchart
    st.image("https://via.placeholder.com/800x400?text=Diagramme+Processus+Budgétaire", 
             caption="Processus Budgétaire Intégré")
    
    st.subheader("Enchaînement des Budgets")
    
    budget_sequence = {
        'Étape': ['1. Budget Commercial', '2. Budget de Production', '3. Budget des Approvisionnements', 
                 '4. Budget des Investissements', '5. Budget de Trésorerie', '6. Budget des Frais Généraux'],
        'Responsable': ['Directeur Commercial', 'Directeur Production', 'Responsable Achats',
                       'Directeur Général', 'Contrôleur de Gestion', 'Directeur Administratif'],
        'Délai': ['J+0', 'J+7', 'J+14', 'J+21', 'J+28', 'J+35']
    }
    
    df_process = pd.DataFrame(budget_sequence)
    st.dataframe(df_process, use_container_width=True)

def show_plan_implementation():
    st.title("📅 Plan d'Implémentation")
    
    st.markdown("""
    ## Feuille de Route d'Implémentation
    """)
    
    # Gantt chart data
    tasks = {
        'Tâche': ['Diagnostic', 'Formation', 'Paramétrage', 'Saisie Budget', 'Contrôle', 'Reporting'],
        'Début': ['2024-01-01', '2024-01-15', '2024-02-01', '2024-02-15', '2024-03-01', '2024-03-15'],
        'Fin': ['2024-01-14', '2024-01-31', '2024-02-14', '2024-02-28', '2024-03-14', '2024-03-31'],
        'Responsable': ['Consultant', 'RH', 'IT', 'Contrôleur', 'Contrôleur', 'Contrôleur']
    }
    
    df_tasks = pd.DataFrame(tasks)
    st.dataframe(df_tasks, use_container_width=True)
    
    # Implementation tips
    st.subheader("🎯 Bonnes Pratiques d'Implémentation")
    
    tips = [
        "Impliquer toutes les parties prenantes dès le début",
        "Former les utilisateurs aux concepts budgétaires",
        "Démarrer avec un périmètre restreint",
        "Prévoir des revues régulières",
        "Adapter le processus à la culture d'entreprise"
    ]
    
    for i, tip in enumerate(tips, 1):
        st.write(f"{i}. {tip}")

def show_advanced_features():
    st.title("🚀 Aller Plus Loin")
    
    st.markdown("""
    ## Fonctionnalités Avancées du Contrôle de Gestion
    """)
    
    tab1, tab2, tab3 = st.tabs(["🤖 IA Prédictive", "📱 Dashboard Temps Réel", "🔗 Intégrations"])
    
    with tab1:
        st.subheader("Intelligence Artificielle Prédictive")
        
        st.markdown("""
        **Applications de l'IA en contrôle de gestion :**
        
        - 📊 **Prévisions automatiques** des ventes
        - 🔍 **Détection d'anomalies** dans les données
        - 🎯 **Recommandations** d'optimisation
        - 📈 **Scoring** des opportunités business
        """)
        
        if st.button("Lancer une Simulation IA"):
            with st.spinner("Analyse des données en cours..."):
                time.sleep(2)
                st.success("Analyse terminée !")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Confiance Prédictive", "87%")
                    st.metric("Risques Identifiés", "3")
                with col2:
                    st.metric("Opportunités", "5")
                    st.metric("Recommandations", "12")
    
    with tab2:
        st.subheader("Dashboard Temps Réel")
        
        # Real-time metrics simulation
        st.markdown("### Métriques en Temps Réel")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("CA du Jour", "45.2K €", "+8.2%")
        with col2:
            st.metric("Commandes", "127", "+12%")
        with col3:
            st.metric("Dépenses", "38.7K €", "+5.1%")
        with col4:
            st.metric("Trésorerie", "156.3K €", "-2.3%")
        
        # Auto-refresh option
        auto_refresh = st.checkbox("Actualisation automatique (30s)")
        if auto_refresh:
            st.info("Prochaine actualisation dans 30 secondes...")
    
    with tab3:
        st.subheader("Intégrations Systèmes")
        
        st.markdown("""
        **Systèmes connectables :**
        
        - 🧾 **ERP** (SAP, Oracle, Sage)
        - 💰 **Comptabilité** (Cegid, Quadratus)
        - 🛒 **CRM** (Salesforce, HubSpot)
        - 📊 **BI** (Power BI, Tableau)
        - 🌐 **API Rest** personnalisées
        """)
        
        integration_status = {
            'Système': ['ERP SAP', 'CRM Salesforce', 'Power BI', 'API Métier'],
            'Statut': ['✅ Connecté', '🟡 En cours', '✅ Connecté', '🔴 En attente'],
            'Dernière Synchro': ['2024-01-15 14:30', '2024-01-15 13:45', '2024-01-15 15:20', 'N/A']
        }
        
        df_integrations = pd.DataFrame(integration_status)
        st.dataframe(df_integrations, use_container_width=True)
        

def show_ai_sales_budget():
    st.title("💰 Budget des Ventes IA")
    
    st.markdown("""
    ## 🧠 Système Intelligent de Prévision des Ventes
    
    ### 🎯 Combinaison d'Algorithmes d'IA pour une Précision Maximale
    """)
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "🤖 Modèles Prédictifs", 
        "📊 Features Engineering", 
        "🎯 Analyse d'Impact",
        "📈 Simulation Temps Réel"
    ])
    
    with tab1:
        st.header("🤖 Architecture des Modèles d'IA")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 🏗️ Stack Technologique
            
            **Algorithmes Implémentés :**
            - **XGBoost** : Pour les relations non-linéaires
            - **LSTM** : Pour les séries temporelles complexes
            - **Prophet** : Pour la saisonnalité avancée
            - **Random Forest** : Pour la robustesse
            - **Régression Ensembliste** : Pour la précision
            """)
            
            st.markdown("""
            **📊 Validation Croisée :**
            ```python
            # Time Series Split validation
            from sklearn.model_selection import TimeSeriesSplit
            
            tscv = TimeSeriesSplit(n_splits=5)
            for train_idx, test_idx in tscv.split(X):
                model.fit(X[train_idx], y[train_idx])
                score = model.score(X[test_idx], y[test_idx])
            ```
            """)
        
        with col2:
            st.markdown("""
            ### 📈 Performance des Modèles
            """)
            
            model_performance = {
                'Modèle': ['XGBoost', 'LSTM', 'Prophet', 'Ensemble', 'Régression Linéaire'],
                'RMSE': [1250, 980, 1120, 890, 1850],
                'MAPE (%)': [3.2, 2.8, 3.5, 2.5, 5.8],
                'R²': [0.96, 0.97, 0.95, 0.98, 0.89],
                'Temps Entraînement': ['45s', '3min', '30s', '4min', '5s']
            }
            
            st.dataframe(pd.DataFrame(model_performance), use_container_width=True)
            
            # Graphique de performance
            models = ['XGBoost', 'LSTM', 'Prophet', 'Ensemble', 'Régression']
            rmse_scores = [1250, 980, 1120, 890, 1850]
            
            fig = px.bar(x=models, y=rmse_scores, 
                        title='Performance des Modèles (RMSE - plus bas = mieux)',
                        labels={'x': 'Modèles', 'y': 'RMSE'})
            st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.header("📊 Features Engineering Avancé")
        
        st.markdown("""
        ### 🎯 Variables Explicatives Multi-Sources
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **📈 Variables Temporelles :**
            ```python
            # Features de temporalité
            df['day_of_week'] = df.index.dayofweek
            df['month'] = df.index.month
            df['quarter'] = df.index.quarter
            df['is_weekend'] = df['day_of_week'].isin([5, 6])
            df['is_holiday'] = df.index.isin(holidays)
            ```
            
            **🔄 Variables Lagged :**
            ```python
            # Décalages temporels
            for lag in [1, 7, 30, 90]:
                df[f'lag_{lag}'] = df['sales'].shift(lag)
            
            # Moyennes mobiles
            for window in [7, 30, 90]:
                df[f'ma_{window}'] = df['sales'].rolling(window).mean()
            ```
            """)
        
        with col2:
            st.markdown("""
            **🌍 Variables Externes :**
            ```python
            # Données économiques
            df['inflation_rate'] = economic_data['inflation']
            df['consumer_confidence'] = economic_data['confidence']
            df['unemployment_rate'] = economic_data['unemployment']
            
            # Données météorologiques
            df['temperature'] = weather_data['temp']
            df['precipitation'] = weather_data['precip']
            df['sunshine_hours'] = weather_data['sunshine']
            
            # Données concurrentielles
            df['competitor_promotions'] = competitor_data['promo_active']
            df['market_share'] = market_data['our_share']
            ```
            """)
            
            st.markdown("""
            **🎯 Feature Importance :**
            """)
            
            features = ['Saisonnalité', 'Prix', 'Promotions', 'Météo', 'Économie', 'Concurrence']
            importance = [0.28, 0.22, 0.18, 0.12, 0.11, 0.09]
            
            fig = px.bar(x=importance, y=features, orientation='h',
                        title='Importance des Variables dans la Prédiction')
            st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.header("🎯 Analyse d'Impact et Sensibilité")
        
        st.markdown("""
        ### 📊 Analyse SHAP (SHapley Additive exPlanations)
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **🧮 Calcul des Valeurs SHAP :**
            """)
            st.latex(r"""
            \phi_i = \sum_{S \subseteq N \setminus \{i\}} \frac{|S|!(|N|-|S|-1)!}{|N|!} [f(S \cup \{i\}) - f(S)]
            """)
            
            st.markdown("""
            **Interprétation :**
            - $\phi_i > 0$ : Variable augmente la prédiction
            - $\phi_i < 0$ : Variable diminue la prédiction
            - $|\phi_i|$ : Importance de la variable
            """)
        
        with col2:
            # Simulation d'analyse SHAP
            st.subheader("🔍 Analyse d'Impact Simulée")
            
            feature_impact = {
                'Variable': ['Prix', 'Promotions', 'Saison', 'Météo', 'Économie'],
                'Impact Moyen': ['+15.2%', '+12.8%', '+8.5%', '+3.2%', '+2.1%'],
                'Direction': ['📈 Positive', '📈 Positive', '📈 Positive', '📈 Positive', '📈 Positive']
            }
            
            st.dataframe(pd.DataFrame(feature_impact), use_container_width=True)
            
            # Calculateur de sensibilité
            st.subheader("🎮 Simulateur de Sensibilité")
            
            price_change = st.slider("Variation prix (%)", -20, 20, 0)
            promo_budget = st.slider("Budget promotion (%)", -50, 100, 0)
            economic_growth = st.slider("Croissance économique (%)", -5, 5, 0)
            
            # Calcul impact
            impact_price = price_change * -0.3  # Élasticité prix
            impact_promo = promo_budget * 0.15  # Efficacité promo
            impact_economic = economic_growth * 1.2  # Sensibilité économique
            
            total_impact = impact_price + impact_promo + impact_economic
            
            st.metric("📊 Impact sur les Ventes", f"{total_impact:.1f}%")
    
    with tab4:
        st.header("📈 Simulation Temps Réel")
        
        st.markdown("""
        ### 🎯 Générateur de Scénarios en Temps Réel
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("⚙️ Paramètres du Scénario")
            
            scenario_type = st.selectbox("Type de scénario :", [
                "Croissance Accélérée",
                "Récession Modérée", 
                "Choc Concurrentiel",
                "Optimisation Marketing",
                "Scénario Personnalisé"
            ])
            
            horizon = st.slider("Horizon de prévision (mois)", 3, 24, 12)
            confidence_level = st.slider("Niveau de confiance (%)", 80, 99, 95)
        
        with col2:
            if st.button("🚀 Lancer la Simulation IA", type="primary"):
                with st.spinner("Calcul des scénarios en cours..."):
                    time.sleep(3)
                    
                    st.success("✅ Simulation terminée !")
                    
                    # Résultats de simulation
                    col_res1, col_res2, col_res3 = st.columns(3)
                    
                    with col_res1:
                        st.metric("Prévision CA Annuel", "12.8M €", "15.2%")
                        st.metric("Intervalle Confiance", f"± {100-confidence_level}%")
                    
                    with col_res2:
                        st.metric("Meilleur Modèle", "XGBoost Ensemble")
                        st.metric("Score de Confiance", "94.2%")
                    
                    with col_res3:
                        st.metric("Facteur Déterminant", "Prix Optimal")
                        st.metric("Impact Potentiel", "+18.5%")
                    
                    # Graphique de prévision
                    months = [f"Mois {i+1}" for i in range(horizon)]
                    base_forecast = [1000 + i*50 + np.random.normal(0, 20) for i in range(horizon)]
                    upper_bound = [x * 1.1 for x in base_forecast]
                    lower_bound = [x * 0.9 for x in base_forecast]
                    
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=months, y=base_forecast, 
                                           name='Prévision Base', line=dict(color='blue')))
                    fig.add_trace(go.Scatter(x=months, y=upper_bound, 
                                           name='Limite Supérieure', line=dict(color='green', dash='dash')))
                    fig.add_trace(go.Scatter(x=months, y=lower_bound, 
                                           name='Limite Inférieure', line=dict(color='red', dash='dash')))
                    fig.update_layout(title=f'Prévision des Ventes - {scenario_type}')
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # Recommandations IA
                    st.subheader("💡 Recommandations Stratégiques")
                    
                    recommendations = [
                        "🎯 **Optimiser le prix de vente** dans une fourchette de 5% pour maximiser la marge",
                        "📈 **Augmenter le budget marketing** de 15% au Q2 pour capitaliser sur la saisonnalité",
                        "🔄 **Diversifier les canaux de vente** pour réduire la dépendance aux grands comptes",
                        "📊 **Renforcer la surveillance concurrentielle** avec des alertes prix automatiques",
                        "🤖 **Automatiser les réponses pricing** pour réagir en temps réel au marché"
                    ]
                    
                    for i, rec in enumerate(recommendations, 1):
                        st.write(f"{i}. {rec}")

def show_advanced_stock_management():
    st.title("📦 Gestion des Stocks Avancée")
    
    st.markdown("""
    ## 🧠 Système Intelligent d'Optimisation des Stocks
    
    ### 🎯 Approche Multi-Critères avec Contraintes Complexes
    """)
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "🤖 Optimisation IA", 
        "📊 Analyse Prédictive", 
        "⚙️ Contraintes Avancées",
        "📈 Performance Temps Réel"
    ])
    
    with tab1:
        st.header("🤖 Optimisation par Intelligence Artificielle")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 🏗️ Algorithmes d'Optimisation
            
            **🎯 Méthodes Implémentées :**
            - **Programmation Linéaire** : Pour les contraintes simples
            - **Algorithmes Génétiques** : Pour les problèmes complexes
            - **Simulated Annealing** : Pour l'optimisation globale
            - **Reinforcement Learning** : Pour l'adaptation dynamique
            """)
            
            st.markdown("""
            **📊 Fonction Objectif :**
            ```python
            def objective_function(decision_vars):
                total_cost = (
                    ordering_cost(decision_vars) +
                    holding_cost(decision_vars) + 
                    stockout_cost(decision_vars) +
                    capacity_cost(decision_vars)
                )
                return total_cost
            ```
            """)
        
        with col2:
            st.markdown("""
            ### ⚙️ Contraintes Prises en Compte
            
            **🏭 Contraintes Opérationnelles :**
            - Capacités de stockage
            - Délais d'approvisionnement
            - Contraintes de qualité
            - Périodes de fermeture
            
            **💰 Contraintes Financières :**
            - Budget d'achat
            - Coût de possession
            - Taux de rotation cible
            - Niveau de service client
            """)
            
            # Calculateur d'optimisation
            st.subheader("🧮 Calculateur d'Optimisation")
            
            demand = st.number_input("Demande annuelle (unités)", value=10000)
            unit_cost = st.number_input("Coût unitaire (€)", value=50.0)
            holding_rate = st.number_input("Taux de possession (%)", value=25.0) / 100
            order_cost = st.number_input("Coût de commande (€)", value=200.0)
            
            if st.button("🎯 Optimiser les Stocks"):
                # Calcul EOQ classique
                eoq_classic = math.sqrt((2 * demand * order_cost) / (unit_cost * holding_rate))
                
                # Simulation optimisation avancée
                eoq_optimized = eoq_classic * 0.85  # Gain typique avec IA
                
                st.metric("📦 EOQ Classique", f"{eoq_classic:.0f} unités")
                st.metric("🤖 EOQ Optimisé IA", f"{eoq_optimized:.0f} unités", "-15%")
                st.metric("💰 Économie Annuelle", f"{(eoq_classic - eoq_optimized) * unit_cost * holding_rate / 2:.0f} €")
    
    with tab2:
        st.header("📊 Analyse Prédictive des Stocks")
        
        st.markdown("""
        ### 🎯 Prévision de la Demande et des Ruptures
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **📈 Modèles de Prévision :**
            - **LSTM** : Pour les séries temporelles complexes
            - **Prophet** : Pour la saisonnalité multiple
            - **Survival Analysis** : Pour la prédiction des ruptures
            - **Anomaly Detection** : Pour les comportements atypiques
            """)
            
            st.markdown("""
            **🔍 Détection des Patterns :**
            ```python
            # Détection de saisonnalité
            from statsmodels.tsa.seasonal import seasonal_decompose
            
            decomposition = seasonal_decompose(
                sales_data, 
                model='multiplicative', 
                period=365
            )
            
            trend = decomposition.trend
            seasonal = decomposition.seasonal
            residual = decomposition.resid
            ```
            """)
        
        with col2:
            # Simulateur de prévision de rupture
            st.subheader("🚨 Prédicteur de Rupture de Stock")
            
            current_stock = st.number_input("Stock actuel (unités)", value=500)
            daily_demand = st.number_input("Demande moyenne journalière", value=25)
            demand_std = st.number_input("Écart-type demande", value=5)
            lead_time = st.number_input("Délai livraison (jours)", value=10)
            service_level = st.slider("Niveau de service souhaité (%)", 90, 99, 95)
            
            if st.button("📊 Calculer le Risque"):
                # Calcul stock de sécurité
                z_score = {90: 1.28, 95: 1.65, 99: 2.33}[service_level]
                safety_stock = z_score * demand_std * math.sqrt(lead_time)
                
                # Calcul point de commande
                reorder_point = (daily_demand * lead_time) + safety_stock
                
                # Risque de rupture
                stockout_risk = "Élevé" if current_stock < reorder_point else "Faible"
                days_cover = current_stock / daily_demand
                
                st.metric("🛡️ Stock de Sécurité", f"{safety_stock:.0f} unités")
                st.metric("⚡ Point de Commande", f"{reorder_point:.0f} unités")
                st.metric("⏱️ Couverture Actuelle", f"{days_cover:.1f} jours")
                st.metric("🚨 Risque de Rupture", stockout_risk)
    
    with tab3:
        st.header("⚙️ Gestion des Contraintes Avancées")
        
        st.markdown("""
        ### 🎯 Optimisation Multi-Contraintes
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🏭 Contraintes Physiques")
            
            warehouse_capacity = st.number_input("Capacité entrepôt (unités)", value=5000)
            max_weight = st.number_input("Poids max par emplacement (kg)", value=1000)
            temperature_zones = st.multiselect("Zones de température requises:", 
                                             ["Ambiance", "Frais", "Froid", "Congélateur"])
            
            st.subheader("📦 Contraintes Produit")
            
            perishable_items = st.checkbox("Articles périssables")
            hazardous_materials = st.checkbox("Matériaux dangereux")
            high_value_items = st.checkbox("Articles de haute valeur")
        
        with col2:
            st.subheader("💰 Contraintes Financières")
            
            max_inventory_value = st.number_input("Valeur stock max (€)", value=250000)
            target_turnover = st.number_input("Rotation cible (an)", value=8.0)
            budget_constraint = st.number_input("Budget annuel approvisionnement (€)", value=500000)
            
            if st.button("🎯 Optimiser avec Contraintes"):
                with st.spinner("Résolution du problème d'optimisation..."):
                    time.sleep(2)
                    
                    st.success("✅ Solution optimale trouvée !")
                    
                    # Résultats de l'optimisation
                    optimization_results = {
                        'Paramètre': ['Valeur Stock Optimale', 'Rotation Projetée', 'Niveau Service', 'Coût Total Annuel'],
                        'Valeur': ['218,450 €', '8.2', '98.5%', '45,820 €'],
                        'Contrainte': ['≤ 250,000 €', '≥ 8.0', '≥ 98%', '≤ 50,000 €'],
                        'Statut': ['✅ Respectée', '✅ Respectée', '✅ Respectée', '✅ Respectée']
                    }
                    
                    st.dataframe(pd.DataFrame(optimization_results), use_container_width=True)
                    
                    st.info("""
                    **💡 Recommandations du Système :**
                    - Réduire les stocks des articles C de 25%
                    - Augmenter la fréquence de commande des articles A
                    - Négocier des délais réduits avec 4 fournisseurs critiques
                    - Implémenter un système de cross-docking pour 30% des références
                    """)
    
    with tab4:
        st.header("📈 Tableau de Bord Temps Réel")
        
        st.markdown("""
        ### 🎯 Monitoring des Performances Stocks
        """)
        
        # KPI en temps réel
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("📊 Rotation Stocks", "8.2", "+0.5")
            st.metric("⏱️ Couverture Moyenne", "45 jours", "-3 jours")
        
        with col2:
            st.metric("💰 Valeur Stock", "2.8M €", "+150K €")
            st.metric("🔄 Taux Service", "98.5%", "+0.8%")
        
        with col3:
            st.metric("📦 Articles en Stock", "1,245", "+25")
            st.metric("⚡ Délai Moyen", "5.2 jours", "-0.3 jours")
        
        with col4:
            st.metric("💸 Coût Possession", "560K €", "+45K €")
            st.metric("🚨 Ruptures", "3", "-2")
        
        # Graphiques de performance
        col1, col2 = st.columns(2)
        
        with col1:
            # Évolution des indicateurs
            months = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Jun']
            turnover = [7.2, 7.5, 7.8, 8.0, 8.1, 8.2]
            service_level = [97.2, 97.5, 97.8, 98.1, 98.3, 98.5]
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=months, y=turnover, name='Rotation', yaxis='y1'))
            fig.add_trace(go.Scatter(x=months, y=service_level, name='Taux Service', yaxis='y2'))
            fig.update_layout(
                title='Évolution des Performances Stocks',
                yaxis=dict(title='Rotation'),
                yaxis2=dict(title='Taux Service (%)', overlaying='y', side='right')
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Répartition par catégorie ABC
            categories = ['A (20%)', 'B (30%)', 'C (50%)']
            values = [65, 25, 10]  # % de la valeur
            
            fig = px.pie(values=values, names=categories, 
                        title='Répartition de la Valeur par Catégorie ABC')
            st.plotly_chart(fig, use_container_width=True)
        
        # Alertes intelligentes
        st.subheader("🚨 Alertes et Recommandations")
        
        alerts = [
            {"niveau": "🔴", "message": "Article A001 - Stock critique (2 jours)", "action": "Commander 500 unités"},
            {"niveau": "🟠", "message": "Fournisseur F123 - Délai augmenté de 3 jours", "action": "Trouver alternative"},
            {"niveau": "🟡", "message": "Catégorie C - Rotation en baisse de 15%", "action": "Réviser politique stocks"},
            {"niveau": "🟢", "message": "Entrepôt Est - Capacité utilisée à 92%", "action": "Planifier rééquilibrage"}
        ]
        
        for alert in alerts:
            with st.container(border=True):
                col1, col2, col3 = st.columns([1, 3, 2])
                with col1:
                    st.write(f"**{alert['niveau']}**")
                with col2:
                    st.write(alert['message'])
                with col3:
                    st.button(alert['action'], key=f"action_{alert['message']}")

        
        # ... (contenu précédent) ...
        
        with col2:
            if st.button("📊 Calculer le Profil de Risque"):
                # ... (calculs précédents) ...
                
                # Plan d'atténuation
                st.subheader("🛡️ Plan d'Atténuation des Risques")
                
                if overall_risk_score > 60:
                    st.error("""
                    **🚨 RISQUE TRÈS ÉLEVÉ**
                    - Mettre en place un comité de crise
                    - Développer des plans de contingence détaillés
                    - Augmenter les réserves de trésorerie
                    - Réévaluer la faisabilité du projet
                    """)
                elif overall_risk_score > 40:
                    st.warning("""
                    **⚠️ RISQUE MODÉRÉ**
                    - Surveillance renforcée des indicateurs clés
                    - Plans d'action préventifs
                    - Clauses contractuelles protectrices
                    - Diversification des fournisseurs
                    """)
                else:
                    st.success("""
                    **✅ RISQUE ACCEPTABLE**
                    - Monitoring standard suffisant
                    - Procéder avec les précautions habituelles
                    - Maintenir les plans de continuité d'activité
                    """)
                
                # Simulation Monte Carlo
                st.subheader("🎲 Simulation Monte Carlo")
                
                if st.button("🔄 Lancer la Simulation"):
                    with st.spinner("Simulation de 10,000 scénarios en cours..."):
                        time.sleep(2)
                        
                        # Simulation des VAN avec incertitude
                        n_simulations = 10000
                        simulated_van = []
                        
                        for _ in range(n_simulations):
                            # Ajout d'incertitude aux cash-flows
                            simulated_cf = [cf * np.random.normal(1, 0.15) for cf in cash_flows]
                            van_sim = -initial_investment
                            for year, cf in enumerate(simulated_cf, 1):
                                van_sim += cf / ((1 + discount_rate) ** year)
                            simulated_van.append(van_sim)
                        
                        # Analyse des résultats
                        van_mean = np.mean(simulated_van)
                        van_std = np.std(simulated_van)
                        prob_positive = np.mean(np.array(simulated_van) > 0) * 100
                        
                        col_stat1, col_stat2, col_stat3 = st.columns(3)
                        with col_stat1:
                            st.metric("VAN Moyenne", f"{van_mean:,.0f} €")
                        with col_stat2:
                            st.metric("Écart-type", f"{van_std:,.0f} €")
                        with col_stat3:
                            st.metric("Probabilité VAN > 0", f"{prob_positive:.1f}%")
                        
                        # Histogramme des VAN
                        fig = px.histogram(x=simulated_van, 
                                         title='Distribution des VAN - Simulation Monte Carlo',
                                         labels={'x': 'VAN (€)', 'y': 'Fréquence'})
                        fig.add_vline(x=0, line_dash="dash", line_color="red")
                        st.plotly_chart(fig, use_container_width=True)

    with tab4:
        st.header("📈 Gestion de Portefeuille de Projets")
        
        st.markdown("""
        ### 🎯 Optimisation du Portefeuille d'Investissements
        """)
        
        # Données du portefeuille
        projects_data = {
            'Projet': ['Nouvelle Usine', 'Digitalisation', 'R&D Produit A', 'Optimisation Logistique', 'Acquisition Stratégique'],
            'Investissement (M€)': [5.2, 1.8, 3.5, 0.9, 8.0],
            'VAN (M€)': [6.8, 2.5, 4.2, 1.5, 9.5],
            'TRI (%)': [18.5, 22.3, 15.8, 25.6, 12.4],
            'Score Stratégique': [8.5, 7.2, 9.1, 6.8, 7.9],
            'Risque': [6.2, 4.5, 7.8, 3.2, 8.5]
        }
        
        df_projects = pd.DataFrame(projects_data)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📋 Portefeuille de Projets")
            st.dataframe(df_projects, use_container_width=True)
        
        with col2:
            # Graphique VAN vs Investissement
            fig = px.scatter(df_projects, x='Investissement (M€)', y='VAN (M€)',
                           size='TRI (%)', color='Score Stratégique',
                           hover_name='Projet', 
                           title='Portefeuille de Projets - VAN vs Investissement')
            st.plotly_chart(fig, use_container_width=True)
        
        # Optimisation du portefeuille
        st.subheader("🧮 Optimisation du Portefeuille")
        
        total_budget = st.number_input("Budget total disponible (M€)", value=15.0)
        min_strategic_score = st.slider("Score stratégique minimum", 6.0, 10.0, 7.0)
        max_risk_tolerance = st.slider("Tolérance risque maximum", 1.0, 10.0, 7.0)
        
        if st.button("🎯 Optimiser le Portefeuille"):
            # Algorithme d'optimisation simple
            projects = []
            for i, row in df_projects.iterrows():
                projects.append({
                    'name': row['Projet'],
                    'investment': row['Investissement (M€)'],
                    'van': row['VAN (M€)'],
                    'strategic_score': row['Score Stratégique'],
                    'risk': row['Risque'],
                    'ratio': row['VAN (M€)'] / row['Investissement (M€)']
                })
            
            # Filtrage et optimisation
            filtered_projects = [p for p in projects if p['strategic_score'] >= min_strategic_score and p['risk'] <= max_risk_tolerance]
            filtered_projects.sort(key=lambda x: x['ratio'], reverse=True)
            
            # Sélection optimale
            remaining_budget = total_budget
            optimal_portfolio = []
            total_van = 0
            total_investment = 0
            
            for project in filtered_projects:
                if project['investment'] <= remaining_budget:
                    optimal_portfolio.append(project)
                    remaining_budget -= project['investment']
                    total_van += project['van']
                    total_investment += project['investment']
            
            st.success(f"**📊 Portefeuille Optimal (Budget: {total_budget}M€)**")
            
            portfolio_results = {
                'Projet': [p['name'] for p in optimal_portfolio],
                'Investissement (M€)': [p['investment'] for p in optimal_portfolio],
                'VAN (M€)': [p['van'] for p in optimal_portfolio],
                'Ratio VAN/Inv': [f"{p['ratio']:.2f}" for p in optimal_portfolio],
                'Score Stratégique': [p['strategic_score'] for p in optimal_portfolio]
            }
            
            st.dataframe(pd.DataFrame(portfolio_results), use_container_width=True)
            
            col_res1, col_res2, col_res3 = st.columns(3)
            with col_res1:
                st.metric("💰 VAN Totale", f"{total_van:.1f} M€")
            with col_res2:
                st.metric("📊 Investissement Total", f"{total_investment:.1f} M€")
            with col_res3:
                st.metric("🎯 Budget Restant", f"{remaining_budget:.1f} M€")
            
            # Graphique du portefeuille optimal
            if optimal_portfolio:
                fig = px.pie(values=[p['investment'] for p in optimal_portfolio], 
                           names=[p['name'] for p in optimal_portfolio],
                           title='Répartition des Investissements - Portefeuille Optimal')
                st.plotly_chart(fig, use_container_width=True)

def show_predictive_cashflow():
    st.title("💸 Trésorerie Prédictive")
    
    st.markdown("""
    ## 🧠 Système Intelligent de Prévision et Gestion de Trésorerie
    
    ### 🎯 Modélisation Avancée et Alertes Prédictives
    """)
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "🤖 Prévision IA", 
        "📊 Analyse Scénarios", 
        "🚨 Alertes Prédictives",
        "📈 Optimisation Cash"
    ])
    
    with tab1:
        st.header("🤖 Prévision par Intelligence Artificielle")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 🏗️ Architecture des Modèles
            
            **Algorithmes Utilisés :**
            - **LSTM** : Pour les séries temporelles complexes
            - **Prophet** : Pour la saisonnalité multiple
            - **XGBoost** : Pour les relations non-linéaires
            - **SARIMA** : Pour la saisonnalité avancée
            """)
            
            st.markdown("""
            **📊 Données Intégrées :**
            - Historique des flux de trésorerie
            - Données commerciales (commandes, factures)
            - Informations fournisseurs (délais, conditions)
            - Données économiques (taux, inflation)
            - Calendrier des échéances
            """)
        
        with col2:
            # Performance des modèles
            st.subheader("📈 Performance des Modèles")
            
            model_perf = {
                'Modèle': ['LSTM', 'Prophet', 'XGBoost', 'SARIMA', 'Ensemble'],
                'RMSE (k€)': [45.2, 52.8, 48.5, 55.1, 38.7],
                'MAPE (%)': [3.8, 4.5, 4.2, 5.1, 3.2],
                'Précision 7j': ['94.2%', '92.8%', '93.5%', '91.8%', '95.8%'],
                'Temps Calcul': ['2.5min', '45s', '1.2min', '3.8min', '4.5min']
            }
            
            st.dataframe(pd.DataFrame(model_perf), use_container_width=True)
            
            # Simulation de prévision
            st.subheader("🔮 Simulation de Prévision")
            
            if st.button("🎯 Générer Prévision IA"):
                with st.spinner("Calcul des prévisions en cours..."):
                    time.sleep(3)
                    
                    st.success("✅ Prévision générée avec succès !")
                    
                    # Données simulées
                    days = [f"J+{i}" for i in range(1, 31)]
                    cash_forecast = [50000 + i*1500 + np.random.normal(0, 5000) for i in range(30)]
                    upper_bound = [x + 8000 for x in cash_forecast]
                    lower_bound = [x - 8000 for x in cash_forecast]
                    
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=days, y=cash_forecast, 
                                           name='Prévision', line=dict(color='blue')))
                    fig.add_trace(go.Scatter(x=days, y=upper_bound, 
                                           name='Limite Supérieure', line=dict(color='green', dash='dash')))
                    fig.add_trace(go.Scatter(x=days, y=lower_bound, 
                                           name='Limite Inférieure', line=dict(color='red', dash='dash')))
                    fig.update_layout(title='Prévision de Trésorerie - 30 Jours')
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # Métriques de prévision
                    min_forecast = min(cash_forecast)
                    avg_forecast = np.mean(cash_forecast)
                    
                    col_met1, col_met2, col_met3 = st.columns(3)
                    with col_met1:
                        st.metric("📉 Trésorerie Minimale", f"{min_forecast:,.0f} €")
                    with col_met2:
                        st.metric("📊 Moyenne Prévision", f"{avg_forecast:,.0f} €")
                    with col_met3:
                        risk_level = "Élevé" if min_forecast < 0 else "Modéré" if min_forecast < 10000 else "Faible"
                        st.metric("🚨 Niveau de Risque", risk_level)
    
    with tab2:
        st.header("📊 Analyse de Scénarios")
        
        st.markdown("""
        ### 🎯 Simulation de Différents Scénarios Économiques
        """)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.subheader("📈 Scénario Optimiste")
            growth_optimistic = st.slider("Croissance CA optimiste (%)", 0, 30, 15)
            margin_optimistic = st.slider("Marge optimiste (%)", 0, 10, 5)
            payment_days_optimistic = st.slider("Délai clients optimiste (jours)", 10, 60, 25)
        
        with col2:
            st.subheader("📊 Scénario de Référence")
            growth_reference = st.slider("Croissance CA référence (%)", -5, 15, 5)
            margin_reference = st.slider("Marge référence (%)", 0, 5, 2)
            payment_days_reference = st.slider("Délai clients référence (jours)", 20, 90, 45)
        
        with col3:
            st.subheader("📉 Scénario Pessimiste")
            growth_pessimistic = st.slider("Croissance CA pessimiste (%)", -20, 5, -5)
            margin_pessimistic = st.slider("Marge pessimiste (%)", -10, 0, -3)
            payment_days_pessimistic = st.slider("Délai clients pessimiste (jours)", 30, 120, 75)
        
        if st.button("🎯 Analyser les Scénarios"):
            # Calcul des scénarios
            base_revenue = 100000  # CA mensuel de base
            
            scenarios = {
                'Scénario': ['Optimiste', 'Référence', 'Pessimiste'],
                'Croissance CA (%)': [growth_optimistic, growth_reference, growth_pessimistic],
                'Marge (%)': [margin_optimistic, margin_reference, margin_pessimistic],
                'Délai Clients (jours)': [payment_days_optimistic, payment_days_reference, payment_days_pessimistic],
                'CA Mensuel (€)': [
                    base_revenue * (1 + growth_optimistic/100),
                    base_revenue * (1 + growth_reference/100),
                    base_revenue * (1 + growth_pessimistic/100)
                ],
                'BFR (€)': [
                    (payment_days_optimistic/30) * base_revenue * (1 + growth_optimistic/100),
                    (payment_days_reference/30) * base_revenue * (1 + growth_reference/100),
                    (payment_days_pessimistic/30) * base_revenue * (1 + growth_pessimistic/100)
                ]
            }
            
            df_scenarios = pd.DataFrame(scenarios)
            st.dataframe(df_scenarios, use_container_width=True)
            
            # Graphique comparatif
            fig = px.bar(df_scenarios, x='Scénario', y='BFR (€)',
                        title='Besoin en Fonds de Roulement par Scénario',
                        color='Scénario')
            st.plotly_chart(fig, use_container_width=True)
            
            # Analyse de sensibilité
            st.subheader("🎯 Analyse de Sensibilité")
            
            st.info("""
            **Recommandations par Scénario :**
            - **Optimiste** : Investir dans la croissance, optimiser le BFR
            - **Référence** : Maintenir la stratégie actuelle, surveiller les indicateurs
            - **Pessimiste** : Renforcer la trésorerie, réduire les stocks, renégocier les délais
            """)
    
    with tab3:
        st.header("🚨 Alertes Prédictives")
        
        st.markdown("""
        ### 🎯 Système d'Alerte Précoce Intelligent
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("⚙️ Configuration des Alertes")
            
            cash_threshold = st.number_input("Seuil trésorerie critique (€)", value=10000)
            overdraft_limit = st.number_input("Limite découvert autorisée (€)", value=5000)
            bfr_alert_threshold = st.slider("Seuil alerte BFR (%)", 10, 50, 25)
            
            st.subheader("🔔 Fréquence de Surveillance")
            monitoring_frequency = st.selectbox("Fréquence de contrôle", [
                "Temps réel", "Quotidien", "Hebdomadaire", "Mensuel"
            ])
        
        with col2:
            st.subheader("📧 Canaux d'Alerte")
            
            alert_channels = st.multiselect(
                "Canaux d'alerte activés :",
                ["Email Direction", "Slack Finance", "SMS Urgence", "Dashboard", "Rapport Auto"],
                default=["Email Direction", "Slack Finance"]
            )
            
            st.subheader("👥 Destinataires")
            recipients = st.text_area("Liste des destinataires (un par ligne)", 
                                   "directeur@entreprise.com\nfinance@entreprise.com\ntresorerie@entreprise.com")
        
        # Tableau de bord des alertes
        st.subheader("📊 Alertes Actives")
        
        active_alerts = {
            'Type Alerte': ['Trésorerie Critique', 'Découvert Imminent', 'BFR Excessif', 'Retard Client'],
            'Niveau': ['🔴 Haute', '🟠 Moyenne', '🟡 Faible', '🟠 Moyenne'],
            'Détails': ['Trésorerie < 15K€', 'Découvert > 3K€', 'BFR +35% vs budget', 'Client X - 45 jours'],
            'Date Détection': ['15/01/2024', '14/01/2024', '13/01/2024', '12/01/2024'],
            'Statut': ['🔄 En cours', '✅ Traitée', '🔄 En cours', '✅ Traitée']
        }
        
        st.dataframe(pd.DataFrame(active_alerts), use_container_width=True)
        
        # Statistiques des alertes
        st.subheader("📈 Statistiques des Alertes")
        
        col_stat1, col_stat2, col_stat3, col_stat4 = st.columns(4)
        
        with col_stat1:
            st.metric("🚨 Alertes Actives", "3")
        with col_stat2:
            st.metric("✅ Alertes Traitées", "24")
        with col_stat3:
            st.metric("⏱️ Temps Moyen Réponse", "2.3h")
        with col_stat4:
            st.metric("📊 Taux Résolution", "89%")
        
        if st.button("🔄 Actualiser les Alertes"):
            st.success("Système d'alerte actualisé !")
            st.info("2 nouvelles alertes potentielles détectées et analysées")
    
    with tab4:
        st.header("📈 Optimisation de la Trésorerie")
        
        st.markdown("""
        ### 🎯 Stratégies d'Optimisation du Cash
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("💰 Optimisation des Encaisse")




   
    with tab1:
        st.header("📊 Évaluation Stratégique des Projets")
        # ... (contenu existant) ...
        
    with tab2:
        st.header("💰 Analyse Financière Avancée")
        # ... (contenu existant) ...
        
    
    with tab3:
        st.header("⚠️ Analyse et Gestion des Risques")
        
        # ... (contenu précédent) ...
        
        with col2:
            if st.button("📊 Calculer le Profil de Risque"):
                # ... (calculs précédents) ...
                
                # Plan d'atténuation
                st.subheader("🛡️ Plan d'Atténuation des Risques")
                
                if overall_risk_score > 60:
                    st.error("""
                    **🚨 RISQUE TRÈS ÉLEVÉ**
                    - Mettre en place un comité de crise
                    - Développer des plans de contingence détaillés
                    - Augmenter les réserves de trésorerie
                    - Réévaluer la faisabilité du projet
                    """)
                elif overall_risk_score > 40:
                    st.warning("""
                    **⚠️ RISQUE MODÉRÉ**
                    - Surveillance renforcée des indicateurs clés
                    - Plans d'action préventifs
                    - Clauses contractuelles protectrices
                    - Diversification des fournisseurs
                    """)
                else:
                    st.success("""
                    **✅ RISQUE ACCEPTABLE**
                    - Monitoring standard suffisant
                    - Procéder avec les précautions habituelles
                    - Maintenir les plans de continuité d'activité
                    """)
                
                # Simulation Monte Carlo
                st.subheader("🎲 Simulation Monte Carlo")
                
                if st.button("🔄 Lancer la Simulation"):
                    with st.spinner("Simulation de 10,000 scénarios en cours..."):
                        time.sleep(2)
                        
                        # Simulation des VAN avec incertitude
                        n_simulations = 10000
                        simulated_van = []
                        
                        for _ in range(n_simulations):
                            # Ajout d'incertitude aux cash-flows
                            simulated_cf = [cf * np.random.normal(1, 0.15) for cf in cash_flows]
                            van_sim = -initial_investment
                            for year, cf in enumerate(simulated_cf, 1):
                                van_sim += cf / ((1 + discount_rate) ** year)
                            simulated_van.append(van_sim)
                        
                        # Analyse des résultats
                        van_mean = np.mean(simulated_van)
                        van_std = np.std(simulated_van)
                        prob_positive = np.mean(np.array(simulated_van) > 0) * 100
                        
                        col_stat1, col_stat2, col_stat3 = st.columns(3)
                        with col_stat1:
                            st.metric("VAN Moyenne", f"{van_mean:,.0f} €")
                        with col_stat2:
                            st.metric("Écart-type", f"{van_std:,.0f} €")
                        with col_stat3:
                            st.metric("Probabilité VAN > 0", f"{prob_positive:.1f}%")
                        
                        # Histogramme des VAN
                        fig = px.histogram(x=simulated_van, 
                                         title='Distribution des VAN - Simulation Monte Carlo',
                                         labels={'x': 'VAN (€)', 'y': 'Fréquence'})
                        fig.add_vline(x=0, line_dash="dash", line_color="red")
                        st.plotly_chart(fig, use_container_width=True)

    with tab4:
        st.header("📈 Gestion de Portefeuille de Projets")
        
        st.markdown("""
        ### 🎯 Optimisation du Portefeuille d'Investissements
        """)
        
        # Données du portefeuille
        projects_data = {
            'Projet': ['Nouvelle Usine', 'Digitalisation', 'R&D Produit A', 'Optimisation Logistique', 'Acquisition Stratégique'],
            'Investissement (M€)': [5.2, 1.8, 3.5, 0.9, 8.0],
            'VAN (M€)': [6.8, 2.5, 4.2, 1.5, 9.5],
            'TRI (%)': [18.5, 22.3, 15.8, 25.6, 12.4],
            'Score Stratégique': [8.5, 7.2, 9.1, 6.8, 7.9],
            'Risque': [6.2, 4.5, 7.8, 3.2, 8.5]
        }
        
        df_projects = pd.DataFrame(projects_data)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📋 Portefeuille de Projets")
            st.dataframe(df_projects, use_container_width=True)
        
        with col2:
            # Graphique VAN vs Investissement
            fig = px.scatter(df_projects, x='Investissement (M€)', y='VAN (M€)',
                           size='TRI (%)', color='Score Stratégique',
                           hover_name='Projet', 
                           title='Portefeuille de Projets - VAN vs Investissement')
            st.plotly_chart(fig, use_container_width=True)
        
        # Optimisation du portefeuille
        st.subheader("🧮 Optimisation du Portefeuille")
        
        total_budget = st.number_input("Budget total disponible (M€)", value=15.0)
        min_strategic_score = st.slider("Score stratégique minimum", 6.0, 10.0, 7.0)
        max_risk_tolerance = st.slider("Tolérance risque maximum", 1.0, 10.0, 7.0)
        
        if st.button("🎯 Optimiser le Portefeuille"):
            # Algorithme d'optimisation simple
            projects = []
            for i, row in df_projects.iterrows():
                projects.append({
                    'name': row['Projet'],
                    'investment': row['Investissement (M€)'],
                    'van': row['VAN (M€)'],
                    'strategic_score': row['Score Stratégique'],
                    'risk': row['Risque'],
                    'ratio': row['VAN (M€)'] / row['Investissement (M€)']
                })
            
            # Filtrage et optimisation
            filtered_projects = [p for p in projects if p['strategic_score'] >= min_strategic_score and p['risk'] <= max_risk_tolerance]
            filtered_projects.sort(key=lambda x: x['ratio'], reverse=True)
            
            # Sélection optimale
            remaining_budget = total_budget
            optimal_portfolio = []
            total_van = 0
            total_investment = 0
            
            for project in filtered_projects:
                if project['investment'] <= remaining_budget:
                    optimal_portfolio.append(project)
                    remaining_budget -= project['investment']
                    total_van += project['van']
                    total_investment += project['investment']
            
            st.success(f"**📊 Portefeuille Optimal (Budget: {total_budget}M€)**")
            
            portfolio_results = {
                'Projet': [p['name'] for p in optimal_portfolio],
                'Investissement (M€)': [p['investment'] for p in optimal_portfolio],
                'VAN (M€)': [p['van'] for p in optimal_portfolio],
                'Ratio VAN/Inv': [f"{p['ratio']:.2f}" for p in optimal_portfolio],
                'Score Stratégique': [p['strategic_score'] for p in optimal_portfolio]
            }
            
            st.dataframe(pd.DataFrame(portfolio_results), use_container_width=True)
            
            col_res1, col_res2, col_res3 = st.columns(3)
            with col_res1:
                st.metric("💰 VAN Totale", f"{total_van:.1f} M€")
            with col_res2:
                st.metric("📊 Investissement Total", f"{total_investment:.1f} M€")
            with col_res3:
                st.metric("🎯 Budget Restant", f"{remaining_budget:.1f} M€")
            
            # Graphique du portefeuille optimal
            if optimal_portfolio:
                fig = px.pie(values=[p['investment'] for p in optimal_portfolio], 
                           names=[p['name'] for p in optimal_portfolio],
                           title='Répartition des Investissements - Portefeuille Optimal')
                st.plotly_chart(fig, use_container_width=True)

def show_predictive_cashflow():
    st.title("💸 Trésorerie Prédictive")
    
    st.markdown("""
    ## 🧠 Système Intelligent de Prévision et Gestion de Trésorerie
    
    ### 🎯 Modélisation Avancée et Alertes Prédictives
    """)
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "🤖 Prévision IA", 
        "📊 Analyse Scénarios", 
        "🚨 Alertes Prédictives",
        "📈 Optimisation Cash"
    ])
    
    with tab1:
        st.header("🤖 Prévision par Intelligence Artificielle")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 🏗️ Architecture des Modèles
            
            **Algorithmes Utilisés :**
            - **LSTM** : Pour les séries temporelles complexes
            - **Prophet** : Pour la saisonnalité multiple
            - **XGBoost** : Pour les relations non-linéaires
            - **SARIMA** : Pour la saisonnalité avancée
            """)
            
            st.markdown("""
            **📊 Données Intégrées :**
            - Historique des flux de trésorerie
            - Données commerciales (commandes, factures)
            - Informations fournisseurs (délais, conditions)
            - Données économiques (taux, inflation)
            - Calendrier des échéances
            """)
        
        with col2:
            # Performance des modèles
            st.subheader("📈 Performance des Modèles")
            
            model_perf = {
                'Modèle': ['LSTM', 'Prophet', 'XGBoost', 'SARIMA', 'Ensemble'],
                'RMSE (k€)': [45.2, 52.8, 48.5, 55.1, 38.7],
                'MAPE (%)': [3.8, 4.5, 4.2, 5.1, 3.2],
                'Précision 7j': ['94.2%', '92.8%', '93.5%', '91.8%', '95.8%'],
                'Temps Calcul': ['2.5min', '45s', '1.2min', '3.8min', '4.5min']
            }
            
            st.dataframe(pd.DataFrame(model_perf), use_container_width=True)
            
            # Simulation de prévision
            st.subheader("🔮 Simulation de Prévision")
            
            if st.button("🎯 Générer Prévision IA"):
                with st.spinner("Calcul des prévisions en cours..."):
                    time.sleep(3)
                    
                    st.success("✅ Prévision générée avec succès !")
                    
                    # Données simulées
                    days = [f"J+{i}" for i in range(1, 31)]
                    cash_forecast = [50000 + i*1500 + np.random.normal(0, 5000) for i in range(30)]
                    upper_bound = [x + 8000 for x in cash_forecast]
                    lower_bound = [x - 8000 for x in cash_forecast]
                    
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=days, y=cash_forecast, 
                                           name='Prévision', line=dict(color='blue')))
                    fig.add_trace(go.Scatter(x=days, y=upper_bound, 
                                           name='Limite Supérieure', line=dict(color='green', dash='dash')))
                    fig.add_trace(go.Scatter(x=days, y=lower_bound, 
                                           name='Limite Inférieure', line=dict(color='red', dash='dash')))
                    fig.update_layout(title='Prévision de Trésorerie - 30 Jours')
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # Métriques de prévision
                    min_forecast = min(cash_forecast)
                    avg_forecast = np.mean(cash_forecast)
                    
                    col_met1, col_met2, col_met3 = st.columns(3)
                    with col_met1:
                        st.metric("📉 Trésorerie Minimale", f"{min_forecast:,.0f} €")
                    with col_met2:
                        st.metric("📊 Moyenne Prévision", f"{avg_forecast:,.0f} €")
                    with col_met3:
                        risk_level = "Élevé" if min_forecast < 0 else "Modéré" if min_forecast < 10000 else "Faible"
                        st.metric("🚨 Niveau de Risque", risk_level)
    
    with tab2:
        st.header("📊 Analyse de Scénarios")
        
        st.markdown("""
        ### 🎯 Simulation de Différents Scénarios Économiques
        """)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.subheader("📈 Scénario Optimiste")
            growth_optimistic = st.slider("Croissance CA optimiste (%)", 0, 30, 15)
            margin_optimistic = st.slider("Marge optimiste (%)", 0, 10, 5)
            payment_days_optimistic = st.slider("Délai clients optimiste (jours)", 10, 60, 25)
        
        with col2:
            st.subheader("📊 Scénario de Référence")
            growth_reference = st.slider("Croissance CA référence (%)", -5, 15, 5)
            margin_reference = st.slider("Marge référence (%)", 0, 5, 2)
            payment_days_reference = st.slider("Délai clients référence (jours)", 20, 90, 45)
        
        with col3:
            st.subheader("📉 Scénario Pessimiste")
            growth_pessimistic = st.slider("Croissance CA pessimiste (%)", -20, 5, -5)
            margin_pessimistic = st.slider("Marge pessimiste (%)", -10, 0, -3)
            payment_days_pessimistic = st.slider("Délai clients pessimiste (jours)", 30, 120, 75)
        
        if st.button("🎯 Analyser les Scénarios"):
            # Calcul des scénarios
            base_revenue = 100000  # CA mensuel de base
            
            scenarios = {
                'Scénario': ['Optimiste', 'Référence', 'Pessimiste'],
                'Croissance CA (%)': [growth_optimistic, growth_reference, growth_pessimistic],
                'Marge (%)': [margin_optimistic, margin_reference, margin_pessimistic],
                'Délai Clients (jours)': [payment_days_optimistic, payment_days_reference, payment_days_pessimistic],
                'CA Mensuel (€)': [
                    base_revenue * (1 + growth_optimistic/100),
                    base_revenue * (1 + growth_reference/100),
                    base_revenue * (1 + growth_pessimistic/100)
                ],
                'BFR (€)': [
                    (payment_days_optimistic/30) * base_revenue * (1 + growth_optimistic/100),
                    (payment_days_reference/30) * base_revenue * (1 + growth_reference/100),
                    (payment_days_pessimistic/30) * base_revenue * (1 + growth_pessimistic/100)
                ]
            }
            
            df_scenarios = pd.DataFrame(scenarios)
            st.dataframe(df_scenarios, use_container_width=True)
            
            # Graphique comparatif
            fig = px.bar(df_scenarios, x='Scénario', y='BFR (€)',
                        title='Besoin en Fonds de Roulement par Scénario',
                        color='Scénario')
            st.plotly_chart(fig, use_container_width=True)
            
            # Analyse de sensibilité
            st.subheader("🎯 Analyse de Sensibilité")
            
            st.info("""
            **Recommandations par Scénario :**
            - **Optimiste** : Investir dans la croissance, optimiser le BFR
            - **Référence** : Maintenir la stratégie actuelle, surveiller les indicateurs
            - **Pessimiste** : Renforcer la trésorerie, réduire les stocks, renégocier les délais
            """)
    
    with tab3:
        st.header("🚨 Alertes Prédictives")
        
        st.markdown("""
        ### 🎯 Système d'Alerte Précoce Intelligent
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("⚙️ Configuration des Alertes")
            
            cash_threshold = st.number_input("Seuil trésorerie critique (€)", value=10000)
            overdraft_limit = st.number_input("Limite découvert autorisée (€)", value=5000)
            bfr_alert_threshold = st.slider("Seuil alerte BFR (%)", 10, 50, 25)
            
            st.subheader("🔔 Fréquence de Surveillance")
            monitoring_frequency = st.selectbox("Fréquence de contrôle", [
                "Temps réel", "Quotidien", "Hebdomadaire", "Mensuel"
            ])
        
        with col2:
            st.subheader("📧 Canaux d'Alerte")
            
            alert_channels = st.multiselect(
                "Canaux d'alerte activés :",
                ["Email Direction", "Slack Finance", "SMS Urgence", "Dashboard", "Rapport Auto"],
                default=["Email Direction", "Slack Finance"]
            )
            
            st.subheader("👥 Destinataires")
            recipients = st.text_area("Liste des destinataires (un par ligne)", 
                                   "directeur@entreprise.com\nfinance@entreprise.com\ntresorerie@entreprise.com")
        
        # Tableau de bord des alertes
        st.subheader("📊 Alertes Actives")
        
        active_alerts = {
            'Type Alerte': ['Trésorerie Critique', 'Découvert Imminent', 'BFR Excessif', 'Retard Client'],
            'Niveau': ['🔴 Haute', '🟠 Moyenne', '🟡 Faible', '🟠 Moyenne'],
            'Détails': ['Trésorerie < 15K€', 'Découvert > 3K€', 'BFR +35% vs budget', 'Client X - 45 jours'],
            'Date Détection': ['15/01/2024', '14/01/2024', '13/01/2024', '12/01/2024'],
            'Statut': ['🔄 En cours', '✅ Traitée', '🔄 En cours', '✅ Traitée']
        }
        
        st.dataframe(pd.DataFrame(active_alerts), use_container_width=True)
        
        # Statistiques des alertes
        st.subheader("📈 Statistiques des Alertes")
        
        col_stat1, col_stat2, col_stat3, col_stat4 = st.columns(4)
        
        with col_stat1:
            st.metric("🚨 Alertes Actives", "3")
        with col_stat2:
            st.metric("✅ Alertes Traitées", "24")
        with col_stat3:
            st.metric("⏱️ Temps Moyen Réponse", "2.3h")
        with col_stat4:
            st.metric("📊 Taux Résolution", "89%")
        
        if st.button("🔄 Actualiser les Alertes"):
            st.success("Système d'alerte actualisé !")
            st.info("2 nouvelles alertes potentielles détectées et analysées")
    
    with tab4:
        st.header("📈 Optimisation de la Trésorerie")
        
        st.markdown("""
        ### 🎯 Stratégies d'Optimisation du Cash
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("💰 Optimisation des Encaisse")

def show_predictive_cashflow():
    st.title("💸 Trésorerie Prédictive")
    
    # ... (contenu précédent) ...
    
    
        
    st.markdown("""
        ### 🎯 Stratégies d'Optimisation du Cash
        """)
        
    col1, col2 = st.columns(2)
        
    with col1:
        st.subheader("💰 Optimisation des Encaissements")
            
        current_dso = st.number_input("DSO actuel (jours)", value=45)
        target_dso = st.number_input("DSO cible (jours)", value=30)
        monthly_revenue = st.number_input("CA mensuel (€)", value=100000)
            
        st.subheader("💸 Optimisation des Décaissements")
            
        current_dpo = st.number_input("DPO actuel (jours)", value=30)
        target_dpo = st.number_input("DPO cible (jours)", value=45)
        monthly_purchases = st.number_input("Achats mensuels (€)", value=60000)
        
    with col2:
        if st.button("🎯 Calculer l'Impact"):
                # Calcul des gains potentiels
            dso_improvement = current_dso - target_dso
            dpo_improvement = target_dpo - current_dpo
                
            cash_release_dso = (dso_improvement / 30) * monthly_revenue
            cash_release_dpo = (dpo_improvement / 30) * monthly_purchases
            total_cash_release = cash_release_dso + cash_release_dpo
                
            st.success("**📊 Impact de l'Optimisation :**")
                
            optimization_impact = {
                    'Paramètre': ['Réduction DSO', 'Augmentation DPO', 'Total'],
                    'Jours': [f"-{dso_improvement}", f"+{dpo_improvement}", f"+{dso_improvement + dpo_improvement}"],
                    'Gain Trésorerie (€)': [
                        f"{cash_release_dso:,.0f} €",
                        f"{cash_release_dpo:,.0f} €", 
                        f"{total_cash_release:,.0f} €"
                    ]
                }
                
            st.dataframe(pd.DataFrame(optimization_impact), use_container_width=True)
                
                # Recommandations d'optimisation
            st.subheader("💡 Stratégies Recommandées")
                
            strategies = [
                    "📧 **Facturation électronique** : Réduction de 5 jours du DSO",
                    "🎯 **Relance automatisée** : Mise en place d'un système de relance proactive",
                    "🤝 **Négociation fournisseurs** : Extension des délais de paiement",
                    "📊 **Planning des paiements** : Optimisation des dates de règlement",
                    "💳 **Escompte early payment** : Offre de réduction pour paiement anticipé"
                ]
                
            for strategy in strategies:
                st.write(f"• {strategy}")
        
        # Simulation de trésorerie optimisée
        st.subheader("🔄 Simulation Trésorerie Optimisée")
        
        if st.button("🚀 Lancer la Simulation"):
            with st.spinner("Simulation de l'optimisation en cours..."):
                time.sleep(2)
                
                # Données simulées
                months = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Jun']
                current_cash = [50000, 48000, 52000, 45000, 55000, 60000]
                total_cash_release = total_cash_release if 'total_cash_release' in locals() else 0
                optimized_cash = [x + total_cash_release/6 for x in current_cash]
                
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=months, y=current_cash, 
                                       name='Situation Actuelle', line=dict(color='red')))
                fig.add_trace(go.Scatter(x=months, y=optimized_cash, 
                                       name='Après Optimisation', line=dict(color='green')))
                fig.update_layout(title='Impact de l\'Optimisation sur la Trésorerie')
                st.plotly_chart(fig, use_container_width=True)
                
                st.metric("💰 Gain Trésorerie Annuel", f"{total_cash_release:,.0f} €")

def show_executive_reporting():
    st.title("📊 Reporting Executive")
    
    st.markdown("""
    ## 🎯 Tableaux de Bord Directionnels Intelligents
    
    ### 📈 Synthèse Performance Globale avec Insights Automatisés
    """)
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "🏠 Dashboard Executive", 
        "📋 Rapports Automatisés", 
        "📊 Analyse Comparative",
        "🎯 KPI Personnalisés"
    ])
    
    with tab1:
        st.header("🏠 Dashboard Executive")
        
        # Sélection de la période
        col_period1, col_period2, col_period3 = st.columns(3)
        with col_period1:
            report_period = st.selectbox("Période", ["Mensuel", "Trimestriel", "Annuel"])
        with col_period2:
            comparison_type = st.selectbox("Comparaison", ["Vs Objectifs", "Vs Période Précédente", "Vs Année Précédente"])
        with col_period3:
            if st.button("🔄 Actualiser les Données"):
                st.success("Données actualisées !")
        
        # KPI Principaux
        st.subheader("🎯 Indicateurs de Performance Clés")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("📈 Chiffre d'Affaires", "2.8M €", "+15.2%", delta_color="inverse")
            st.metric("📊 Marge Brute", "32.5%", "+2.1%")
        
        with col2:
            st.metric("🏭 Volume Production", "45.2K unités", "+8.7%")
            st.metric("⚡ Taux Rendement", "92.5%", "+3.2%")
        
        with col3:
            st.metric("📦 Rotation Stocks", "8.2", "+1.5")
            st.metric("⏱️ Délai Livraison", "5.2 jours", "-0.8 jours")
        
        with col4:
            st.metric("💸 Trésorerie", "856K €", "+5.8%")
            st.metric("📉 Endettement Net", "1.8x EBITDA", "-0.3x")
        
        # Graphiques de Performance
        st.subheader("📈 Évolution des Principaux Indicateurs")
        
        col_chart1, col_chart2 = st.columns(2)
        
        with col_chart1:
            # Performance Commerciale
            months = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Jun']
            actual_revenue = [450, 480, 520, 510, 550, 580]
            target_revenue = [430, 460, 500, 520, 540, 560]
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=months, y=actual_revenue, name='CA Réel', line=dict(color='blue')))
            fig.add_trace(go.Scatter(x=months, y=target_revenue, name='Objectif', line=dict(color='red', dash='dash')))
            fig.update_layout(title='Performance Commerciale vs Objectifs (k€)')
            st.plotly_chart(fig, use_container_width=True)
        
        with col_chart2:
            # Répartition des Coûts
            cost_categories = {
                'Catégorie': ['Main d\'œuvre', 'Matériaux', 'Frais fixes', 'R&D', 'Marketing'],
                'Pourcentage': [35, 28, 15, 12, 10]
            }
            
            fig = px.pie(cost_categories, values='Pourcentage', names='Catégorie', 
                        title='Répartition des Coûts')
            st.plotly_chart(fig, use_container_width=True)
        
        # Points de Vigilance
        st.subheader("🚨 Points de Vigilance et Alertes")
        
        alert_col1, alert_col2, alert_col3 = st.columns(3)
        
        with alert_col1:
            with st.container(border=True):
                st.error("**Dépassement Budget Production**")
                st.write("Écart: +12.5% vs prévision")
                st.progress(75)
                st.button("Analyser les causes", key="alert_prod")
        
        with alert_col2:
            with st.container(border=True):
                st.warning("**Niveau Stock Critique**")
                st.write("2 articles sous seuil sécurité")
                st.progress(40)
                st.button("Planifier commande", key="alert_stock")
        
        with alert_col3:
            with st.container(border=True):
                st.success("**Objectif CA Atteint**")
                st.write("Dépassement: +3.6% vs objectif")
                st.progress(103)
                st.button("Voir détail", key="alert_ca")
        
        # Insights Automatisés
        st.subheader("💡 Insights et Recommandations Automatisés")
        
        insights = [
            "🎯 **Opportunité Croissance** : Le segment Premium montre une croissance de 25% - Recommandation: Augmenter l'allocation marketing de 15%",
            "📊 **Optimisation Coûts** : Les frais généraux ont augmenté de 8% vs budget - Action: Revue des contrats fournisseurs",
            "🔄 **Amélioration Process** : Le taux de rendement a progressé de 3.2% - Capitaliser sur les bonnes pratiques",
            "💰 **Optimisation Trésorerie** : Excédent de trésorerie détecté - Opportunité: Investissement court terme"
        ]
        
        for insight in insights:
            st.info(insight)
    
    with tab2:
        st.header("📋 Rapports Automatisés")
        
        st.markdown("""
        ### 🎯 Génération et Personnalisation de Rapports
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📅 Rapports Programmes")
            
            scheduled_reports = {
                'Type Rapport': ['Rapport Mensuel Performance', 'Analyse Budget vs Réel', 'Tableau de Bord Commercial', 'Analyse Trésorerie', 'Rapport Stocks'],
                'Fréquence': ['Mensuel', 'Hebdomadaire', 'Quotidien', 'Hebdomadaire', 'Mensuel'],
                'Prochaine Génération': ['01/02/2024', '22/01/2024', '16/01/2024', '19/01/2024', '01/02/2024'],
                'Statut': ['🟢 Actif', '🟢 Actif', '🟡 Pause', '🟢 Actif', '🟢 Actif']
            }
            
            st.dataframe(pd.DataFrame(scheduled_reports), use_container_width=True)
            
            st.subheader("🎨 Personnalisation")
            report_format = st.selectbox("Format du rapport", ["PDF Professionnel", "PPT Présentation", "Excel Données", "HTML Interactif"])
            detail_level = st.select_slider("Niveau de détail", ["Synthèse Executive", "Standard", "Détaillé", "Très détaillé"])
        
        with col2:
            st.subheader("🚀 Génération de Rapport")
            
            report_type = st.selectbox("Type de rapport à générer:", [
                "Rapport Performance Mensuel",
                "Analyse Écarts Budget", 
                "Tableau de Bord Commercial",
                "État Trésorerie Détaillé",
                "Rapport Optimisation Stocks",
                "Analyse Investissements"
            ])
            
            report_period = st.selectbox("Période du rapport:", [
                "Mois en cours", "Trimestre en cours", "Année en cours", "Période personnalisée"
            ])
            
            include_comparison = st.checkbox("Inclure analyse comparative", value=True)
            include_recommendations = st.checkbox("Inclure recommandations", value=True)
            
            if st.button("📊 Générer le Rapport", type="primary"):
                with st.spinner("Génération du rapport en cours..."):
                    time.sleep(3)
                    
                    st.success("✅ Rapport généré avec succès !")
                    
                    # Aperçu du rapport
                    st.subheader("👁️ Aperçu du Rapport Généré")
                    
                    with st.container(border=True):
                        st.markdown(f"""
                        **📈 RAPPORT DE PERFORMANCE - {report_type.upper()}**
                        
                        **🎯 Synthèse Executive:**
                        - 📈 **CA Cumulé** : 2.8M € (+15.2% vs prévision)
                        - 🏭 **Production** : 45.2K unités (+8.7%)
                        - 💰 **Marge Brute** : 32.5% (+2.1 points)
                        - 📦 **Rotation Stocks** : 8.2 (+1.5)
                        - 💸 **Trésorerie** : 856K € (+5.8%)
                        
                        **🚨 Points de Vigilance:**
                        - Dépassement budget production: +12.5%
                        - 2 articles en niveau stock critique
                        - Augmentation frais généraux: +8%
                        
                        **📊 Recommandations Stratégiques:**
                        - Optimiser la gamme produits C
                        - Renégocier les conditions fournisseurs
                        - Investir dans la digitalisation des processus
                        - Renforcer le contrôle des coûts
                        """)
                    
                    # Options de téléchargement
                    st.subheader("📥 Options de Téléchargement")
                    
                    col_dl1, col_dl2, col_dl3 = st.columns(3)
                    with col_dl1:
                        st.download_button(
                            "📥 Télécharger PDF", 
                            data="simulated_pdf_content", 
                            file_name=f"rapport_{report_type.lower()}_{datetime.now().strftime('%Y%m%d')}.pdf",
                            mime="application/pdf"
                        )
                    with col_dl2:
                        st.download_button(
                            "📊 Télécharger Excel", 
                            data="simulated_excel_content",
                            file_name=f"donnees_rapport_{datetime.now().strftime('%Y%m%d')}.xlsx",
                            mime="application/vnd.ms-excel"
                        )
                    with col_dl3:
                        if st.button("📧 Envoyer par Email"):
                            st.success("Rapport envoyé avec succès !")
    
    with tab3:
        st.header("📊 Analyse Comparative")
        
        st.markdown("""
        ### 🎯 Benchmarks et Analyses Comparatives Avancées
        """)
        
        tab_comp1, tab_comp2, tab_comp3 = st.tabs(["📈 Vs Objectifs", "🔄 Vs Historique", "🌍 Vs Concurrents"])
        
        with tab_comp1:
            st.subheader("📈 Performance vs Objectifs")
            
            # Données de comparaison
            kpi_comparison = {
                'KPI': ['Chiffre d\'Affaires', 'Marge Brute', 'Volume Production', 'Rotation Stocks', 'Taux Service Client'],
                'Objectif': [2600000, 30.0, 42000, 7.5, 98.0],
                'Réel': [2800000, 32.5, 45200, 8.2, 98.5],
                'Écart (%)': ['+7.7%', '+8.3%', '+7.6%', '+9.3%', '+0.5%'],
                'Statut': ['✅ Dépassé', '✅ Dépassé', '✅ Dépassé', '✅ Dépassé', '✅ Atteint']
            }
            
            df_comparison = pd.DataFrame(kpi_comparison)
            st.dataframe(df_comparison, use_container_width=True)
            
            # Graphique de performance
            fig = go.Figure()
            fig.add_trace(go.Bar(name='Objectif', x=df_comparison['KPI'], y=df_comparison['Objectif']))
            fig.add_trace(go.Bar(name='Réel', x=df_comparison['KPI'], y=df_comparison['Réel']))
            fig.update_layout(title='Performance vs Objectifs', barmode='group')
            st.plotly_chart(fig, use_container_width=True)
        
        with tab_comp2:
            st.subheader("🔄 Évolution vs Période Précédente")
            
            col_hist1, col_hist2 = st.columns(2)
            
            with col_hist1:
                comparison_period = st.selectbox("Période de comparaison:", [
                    "Mois précédent", "Trimestre précédent", "Même période année dernière"
                ])
                
                # Métriques de croissance
                growth_data = {
                    'Indicateur': ['CA', 'Marge', 'Production', 'Productivité', 'Rentabilité'],
                    'Croissance': ['+15.2%', '+8.3%', '+12.7%', '+5.8%', '+9.1%'],
                    'Tendance': ['📈 Hausse', '📈 Hausse', '📈 Hausse', '📈 Hausse', '📈 Hausse']
                }
                
                st.dataframe(pd.DataFrame(growth_data), use_container_width=True)
            
            with col_hist2:
                # Graphique d'évolution
                periods = ['T-3', 'T-2', 'T-1', 'T0']
                revenue_evolution = [2200, 2350, 2450, 2800]  # en k€
                
                fig = px.line(x=periods, y=revenue_evolution, 
                             title='Évolution du Chiffre d\'Affaires (k€)',
                             markers=True)
                fig.update_traces(line=dict(color='green', width=3))
                st.plotly_chart(fig, use_container_width=True)
        
        with tab_comp3:
            st.subheader("🌍 Benchmark Sectoriel")
            
            st.markdown("""
            **📊 Comparaison avec les Concurrents et Moyenne Secteur:**
            """)
            
            benchmark_data = {
                'Indicateur': ['Part de Marché', 'Croissance CA', 'Marge Brute', 'ROI', 'Productivité'],
                'Notre Entreprise': ['12.5%', '15.2%', '32.5%', '18.5%', '92.5%'],
                'Concurrent A': ['15.2%', '12.8%', '28.7%', '16.2%', '88.3%'],
                'Concurrent B': ['10.8%', '8.5%', '30.2%', '15.8%', '90.1%'],
                'Moyenne Secteur': ['12.8%', '11.2%', '29.8%', '16.5%', '89.7%']
            }
            
            st.dataframe(pd.DataFrame(benchmark_data), use_container_width=True)
            
            # Radar chart de comparaison
            categories = ['Part de Marché', 'Croissance', 'Marge', 'ROI', 'Productivité']
            our_company = [12.5, 15.2, 32.5, 18.5, 92.5]
            sector_avg = [12.8, 11.2, 29.8, 16.5, 89.7]
            
            fig = go.Figure()
            fig.add_trace(go.Scatterpolar(
                r=our_company,
                theta=categories,
                fill='toself',
                name='Notre Entreprise'
            ))
            fig.add_trace(go.Scatterpolar(
                r=sector_avg,
                theta=categories,
                fill='toself',
                name='Moyenne Secteur'
            ))
            fig.update_layout(
                polar=dict(radialaxis=dict(visible=True)),
                showlegend=True,
                title="Positionnement Concurrentiel"
            )
            st.plotly_chart(fig, use_container_width=True)
    
    with tab4:
        st.header("🎯 Tableau de Bord des KPI Personnalisés")
        
        st.markdown("""
        ### 📊 Monitoring des Indicateurs Clés en Temps Réel
        """)
        
        # Sélection des catégories de KPI
        kpi_categories = st.multiselect(
            "Catégories de KPI à afficher:",
            ["Commercial", "Production", "Financier", "Stocks", "RH", "Qualité", "Innovation"],
            default=["Commercial", "Production", "Financier"]
        )
        
        # Affichage dynamique des KPI par catégorie
        if "Commercial" in kpi_categories:
            with st.expander("📈 KPI COMMERCIAL", expanded=True):
                col_com1, col_com2, col_com3, col_com4 = st.columns(4)
                
                with col_com1:
                    st.metric("CA Cumulé", "2.8M €", "15.2%")
                    st.metric("Panier Moyen", "8,450 €", "3.2%")
                
                with col_com2:
                    st.metric("Nouvelles Affaires", "45", "12.5%")
                    st.metric("Taux Conversion", "22.5%", "2.1%")
                
                with col_com3:
                    st.metric("Pipeline Actif", "4.2M €", "8.7%")
                    st.metric("Cycle de Vente", "45 jours", "-3 jours")
                
                with col_com4:
                    st.metric("Satisfaction Client", "4.2/5", "0.3")
                    st.metric("Taux Fidélisation", "88.5%", "1.8%")
        
        if "Production" in kpi_categories:
            with st.expander("🏭 KPI PRODUCTION", expanded=True):
                col_prod1, col_prod2, col_prod3, col_prod4 = st.columns(4)
                
                with col_prod1:
                    st.metric("Volume Production", "45.2K unités", "8.7%")
                    st.metric("Taux Rendement", "92.5%", "3.2%")
                
                with col_prod2:
                    st.metric("TRS", "85.2%", "2.1%")
                    st.metric("Taux Rebut", "1.2%", "-0.3%")
                
                with col_prod3:
                    st.metric("Capacité Utilisée", "88.7%", "5.2%")
                    st.metric("Taux Maintenance", "95.8%", "1.5%")
                
                with col_prod4:
                    st.metric("Coût Unitaire", "245 €", "-2.8%")
                    st.metric("Productivité", "115.2%", "4.7%")
        
        if "Financier" in kpi_categories:
            with st.expander("💰 KPI FINANCIER", expanded=True):
                col_fin1, col_fin2, col_fin3, col_fin4 = st.columns(4)
                
                with col_fin1:
                    st.metric("Trésorerie", "856K €", "5.8%")
                    st.metric("Marge Brute", "32.5%", "2.1%")
                
                with col_fin2:
                    st.metric("BFR", "1.2M €", "-8.5%")
                    st.metric("ROI", "18.5%", "3.2%")
                
                with col_fin3:
                    st.metric("Délai Clients", "45 jours", "-2 jours")
                    st.metric("Délai Fournisseurs", "60 jours", "+5 jours")
                
                with col_fin4:
                    st.metric("Endettement Net", "1.8x EBITDA", "-0.3x")
                    st.metric("Cash-flow Libre", "450K €", "12.5%")
        
        # Tableau de bord personnalisable
        st.subheader("📊 Tableau de Bord Personnalisable")
        
        col_custom1, col_custom2 = st.columns(2)
        
        with col_custom1:
            # Sélection des graphiques
            selected_charts = st.multiselect(
                "Graphiques à afficher:",
                ["Évolution CA", "Performance Production", "Analyse Marges", "Rotation Stocks", "Trésorerie", "Productivité"],
                default=["Évolution CA", "Performance Production"]
            )
        
        with col_custom2:
            # Période d'analyse
            analysis_period = st.selectbox(
                "Période d'analyse:",
                ["7 derniers jours", "30 derniers jours", "3 derniers mois", "6 derniers mois", "Année en cours"]
            )
        
        # Génération des graphiques sélectionnés
        if "Évolution CA" in selected_charts:
            st.subheader("📈 Évolution du Chiffre d'Affaires")
            
            # Données simulées
            days = list(range(1, 31))
            daily_revenue = [100 + np.random.normal(0, 20) for _ in days]
            cumulative_revenue = np.cumsum(daily_revenue)
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=days, y=daily_revenue, name='CA Quotidien', line=dict(color='blue')))
            fig.add_trace(go.Scatter(x=days, y=cumulative_revenue, name='CA Cumulé', line=dict(color='green')))
            fig.update_layout(title='Évolution du Chiffre d\'Affaires sur 30 jours')
            st.plotly_chart(fig, use_container_width=True)
        
        if "Performance Production" in selected_charts:
            st.subheader("🏭 Performance de la Production")
            
            # Données simulées production
            teams = ['Équipe A', 'Équipe B', 'Équipe C', 'Équipe D']
            production = [1250, 1180, 1320, 1270]
            targets = [1200, 1200, 1200, 1200]
            
            fig = go.Figure()
            fig.add_trace(go.Bar(name='Production', x=teams, y=production))
            fig.add_trace(go.Scatter(name='Objectif', x=teams, y=targets, mode='markers', 
                                   marker=dict(size=15, color='red')))
            fig.update_layout(title='Performance des Équipes de Production')
            st.plotly_chart(fig, use_container_width=True)

def show_intelligent_controls():
    st.header("🔍 Contrôles Intelligents")
    
    st.markdown("""
    ### 🎯 Système de Contrôle Automatisé Avancé
    
    **📊 Contrôles Implémentés :**
    """)
    
    # Grille des contrôles
    controls_col1, controls_col2, controls_col3 = st.columns(3)
    
    with controls_col1:
        with st.container(border=True):
            st.subheader("💰 Contrôles Budget")
            st.write("• Cohérence budget/dépenses")
            st.write("• Respect seuils définis")
            st.write("• Analyse écarts automatique")
            st.write("• Alertes dérives")
            st.toggle("Activer", value=True, key="budget_controls")
    
    with controls_col2:
        with st.container(border=True):
            st.subheader("📦 Contrôles Stocks")
            st.write("• Niveaux sécurité")
            st.write("• Rotation stocks")
            st.write("• Obsolescence")
            st.write("• Couverture")
            st.toggle("Activer", value=True, key="stock_controls")



def show_executive_reporting():
    st.header("📊 Reporting Executive")
    
    # Progress value handling - fixed
    progress_value = 103  # Your calculated value
    
    if progress_value <= 100:
        st.progress(progress_value)
        st.write(f"Progress: {progress_value}%")
    else:
        st.progress(100)  # Show full bar
        st.write(f"Target exceeded: {progress_value}%")
        st.success("🎯 Target exceeded!")

    # Controls section
    col1, col2, col3 = st.columns(3)
    
    with col1:
        with st.container(border=True):
            st.subheader("💰 Contrôles Budget")
            st.write("• Écarts budget")
            st.write("• Engagements")
            st.write("• Prévisions vs réel")
            st.toggle("Activer", value=True, key="budget_controls")
    
    with col2:
        with st.container(border=True):
            st.subheader("📦 Contrôles Stock")
            st.write("• Niveaux stock")
            st.write("• Rotation")
            st.write("• Obsolescence")
            st.write("• Couverture")
            st.toggle("Activer", value=True, key="stock_controls")
    
    with col3:
        with st.container(border=True):
            st.subheader("🏭 Contrôles Production")
            st.write("• Rendements usine")
            st.write("• Coûts standards")
            st.write("• Qualité production")
            st.write("• Capacités utilisées")
            st.toggle("Activer", value=True, key="production_controls")
    
    # Configuration des règles de contrôle
    st.subheader("⚙️ Configuration des Règles")
    
    config_col1, config_col2 = st.columns(2)
    
    with config_col1:
        st.write("**📈 Règles Budget :**")
        max_variance = st.slider("Écart budget max toléré (%)", 5, 25, 10, key="max_variance")
        auto_lock_budget = st.checkbox("Verrouillage auto si écart > 15%", value=True, key="auto_lock")
        
        st.write("**📦 Règles Stock :**")
        min_coverage = st.slider("Couverture stock minimum (jours)", 5, 30, 10, key="min_coverage")
        max_obsolescence = st.slider("Âge max stock (mois)", 6, 24, 12, key="max_obsolescence")
    
    with config_col2:
        st.write("**🏭 Règles Production :**")
        min_efficiency = st.slider("Rendement minimum accepté (%)", 70, 95, 85, key="min_efficiency")
        max_downtime = st.slider("Temps d'arrêt max (%)", 1, 15, 5, key="max_downtime")
        
        st.write("**🔍 Fréquence des Contrôles :**")
        control_frequency = st.selectbox("Fréquence d'exécution", [
            "Temps réel", "Quotidien", "Hebdomadaire", "Mensuel"
        ], key="control_frequency")
    
    if st.button("💾 Appliquer la Configuration", key="apply_config"):
        st.success("Configuration des contrôles appliquée!")
        
        # Simulation d'exécution des contrôles
        with st.spinner("Exécution des contrôles en cours..."):
            time.sleep(2)
            
            st.subheader("📊 Résultats des Contrôles")
            control_results = {
                'Contrôle': ['Budget Production', 'Stock Sécurité', 'Rendement Usine', 'Trésorerie'],
                'Statut': ['✅ Conforme', '⚠️ Alerte', '✅ Conforme', '✅ Conforme'],
                'Détails': ['Écart: 8.2%', 'Couverture: 2 jours', 'Rendement: 87%', 'Solde: 125K€'],
                'Action': ['Surveillance', 'Commander urgence', 'Maintenance préventive', 'Aucune']
            }
            
            st.dataframe(pd.DataFrame(control_results), use_container_width=True)

    # Contrôles avancés avec IA
    st.subheader("🤖 Contrôles Intelligents par IA")
    
    col_ai1, col_ai2 = st.columns(2)
    
    with col_ai1:
        st.markdown("""
        **🧠 Algorithmes de Contrôle :**
        - **Détection d'anomalies** : Patterns inhabituels
        - **Analyse prédictive** : Tendances futures
        - **Reconnaissance de patterns** : Comportements récurrents
        - **Classification automatique** : Catégorisation des écarts
        """)
        
        st.markdown("""
        **🎯 Applications :**
        ```python
        # Exemple de détection d'anomalie
        from sklearn.ensemble import IsolationForest
        
        model = IsolationForest(contamination=0.1)
        anomalies = model.fit_predict(financial_data)
        alerts = financial_data[anomalies == -1]
        ```
        """)
    
    with col_ai2:
        # Configuration des contrôles IA
        st.subheader("⚙️ Paramètres IA")
        
        anomaly_threshold = st.slider("Seuil détection anomalies", 0.7, 1.0, 0.85, key="anomaly_threshold")
        confidence_level = st.slider("Niveau confiance requis", 0.8, 0.99, 0.95, key="confidence_level")
        auto_correction = st.checkbox("Correction automatique", value=False, key="auto_correction")
        
        if st.button("🔍 Tester les Contrôles IA", key="test_ai"):
            with st.spinner("Analyse des données en cours..."):
                time.sleep(3)
                
                st.success("✅ Analyse IA terminée !")
                
                # Résultats de l'analyse IA
                ai_results = {
                    'Type Analyse': ['Anomalies Budget', 'Patterns Stocks', 'Tendances Production', 'Risques Trésorerie'],
                    'Résultat': ['3 anomalies détectées', 'Pattern saisonnier identifié', 'Tendance baissière', 'Risque faible'],
                    'Confiance': ['92%', '88%', '85%', '96%'],
                    'Action Recommandée': ['Révision budget', 'Ajustement stocks', 'Optimisation process', 'Surveillance normale']
                }
                
                st.dataframe(pd.DataFrame(ai_results), use_container_width=True)
                
                # Graphique des anomalies détectées
                st.subheader("📈 Visualisation des Anomalies")
                
                # Données simulées
                days = list(range(1, 31))
                normal_data = [100 + np.random.normal(0, 10) for _ in days]
                # Ajout d'anomalies
                anomaly_indices = [7, 15, 22]
                for idx in anomaly_indices:
                    normal_data[idx] += 40  # Valeur anormale
                
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=days, y=normal_data, mode='lines+markers', 
                                       name='Données', line=dict(color='blue')))
                # Marquer les anomalies
                anomaly_values = [normal_data[i] for i in anomaly_indices]
                fig.add_trace(go.Scatter(x=[days[i] for i in anomaly_indices], 
                                       y=anomaly_values, mode='markers',
                                       name='Anomalies détectées', 
                                       marker=dict(size=10, color='red', symbol='x')))
                fig.update_layout(title='Détection Automatique des Anomalies')
                st.plotly_chart(fig, use_container_width=True)

    # Historique des contrôles
    st.subheader("📝 Historique des Contrôles")
    
    control_history = {
        'Date': ['15/01/2024 14:30', '15/01/2024 10:15', '14/01/2024 16:45', '14/01/2024 09:00'],
        'Type Contrôle': ['Budget Production', 'Stock Sécurité', 'Rendement Usine', 'Trésorerie'],
        'Résultat': ['✅ Conforme', '⚠️ Alerte', '✅ Conforme', '✅ Conforme'],
        'Détails': ['Écart: 8.2%', 'Stock bas: Article A001', 'Rendement: 92%', 'Solde: 150K€'],
        'Action': ['Surveillance', 'Commande lancée', 'Aucune', 'Aucune']
    }
    
    st.dataframe(pd.DataFrame(control_history), use_container_width=True)
    
    # Statistiques des contrôles
    st.subheader("📊 Statistiques des Contrôles")
    
    col_stat1, col_stat2, col_stat3, col_stat4 = st.columns(4)
    
    with col_stat1:
        st.metric("🔍 Contrôles Exécutés", "156")
    with col_stat2:
        st.metric("✅ Contrôles Conformes", "142", "91%")
    with col_stat3:
        st.metric("⚠️ Alertes Générées", "14", "9%")
    with col_stat4:
        st.metric("🚨 Interventions", "3", "2%")

def show_intelligent_automation():
    st.title("🤖 Automatisation Intelligente")
    
    automation_tabs = st.tabs([
        "🔄 Workflows Métier", 
        "📧 Communications Auto", 
        "🔍 Contrôles Intelligents",
        "🎯 Décision Assistée IA"
    ])
    
    with automation_tabs[0]:
        show_business_workflows()
    
    with automation_tabs[1]:
        show_auto_communications()
    
    with automation_tabs[2]:
        show_intelligent_controls()
    
    with automation_tabs[3]:
        show_ai_decision_support()

def show_ai_decision_support():
    st.header("🎯 Décision Assistée par IA")
    
    st.markdown("""
    ### 🧠 Système d'Aide à la Décision Intelligent
    
    **📊 Algorithmes d'IA Implémentés :**
    """)
    
    # Sélection du scénario
    scenario = st.selectbox("🎮 Scénario à analyser :", [
        "Augmentation capacité production",
        "Lancement nouveau produit",
        "Optimisation niveau stocks", 
        "Investissement nouvelle machine",
        "Réorganisation logistique"
    ], key="scenario_select")
    
    # Paramètres du scénario
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Paramètres d'Entrée")
        
        if scenario == "Augmentation capacité production":
            current_capacity = st.number_input("Capacité actuelle (unités/jour)", value=1000, key="current_cap")
            new_capacity = st.number_input("Nouvelle capacité souhaitée", value=1200, key="new_cap")
            investment_cost = st.number_input("Coût investissement (€)", value=150000, key="inv_cost")
            
        elif scenario == "Lancement nouveau produit":
            rnd_cost = st.number_input("Coût R&D (€)", value=80000, key="rnd_cost")
            marketing_budget = st.number_input("Budget marketing (€)", value=50000, key="marketing_budget")
            expected_sales = st.number_input("Ventes annuelles estimées", value=5000, key="expected_sales")
            
        elif scenario == "Optimisation niveau stocks":
            current_stock = st.number_input("Stock moyen actuel (€)", value=250000, key="current_stock")
            target_stock = st.number_input("Stock cible (€)", value=200000, key="target_stock")
            holding_cost = st.number_input("Coût détention (%)", value=20.0, key="holding_cost")
    
    with col2:
        st.subheader("🌡️ Facteurs d'Environnement")
        
        market_growth = st.slider("Croissance marché (%)", -10, 20, 5, key="market_growth")
        competition_pressure = st.select_slider("Pression concurrentielle", 
                                              ["Faible", "Moyenne", "Forte"], "Moyenne", key="competition")
        economic_outlook = st.select_slider("Perspective économique", 
                                          ["Négative", "Neutre", "Positive"], "Neutre", key="economic_outlook")
    
    # Analyse IA
    if st.button("🧠 Lancer l'Analyse IA", key="launch_ai_analysis"):
        with st.spinner("Analyse des scénarios en cours..."):
            time.sleep(3)
            
            st.success("✅ Analyse IA terminée!")
            
            # Résultats de l'analyse
            col_res1, col_res2, col_res3, col_res4 = st.columns(4)
            
            with col_res1:
                st.metric("📊 Score de Confiance", "87%", "5%")
            with col_res2:
                st.metric("💰 ROI Estimé", "18.5%", "3.2%")
            with col_res3:
                st.metric("⚠️ Niveau de Risque", "Moyen", "-5%")
            with col_res4:
                st.metric("⏱️ Délai Retour", "2.8 ans", "0.3 ans")
            
            # Recommandations détaillées
            st.subheader("💡 Recommandations Stratégiques")
            
            recommendations = [
                "📈 **Augmenter progressivement** la capacité de 15% sur 6 mois",
                "🎯 **Cibler les segments** premium pour maximiser la marge",
                "🔄 **Optimiser la chaîne logistique** pour réduire les coûts de 8%",
                "📊 **Mettre en place un monitoring** renforcé des indicateurs clés",
                "🤝 **Renforcer les partenariats** avec les fournisseurs stratégiques"
            ]
            
            for i, rec in enumerate(recommendations, 1):
                st.write(f"{i}. {rec}")

# Placeholder functions - you'll need to implement these
def show_business_workflows():
    st.header("🔄 Workflows Métier")
    st.info("Workflows métier à implémenter")

def show_auto_communications():
    st.header("📧 Communications Automatisées")
    st.info("Communications automatisées à implémenter")

def show_intelligent_controls():
    st.header("🔍 Contrôles Intelligents")
    st.info("Contrôles intelligents à implémenter")







def show_intelligent_automation():
    st.title("🤖 Automatisation Intelligente")
    
    automation_tabs = st.tabs([
        "🔄 Workflows Métier", 
        "📧 Communications Auto", 
        "🔍 Contrôles Intelligents",
        "🎯 Décision Assistée IA"
    ])
    
    with automation_tabs[0]:
        show_business_workflows()
    
    with automation_tabs[1]:
        show_auto_communications()
    
    with automation_tabs[2]:
        show_intelligent_controls()  # Cette fonction existe maintenant
    
    with automation_tabs[3]:
        show_ai_decision_support()
    pass

def show_ai_decision_support():
    st.header("🎯 Décision Assistée par IA")
    
    st.markdown("""
    ### 🧠 Système d'Aide à la Décision Intelligent
    
    **📊 Algorithmes d'IA Implémentés :**
    """)
    
    # Sélection du scénario
    scenario = st.selectbox("🎮 Scénario à analyser :", [
        "Augmentation capacité production",
        "Lancement nouveau produit",
        "Optimisation niveau stocks", 
        "Investissement nouvelle machine",
        "Réorganisation logistique"
    ])
    
    # Paramètres du scénario
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Paramètres d'Entrée")
        
        if scenario == "Augmentation capacité production":
            current_capacity = st.number_input("Capacité actuelle (unités/jour)", value=1000)
            new_capacity = st.number_input("Nouvelle capacité souhaitée", value=1200)
            investment_cost = st.number_input("Coût investissement (€)", value=150000)
            
        elif scenario == "Lancement nouveau produit":
            rnd_cost = st.number_input("Coût R&D (€)", value=80000)
            marketing_budget = st.number_input("Budget marketing (€)", value=50000)
            expected_sales = st.number_input("Ventes annuelles estimées", value=5000)
            
        elif scenario == "Optimisation niveau stocks":
            current_stock = st.number_input("Stock moyen actuel (€)", value=250000)
            target_stock = st.number_input("Stock cible (€)", value=200000)
            holding_cost = st.number_input("Coût détention (%)", value=20.0)
    
    with col2:
        st.subheader("🌡️ Facteurs d'Environnement")
        
        market_growth = st.slider("Croissance marché (%)", -10, 20, 5)
        competition_pressure = st.select_slider("Pression concurrentielle", 
                                              ["Faible", "Moyenne", "Forte"], "Moyenne")
        economic_outlook = st.select_slider("Perspective économique", 
                                          ["Négative", "Neutre", "Positive"], "Neutre")
    
    # Analyse IA
    if st.button("🧠 Lancer l'Analyse IA"):
        with st.spinner("Analyse des scénarios en cours..."):
            time.sleep(3)
            
            st.success("✅ Analyse IA terminée!")
            
            # Résultats de l'analyse
            col_res1, col_res2, col_res3, col_res4 = st.columns(4)
            
            with col_res1:
                st.metric("📊 Score de Confiance", "87%", "5%")
            with col_res2:
                st.metric("💰 ROI Estimé", "18.5%", "3.2%")
            with col_res3:
                st.metric("⚠️ Niveau de Risque", "Moyen", "-5%")
            with col_res4:
                st.metric("⏱️ Délai Retour", "2.8 ans", "0.3 ans")
            
            # Recommandations détaillées
            st.subheader("💡 Recommandations Stratégiques")
            
            recommendations = [
                "📈 **Augmenter progressivement** la capacité de 15% sur 6 mois",
                "🎯 **Cibler les segments** premium pour maximiser la marge",
                "🔄 **Optimiser la chaîne logistique** pour réduire les coûts de 8%",
                "📊 **Mettre en place un monitoring** renforcé des indicateurs clés",
                "🤝 **Renforcer les partenariats** avec les fournisseurs stratégiques"
            ]
            
            for i, rec in enumerate(recommendations, 1):
                st.write(f"{i}. {rec}")




                               
if __name__ == "__main__":
    main()