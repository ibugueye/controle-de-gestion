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

def main():
    # Sidebar navigation améliorée
    st.sidebar.title("🏢 Budget Management System")
    st.sidebar.markdown("---")
    
    sections = [
        "🏠 Accueil & Dashboard",
        "🔗 Intégrations Systèmes", 
        "🤖 Automatisation Avancée",
        "📚 Encyclopédie Budgétaire",
        "💰 Budget des Ventes IA",
        "🏭 Production Intelligente",
        "📦 Optimisation Stocks",
        "🏗️ Investissement Stratégique",
        "💸 Trésorerie Prédictive",
        "📊 Reporting Executive"
    ]
    choice = st.sidebar.radio("Navigation Principale:", sections)
    
    # Section d'intégration visible partout
    st.sidebar.markdown("---")
    st.sidebar.subheader("🔗 Statut des Intégrations")
    
    integration_status = {
        'Système': ['ERP SAP', 'CRM Salesforce', 'Power BI', 'Sage Compta', 'API Métier'],
        'Statut': ['✅ Connecté', '✅ Connecté', '🟡 Partiel', '🔴 En attente', '✅ Connecté'],
    }
    
    df_status = pd.DataFrame(integration_status)
    st.sidebar.dataframe(df_status, hide_index=True, use_container_width=True)

    if choice == "🏠 Accueil & Dashboard":
        show_advanced_dashboard()
    elif choice == "🔗 Intégrations Systèmes":
        show_system_integrations()
    elif choice == "🤖 Automatisation Avancée":
        show_automation_features()
    elif choice == "📚 Encyclopédie Budgétaire":
        show_budget_encyclopedia()
    elif choice == "💰 Budget des Ventes IA":
        show_ai_sales_budget()
    elif choice == "🏭 Production Intelligente":
        show_smart_production()
    elif choice == "📦 Optimisation Stocks":
        show_stock_optimization()
    elif choice == "🏗️ Investissement Stratégique":
        show_strategic_investment()
    elif choice == "💸 Trésorerie Prédictive":
        show_predictive_cashflow()
    elif choice == "📊 Reporting Executive":
        show_executive_reporting()

def show_advanced_dashboard():
    st.title("🏢 Tableau de Bord Intelligent")
    
    # KPI en temps réel
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("📈 CA Cumulé", "2.8M €", "+15.2%", delta_color="inverse")
    with col2:
        st.metric("🏭 Production", "45.2K unités", "+8.7%")
    with col3:
        st.metric("📦 Niveau Stocks", "18.5 jours", "-12.3%")
    with col4:
        st.metric("💸 Trésorerie", "856K €", "+5.8%")
    
    # Alertes automatiques
    st.subheader("🚨 Alertes Intelligentes")
    alert_col1, alert_col2, alert_col3 = st.columns(3)
    
    with alert_col1:
        st.error("**Dépassement Budget Production**\nÉcart: +12.5% vs prévision")
    with alert_col2:
        st.warning("**Niveau Stock Critique**\nArticle A001: 2 jours restants")
    with alert_col3:
        st.info("**Opportunité Investissement**\nROI potentiel: 22.3%")

def show_system_integrations():
    st.title("🔗 Architecture d'Intégration Systèmes")
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "🏗️ Architecture Globale", "🧾 ERP", "🛒 CRM", "💰 Comptabilité", "📊 BI", "🌐 API"
    ])
    
    with tab1:
        st.subheader("🏗️ Architecture d'Intégration Globale")
        
        st.markdown("""
        ### Pourquoi l'Intégration Système est Cruciale ?
        
        **🎯 Objectifs Stratégiques :**
        - **Élimination des silos** de données
        - **Automatisation** des flux d'information
        - **Décision en temps réel** basée sur des données consolidées
        - **Réduction des erreurs** manuelles
        - **Gain de productivité** : jusqu'à 40% de temps économisé
        
        **📊 Bénéfices Mesurables :**
        ```python
        # Avant intégration
        temps_traitement_manuel = 15  # heures/semaine
        taux_erreur_manuel = 8.5  # %
        
        # Après intégration  
        temps_traitement_auto = 2  # heures/semaine
        taux_erreur_auto = 0.5  # %
        ```
        """)
        
        # Diagramme d'architecture
        st.image("https://via.placeholder.com/800x400/4A90E2/FFFFFF?text=Architecture+Cloud+Modern+API-First", 
                caption="Architecture Microservices avec APIs REST")
    
    with tab2:
        st.subheader("🧾 Intégration ERP (SAP, Oracle, Sage)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **📦 Données Récupérées :**
            - Stocks en temps réel
            - Coûts de production
            - Commandes fournisseurs
            - Données clients
            - Données articles
            
            **🔌 Méthodes d'Intégration :**
            ```python
            # Exemple connexion SAP RFC
            import pyrfc
            connection = pyrfc.Connection(
                ashost='sap.server.com',
                sysnr='00',
                client='100',
                user='user',
                passwd='password'
            )
            
            # Appel fonction module
            result = connection.call('BAPI_MATERIAL_GET_LIST')
            ```
            """)
        
        with col2:
            st.markdown("""
            **🎯 Processus Automatisés :**
            
            1. **Synchronisation stocks** toutes les 15 min
            2. **Mise à jour coûts** en temps réel
            3. **Création commandes** automatique
            4. **Rapprochement** comptable auto
            
            **📈 Impact Business :**
            - Réduction délais de 65%
            - Exactitude données: 99.8%
            - Temps réel vs batch quotidien
            """)
            
            # Simulation données ERP
            erp_data = {
                'Module': ['MM', 'SD', 'PP', 'FI', 'CO'],
                'Statut': ['✅', '✅', '🟡', '✅', '🟡'],
                'Dernière Synchro': ['14:25', '14:23', '13:45', '14:28', '12:15']
            }
            st.dataframe(pd.DataFrame(erp_data), use_container_width=True)
    
    with tab3:
        st.subheader("🛒 Intégration CRM (Salesforce, HubSpot)")
        
        st.markdown("""
        ### Formules de Prévision des Ventes Intégrées
        
        **📈 Méthode des Moindres Carrés Améliorée :**
        """)
        
        # Démonstration interactive formule moindres carrés
        col1, col2 = st.columns(2)
        
        with col1:
            st.latex(r"""
            a = \frac{\sum{(x_i - \bar{x})(y_i - \bar{y})}}{\sum{(x_i - \bar{x})^2}}
            """)
            st.latex(r"""
            b = \bar{y} - a\bar{x}
            """)
            st.latex(r"""
            y = ax + b
            """)
        
        with col2:
            st.markdown("""
            **Où :**
            - $x_i$ : Période temporelle
            - $y_i$ : Ventes historiques  
            - $\bar{x}$ : Moyenne des périodes
            - $\bar{y}$ : Moyenne des ventes
            - $a$ : Pente de la droite
            - $b$ : Ordonnée à l'origine
            
            **🎯 Données CRM utilisées :**
            - Pipeline commercial
            - Taux de conversion
            - Cycle de vente
            - Segmentation clients
            """)
        
        # Simulation intégration CRM
        st.subheader("🔄 Flux de Données CRM")
        crm_metrics = {
            'KPI': ['Pipeline Actif', 'Taux Conversion', 'Cycle Vente', 'Panier Moyen'],
            'Valeur': ['4.2M €', '22.5%', '45 jours', '8,450 €'],
            'Source': ['Salesforce', 'HubSpot', 'Salesforce', 'ERP']
        }
        st.dataframe(pd.DataFrame(crm_metrics), use_container_width=True)
    
    with tab4:
        st.subheader("💰 Intégration Comptabilité (Cegid, Quadratus)")
        
        st.markdown("""
        ### Automatisation du Rapprochement Comptable
        
        **🔧 Algorithmes Utilisés :**
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **🧠 Reconnaissance Intelligente :**
            ```python
            def match_transactions(bank_stmt, accounting_data):
                matches = []
                for bank_tx in bank_stmt:
                    best_match = None
                    highest_score = 0
                    
                    for acc_tx in accounting_data:
                        score = similarity_score(bank_tx, acc_tx)
                        if score > 0.85:  # Seuil de confiance
                            matches.append((bank_tx, acc_tx))
                            
                return matches
            ```
            """)
        
        with col2:
            st.markdown("""
            **📊 Formules de Contrôle :**
            """)
            st.latex(r"""
            \text{Solde Vérifié} = \sum\text{Débits} - \sum\text{Crédits}
            """)
            st.latex(r"""
            \text{Écart} = |\text{Banque} - \text{Comptabilité}|
            """)
            st.latex(r"""
            \text{Taux Reconnaissance} = \frac{\text{Tx Appariés}}{\text{Tx Totaux}} \times 100
            """)
        
        # Statistiques automatisation
        st.subheader("📈 Impact de l'Automatisation")
        auto_stats = {
            'Processus': ['Saisie Écritures', 'Rapprochement', 'Contrôle TVA', 'Clôture'],
            'Avant (heures)': [20, 15, 8, 40],
            'Après (heures)': [2, 1, 0.5, 8],
            'Gain': ['90%', '93%', '94%', '80%']
        }
        st.dataframe(pd.DataFrame(auto_stats), use_container_width=True)
    
    with tab5:
        show_bi_integration()
    
    with tab6:
        show_api_integration()

def show_bi_integration():
    st.subheader("📊 Intégration Business Intelligence")
    
    st.markdown("""
    ### Architecture Data Lake + Data Warehouse
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **📊 Flux de Données BI :**
        
        ```sql
        -- Exemple requête OLAP
        SELECT 
            [Temps].[Trimestre],
            [Géographie].[Région],
            SUM([Ventes].[Montant]) AS CA,
            AVG([Ventes].[Marge]) AS Marge_Moyenne
        FROM 
            Cube_Ventes
        WHERE 
            [Temps].[Année] = 2024
        GROUP BY 
            [Temps].[Trimestre], 
            [Géographie].[Région]
        ```
        
        **🔗 Connecteurs Utilisés :**
        - Power BI DirectQuery
        - Tableau Web Data Connector
        - APIs REST personnalisées
        """)
    
    with col2:
        st.markdown("""
        **📈 Métriques Calculées Automatiquement :**
        """)
        
        # Formules KPI
        st.latex(r"""
        \text{CA Cumulé} = \sum_{i=1}^{n} \text{Ventes}_i
        """)
        
        st.latex(r"""
        \text{Croissance} = \frac{\text{CA}_t - \text{CA}_{t-1}}{\text{CA}_{t-1}} \times 100
        """)
        
        st.latex(r"""
        \text{Part de Marché} = \frac{\text{CA Entreprise}}{\text{CA Secteur}} \times 100
        """)
        
        # Dashboard intégré simulé
        st.metric("📊 Données Temps Réel", "15 sources connectées")
        st.metric("🔄 Actualisation", "Toutes les 30 min")
        st.metric("👥 Utilisateurs", "45 actifs")

def show_api_integration():
    st.subheader("🌐 APIs REST Personnalisées")
    
    st.markdown("""
    ### Architecture API-First Modern
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🔌 Endpoints Principaux :**
        
        ```python
        # API Budget Management
        POST /api/v1/budget/calculate
        GET /api/v1/sales/forecast/{period}
        PUT /api/v1/inventory/levels
        POST /api/v1/ai/predictions
        
        # Sécurité OAuth2
        HEADER: Authorization: Bearer {jwt_token}
        ```
        
        **📊 Format Réponse Standardisé :**
        ```json
        {
          "status": "success",
          "data": {
            "forecast": 450000,
            "confidence": 0.92,
            "factors": ["saisonnalité", "tendance"]
          },
          "metadata": {
            "timestamp": "2024-01-15T10:30:00Z",
            "version": "1.0"
          }
        }
        ```
        """)
    
    with col2:
        st.markdown("""
        **🛡️ Sécurité & Performance :**
        
        **Algorithmes de Sécurité :**
        ```python
        # Hachage mots de passe
        import bcrypt
        password_hash = bcrypt.hashpw(
            password.encode('utf-8'), 
            bcrypt.gensalt()
        )
        
        # Token JWT
        import jwt
        token = jwt.encode(
            {'user_id': 123, 'exp': datetime.utcnow() + timedelta(hours=24)},
            SECRET_KEY, 
            algorithm='HS256'
        )
        ```
        
        **📈 Monitoring des APIs :**
        - Latence < 200ms
        - Uptime 99.95%
        - Rate limiting
        - Logs centralisés
        """)
    
    # Test d'API interactif
    st.subheader("🧪 Testeur d'API Interactif")
    
    api_endpoint = st.selectbox("Endpoint à tester:", [
        "/api/v1/sales/forecast/next-quarter",
        "/api/v1/inventory/optimization",
        "/api/v1/financial/ratios"
    ])
    
    if st.button("🔍 Tester l'API"):
        with st.spinner("Appel API en cours..."):
            time.sleep(2)
            
            # Simulation réponse API
            mock_response = {
                "status": "success",
                "data": {
                    "forecast": 1250000,
                    "confidence_interval": [1180000, 1320000],
                    "calculation_details": {
                        "method": "moindres_carres",
                        "r_squared": 0.94,
                        "seasonal_adjustment": 1.15
                    }
                }
            }
            
            st.json(mock_response)
            
            st.success("✅ API fonctionnelle - Latence: 156ms")

def show_automation_features():
    st.title("🤖 Automatisation Avancée des Processus")
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "🔄 Workflows Intelligents", "📧 Communications Auto", "🔍 Contrôles Auto", "🎯 Décision Assistée"
    ])
    
    with tab1:
        st.subheader("🔄 Workflows Métier Automatisés")
        
        st.markdown("""
        ### Architecture de Automatisation
        
        **⚙️ Processus Automatisés :**
        """)
        
        # Diagramme de workflow
        workflow_steps = {
            'Étape': ['Déclencheur', 'Collecte Données', 'Calcul', 'Validation', 'Action', 'Reporting'],
            'Technologie': ['Webhook', 'API REST', 'Python/Pandas', 'Règles Métier', 'ERP API', 'Email/BI'],
            'Exemple': ['Nouvelle vente CRM', 'Extraction stocks ERP', 'Calcul besoin production', 'Seuil alerte 10%', 'Création commande auto', 'Dashboard temps réel']
        }
        
        st.dataframe(pd.DataFrame(workflow_steps), use_container_width=True)
        
        # Exemple code automation
        st.subheader("🧠 Code d'Automatisation Intelligent")
        
        code = """
        # Workflow Automatisé Budget des Ventes
        def automated_sales_budget_workflow():
            # 1. Déclencheur - Nouveau mois
            trigger_date = datetime.now()
            
            # 2. Collecte données multi-sources
            sales_data = get_crm_sales_data()
            market_data = get_market_indices()
            stock_data = get_erp_inventory()
            
            # 3. Calcul prévisions IA
            forecast = ai_sales_forecast(
                historical_data=sales_data,
                market_conditions=market_data,
                stock_levels=stock_data
            )
            
            # 4. Validation automatique
            if forecast.confidence > 0.85:
                # 5. Action - Mise à jour budget
                update_budget_system(forecast)
                
                # 6. Reporting automatique
                send_automated_report(forecast)
                
            return forecast
        """
        
        st.code(code, language='python')
    
    with tab2:
        show_communication_automation()
    
    with tab3:
        show_auto_controls()
    
    with tab4:
        show_decision_support()

def show_communication_automation():
    st.subheader("📧 Automatisation des Communications")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🤖 Scénarios Automatisés :**
        
        **🎯 Alertes Budget :**
        ```python
        def check_budget_alerts(actual, budget, threshold=0.1):
            variance = (actual - budget) / budget
            if abs(variance) > threshold:
                send_alert(
                    recipient="direction@entreprise.com",
                    subject=f"Alerte Budget - Écart {variance:.1%}",
                    message=f"Budget: {budget}, Réel: {actual}"
                )
        ```
        
        **📊 Rapports Auto :**
        - Rapport mensuel performance
        - Alertes seuils dépassés
        - Suggestions optimisation
        - Benchmark sectoriel
        """)
    
    with col2:
        st.markdown("""
        **🔔 Canaux de Communication :**
        
        **📧 Email Intelligent :**
        ```python
        def send_automated_report(metrics):
            html_template = '''
            <h3>Rapport Automatisé Performance</h3>
            <p>CA: {revenue}</p>
            <p>Marge: {margin}%</p>
            <p>Recommandation: {recommendation}</p>
            '''
            send_email(html_template.format(**metrics))
        ```
        
        **💬 Slack/Teams :**
        - Notifications temps réel
        - Approbations workflows
        - Alertes critiques
        """)
        
        # Test de notification
        if st.button("🧪 Tester Notification"):
            st.success("✅ Notification envoyée avec succès!")
            st.info("📧 Email: alerte@entreprise.com")
            st.info("💬 Slack: #alerts-budget")

