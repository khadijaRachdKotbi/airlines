#!/usr/bin/env python3
"""
airLines_Project Support Configuration
Configuration pour les options de financement et reconnaissance
"""

import os
from datetime import datetime

class SupportConfig:
    """Configuration pour la gestion des soutiens"""

    def __init__(self):
        self.support_links = {
            'github_sponsors': 'https://github.com/sponsors/khadijaRachdKotbi',
            'buymeacoffee': 'https://www.buymeacoffee.com/khadijaRachdKotbi',
            'paypal': 'https://paypal.me/khadijaRachdKotbi',
            'github_repo': 'https://github.com/khadijaRachdKotbi/airLines_Project'
        }

        self.tiers = {
            'platinum': {
                'min_amount': 100,
                'benefits': ['Logo VIP', 'Webinaires privés', 'Consultations', 'Roadmap influence'],
                'color': '#9370DB'
            },
            'gold': {
                'min_amount': 50,
                'benefits': ['Logo premium', 'Support prioritaire', 'Reconnaissance'],
                'color': '#FFD700'
            },
            'silver': {
                'min_amount': 10,
                'benefits': ['Logo silver', 'Support prioritaire'],
                'color': '#C0C0C0'
            },
            'bronze': {
                'min_amount': 1,
                'benefits': ['Mentions README', 'Badge Supporter'],
                'color': '#CD7F32'
            }
        }

        self.impact_messages = {
            1: "☕ Un café pour maintenir la motivation pendant les sessions de debug",
            5: "📝 Une heure d'amélioration de la documentation ou d'une fonctionnalité",
            10: "✨ Développement d'une nouvelle visualisation ou métrique",
            25: "🚀 Amélioration significative (nouvel algorithme, temps réel, etc.)",
            50: "🏆 Support mensuel - reconnaissance spéciale et influence sur la roadmap"
        }

        self.contact_info = {
            'email': 'khadija.rachd.kotbi@example.com',
            'github_discussions': 'https://github.com/khadijaRachdKotbi/airLines_Project/discussions',
            'github_issues': 'https://github.com/khadijaRachdKotbi/airLines_Project/issues'
        }

    def get_tier_from_amount(self, amount):
        """Détermine le niveau de soutien en fonction du montant"""
        if amount >= self.tiers['platinum']['min_amount']:
            return 'platinum'
        elif amount >= self.tiers['gold']['min_amount']:
            return 'gold'
        elif amount >= self.tiers['silver']['min_amount']:
            return 'silver'
        elif amount >= self.tiers['bronze']['min_amount']:
            return 'bronze'
        else:
            return None

    def get_impact_message(self, amount):
        """Récupère le message d'impact correspondant au montant"""
        for threshold in sorted(self.impact_messages.keys(), reverse=True):
            if amount >= threshold:
                return self.impact_messages[threshold]
        return "❤️ Merci pour votre soutien qui aide à maintenir ce projet!"

    def get_support_badges(self):
        """Génère les badges HTML pour le README"""
        return {
            'github_sponsors': f'<a href="{self.support_links["github_sponsors"]}"><img src="https://img.shields.io/github/sponsors/khadijaRachdKotbi?style=social&logo=github&logoColor=ea4aaa" alt="GitHub Sponsors"></a>',
            'buymeacoffee': f'<a href="{self.support_links["buymeacoffee"]}"><img src="https://img.shields.io/badge/Buy_Me_A_Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me A Coffee"></a>',
            'paypal': f'<a href="{self.support_links["paypal"]}"><img src="https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white" alt="PayPal"></a>'
        }

    def get_support_sidebar_html(self):
        """Génère le HTML pour la section sidebar de soutien"""
        return f"""
        <div class="support-section">
            <h3>☕ Soutenir airLines_Project</h3>
            <p><strong>Aidez-nous à maintenir et améliorer ce projet open-source!</strong></p>

            <div style="display: flex; flex-wrap: wrap; gap: 10px; margin: 15px 0;">
                <a href="{self.support_links['github_sponsors']}" target="_blank" class="support-button">🎯 GitHub</a>
                <a href="{self.support_links['buymeacoffee']}" target="_blank" class="support-button">☕ Coffee</a>
                <a href="{self.support_links['paypal']}" target="_blank" class="support-button">💳 PayPal</a>
            </div>

            <p><small><em>Chaque contribution, même symbolique, aide à rendre ce projet accessible! 🙏</em></small></p>
        </div>
        """

    def generate_sponsor_thank_you(self, name, amount, tier=None):
        """Génère un message de remerciement personnalisé"""
        if not tier:
            tier = self.get_tier_from_amount(amount)

        emojis = {'platinum': '🏆', 'gold': '🥇', 'silver': '🥈', 'bronze': '🥉'}
        emoji = emojis.get(tier, '⭐')

        message = f"""
        {emoji} Merci {name} pour votre soutien de {amount}€!

        Votre contribution {self.get_impact_message(amount)}

        🌟 Niveau: {tier.capitalize() if tier else 'Supporter'}
        """

        return message

    def get_compliance_info(self):
        """Informations de conformité pour les sponsors"""
        return {
            'transparency': "100% transparent sur l'utilisation des fonds",
            'reporting': "Rapports trimestriels disponibles pour les supporters",
            'privacy': "Respect total de la vie privée des supporters",
            'tax_deductible': "Les donations peuvent être déductibles d'impôts selon votre pays"
        }

    def create_funding_roadmap(self):
        """Roadmap d'utilisation des fonds"""
        return {
            'maintenance': {
                'percentage': 40,
                'description': 'Mises à jour, compatibilité, correction de bugs',
                'estimated_hours': 40,
                'examples': ['Support Python 3.12+', 'Mise à jour pandas', 'Fix CVEs']
            },
            'documentation': {
                'percentage': 25,
                'description': 'Guides, tutoriels, exemples',
                'estimated_hours': 25,
                'examples': ['Tutoriels vidéo', 'Cas d\'usage', 'Documentation API']
            },
            'development': {
                'percentage': 25,
                'description': 'Nouvelles fonctionnalités, optimisations',
                'estimated_hours': 25,
                'examples': ['Nouveaux modèles ML', 'Temps réel', 'Interface améliorée']
            },
            'community': {
                'percentage': 10,
                'description': 'Webinaires, support, événements',
                'estimated_hours': 10,
                'examples': ['Webinaires mensuels', 'Support prioritaire', 'Workshops']
            }
        }

    def get_success_metrics(self):
        """Métriques de succès pour suivre l'impact du soutien"""
        return {
            'academic_impact': {
                'universities': 0,
                'students': 0,
                'publications': 0,
                'courses': 0
            },
            'industry_impact': {
                'companies': 0,
                'deployments': 0,
                'countries': 0,
                'downloads': 0
            },
            'community_impact': {
                'github_stars': 0,
                'forks': 0,
                'contributors': 0,
                'issues_resolved': 0
            }
        }

# Instance globale pour l'application
support_config = SupportConfig()