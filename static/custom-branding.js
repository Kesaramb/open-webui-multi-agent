// BrandFactory custom branding script
// This script runs client-side to customize the displayed name
// Note: This maintains legal compliance as it's client-side presentation only

(function() {
    'use strict';

    // Function to clean up the displayed name
    function cleanBrandingText() {
        // Find all text nodes containing "(Open WebUI)" and replace
        const walker = document.createTreeWalker(
            document.body,
            NodeFilter.SHOW_TEXT,
            null,
            false
        );

        let node;
        while (node = walker.nextNode()) {
            if (node.nodeValue && node.nodeValue.includes('(Open WebUI)')) {
                node.nodeValue = node.nodeValue.replace(/\s*\(Open WebUI\)/g, '');
            }
        }

        // Update document title
        if (document.title.includes('(Open WebUI)')) {
            document.title = document.title.replace(/\s*\(Open WebUI\)/g, '');
        }
    }

    // Run on page load
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', cleanBrandingText);
    } else {
        cleanBrandingText();
    }

    // Also run when content changes (for SPAs)
    const observer = new MutationObserver(cleanBrandingText);
    observer.observe(document.body, {
        childList: true,
        subtree: true
    });

    // Run periodically to catch any dynamic updates
    setInterval(cleanBrandingText, 1000);
})();