def show_auto_controls():
    st.subheader("🔍 Contrôles Automatiques Intelligents")
    
    st.markdown("""
    ### Système de Contrôle Continu
    
    **🎯 Contrôles Implémentés :**
    """)
    
    controls_grid = st.columns(3)
    
    with controls_grid[0]:
        st.markdown("""
        **💰 Contrôles Budget :**
        - Cohérence budget/dépenses
        - Respect seuils
        - Analyse écarts
        - Alertes dérives
        """)
    
    with controls_grid[1]:
        st.markdown("""
        **📦 Contrôles Stocks :**
        - Niveaux sécurité
        - Rotation stocks
        - Obsolescence
        - Couverture
        """)
    
    with controls_grid[2]:
        st.markdown("""
        **🏭 Contrôles Production :**
        - Rendements usine
        - Coûts standards
        - Qualité production
        - Capacités utilisées
        """)
    
    # Formules de contrôle
    st.subheader("📐 Formules de Contrôle Automatisées")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.latex(r"""
        \text{Écart Budget} = \frac{\text{Réel} - \text{Prévision}}{\text{Prévision}} \times 100
        """)
        
        st.latex(r"""
        \text{Seuil Alerte} = \mu \pm 2\sigma
        """)
        
        st.latex(r"""
        \text{Rotation Stocks} = \frac{\text{COGS}}{\text{Stock Moyen}}
        """)
    
    with col2:
        st.latex(r"""
        \text{Couverture} = \frac{\text{Stock}}{\text{Consommation Moyenne}}
        """)
        
        st.latex(r"""
        \text{Rendement} = \frac{\text{Output}}{\text{Input}} \times 100
        """)
        
        st.latex(r"""
        \text{Capacité Utilisée} = \frac{\text{Production Réelle}}{\text{Capacité Max}} \times 100
        """)

def show_decision_support():
    st.subheader("🎯 Système d'Aide à la Décision")
    
    st.markdown("""
    ### Intelligence Artificielle pour la Décision
    
    **🧠 Algorithmes Utilisés :**
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **📈 Prévision Saisonnière :**
        ```python
        from statsmodels.tsa.seasonal import seasonal_decompose
        
        # Décomposition série temporelle
        decomposition = seasonal_decompose(
            sales_data, 
            model='multiplicative', 
            period=12
        )
        
        trend = decomposition.trend
        seasonal = decomposition.seasonal
        residual = decomposition.resid
        ```
        
        **🎯 Classification Clients :**
        - RFM (Récence, Fréquence, Montant)
        - Clustering comportemental
        - Scoring potentiel
        """)
    
    with col2:
        st.markdown("""
        **📊 Analyse de Scénarios :**
        ```python
        def scenario_analysis(base_case, optimistic, pessimistic):
            return {
                'best_case': optimistic * 1.15,
                'worst_case': pessimistic * 0.85,
                'expected': base_case,
                'confidence_interval': [pessimistic, optimistic]
            }
        ```
        
        **🔍 Détection Anomalies :**
        - Machine Learning non supervisé
        - Règles métier
        - Analyse trend
        """)
    
    # Simulation décision assistée
    st.subheader("🎮 Simulateur de Décision")
    
    scenario = st.selectbox("Scénario à simuler:", [
        "Augmentation capacité production",
        "Lancement nouveau produit", 
        "Optimisation niveau stocks",
        "Investissement nouvelle machine"
    ])
    
    if st.button("🎯 Lancer la Simulation IA"):
        with st.spinner("Analyse des scénarios en cours..."):
            time.sleep(3)
            
            # Résultats simulation
            st.success("✅ Analyse terminée!")
            
            results_col1, results_col2, results_col3 = st.columns(3)
            
            with results_col1:
                st.metric("ROI Estimé", "18.5%", "3.2%")
            with results_col2:
                st.metric("Risque", "Moyen", "-5%")
            with results_col3:
                st.metric("Délai Retour", "2.8 ans", "0.3 ans")
            
            st.info("**🎯 Recommandation IA:** Projet recommandé avec surveillance trimestrielle")

def show_budget_encyclopedia():
    st.title("📚 Encyclopédie du Contrôle de Gestion")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "💰 Budget des Ventes", "🏭 Budget Production", "📦 Gestion Stocks", 
        "🏗️ Investissement", "💸 Trésorerie"
    ])
    
    with tab1:
        show_sales_budget_theory()
    
    with tab2:
        show_production_budget_theory()
    
    with tab3:
        show_stock_management_theory()
    
    with tab4:
        show_investment_theory()
    
    with tab5:
        show_cashflow_theory()

def show_sales_budget_theory():
    st.header("💰 Théorie du Budget des Ventes")
    
    st.markdown("""
    ## 📚 Fondements Théoriques et Formules
    
    ### 🎯 Méthode des Moindres Carrés
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **📐 Formules Mathématiques :**
        
        **Droite de régression :**
        """)
        st.latex(r"y = ax + b")
        
        st.markdown("""
        **Calcul de la pente a :**
        """)
        st.latex(r"""
        a = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n}(x_i - \bar{x})^2}
        """)
        
        st.markdown("""
        **Calcul de l'ordonnée à l'origine b :**
        """)
        st.latex(r"b = \bar{y} - a\bar{x}")
    
    with col2:
        st.markdown("""
        **📊 Coefficients Saisonniers :**
        
        **Calcul du coefficient :**
        """)
        st.latex(r"""
        C_s = \frac{\bar{V}_s}{\bar{V}_t}
        """)
        
        st.markdown("""
        Où :
        - $C_s$ : Coefficient saisonnier
        - $\bar{V}_s$ : Moyenne des ventes pour la saison s
        - $\bar{V}_t$ : Moyenne générale des ventes
        
        **Ajustement saisonnier :**
        """)
        st.latex(r"""
        V_{ajustée} = V_{trend} \times C_s
        """)
    
    # Démonstration interactive
    st.subheader("🧮 Calculateur Interactif")
    
    col1, col2 = st.columns(2)
    
    with col1:
        periods = st.number_input("Nombre de périodes:", min_value=3, max_value=24, value=6)
        x_values = list(range(1, periods + 1))
        y_values = []
        
        st.write("Saisissez les ventes historiques:")
        for i in range(periods):
            y_val = st.number_input(f"Période {i+1}:", value=100 + i*20, key=f"y_{i}")
            y_values.append(y_val)
    
    with col2:
        if st.button("📊 Calculer la Prévision"):
            # Calcul des moindres carrés
            x_mean = np.mean(x_values)
            y_mean = np.mean(y_values)
            
            numerator = sum((x - x_mean) * (y - y_mean) for x, y in zip(x_values, y_values))
            denominator = sum((x - x_mean) ** 2 for x in x_values)
            
            a = numerator / denominator
            b = y_mean - a * x_mean
            
            st.success(f"**Équation trouvée :** y = {a:.2f}x + {b:.2f}")
            
            # Prévision
            next_period = periods + 1
            forecast = a * next_period + b
            st.metric(f"Prévision Période {next_period}", f"{forecast:.0f}")

# Continuer avec les autres fonctions théoriques...
def show_production_budget_theory():
    st.header("🏭 Théorie du Budget de Production")
    
    st.markdown("""
    ## 📚 Concepts Fondamentaux
    
    ### 🎯 Équation Fondamentale de Production
    """)
    
    st.latex(r"""
    \text{Production} = \text{Ventes Prévues} + \text{Stock Final Cible} - \text{Stock Initial}
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **📊 Formules Clés :**
        
        **Coût de Production :**
        """)
        st.latex(r"""
        C_{production} = \sum (QM_i \times PU_i) + \text{Main d'œuvre} + \text{Frais}
        """)
        
        st.markdown("""
        **Rendement :**
        """)
        st.latex(r"""
        R = \frac{\text{Output}}{\text{Input}} \times 100
        """)
    
    with col2:
        st.markdown("""
        **📈 Indicateurs Performance :**
        
        **Taux de Rendement Synthétique :**
        """)
        st.latex(r"""
        TRS = \frac{\text{Temps Utile}}{\text{Temps Total}} \times 100
        """)
        
        st.markdown("""
        **Coût Standard :**
        """)
        st.latex(r"""
        C_{standard} = \text{Matieres} + \text{Main d'œuvre} + \text{Frais}
        """)

