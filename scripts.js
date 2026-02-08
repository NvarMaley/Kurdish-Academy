// Attendre que le document soit complètement chargé
document.addEventListener('DOMContentLoaded', function() {
    // Fonction pour initialiser la navigation
    function initializeNavigation() {
        // Récupérer les éléments du DOM
        const kurmancLinks = document.querySelectorAll('#kurmanci-link');
        const soraniLinks = document.querySelectorAll('#sorani-link');
        const cultureLinks = document.querySelectorAll('#culture-link');
        const homeSubnav = document.getElementById('home-subnav');
        const kurmanciSubnav = document.getElementById('kurmanci-subnav');
        const soraniSubnav = document.getElementById('sorani-subnav');
        const cultureSubnav = document.getElementById('culture-subnav');
        
        // Fonction pour masquer toutes les barres de sous-navigation
        function hideAllSubnavs() {
            if (homeSubnav) homeSubnav.style.display = 'none';
            if (kurmanciSubnav) kurmanciSubnav.style.display = 'none';
            if (soraniSubnav) soraniSubnav.style.display = 'none';
            if (cultureSubnav) cultureSubnav.style.display = 'none';
        }
        
        // Fonction pour réinitialiser les classes active
        function resetActiveClasses() {
            document.querySelectorAll('.main-nav a').forEach(function(link) {
                link.classList.remove('active');
            });
        }
        
        // Ajouter des écouteurs d'événements pour tous les liens Kurmancî
        kurmancLinks.forEach(function(link) {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                hideAllSubnavs();
                if (kurmanciSubnav) kurmanciSubnav.style.display = 'block';
                resetActiveClasses();
                link.classList.add('active');
            });
        });
        
        // Ajouter des écouteurs d'événements pour tous les liens Sorani
        soraniLinks.forEach(function(link) {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                hideAllSubnavs();
                if (soraniSubnav) soraniSubnav.style.display = 'block';
                resetActiveClasses();
                link.classList.add('active');
            });
        });
        
        // Ajouter des écouteurs d'événements pour tous les liens Culture
        cultureLinks.forEach(function(link) {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                hideAllSubnavs();
                if (cultureSubnav) cultureSubnav.style.display = 'block';
                resetActiveClasses();
                link.classList.add('active');
            });
        });
        
        // Ajouter des écouteurs d'événements pour tous les liens Home
        const homeLinks = document.querySelectorAll('.main-nav a[href*="index.html"]');
        homeLinks.forEach(function(link) {
            link.addEventListener('click', function() {
                hideAllSubnavs();
                if (homeSubnav) homeSubnav.style.display = 'block';
                resetActiveClasses();
                link.classList.add('active');
            });
        });
    }
    
    // Initialiser la navigation
    initializeNavigation();
});
