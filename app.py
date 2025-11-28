import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta

def show_strategic_investment():
    st.header("🏗️ Analyse des Investissements Stratégiques")
    
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

# Ajouter cette fonction dans votre main()
def main():
    st.set_page_config(
        page_title="Contrôle de Gestion - Investissement Stratégique",
        page_icon="🏗️",
        layout="wide"
    )
    
    # Vos autres onglets...
    tab1, tab2, tab3, tab4 = st.tabs([
        "🏗️ Investissement Stratégique",
        "💸 Trésorerie Prédictive", 
        "📊 Reporting Executive",
        "📈 Tableau de Bord"
    ])
    
    with tab1:
        show_strategic_investment()
    
    # ... autres onglets

if __name__ == "__main__":
    main()