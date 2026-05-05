/**
 * TRITECH Theme Toggle System
 * Handles dark/light mode switching with localStorage persistence
 */
(function () {
  'use strict';

  // Apply saved theme IMMEDIATELY (before DOM paint) to prevent flash
  const savedTheme = localStorage.getItem('tritech-theme') || 'light';
  document.documentElement.setAttribute('data-theme', savedTheme);

  document.addEventListener('DOMContentLoaded', function () {
    // Find the toggle button
    const toggleBtn = document.querySelector('.theme-toggle');
    if (!toggleBtn) return;

    toggleBtn.addEventListener('click', function () {
      const currentTheme = document.documentElement.getAttribute('data-theme');
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';

      document.documentElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('tritech-theme', newTheme);
    });
  });
})();