# Les autres fonctions show_* suivent le même pattern avec explications théoriques détaillées
def show_budget_ventes():
    st.markdown('<div class="main-header">💰 Budget des Ventes</div>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["📋 Méthodologie", "📈 Prévisions", "⚙️ Optimisation", "🎯 Simulation"])
    
    with tab1:
        st.markdown('<div class="section-header">📋 Méthodes de Prévision des Ventes</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 🎯 Trois Approches Complémentaires
            
            1. **Études de Marché**
               - Analyse de la demande
               - Concurrence
               - Conjoncture économique
            
            2. **Fichiers Clients**
               - Historique des ventes
               - Cartographie de la demande
               - Comportement d'achat
            
            3. **Techniques d'Ajustement**
               - Série chronologique
               - Méthode des moindres carrés
               - Coefficients saisonniers
            """)
        
        with col2:
            st.markdown("""
            ### 📊 Méthode des Moindres Carrés
            
            **Objectif** : Trouver la droite y = ax + b qui minimise les écarts
            
            **Formules** :
            - a = Σ(xy) - n·x̄·ȳ / Σ(x²) - n·x̄²
            - b = ȳ - a·x̄
            
            **Application** : Prévision des ventes futures basée sur l'historique
            """)
            
            # Exemple visuel
            x = np.array([1, 2, 3, 4, 5])
            y = np.array([2, 4, 5, 4, 5])
            
            a, b = np.polyfit(x, y, 1)
            y_pred = a * x + b
            
            fig, ax = plt.subplots()
            ax.scatter(x, y, color='blue', label='Données réelles')
            ax.plot(x, y_pred, color='red', label=f'Droite: y = {a:.2f}x + {b:.2f}')
            ax.set_xlabel('Période')
            ax.set_ylabel('Ventes')
            ax.legend()
            ax.set_title('Ajustement Linéaire - Moindres Carrés')
            st.pyplot(fig)
    
    with tab2:
        st.markdown('<div class="section-header">📈 Outil de Prévision des Ventes</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Données Historiques")
            
            # Entrée des données
            periods = st.number_input("Nombre de périodes historiques:", min_value=3, max_value=12, value=6)
            
            st.write("Saisissez les ventes historiques :")
            ventes_historiques = []
            for i in range(int(periods)):
                vente = st.number_input(f"Période {i+1} (ventes):", value=100*(i+1))
                ventes_historiques.append(vente)
            
            # Calcul des prévisions
            if len(ventes_historiques) >= 3:
                x = np.arange(1, len(ventes_historiques) + 1)
                y = np.array(ventes_historiques)
                
                a, b = np.polyfit(x, y, 1)
                
                st.markdown(f"""
                <div class="info-box">
                **Équation de prévision** : y = {a:.2f}x + {b:.2f}
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.subheader("Prévisions Futures")
            
            if len(ventes_historiques) >= 3:
                periode_future = st.number_input("Période à prévoir:", min_value=1, value=len(ventes_historiques)+1)
                prevision = a * periode_future + b
                
                st.metric(f"Prévision période {periode_future}", f"{prevision:.0f} unités")
                
                # Graphique des prévisions
                x_future = np.arange(1, periode_future + 1)
                y_future = a * x_future + b
                
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name='Historique', 
                                       marker=dict(size=10, color='blue')))
                fig.add_trace(go.Scatter(x=x_future, y=y_future, mode='lines', name='Prévision',
                                       line=dict(color='red', dash='dash')))
                fig.update_layout(title='Prévisions des Ventes', xaxis_title='Période', yaxis_title='Ventes')
                st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.markdown('<div class="section-header">⚙️ Optimisation des Ressources Commerciales</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Allocation du Budget Commercial")
            
            budget_total = st.number_input("Budget commercial total (k€):", value=500)
            
            st.write("**Répartition par canal**:")
            digital = st.slider("Digital (%)", 0, 100, 40)
            evenements = st.slider("Événements (%)", 0, 100, 25)
            pub_traditionnelle = st.slider("Publicité traditionnelle (%)", 0, 100, 20)
            relations_presse = st.slider("Relations presse (%)", 0, 100, 15)
            
            # Vérification que la somme fait 100%
            total = digital + evenements + pub_traditionnelle + relations_presse
            if total != 100:
                st.warning(f"La somme des pourcentages est de {total}%. Ajustez pour atteindre 100%.")
        
        with col2:
            st.subheader("Rentabilité par Canal")
            
            if total == 100:
                # Calcul des budgets par canal
                budget_digital = budget_total * digital / 100
                budget_evenements = budget_total * evenements / 100
                budget_pub = budget_total * pub_traditionnelle / 100
                budget_rp = budget_total * relations_presse / 100
                
                # Efficacité supposée par canal (ROI)
                roi_digital = 3.5  # Pour 1€ investi, retour de 3.5€
                roi_evenements = 2.0
                roi_pub = 1.5
                roi_rp = 2.5
                
                # Calcul des retours
                retour_digital = budget_digital * roi_digital
                retour_evenements = budget_evenements * roi_evenements
                retour_pub = budget_pub * roi_pub
                retour_rp = budget_rp * roi_rp
                
                data = {
                    'Canal': ['Digital', 'Événements', 'Publicité', 'Relations Presse'],
                    'Budget (k€)': [budget_digital, budget_evenements, budget_pub, budget_rp],
                    'ROI': [roi_digital, roi_evenements, roi_pub, roi_rp],
                    'Retour estimé (k€)': [retour_digital, retour_evenements, retour_pub, retour_rp]
                }
                
                df_optimisation = pd.DataFrame(data)
                
                fig = px.bar(df_optimisation, x='Canal', y=['Budget (k€)', 'Retour estimé (k€)'],
                            title='Optimisation du Budget Commercial',
                            barmode='group')
                st.plotly_chart(fig, use_container_width=True)
                
                st.metric("Retour total estimé", f"{sum(df_optimisation['Retour estimé (k€)']):.0f} k€")
                st.metric("ROI moyen", f"{(sum(df_optimisation['Retour estimé (k€)']) / budget_total):.2f}")
    
    with tab4:
        st.markdown('<div class="section-header">🎯 Simulation Complète du Budget des Ventes</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Scénarios de Vente")
            
            scenario = st.selectbox("Choisissez un scénario:", 
                                  ["Optimiste", "Réaliste", "Pessimiste"])
            
            if scenario == "Optimiste":
                croissance = 15
                part_marche = 8
            elif scenario == "Réaliste":
                croissance = 10
                part_marche = 5
            else:  # Pessimiste
                croissance = 5
                part_marche = 3
            
            ca_annee_precedente = st.number_input("CA année précédente (k€):", value=10000)
            budget_marketing = st.number_input("Budget marketing (k€):", value=500)
            
        with col2:
            st.subheader("Résultats de la Simulation")
            
            # Calculs basés sur le scénario
            ca_projete = ca_annee_precedente * (1 + croissance/100)
            impact_marketing = budget_marketing * 2  # Multiplicateur simplifié
            ca_final = ca_projete + impact_marketing
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Croissance marché", f"{croissance}%")
            col2.metric("Part de marché", f"{part_marche}%")
            col3.metric("CA projeté", f"{ca_final:,.0f} k€")
            
            # Graphique d'évolution
            mois = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Jun', 'Jul', 'Aoû', 'Sep', 'Oct', 'Nov', 'Déc']
            if scenario == "Optimiste":
                evolution = [800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350]
            elif scenario == "Réaliste":
                evolution = [800, 820, 840, 860, 880, 900, 920, 940, 960, 980, 1000, 1020]
            else:
                evolution = [800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910]
            
            fig = px.line(x=mois, y=evolution, title=f'Évolution du CA - Scénario {scenario}',
                         labels={'x': 'Mois', 'y': 'Chiffre d\'affaires (k€)'})
            st.plotly_chart(fig, use_container_width=True)

def show_budget_production():
    st.markdown('<div class="main-header">🏭 Budget de Production</div>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["📊 Programmation Linéaire", "⚙️ Optimisation Ressources", "🔧 Simulation Production"])
    
    with tab1:
        st.markdown('<div class="section-header">📊 Optimisation par Programmation Linéaire</div>', unsafe_allow_html=True)
        
        st.markdown("""
        ### 🎯 Maximisation de la Marge sur Coûts Variables
        
        **Fonction économique** : Z = Marge₁·x + Marge₂·y → **Max**
        
        **Sous contraintes** :
        - Capacité de production
        - Contraintes commerciales
        - Ressources limitées
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Données des Produits")
            
            st.write("**Produit A**")
            marge_a = st.number_input("Marge unitaire Produit A (€):", value=55.0)
            temps_usinage_a = st.number_input("Temps usinage A (h):", value=1.0)
            temps_montage_a = st.number_input("Temps montage A (h):", value=1.2)
            aluminium_a = st.number_input("Aluminium A (kg):", value=0.6)
            demande_a = st.number_input("Demande max Produit A:", value=10000)
            
            st.write("**Produit B**")
            marge_b = st.number_input("Marge unitaire Produit B (€):", value=90.0)
            temps_usinage_b = st.number_input("Temps usinage B (h):", value=1.5)
            temps_montage_b = st.number_input("Temps montage B (h):", value=1.0)
            aluminium_b = st.number_input("Aluminium B (kg):", value=0.8)
            demande_b = st.number_input("Demande max Produit B:", value=8000)
        
        with col2:
            st.subheader("Contraintes de Production")
            
            capacite_usinage = st.number_input("Capacité usinage (h):", value=13000)
            capacite_montage = st.number_input("Capacité montage (h):", value=10000)
            stock_aluminium = st.number_input("Stock aluminium (kg):", value=12000)
            
            if st.button("Calculer la Production Optimale"):
                # Résolution du problème d'optimisation
                c = [-marge_a, -marge_b]  # Negative pour maximisation
                
                # Contraintes
                A = [
                    [temps_usinage_a, temps_usinage_b],      # Usinage
                    [temps_montage_a, temps_montage_b],      # Montage
                    [aluminium_a, aluminium_b],              # Aluminium
                    [1, 0],                                  # Demande A
                    [0, 1]                                   # Demande B
                ]
                
                b = [capacite_usinage, capacite_montage, stock_aluminium, demande_a, demande_b]
                
                bounds = [(0, None), (0, None)]
                
                result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
                
                if result.success:
                    prod_a = result.x[0]
                    prod_b = result.x[1]
                    marge_totale = -result.fun
                    
                    st.success("✅ Solution optimale trouvée !")
                    
                    col1, col2, col3 = st.columns(3)
                    col1.metric("Production A", f"{prod_a:.0f} unités")
                    col2.metric("Production B", f"{prod_b:.0f} unités")
                    col3.metric("Marge Totale", f"{marge_totale:,.0f} €")
                    
                    # Graphique des contraintes
                    x = np.linspace(0, max(demande_a, demande_b), 100)
                    
                    # Contrainte usinage
                    y_usinage = (capacite_usinage - temps_usinage_a * x) / temps_usinage_b
                    # Contrainte montage
                    y_montage = (capacite_montage - temps_montage_a * x) / temps_montage_b
                    # Contrainte aluminium
                    y_alu = (stock_aluminium - aluminium_a * x) / aluminium_b
                    
                    fig, ax = plt.subplots(figsize=(10, 6))
                    
                    ax.plot(x, y_usinage, label='Usinage', color='red')
                    ax.plot(x, y_montage, label='Montage', color='blue')
                    ax.plot(x, y_alu, label='Aluminium', color='green')
                    ax.axvline(demande_a, color='orange', label='Demande A')
                    ax.axhline(demande_b, color='purple', label='Demande B')
                    
                    # Zone réalisable
                    y_min = np.minimum.reduce([y_usinage, y_montage, y_alu, np.full_like(x, demande_b)])
                    ax.fill_between(x, 0, y_min, where=(x <= demande_a), alpha=0.3, color='gray', label='Zone réalisable')
                    
                    # Point optimal
                    ax.plot(prod_a, prod_b, 'ro', markersize=10, label='Solution optimale')
                    
                    ax.set_xlim(0, demande_a * 1.1)
                    ax.set_ylim(0, demande_b * 1.1)
                    ax.set_xlabel('Production A')
                    ax.set_ylabel('Production B')
                    ax.legend()
                    ax.set_title('Espace des Solutions - Programmation Linéaire')
                    ax.grid(True, alpha=0.3)
                    
                    st.pyplot(fig)
    
    with tab2:
        st.markdown('<div class="section-header">⚙️ Optimisation des Ressources de Production</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Ressources Disponibles")
            
            ouvriers = st.number_input("Nombre d'ouvriers:", value=50)
            heures_travail = st.number_input("Heures travaillées/semaine:", value=35)
            machines = st.number_input("Nombre de machines:", value=20)
            rendement_machine = st.slider("Rendement machines (%)", 50, 100, 85)
            
            st.subheader("Coûts de Production")
            cout_horaire = st.number_input("Coût horaire main d'œuvre (€):", value=25.0)
            cout_machine = st.number_input("Coût machine/heure (€):", value=15.0)
            cout_matiere = st.number_input("Coût matière/unité (€):", value=10.0)
        
        with col2:
            st.subheader("Optimisation de la Capacité")
            
            # Calcul de la capacité
            heures_disponibles = ouvriers * heures_travail * 4  # Par mois
            capacite_theorique = machines * heures_disponibles * rendement_machine / 100
            
            # Calcul des coûts
            cout_main_oeuvre = heures_disponibles * cout_horaire
            cout_machines = capacite_theorique * cout_machine
            cout_fixe = cout_main_oeuvre + cout_machines
            
            production_souhaitee = st.number_input("Production souhaitée (unités/mois):", value=10000)
            
            if production_souhaitee > 0:
                cout_variable = production_souhaitee * cout_matiere
                cout_total = cout_fixe + cout_variable
                cout_unitaire = cout_total / production_souhaitee
                
                st.metric("Capacité théorique mensuelle", f"{capacite_theorique:.0f} unités")
                st.metric("Coût total de production", f"{cout_total:,.0f} €")
                st.metric("Coût unitaire", f"{cout_unitaire:.2f} €")
                
                # Analyse de rentabilité
                prix_vente = st.number_input("Prix de vente unitaire (€):", value=25.0)
                if prix_vente > 0:
                    marge_unitaire = prix_vente - cout_unitaire
                    marge_totale = marge_unitaire * production_souhaitee
                    
                    st.metric("Marge unitaire", f"{marge_unitaire:.2f} €")
                    st.metric("Marge totale mensuelle", f"{marge_totale:,.0f} €")
                    
                    if marge_unitaire < 0:
                        st.error("⚠️ Production non rentable au prix de vente actuel")
    
    with tab3:
        st.markdown('<div class="section-header">🔧 Simulation de Plan de Production</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Paramètres de Simulation")
            
            stock_initial = st.number_input("Stock initial:", value=1000)
            production_jour = st.number_input("Production par jour:", value=300)
            jours_ouvres = st.number_input("Jours ouvrés/mois:", value=22)
            ventes_jour = st.number_input("Ventes moyennes/jour:", value=280)
            stock_securite = st.number_input("Stock de sécurité:", value=500)
            
            simulation_mois = st.slider("Mois de simulation:", 1, 12, 1)
        
        with col2:
            st.subheader("Résultats de la Simulation")
            
            # Simulation sur 30 jours
            jours = list(range(1, 31))
            stock = stock_initial
            stocks = []
            productions = []
            ventes = []
            
            for jour in jours:
                # Production les jours ouvrés seulement
                production = production_jour if (jour % 7) not in [0, 6] else 0
                vente = ventes_jour if (jour % 7) not in [0, 6] else ventes_jour * 0.3  # Réduction week-end
                
                stock += production - vente
                stocks.append(stock)
                productions.append(production)
                ventes.append(vente)
            
            df_simulation = pd.DataFrame({
                'Jour': jours,
                'Stock': stocks,
                'Production': productions,
                'Ventes': ventes
            })
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=jours, y=stocks, name='Stock', line=dict(color='blue')))
            fig.add_trace(go.Scatter(x=jours, y=productions, name='Production', line=dict(color='green')))
            fig.add_trace(go.Scatter(x=jours, y=ventes, name='Ventes', line=dict(color='red')))
            fig.add_hline(y=stock_securite, line_dash="dash", line_color="orange", name="Stock sécurité")
            
            fig.update_layout(title='Simulation de Production Mensuelle',
                             xaxis_title='Jours',
                             yaxis_title='Unités')
            st.plotly_chart(fig, use_container_width=True)
            
            # Alertes
            stock_final = stocks[-1]
            if stock_final < stock_securite:
                st.error(f"⚠️ Stock final ({stock_final}) inférieur au stock de sécurité ({stock_securite})")
            else:
                st.success(f"✅ Stock final ({stock_final}) conforme")

def show_gestion_stocks():
    st.markdown('<div class="main-header">📦 Gestion des Stocks et Approvisionnements</div>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["📊 Coûts des Stocks", "📈 Modèle de Wilson", "🔄 Budget Approvisionnements"])
    
    with tab1:
        st.markdown('<div class="section-header">📊 Analyse des Coûts de Stockage</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Paramètres de Coût")
            
            valeur_locaux = st.number_input("Valeur des locaux (€):", value=200000)
            frais_gardiennage = st.number_input("Frais gardiennage (€):", value=25000)
            primes_assurance = st.number_input("Primes assurance (€):", value=5000)
            cout_financement = st.number_input("Coût financement (€):", value=2500)
            
            stock_debut = st.number_input("Stock début période (€):", value=1000000)
            stock_fin = st.number_input("Stock fin période (€):", value=1300000)
            
            if st.button("Calculer Coût de Possession"):
                cout_stockage_annuel = valeur_locaux + frais_gardiennage + primes_assurance + cout_financement
                stock_moyen = (stock_debut + stock_fin) / 2
                taux_possession = (cout_stockage_annuel / stock_moyen) * 100
                
                st.markdown(f"""
                <div class="info-box">
                **Résultats** :
                - Coût stockage annuel : {cout_stockage_annuel:,.0f} €
                - Stock moyen : {stock_moyen:,.0f} €
                - **Taux de possession : {taux_possession:.2f}%**
                </div>
                """, unsafe_allow_html=True)
                
                st.info("💡 Pour 100€ de stock, le coût de possession est de {:.2f}€".format(taux_possession))
    
    with tab2:
        st.markdown('<div class="section-header">📈 Modèle de Wilson - Lot Économique</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Paramètres du Modèle")
            
            consommation_annuelle = st.number_input("Consommation annuelle (unités):", value=320000)
            cout_lancement = st.number_input("Coût de lancement (€/commande):", value=560)
            cout_stockage_unitaire = st.number_input("Coût stockage unitaire (€/mois):", value=0.90)
            cout_penurie = st.number_input("Coût pénurie (€/unité):", value=67.0, help="Optionnel pour modèle avec pénurie")
            
            avec_penurie = st.checkbox("Inclure le coût de pénurie")
        
        with col2:
            if st.button("Calculer Lot Économique"):
                # Coût de stockage annuel
                cout_stockage_annuel = cout_stockage_unitaire * 12
                
                if not avec_penurie:
                    # Modèle Wilson classique
                    q_etoile = np.sqrt((2 * consommation_annuelle * cout_lancement) / cout_stockage_annuel)
                    n_commandes = consommation_annuelle / q_etoile
                    periode_eco = 360 / n_commandes
                    
                    st.success("🎯 Résultats du modèle Wilson classique")
                    
                else:
                    # Modèle avec pénurie
                    facteur_penurie = np.sqrt((cout_penurie + cout_stockage_annuel) / cout_penurie)
                    q_etoile_base = np.sqrt((2 * consommation_annuelle * cout_lancement) / cout_stockage_annuel)
                    q_etoile = q_etoile_base * facteur_penurie
                    n_commandes = consommation_annuelle / q_etoile
                    periode_eco = 360 / n_commandes
                    
                    st.success("🎯 Résultats du modèle Wilson avec pénurie")
                
                col1, col2, col3 = st.columns(3)
                col1.metric("Lot économique", f"{q_etoile:.0f} unités")
                col2.metric("Nombre commandes", f"{n_commandes:.1f}")
                col3.metric("Période économique", f"{periode_eco:.1f} jours")
                
                # Graphique des coûts
                q_values = np.linspace(q_etoile * 0.5, q_etoile * 2, 100)
                couts_lancement = (consommation_annuelle / q_values) * cout_lancement
                couts_possession = (q_values / 2) * cout_stockage_annuel
                couts_totaux = couts_lancement + couts_possession
                
                fig, ax = plt.subplots(figsize=(10, 6))
                ax.plot(q_values, couts_lancement, label='Coût de lancement', linestyle='--')
                ax.plot(q_values, couts_possession, label='Coût de possession', linestyle='--')
                ax.plot(q_values, couts_totaux, label='Coût total', linewidth=2)
                ax.axvline(q_etoile, color='red', linestyle=':', label=f'Lot optimal = {q_etoile:.0f}')
                ax.set_xlabel('Quantité commandée')
                ax.set_ylabel('Coût (€)')
                ax.legend()
                ax.set_title('Optimisation du Lot Économique')
                ax.grid(True, alpha=0.3)
                
                st.pyplot(fig)
    
    with tab3:
        st.markdown('<div class="section-header">🔄 Budget des Approvisionnements</div>', unsafe_allow_html=True)
        
        st.markdown("""
        ### 📋 Planification des Commandes
        
        Ce module vous aide à établir un budget d'approvisionnement sur 6 mois
        en tenant compte des délais de livraison et des stocks de sécurité.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Paramètres de Base")
            
            stock_initial = st.number_input("Stock initial (unités):", value=1000)
            stock_securite = st.number_input("Stock de sécurité (unités):", value=500)
            delai_livraison = st.number_input("Délai de livraison (semaines):", value=2)
            lot_commande = st.number_input("Lot de commande (unités):", value=2000)
            
            st.subheader("Prévisions de Consommation")
            mois = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin']
            consommation = []
            for i, mois_nom in enumerate(mois):
                conso = st.number_input(f"Consommation {mois_nom}:", value=1500 + i*100, key=f"conso_{i}")
                consommation.append(conso)
        
        with col2:
            st.subheader("Budget d'Approvisionnement")
            
            # Simulation du budget
            stock_courant = stock_initial
            commandes = [0] * 6
            livraisons = [0] * 6
            stocks_fin = []
            
            for i in range(6):
                # Livraison des commandes passées
                if i >= delai_livraison:
                    livraisons[i] = commandes[i - delai_livraison]
                
                stock_courant += livraisons[i] - consommation[i]
                stocks_fin.append(stock_courant)
                
                # Décision de commande
                if stock_courant < stock_securite:
                    commandes[i] = lot_commande
            
            df_budget = pd.DataFrame({
                'Mois': mois,
                'Consommation': consommation,
                'Commandes': commandes,
                'Livraisons': livraisons,
                'Stock Final': stocks_fin
            })
            
            st.dataframe(df_budget.style.format({
                'Consommation': '{:,.0f}',
                'Commandes': '{:,.0f}',
                'Livraisons': '{:,.0f}',
                'Stock Final': '{:,.0f}'
            }))
            
            # Graphique
            fig, ax = plt.subplots(figsize=(10, 6))
            x = range(len(mois))
            ax.plot(x, stocks_fin, marker='o', label='Stock final', linewidth=2)
            ax.axhline(y=stock_securite, color='red', linestyle='--', label='Stock de sécurité')
            ax.set_xticks(x)
            ax.set_xticklabels(mois)
            ax.set_xlabel('Mois')
            ax.set_ylabel('Unités')
            ax.legend()
            ax.set_title('Évolution du Stock')
            ax.grid(True, alpha=0.3)
            st.pyplot(fig)
            
            # Analyse
            stock_min = min(stocks_fin)
            if stock_min < stock_securite:
                st.error(f"⚠️ Stock minimum ({stock_min}) inférieur au stock de sécurité")
            else:
                st.success("✅ Niveaux de stock conformes aux objectifs")

def show_budget_investissement():
    st.markdown('<div class="main-header">🏗️ Budget d\'Investissement</div>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["📊 Méthodes d'Évaluation", "💰 Calcul VAN", "📈 Comparaison Projets"])
    
    with tab1:
        st.markdown('<div class="section-header">📊 Méthodes d\'Évaluation des Investissements</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 🕒 Délai de Récupération (Payback)
            
            **Avantages** :
            - Simple à calculer
            - Prise en compte du risque
            - Favorise la liquidité
            
            **Inconvénients** :
            - Ignore les flux après récupération
            - Ne tient pas compte de la valeur temps
            """)
            
            st.markdown("""
            ### 📈 Taux de Rentabilité Comptable
            
            **Formule** :
            TRC = (Bénéfice annuel moyen / Investissement initial) × 100
            
            **Limites** :
            - Basé sur des données comptables
            - Ignore l'actualisation
            """)
        
        with col2:
            st.markdown("""
            ### 💰 Valeur Actuelle Nette (VAN)
            
            **Formule** :
            VAN = Σ(Flux actualisés) - Investissement initial
            
            **Avantages** :
            - Prise en compte valeur temps
            - Mesure la création de valeur
            - Cohérente avec l'objectif richesse
            
            **Règle de décision** :
            - VAN > 0 : Projet acceptable
            - VAN maximale : Meilleur projet
            """)
            
            st.markdown("""
            ### 📊 Comparaison des Méthodes
            
            | Méthode | Horizon | Valeur temps | Risque |
            |---------|---------|--------------|--------|
            | Payback | Court | Non | Implicite |
            | TRC | Moyen | Non | Non |
            | VAN | Long | Oui | Via taux |
            """)
    
    with tab2:
        st.markdown('<div class="section-header">💰 Calcul de la Valeur Actuelle Nette</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Paramètres de l'Investissement")
            
            investissement_initial = st.number_input("Investissement initial (€):", value=150000)
            taux_actualisation = st.number_input("Taux d'actualisation (%):", value=15.0) / 100
            duree_projet = st.number_input("Durée du projet (années):", value=5)
            
            st.subheader("Flux de Trésorerie Annuels")
            flux_tresorerie = []
            for i in range(duree_projet):
                flux = st.number_input(f"Flux année {i+1} (€):", value=50000)
                flux_tresorerie.append(flux)
        
        with col2:
            if st.button("Calculer la VAN"):
                # Calcul des flux actualisés
                flux_actualises = []
                for i, flux in enumerate(flux_tresorerie):
                    flux_act = flux / ((1 + taux_actualisation) ** (i + 1))
                    flux_actualises.append(flux_act)
                
                van = sum(flux_actualises) - investissement_initial
                
                st.metric("Valeur Actuelle Nette (VAN)", f"{van:,.2f} €")
                
                # Tableau des flux
                df_flux = pd.DataFrame({
                    'Année': range(1, duree_projet + 1),
                    'Flux': flux_tresorerie,
                    'Flux Actualisé': flux_actualises
                })
                
                st.dataframe(df_flux.style.format({
                    'Flux': '{:,.0f} €',
                    'Flux Actualisé': '{:,.0f} €'
                }))
                
                # Graphique
                fig, ax = plt.subplots(figsize=(10, 6))
                years = range(1, duree_projet + 1)
                ax.bar(years, flux_tresorerie, alpha=0.7, label='Flux nominaux')
                ax.bar(years, flux_actualises, alpha=0.7, label='Flux actualisés')
                ax.axhline(y=0, color='black', linestyle='-', alpha=0.3)
                ax.set_xlabel('Année')
                ax.set_ylabel('Montant (€)')
                ax.legend()
                ax.set_title('Flux de Trésorerie - Nominaux vs Actualisés')
                ax.grid(True, alpha=0.3)
                
                st.pyplot(fig)
                
                # Interprétation
                if van > 0:
                    st.success("✅ Projet rentable - VAN positive")
                else:
                    st.error("❌ Projet non rentable - VAN négative")
    
    with tab3:
        st.markdown('<div class="section-header">📈 Comparaison de Plusieurs Projets d\'Investissement</div>', unsafe_allow_html=True)
        
        st.markdown("""
        ### 🎯 Analyse Multi-Critères
        
        Comparez plusieurs projets d'investissement selon différents critères pour 
        prendre la décision la plus éclairée.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Projet A - Expansion Commerciale")
            invest_a = st.number_input("Investissement Projet A (k€):", value=200)
            flux_a = []
            for i in range(5):
                flux = st.number_input(f"Flux A année {i+1} (k€):", value=60, key=f"flux_a_{i}")
                flux_a.append(flux)
        
        with col2:
            st.subheader("Projet B - Modernisation Usine")
            invest_b = st.number_input("Investissement Projet B (k€):", value=300)
            flux_b = []
            for i in range(5):
                flux = st.number_input(f"Flux B année {i+1} (k€):", value=80, key=f"flux_b_{i}")
                flux_b.append(flux)
        
        taux_actualisation = st.slider("Taux d'actualisation (%):", 5.0, 20.0, 12.0) / 100
        
        if st.button("Comparer les Projets"):
            # Calcul VAN Projet A
            van_a = -invest_a
            for i, flux in enumerate(flux_a):
                van_a += flux / ((1 + taux_actualisation) ** (i + 1))
            
            # Calcul VAN Projet B
            van_b = -invest_b
            for i, flux in enumerate(flux_b):
                van_b += flux / ((1 + taux_actualisation) ** (i + 1))
            
            # Calcul autres indicateurs
            payback_a = invest_a / np.mean(flux_a) if np.mean(flux_a) > 0 else float('inf')
            payback_b = invest_b / np.mean(flux_b) if np.mean(flux_b) > 0 else float('inf')
            
            trc_a = (np.mean(flux_a) / invest_a) * 100
            trc_b = (np.mean(flux_b) / invest_b) * 100
            
            # Tableau comparatif
            data_comparaison = {
                'Critère': ['VAN (k€)', 'Payback (ans)', 'TRC (%)', 'Investissement (k€)'],
                'Projet A': [van_a, payback_a, trc_a, invest_a],
                'Projet B': [van_b, payback_b, trc_b, invest_b]
            }
            
            df_comparaison = pd.DataFrame(data_comparaison)
            st.dataframe(df_comparaison.style.format({
                'Projet A': '{:,.1f}',
                'Projet B': '{:,.1f}'
            }))
            
            # Graphique comparatif
            criteres = ['VAN', 'TRC', 'Payback']
            valeurs_a = [van_a, trc_a, payback_a]
            valeurs_b = [van_b, trc_b, payback_b]
            
            fig, ax = plt.subplots(figsize=(10, 6))
            x = np.arange(len(criteres))
            width = 0.35
            
            ax.bar(x - width/2, valeurs_a, width, label='Projet A')
            ax.bar(x + width/2, valeurs_b, width, label='Projet B')
            
            ax.set_xlabel('Critères')
            ax.set_ylabel('Valeurs')
            ax.set_title('Comparaison des Projets d\'Investissement')
            ax.set_xticks(x)
            ax.set_xticklabels(criteres)
            ax.legend()
            ax.grid(True, alpha=0.3)
            
            st.pyplot(fig)
            
            # Recommandation
            if van_a > van_b and van_a > 0:
                st.success("🎯 RECOMMANDATION : Choisir le Projet A")
            elif van_b > van_a and van_b > 0:
                st.success("🎯 RECOMMANDATION : Choisir le Projet B")
            else:
                st.warning("⚠️ Aucun projet n'est rentable au taux d'actualisation choisi")

def show_budget_tresorerie():
    st.markdown('<div class="main-header">💸 Budget de Trésorerie</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### 🎯 Objectif du Budget de Trésorerie
    
    Le budget de trésorerie est **l'aboutissement** de toute la démarche budgétaire.
    Il traduit en flux monétaires l'ensemble des budgets précédents et permet de :
    """)
    
    st.markdown("""
    - ✅ **Vérifier l'équilibre financier** à court terme
    - 📊 **Anticiper les besoins** de financement
    - 💰 **Optimiser la gestion** de la trésorerie
    - 🚨 **Prévenir les risques** de liquidité
    """)
    
    tab1, tab2, tab3 = st.tabs(["📊 Construction", "🔄 Simulation", "📈 Analyse"])
    
    with tab1:
        st.markdown('<div class="section-header">📊 Processus de Construction</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 📥 Budget des Encaissements
            
            **Sources** :
            - Ventes au comptant
            - Encaissements clients (décalés)
            - Autres produits
            - Subventions
            - Produits financiers
            
            **Décalages typiques** :
            - 30-50% au comptant
            - 40-60% à 30 jours
            - 10-20% à 60 jours
            """)
            
            st.markdown("""
            ### 📤 Budget des Décaissements
            
            **Postes principaux** :
            - Achats fournisseurs
            - Charges de personnel
            - Charges externes
            - Investissements
            - Remboursements d'emprunts
            - Impôts et taxes
            """)
        
        with col2:
            st.markdown("""
            ### 📋 Budget de TVA
            
            **Calcul** :
            ```
            TVA à payer = TVA collectée - TVA déductible
            ```
            
            **Périodicité** :
            - Déclaration mensuelle ou trimestrielle
            - Paiement le mois suivant
            """)
            
            st.markdown("""
            ### ⚖️ Budget Récapitulatif
            
            **Solde = Encaissements - Décaissements**
            
            **Ajustements nécessaires** :
            - Financement des besoins (emprunts)
            - Placement des excédents
            - Lignes de crédit
            """)
            
            st.markdown("""
            ### 📈 Indicateurs de Suivi
            
            - **Point mort** : Niveau d'activité pour équilibrer la trésorerie
            - **Besoin en fonds de roulement (BFR)**
            - **Trésorerie nette**
            - **Ratio de liquidité**
            """)
    
    with tab2:
        st.markdown('<div class="section-header">🔄 Simulation de Budget de Trésorerie</div>', unsafe_allow_html=True)
        
        # Paramètres de base
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.subheader("Encaissements")
            ca_ht_mensuel = st.number_input("CA HT mensuel moyen (k€):", value=100.0)
            taux_tva = st.number_input("Taux TVA (%):", value=20.0) / 100
            delai_encaisse_client = st.select_slider("Délai encaissement clients:", 
                                                   options=['0 jour', '30 jours', '60 jours', '90 jours'], 
                                                   value='30 jours')
            
        with col2:
            st.subheader("Décaissements")
            achats_ht_mensuel = st.number_input("Achats HT mensuel (k€):", value=60.0)
            charges_personnel = st.number_input("Charges personnel (k€):", value=25.0)
            charges_externes = st.number_input("Charges externes (k€):", value=15.0)
            investissements = st.number_input("Investissements (k€):", value=50.0)
            
        with col3:
            st.subheader("Paramètres Financiers")
            tresorerie_initial = st.number_input("Trésorerie initiale (k€):", value=50.0)
            credit_disponible = st.number_input("Ligne de crédit disponible (k€):", value=100.0)
            taux_interet = st.number_input("Taux d'intérêt crédit (%):", value=4.0) / 100
        
        if st.button("Générer le Budget de Trésorerie sur 12 mois"):
            # Calculs de base
            mois = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Jun', 'Jul', 'Aoû', 'Sep', 'Oct', 'Nov', 'Déc']
            ca_ttc_mensuel = ca_ht_mensuel * (1 + taux_tva)
            achats_ttc_mensuel = achats_ht_mensuel * (1 + taux_tva)
            tva_a_payer = (ca_ht_mensuel - achats_ht_mensuel) * taux_tva
            
            # Simulation des flux avec décalages
            encaissements = []
            decaissements = []
            tresorerie_cumulee = [tresorerie_initial]
            
            for i in range(12):
                # Encaissements avec décalage
                if delai_encaisse_client == '0 jour':
                    encaiss_mois = ca_ttc_mensuel
                elif delai_encaisse_client == '30 jours':
                    encaiss_mois = ca_ttc_mensuel * 0.7  # 70% à 30 jours
                    if i > 0:
                        encaiss_mois += ca_ttc_mensuel * 0.3  # 30% à 60 jours
                else:
                    encaiss_mois = ca_ttc_mensuel * 0.5  # 50% à 30 jours
                    if i > 0:
                        encaiss_mois += ca_ttc_mensuel * 0.3  # 30% à 60 jours
                    if i > 1:
                        encaiss_mois += ca_ttc_mensuel * 0.2  # 20% à 90 jours
                
                encaissements.append(encaiss_mois)
                
                # Décaissements
                decaiss_mois = (achats_ttc_mensuel + charges_personnel + 
                               charges_externes + tva_a_payer)
                
                # Investissements répartis
                if i < 3:  # Investissements sur les 3 premiers mois
                    decaiss_mois += investissements / 3
                
                decaissements.append(decaiss_mois)
                
                # Calcul trésorerie cumulée
                solde_mois = encaiss_mois - decaiss_mois
                nouvelle_tresorerie = tresorerie_cumulee[-1] + solde_mois
                
                # Gestion du découvert
                if nouvelle_tresorerie < 0:
                    if abs(nouvelle_tresorerie) <= credit_disponible:
                        nouvelle_tresorerie = 0  # Utilisation du crédit
                    else:
                        st.warning(f"Découvert excessif en {mois[i]} : {nouvelle_tresorerie:.1f} k€")
                
                tresorerie_cumulee.append(nouvelle_tresorerie)
            
            # Création du tableau de bord
            df_tresorerie = pd.DataFrame({
                'Mois': mois,
                'Encaissements': encaissements,
                'Décaissements': decaissements,
                'Solde Mensuel': [e - d for e, d in zip(encaissements, decaissements)],
                'Trésorerie Cumulée': tresorerie_cumulee[1:]
            })
            
            # Affichage des résultats
            st.subheader("Budget de Trésorerie Prévisionnel sur 12 mois")
            st.dataframe(df_tresorerie.style.format({
                'Encaissements': '{:,.1f} k€',
                'Décaissements': '{:,.1f} k€',
                'Solde Mensuel': '{:,.1f} k€',
                'Trésorerie Cumulée': '{:,.1f} k€'
            }))
            
            # Graphiques
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
            
            # Graphique des flux
            ax1.bar(df_tresorerie['Mois'], df_tresorerie['Encaissements'], 
                   label='Encaissements', alpha=0.7, color='green')
            ax1.bar(df_tresorerie['Mois'], df_tresorerie['Décaissements'], 
                   label='Décaissements', alpha=0.7, color='red')
            ax1.set_ylabel('Montant (k€)')
            ax1.legend()
            ax1.set_title('Flux de Trésorerie Mensuels')
            ax1.tick_params(axis='x', rotation=45)
            ax1.grid(True, alpha=0.3)
            
            # Graphique de la trésorerie cumulée
            ax2.plot(df_tresorerie['Mois'], df_tresorerie['Trésorerie Cumulée'], 
                    marker='o', linewidth=2, color='blue')
            ax2.axhline(y=0, color='red', linestyle='--', alpha=0.5, label='Équilibre')
            ax2.set_ylabel('Trésorerie Cumulée (k€)')
            ax2.set_title('Évolution de la Trésorerie')
            ax2.tick_params(axis='x', rotation=45)
            ax2.grid(True, alpha=0.3)
            ax2.legend()
            
            # Zones de couleur pour trésorerie positive/négative
            ax2.fill_between(df_tresorerie['Mois'], df_tresorerie['Trésorerie Cumulée'], 
                            where=(df_tresorerie['Trésorerie Cumulée'] >= 0), 
                            interpolate=True, alpha=0.3, color='green')
            ax2.fill_between(df_tresorerie['Mois'], df_tresorerie['Trésorerie Cumulée'], 
                            where=(df_tresorerie['Trésorerie Cumulée'] < 0), 
                            interpolate=True, alpha=0.3, color='red')
            
            plt.tight_layout()
            st.pyplot(fig)
            
            # Analyse et recommandations
            tresorerie_min = min(df_tresorerie['Trésorerie Cumulée'])
            tresorerie_max = max(df_tresorerie['Trésorerie Cumulée'])
            tresorerie_finale = df_tresorerie['Trésorerie Cumulée'].iloc[-1]
            
            st.subheader("📊 Analyse de la Trésorerie")
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Trésorerie minimum", f"{tresorerie_min:.1f} k€")
            col2.metric("Trésorerie maximum", f"{tresorerie_max:.1f} k€")
            col3.metric("Trésorerie finale", f"{tresorerie_finale:.1f} k€")
            
            # Recommandations
            if tresorerie_min >= 0:
                st.success("✅ Trésorerie toujours positive - Situation saine")
            elif tresorerie_min >= -credit_disponible:
                st.warning("⚠️ Découvert occasionnel - Surveiller la trésorerie")
                st.info("💡 Recommandation : Optimiser les délais de paiement clients")
            else:
                st.error("🚨 Découvert excessif - Risque de liquidité")
                st.info("💡 Actions urgentes : Renégocier les délais fournisseurs, rechercher un financement")
    
    with tab3:
        st.markdown('<div class="section-header">📈 Analyse et Optimisation de la Trésorerie</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Calcul du Besoin en Fonds de Roulement (BFR)")
            
            stocks_moyen = st.number_input("Stock moyen (k€):", value=200.0)
            creances_clients = st.number_input("Créances clients (k€):", value=150.0)
            dettes_fournisseurs = st.number_input("Dettes fournisseurs (k€):", value=100.0)
            
            bfr = stocks_moyen + creances_clients - dettes_fournisseurs
            
            st.metric("Besoin en Fonds de Roulement", f"{bfr:.1f} k€")
            
            if bfr > 0:
                st.info("💡 BFR positif : Besoin de financement du cycle d'exploitation")
            else:
                st.info("💡 BFR négatif : Ressource dégagée par le cycle d'exploitation")
        
        with col2:
            st.subheader("Optimisation de la Trésorerie")
            
            st.markdown("""
            **Stratégies d'amélioration** :
            
            ### 📥 Accélérer les encaissements
            - Escompte pour paiement anticipé
            - Affacturage
            - Relance client proactive
            
            ### 📤 Maîtriser les décaissements
            - Négociation délais fournisseurs
            - Optimisation des commandes
            - Rationalisation des dépenses
            
            ### 💰 Optimisation du BFR
            - Réduction du stock
            - Amélioration de la rotation
            - Négociation commerciale
            """)

def show_processus_complet():
    st.markdown('<div class="main-header">🔄 Processus Budgétaire Complet</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### 🌟 Vision d'Ensemble du Pilotage Intégré
    
    Ce schéma représente le **cycle complet** du contrôle de gestion, démontrant 
    l'intégration de tous les budgets dans un système de pilotage cohérent.
    """)
    
    # Schéma interactif du processus complet
    st.markdown("""
    ```mermaid
    graph TD
        A[Stratégie 3-5 ans] --> B[Plan Opérationnel];
        B --> C[Budget des Ventes];
        B --> D[Budget de Production];
        B --> E[Budget Approvisionnements];
        C --> F[Budget de Trésorerie];
        D --> F;
        E --> F;
        F --> G[Compte de Résultat<br>Prévisionnel];
        F --> H[Bilan Prévisionnel];
        G --> I[Contrôle des Écarts];
        H --> I;
        I --> J[Actions Correctives];
        J --> A;
        
        style A fill:#1f77b4,color:white
        style F fill:#2ca02c,color:white
        style I fill:#d62728,color:white
        style J fill:#ff7f0e,color:white
    ```
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📋 Checklist du Processus Budgétaire
        
        - [ ] **Étape 1** : Définition des objectifs stratégiques
        - [ ] **Étape 2** : Élaboration du plan opérationnel
        - [ ] **Étape 3** : Budget des ventes (chiffrage)
        - [ ] **Étape 4** : Budget de production (optimisation)
        - [ ] **Étape 5** : Budget des approvisionnements (stocks)
        - [ ] **Étape 6** : Budget d'investissement (rentabilité)
        - [ ] **Étape 7** : Budget de trésorerie (synthèse)
        - [ ] **Étape 8** : Documents de synthèse prévisionnels
        - [ ] **Étape 9** : Mise en œuvre et contrôle
        - [ ] **Étape 10** : Analyse des écarts et corrections
        """)
    
    with col2:
        st.markdown("""
        ### 🎯 Bénéfices du Système Intégré
        
        **Pour la Direction** :
        - Vision globale et cohérente
        - Prise de décision éclairée
        - Allocation optimale des ressources
        
        **Pour les Opérationnels** :
        - Objectifs clairs et mesurables
        - Autonomie dans un cadre défini
        - Feedback régulier sur la performance
        
        **Pour l'Entreprise** :
        - Amélioration continue
        - Adaptation rapide aux changements
        - Création de valeur durable
        """)
    
    # Résumé des outils vus dans l'application
    st.markdown('<div class="section-header">🛠️ Boîte à Outils Complète</div>', unsafe_allow_html=True)
    
    tools_data = {
        'Module': ['Contrôle de Gestion', 'Budget Ventes', 'Budget Production', 
                  'Gestion Stocks', 'Budget Investissement', 'Budget Trésorerie'],
        'Outils': ['Tableaux de bord, KPI', 'Prévisions, Moindres carrés', 
                  'Programmation linéaire', 'Modèle de Wilson', 'VAN, TRI, Payback', 
                  'Flux, Solde, Financement'],
        'Objectif': ['Pilotage performance', 'Anticipation demande', 
                    'Optimisation ressources', 'Minimisation coûts', 
                    'Maximisation valeur', 'Équilibre financier']
    }
    
    df_tools = pd.DataFrame(tools_data)
    st.dataframe(df_tools, use_container_width=True)
    
    # Timeline du processus
    st.markdown('<div class="section-header">⏱️ Calendrier Budgétaire Type</div>', unsafe_allow_html=True)
    
    timeline_data = {
        'Période': ['Septembre', 'Octobre', 'Novembre', 'Décembre', 'Janvier', 'Février'],
        'Activité': [
            'Lancement process - Objectifs stratégiques',
            'Budgets opérationnels - Ventes/Production',
            'Budgets support - Approvisionnements/Investissements',
            'Synthèse - Trésorerie et documents prévisionnels',
            'Validation direction - Présentation CA',
            'Mise en œuvre - Début exercice'
        ]
    }
    
    df_timeline = pd.DataFrame(timeline_data)
    st.dataframe(df_timeline, use_container_width=True)

def show_plan_implementation():
    st.markdown('<div class="main-header">📅 Plan d\'Implémentation Détaillé</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ## 🎯 Feuille de Route pour la Mise en Œuvre
    
    Ce plan détaillé vous guide pas à pas dans l'implémentation d'un système de contrôle de gestion 
    performant dans votre entreprise.
    """)
    
    # Timeline interactive
    st.markdown('<div class="section-header">⏱️ Feuille de Route Chronologique</div>', unsafe_allow_html=True)
    
    # Création d'une timeline visuelle
    phases = [
        {"période": "1-2 semaines", "titre": "🚀 Phase Immédiate", "couleur": "#ff6b6b"},
        {"période": "1-3 mois", "titre": "📈 Court Terme", "couleur": "#4ecdc4"},
        {"période": "3-6 mois", "titre": "⚙️ Moyen Terme", "couleur": "#45b7d1"},
        {"période": "6-12 mois", "titre": "🏆 Long Terme", "couleur": "#96ceb4"}
    ]
    
    # Affichage des phases
    cols = st.columns(4)
    for i, phase in enumerate(phases):
        with cols[i]:
            st.markdown(f"""
            <div style="background-color: {phase['couleur']}; padding: 20px; border-radius: 10px; color: white; text-align: center;">
                <h3>{phase['période']}</h3>
                <h4>{phase['titre']}</h4>
            </div>
            """, unsafe_allow_html=True)
    
    # Détail de chaque phase
    tab1, tab2, tab3, tab4 = st.tabs(["🚀 Immédiat (1-2 sem)", "📈 Court terme (1-3 mois)", "⚙️ Moyen terme (3-6 mois)", "🏆 Long terme (6-12 mois)"])
    
    with tab1:
        st.markdown('<div class="subsection-header">🚀 Actions Immédiates (1-2 semaines)</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 🎯 Identifier un Projet Pilote
            
            **Critères de sélection** :
            - 📊 Département avec données disponibles
            - 👥 Équipe motivée et coopérative
            - 🎯 Problème business clair
            - 📈 Potentiel de ROI rapide
            
            **Exemples de projets pilotes** :
            - Optimisation du budget commercial
            - Gestion des stocks d'un produit phare
            - Contrôle des coûts de production
            - Analyse de rentabilité par client
            """)
            
            # Outil de sélection de projet pilote
            st.subheader("🔍 Sélectionneur de Projet Pilote")
            
            criteres = {
                "Disponibilité des données": st.slider("Disponibilité données (1-5)", 1, 5, 3),
                "Motivation de l'équipe": st.slider("Motivation équipe (1-5)", 1, 5, 4),
                "Clarté du problème": st.slider("Clarté problème (1-5)", 1, 5, 3),
                "Potentiel ROI": st.slider("Potentiel ROI (1-5)", 1, 5, 4),
                "Complexité technique": st.slider("Complexité technique (1-5)", 1, 5, 2)
            }
            
            score_total = sum(criteres.values())
            
            if score_total >= 20:
                st.success("✅ Excellent candidat pour projet pilote")
            elif score_total >= 15:
                st.warning("⚠️ Candidat acceptable, nécessite quelques ajustements")
            else:
                st.error("❌ Projet à reconsidérer ou préparer davantage")
        
        with col2:
            st.markdown("""
            ### 👥 Former une Équipe Dédiée
            
            **Composition idéale** :
            - 🎯 **Sponsor executive** : Direction générale
            - 📊 **Chef de projet** : Contrôleur de gestion
            - 🔧 **Expert métier** : Responsable du département
            - 💻 **Support technique** : IT/Data analyst
            - 👥 **Utilisateurs clés** : Équipe opérationnelle
            
            **Rôles et responsabilités** :
            - **Sponsor** : Validation budget, levée des obstacles
            - **Chef de projet** : Coordination, planning, reporting
            - **Expert métier** : Définition des besoins, tests
            - **Support technique** : Intégration, automatisation
            - **Utilisateurs** : Feedback, adoption
            """)
            
            st.markdown("""
            ### 🎯 Définir les Objectifs Spécifiques
            
            **Méthode SMART** :
            - **Spécifique** : Clair et précis
            - **Mesurable** : Chiffré et quantifiable
            - **Atteignable** : Réaliste et faisable
            - **Relevant** : Aligné sur la stratégie
            - **Temporel** : Délai défini
            
            **Exemples d'objectifs** :
            - Réduction de 15% des stocks d'ici 3 mois
            - Augmentation de 10% de la marge d'ici 6 mois
            - Réduction de 20% du BFR d'ici 1 an
            """)
    
    with tab2:
        st.markdown('<div class="subsection-header">📈 Actions Court Terme (1-3 mois)</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 🛠️ Mettre en Place les Premiers Outils
            
            **Priorité 1 : Tableaux de bord simples**
            - 📊 3-5 KPI essentiels
            - 📈 Visualisations basiques
            - 🔄 Mise à jour manuelle initiale
            
            **Outils recommandés** :
            - Excel/Google Sheets pour débuter
            - Power BI/Tableau pour la visualisation
            - Templates prédéfinis pour gagner du temps
            
            **Étapes concrètes** :
            1. Identifier les données sources
            2. Créer le premier tableau de bord
            3. Tester avec l'équipe pilote
            4. Itérer et améliorer
            """)
            
            # Calculateur d'effort
            st.subheader("⏱️ Estimateur d'Effort - Mise en Place")
            
            complexite = st.select_slider("Complexité du projet:", 
                                        ["Simple", "Moyen", "Complexe"])
            equipe = st.number_input("Nombre de personnes dédiées:", 1, 10, 2)
            
            if complexite == "Simple":
                effort = "2-3 semaines"
            elif complexite == "Moyen":
                effort = "4-6 semaines"
            else:
                effort = "8-10 semaines"
                
            st.info(f"💡 Effort estimé : {effort} avec {equipe} personne(s)")
        
        with col2:
            st.markdown("""
            ### 👨‍🏫 Former les Utilisateurs Clés
            
            **Formations prioritaires** :
            - 🎓 **Session dirigeants** : 2 heures
            - 📚 **Formation utilisateurs** : 1 journée
            - 🔧 **Atelier technique** : 1/2 journée
            - 📖 **Documentation utilisateur** : Guide pratique
            
            **Méthodes pédagogiques** :
            - Présentation des concepts
            - Démonstration live
            - Exercices pratiques
            - Études de cas réels
            - Support continu
            """)
            
            st.markdown("""
            ### 📊 Mesurer les Premiers Résultats
            
            **Indicateurs de succès initiaux** :
            - ✅ Adoption par l'équipe (> 80%)
            - ⏱️ Gain de temps sur le reporting (> 30%)
            - 🎯 Exactitude des données (> 95%)
            - 💬 Satisfaction utilisateurs
            
            **Revues régulières** :
            - Point hebdomadaire avec l'équipe projet
            - Revue mensuelle avec la direction
            - Ajustements basés sur le feedback
            """)
            
            # Suivi des premiers résultats
            st.subheader("📈 Tableau de Bord Initial")
            
            metriques_initiales = {
                "Taux d'adoption": st.slider("Taux d'adoption (%)", 0, 100, 75),
                "Gain de temps": st.slider("Gain de temps (%)", 0, 100, 40),
                "Satisfaction": st.slider("Satisfaction (1-5)", 1, 5, 4),
                "Exactitude données": st.slider("Exactitude données (%)", 0, 100, 90)
            }
            
            score_global = sum(metriques_initiales.values()) / 4
            
            if score_global >= 80:
                st.success("✅ Excellents résultats initiaux")
            elif score_global >= 60:
                st.warning("⚠️ Résultats corrects, améliorations possibles")
            else:
                st.error("❌ Nécessite des ajustements importants")
    
    with tab3:
        st.markdown('<div class="subsection-header">⚙️ Actions Moyen Terme (3-6 mois)</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 🌐 Étendre à d'Autres Départements
            
            **Stratégie d'expansion** :
            1. **Capitaliser sur les succès** du pilote
            2. **Identifier les départements** prioritaires
            3. **Adapter les outils** aux besoins spécifiques
            4. **Former les nouveaux utilisateurs**
            
            **Départements typiques** :
            - 📈 Commercial et marketing
            - 🏭 Production et logistique
            - 💰 Finance et comptabilité
            - 📦 Achats et approvisionnements
            - 👥 Ressources humaines
            
            **Plan de déploiement** :
            - 1 département par mois maximum
            - Recueil systématique du feedback
            - Amélioration continue des processus
            """)
            
            # Planificateur d'expansion
            st.subheader("🗓️ Planificateur d'Expansion")
            
            departements = st.multiselect(
                "Départements à inclure:",
                ["Commercial", "Production", "Finance", "Achats", "RH", "Logistique", "R&D"],
                default=["Commercial", "Production"]
            )
            
            if departements:
                st.info(f"📅 Plan recommandé : {len(departements)} départements sur {len(departements)} mois")
        
        with col2:
            st.markdown("""
            ### 🤖 Automatiser les Processus
            
            **Processus à automatiser en priorité** :
            - 📥 Collecte des données
            - 📊 Génération des rapports
            - 📧 Envoi des alertes
            - 🔄 Consolidation des informations
            
            **Technologies recommandées** :
            - APIs pour l'intégration des données
            - ETL pour la transformation
            - Outils BI pour la visualisation
            - Scripts Python/R pour l'analyse
            
            **Bénéfices attendus** :
            - Réduction de 70% du temps de reporting
            - Élimination des erreurs manuelles
            - Information en temps réel
            - Scalabilité du système
            """)
            
            st.markdown("""
            ### 🎯 Optimiser le Système
            
            **Axes d'optimisation** :
            - **Performance** : Temps de réponse, charge
            - **Utilisabilité** : Interface, ergonomie
            - **Fonctionnalités** : Nouvelles features
            - **Intégration** : Connexions systèmes
            
            **Méthodologie** :
            - Mesure continue des performances
            - Enquêtes de satisfaction utilisateurs
            - Benchmark des meilleures pratiques
            - Veille technologique
            """)
            
            # Calculateur de ROI automatisation
            st.subheader("💰 Calculateur ROI Automatisation")
            
            temps_manuel = st.number_input("Temps manuel actuel (h/mois):", value=40)
            cout_horaire = st.number_input("Coût horaire (€):", value=50)
            investissement_auto = st.number_input("Investissement automatisation (€):", value=10000)
            
            gain_annuel = temps_manuel * cout_horaire * 12 * 0.7  # 70% de gain
            roi_mois = investissement_auto / (gain_annuel / 12) if gain_annuel > 0 else float('inf')
            
            st.metric("Gain annuel estimé", f"{gain_annuel:,.0f} €")
            st.metric("ROI (mois)", f"{roi_mois:.1f} mois")
    
    with tab4:
        st.markdown('<div class="subsection-header">🏆 Actions Long Terme (6-12 mois)</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 🔄 Intégration Complète
            
            **Niveau d'intégration cible** :
            - 🤝 **Systèmes connectés** : ERP, CRM, RH
            - 📊 **Data warehouse unique** : Source de vérité
            - 👥 **Tous départements** : Couverture complète
            - 🌐 **Accessibilité totale** : Cloud, mobile
            
            **Architecture cible** :
            - Centralisation des données
            - Standardisation des processus
            - Uniformisation des rapports
            - Gouvernance des données
            
            **Indicateurs de maturité** :
            - Taux d'adoption > 90%
            - Couverture fonctionnelle > 80%
            - Satisfaction utilisateurs > 4/5
            - ROI démontré et mesuré
            """)
            
            # Évaluateur de maturité
            st.subheader("📊 Évaluateur de Maturité")
            
            criteres_maturite = {
                "Intégration systèmes": st.slider("Intégration systèmes (%)", 0, 100, 60),
                "Couverture départements": st.slider("Couverture départements (%)", 0, 100, 70),
                "Automatisation processus": st.slider("Automatisation (%)", 0, 100, 50),
                "Culture data": st.slider("Culture data (1-5)", 1, 5, 3)
            }
            
            score_maturite = sum(criteres_maturite.values()) / 4
            
            if score_maturite >= 80:
                st.success("✅ Niveau de maturité avancé")
            elif score_maturite >= 60:
                st.warning("⚠️ Niveau de maturité intermédiaire")
            else:
                st.info("💡 Niveau de maturité débutant")
        
        with col2:
            st.markdown("""
            ### 🌱 Culture de la Performance
            
            **Éléments clés de la culture** :
            - 🎯 **Orientation résultats** : Focus sur les outcomes
            - 📊 **Décision data-driven** : Basée sur les données
            - 🔄 **Amélioration continue** : Mindset croissance
            - 👥 **Responsabilisation** : Autonomie des équipes
            
            **Actions de transformation culturelle** :
            - Formation continue aux outils et méthodes
            - Reconnaissance des performances
            - Partage des meilleures pratiques
            - Leadership par l'exemple
            
            **Indicateurs culturels** :
            - Utilisation proactive des données
            - Prise de décision fact-based
            - Initiative d'amélioration
            - Collaboration inter-départements
            """)
            
            st.markdown("""
            ### 💡 Innovation Continue
            
            **Domaines d'innovation** :
            - 🧠 **Intelligence Artificielle** : Prédiction, optimisation
            - 📱 **Expérience utilisateur** : Interfaces avancées
            - 🔮 **Analytics prédictif** : Anticipation des tendances
            - 🤖 **Automatisation avancée** : Processus intelligents
            
            **Processus d'innovation** :
            - Veille technologique continue
            - Expérimentation de nouvelles solutions
            - Mesure de l'impact des innovations
            - Capitalisation sur les succès
            
            **Vision long terme** :
            - Système auto-apprenant
            - Décision assistée par IA
            - Optimisation en temps réel
            - Valeur business maximisée
            """)
            
            # Roadmap d'innovation
            st.subheader("🔮 Roadmap d'Innovation")
            
            innovations = st.multiselect(
                "Domaines d'innovation prioritaires:",
                ["IA Prédictive", "Analytics Avancé", "Automatisation Intelligente", 
                 "Mobile First", "Temps Réel", "Personnalisation", "Collaboration"],
                default=["IA Prédictive", "Analytics Avancé"]
            )
            
            if innovations:
                st.success(f"🎯 Roadmap définie : {', '.join(innovations)}")
    
    # Section de suivi et engagement
    st.markdown("---")
    st.markdown('<div class="section-header">📋 Engagement et Suivi</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📝 Contrat d'Engagement
        
        **Engagement de la Direction** :
        - ✅ Allocation des ressources nécessaires
        - ✅ Participation aux revues régulières
        - ✅ Soutien aux changements organisationnels
        - ✅ Communication de l'importance du projet
        
        **Engagement des Équipes** :
        - ✅ Participation active aux formations
        - ✅ Utilisation quotidienne des outils
        - ✅ Feedback constructif et régulier
        - ✅ Adoption des nouvelles pratiques
        """)
    
    with col2:
        st.markdown("""
        ### 🔄 Mécanismes de Suivi
        
        **Indicateurs de Progrès** :
        - 📊 Avancement vs planning
        - 💰 Budget vs dépenses réelles
        - 👥 Adoption et satisfaction
        - 🎯 Atteinte des objectifs business
        
        **Revues Régulières** :
        - Point hebdomadaire équipe projet
        - Revue mensuelle comité de pilotage
        - Bilan trimestriel direction générale
        - Audit annuel des résultats
        """)
    
    # Call to action final
    st.markdown("---")
    st.markdown("""
    <div style="background-color: #e8f5e8; padding: 20px; border-radius: 10px; text-align: center;">
        <h2>🚀 Prêt à Démarrer ?</h2>
        <p><strong>Le meilleur moment pour commencer était hier. Le deuxième meilleur moment, c'est maintenant.</strong></p>
        <p>Commencez par identifier votre projet pilote dès aujourd'hui !</p>
    </div>
    """, unsafe_allow_html=True)

def show_plus_loin():
    st.markdown('<div class="main-header">🚀 Aller Plus Loin</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ## 🎯 Implémentation dans Votre Entreprise
    
    Cette application vous a présenté les concepts fondamentaux. Voici comment 
    les mettre en œuvre concrètement dans votre organisation.
    """)
    
    tab1, tab2, tab3, tab4 = st.tabs(["🏢 Implémentation", "👥 Formation", "🤖 Automatisation", "🛠️ Personnalisation"])
    
    with tab1:
        st.markdown('<div class="section-header">🏢 Implémentez ces Outils dans Votre Entreprise</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 📋 Plan d'Implémentation par Étapes
            
            **Phase 1 : Diagnostic (1-2 mois)**
            - Audit des processus existants
            - Identification des besoins
            - Formation de l'équipe projet
            
            **Phase 2 : Prototype (2-3 mois)**
            - Mise en place des premiers tableaux de bord
            - Tests sur un département pilote
            - Ajustements et améliorations
            
            **Phase 3 : Déploiement (3-6 mois)**
            - Extension à toute l'entreprise
            - Formation des utilisateurs
            - Mesure des résultats
            
            **Phase 4 : Optimisation (continue)**
            - Amélioration continue
            - Intégration de nouvelles données
            - Adaptation aux changements
            """)
        
        with col2:
            st.markdown("""
            ### 🎯 Facteurs Clés de Succès
            
            **Engagement de la Direction** :
            - Implication active du comité de direction
            - Allocation des ressources nécessaires
            - Communication régulière
            
            **Adaptation à la Culture d'Entreprise** :
            - Respect des spécificités métier
            - Implication des équipes opérationnelles
            - Processus progressif et pédagogique
            
            **Outils Appropriés** :
            - Solutions adaptées à la taille de l'entreprise
            - Interface utilisateur intuitive
            - Intégration avec les systèmes existants
            
            **Mesure des Résultats** :
            - Indicateurs de performance clairs
            - Revue régulière des objectifs
            - Célébration des succès
            """)
            
            # Calculateur de ROI
            st.subheader("📊 Calculateur de ROI Potentiel")
            
            investissement_initial = st.number_input("Investissement initial (k€):", value=50)
            gains_annuels = st.number_input("Gains annuels estimés (k€):", value=100)
            duree_amortissement = st.number_input("Durée d'amortissement (ans):", value=3)
            
            if st.button("Calculer ROI"):
                roi_annuel = (gains_annuels / investissement_initial) * 100
                periode_retour = investissement_initial / gains_annuels
                
                st.metric("ROI Annuel", f"{roi_annuel:.1f}%")
                st.metric("Période de retour", f"{periode_retour:.1f} ans")
                
                if roi_annuel > 100:
                    st.success("✅ Investissement très rentable")
                elif roi_annuel > 50:
                    st.success("✅ Investissement rentable")
                else:
                    st.info("💡 Investissement à étudier attentivement")
    
    with tab2:
        st.markdown('<div class="section-header">👥 Formez Vos Équipes aux Concepts Présentés</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 🎓 Programme de Formation Complet
            
            **Formation Direction Générale** (2 jours)
            - Principes du contrôle de gestion
            - Lecture des tableaux de bord
            - Prise de décision stratégique
            
            **Formation Managers Opérationnels** (3 jours)
            - Élaboration des budgets
            - Analyse des écarts
            - Gestion des performances
            
            **Formation Contrôleurs de Gestion** (5 jours)
            - Techniques avancées d'analyse
            - Outils de reporting
            - Optimisation des processus
            
            **Formation Tout Collaborateur** (1 jour)
            - Compréhension des enjeux
            - Contribution aux objectifs
            - Culture de la performance
            """)
        
        with col2:
            st.markdown("""
            ### 📚 Méthodes Pédagogiques
            
            **Apprentissage Théorique** :
            - Concepts fondamentaux
            - Études de cas
            - Bonnes pratiques
            
            **Application Pratique** :
            - Exercices sur données réelles
            - Simulations interactives
            - Ateliers en groupe
            
            **Suivi et Évaluation** :
            - Quiz de validation
            - Projets concrets
            - Mesure des acquis
            
            **Ressources Complémentaires** :
            - Documentation complète
            - Templates réutilisables
            - Support en ligne
            """)
            
            # Planificateur de formation
            st.subheader("📅 Planificateur de Formation")
            
            nb_participants = st.number_input("Nombre de participants:", value=20)
            duree_formation = st.selectbox("Durée de la formation:", 
                                         ["1 jour", "2 jours", "3 jours", "5 jours"])
            niveau = st.selectbox("Niveau des participants:", 
                                ["Débutant", "Intermédiaire", "Avancé"])
            
            if st.button("Estimer le Plan de Formation"):
                if duree_formation == "1 jour":
                    cout_estime = nb_participants * 500
                    sessions = 1
                elif duree_formation == "2 jours":
                    cout_estime = nb_participants * 900
                    sessions = 2
                elif duree_formation == "3 jours":
                    cout_estime = nb_participants * 1200
                    sessions = 3
                else:
                    cout_estime = nb_participants * 1800
                    sessions = 5
                
                st.metric("Coût estimé de la formation", f"{cout_estime:,.0f} €")
                st.metric("Nombre de sessions recommandées", sessions)
    
    with tab3:
        st.markdown('<div class="section-header">🤖 Automatisez la Collecte et l\'Analyse des Données</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 🔄 Flux de Données Automatisé
            
            **Sources de Données** :
            - ERP (SAP, Oracle, Sage)
            - Logiciels de paie
            - Systèmes de vente
            - Applications métier
            - Bases de données externes
            
            **Processus d'Automatisation** :
            - Extraction quotidienne des données
            - Nettoyage et validation
            - Consolidation et agrégation
            - Génération des rapports
            - Alertes automatiques
            
            **Outils Recommandés** :
            - Power BI / Tableau
            - Python / R
            - APIs REST
            - ETL (Extract Transform Load)
            - Cloud computing
            """)
        
        with col2:
            st.markdown("""
            ### 📊 Dashboard en Temps Réel
            
            **Avantages de l'Automatisation** :
            - Gain de temps considérable
            - Réduction des erreurs
            - Information en temps réel
            - Décision plus rapide
            - Meilleure réactivité
            
            **Fonctionnalités Avancées** :
            - Alertes prédictives
            - Analyse de scénarios
            - Reporting personnalisé
            - Mobile friendly
            - Export multi-formats
            """)
            
            # Configuration d'alerte
            st.subheader("⚡ Configuration d'Alerte Automatique")
            
            kpi_alerte = st.selectbox("KPI à surveiller:", 
                                    ["Chiffre d'affaires", "Marge", "Trésorerie", "Stocks"])
            seuil_alerte = st.number_input("Seuil d'alerte:", value=100000)
            frequence_controle = st.selectbox("Fréquence de contrôle:", 
                                            ["Quotidien", "Hebdomadaire", "Mensuel"])
            
            if st.button("Créer l'Alerte"):
                st.success(f"✅ Alerte configurée : {kpi_alerte} > {seuil_alerte:,.0f} € - Contrôle {frequence_controle.lower()}")
                st.info("💡 Cette alerte sera envoyée automatiquement par email aux responsables concernés")
    
    with tab4:
        st.markdown('<div class="section-header">🛠️ Créez Votre Propre Système de Pilotage sur Mesure</div>', unsafe_allow_html=True)
        
        st.markdown("""
        ## 🎨 Personnalisation Avancée
        
        Adaptez ces outils aux spécificités de votre entreprise pour créer 
        un système de pilotage unique et parfaitement adapté.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 📋 Modules Personnalisables
            
            **Indicateurs sur Mesure** :
            - KPI spécifiques à votre secteur
            - Métriques uniques à votre entreprise
            - Objectifs personnalisés
            
            **Workflows Adaptés** :
            - Processus d'approbation spécifiques
            - Circuits de validation sur mesure
            - Alertes personnalisées
            
            **Design Personnalisé** :
            - Chartes graphiques maison
            - Logos et branding
            - Interface utilisateur adaptée
            """)
            
            # Personnalisation d'indicateur
            st.subheader("🎯 Créer un KPI Personnalisé")
            
            nom_kpi = st.text_input("Nom du KPI:", value="Taux de Transformation")
            formule_kpi = st.text_area("Formule de calcul:", 
                                     "Nombre de ventes / Nombre de prospects * 100")
            unite_kpi = st.selectbox("Unité:", ["%", "€", "jours", "unités", "autre"])
            
            if st.button("Ajouter le KPI"):
                st.success(f"✅ KPI '{nom_kpi}' créé avec succès")
                st.info(f"Formule : {formule_kpi} | Unité : {unite_kpi}")
        
        with col2:
            st.markdown("""
            ### 🔧 Développements Spécifiques
            
            **Intégrations Métier** :
            - Connexion avec vos logiciels
            - Adaptation à vos processus
            - Interface avec vos équipements
            
            **Rapports Spécialisés** :
            - Reporting réglementaire
            - Analyses sectorielles
            - Tableaux de bord spécifiques
            
            **Fonctionnalités Avancées** :
            - Intelligence artificielle
            - Analyse prédictive
            - Optimisation automatique
            """)
            
            # Configuration de rapport
            st.subheader("📈 Configurer un Rapport Personnalisé")
            
            type_rapport = st.selectbox("Type de rapport:", 
                                      ["Performance commerciale", 
                                       "Analyse de production", 
                                       "Suivi des stocks",
                                       "Analyse financière"])
            
            frequence_rapport = st.selectbox("Fréquence:", 
                                           ["Quotidien", "Hebdomadaire", "Mensuel", "Trimestriel"])
            
            destinataires = st.text_input("Destinataires (emails séparés par des virgules):")
            
            if st.button("Créer le Rapport"):
                st.success(f"✅ Rapport '{type_rapport}' configuré")
                st.info(f"📧 Envoyé {frequence_rapport.lower()} à : {destinataires}")
        
        st.markdown("""
        ---
        
        ## 🚀 Prochaines Étapes Concrètes
        
        **Immédiates (1-2 semaines)** :
        1. Identifier un projet pilote
        2. Former une équipe dédiée
        3. Définir les objectifs spécifiques
        
        **Court terme (1-3 mois)** :
        1. Mettre en place les premiers outils
        2. Former les utilisateurs clés
        3. Mesurer les premiers résultats
        
        **Moyen terme (3-6 mois)** :
        1. Étendre à d'autres départements
        2. Automatiser les processus
        3. Optimiser le système
        
        **Long terme (6-12 mois)** :
        1. Intégration complète
        2. Culture de la performance
        3. Innovation continue
        
        *Le contrôle de gestion n'est pas une fin en soi, mais un moyen au service 
        de la performance durable de l'entreprise.*
        """)

def main():
    # Sidebar navigation
    st.sidebar.title("📊Gestion Budgetaire")
    sections = [
        "🏠 Accueil",
        "📈 Contrôle de Gestion", 
        "💰 Budget des Ventes",
        "🏭 Budget de Production",
        "📦 Gestion des Stocks",
        "🏗️ Budget d'Investissement", 
        "💸 Budget de Trésorerie",
        "🔄 Processus Complet",
        "📅 Plan d'Implémentation",
        "🚀 Aller Plus Loin"
    ]
    choice = st.sidebar.radio("Sélectionnez une section:", sections)

    if choice == "🏠 Accueil":
        show_home()
    elif choice == "📈 Contrôle de Gestion":
        show_controle_gestion()
    elif choice == "💰 Budget des Ventes":
        show_budget_ventes()
    elif choice == "🏭 Budget de Production":
        show_budget_production()
    elif choice == "📦 Gestion des Stocks":
        show_gestion_stocks()
    elif choice == "🏗️ Budget d'Investissement":
        show_budget_investissement()
    elif choice == "💸 Budget de Trésorerie":
        show_budget_tresorerie()
    elif choice == "🔄 Processus Complet":
        show_processus_complet()
    elif choice == "📅 Plan d'Implémentation":
        show_plan_implementation()
    elif choice == "🚀 Aller Plus Loin":
        show_advanced_features()

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
    
if __name__ == "__main__":
    st.set_page_config(
        page_title="Budget Management System", 
        page_icon="🏢", 
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Chargement CSS personnalisé
    st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
    }
    </style>
    """, unsafe_allow_html=True)
    
    main()