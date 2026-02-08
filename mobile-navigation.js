/* ========== MOBILE NAVIGATION JAVASCRIPT ========== */

// Initialize mobile navigation when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Only run on mobile devices
    if (window.innerWidth <= 768) {
        initMobileNavigation();
    }
    
    // Re-initialize on window resize
    let resizeTimer;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(function() {
            if (window.innerWidth <= 768) {
                initMobileNavigation();
            } else {
                removeMobileNavigation();
            }
        }, 250);
    });
});

function initMobileNavigation() {
    // Check if mobile elements already exist
    if (document.querySelector('.mobile-menu-toggle')) {
        return;
    }
    
    // Create hamburger menu button
    const menuToggle = document.createElement('button');
    menuToggle.className = 'mobile-menu-toggle';
    menuToggle.setAttribute('aria-label', 'Toggle menu');
    menuToggle.innerHTML = `
        <div class="hamburger">
            <span></span>
            <span></span>
            <span></span>
        </div>
    `;
    
    // Create overlay backdrop
    const overlay = document.createElement('div');
    overlay.className = 'mobile-overlay';
    
    // Add elements to body
    document.body.appendChild(menuToggle);
    document.body.appendChild(overlay);
    
    // Get main navigation
    const mainNav = document.querySelector('.main-nav');
    
    // Toggle menu function
    function toggleMenu() {
        const isActive = mainNav.classList.contains('active');
        
        if (isActive) {
            // Close menu
            mainNav.classList.remove('active');
            menuToggle.classList.remove('active');
            overlay.classList.remove('active');
            document.body.classList.remove('menu-open');
        } else {
            // Open menu
            mainNav.classList.add('active');
            menuToggle.classList.add('active');
            overlay.classList.add('active');
            document.body.classList.add('menu-open');
        }
    }
    
    // Event listeners
    menuToggle.addEventListener('click', toggleMenu);
    overlay.addEventListener('click', toggleMenu);
    
    // Close menu when clicking on a navigation link
    const navLinks = mainNav.querySelectorAll('a');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            // Small delay to allow navigation to complete
            setTimeout(toggleMenu, 100);
        });
    });
    
    // Close menu on escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && mainNav.classList.contains('active')) {
            toggleMenu();
        }
    });
    
    // Prevent body scroll when menu is open
    let touchStartY = 0;
    mainNav.addEventListener('touchstart', function(e) {
        touchStartY = e.touches[0].clientY;
    });
    
    mainNav.addEventListener('touchmove', function(e) {
        const touchY = e.touches[0].clientY;
        const touchDelta = touchY - touchStartY;
        const scrollTop = mainNav.scrollTop;
        const scrollHeight = mainNav.scrollHeight;
        const clientHeight = mainNav.clientHeight;
        
        // Prevent overscroll
        if ((scrollTop === 0 && touchDelta > 0) || 
            (scrollTop + clientHeight >= scrollHeight && touchDelta < 0)) {
            e.preventDefault();
        }
    }, { passive: false });
}

function removeMobileNavigation() {
    // Remove mobile elements when switching to desktop
    const menuToggle = document.querySelector('.mobile-menu-toggle');
    const overlay = document.querySelector('.mobile-overlay');
    const mainNav = document.querySelector('.main-nav');
    
    if (menuToggle) menuToggle.remove();
    if (overlay) overlay.remove();
    
    if (mainNav) {
        mainNav.classList.remove('active');
    }
    
    document.body.classList.remove('menu-open');
}

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        if (href !== '#' && href !== '#!') {
            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        }
    });
});
