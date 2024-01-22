import React from 'react';
import './Footer.css'; // Assuming a CSS file for styling the footer component

const Footer = () => {
  return (
    <footer id="footer">
      <div className="footer-content">
        <h3>DevFusion</h3>
        <p>Enhancing development with AI-powered tools.</p>
        <ul className="footer-links">
          <li><a href="https://github.com/DevFusion/DevFusion">GitHub</a></li>
          <li><a href="/docs/user_guide.md">User Guide</a></li>
          <li><a href="/docs/api_reference.md">API Reference</a></li>
        </ul>
      </div>
      <div className="footer-bottom">
        <p>© {new Date().getFullYear()} DevFusion. All rights reserved.</p>
      </div>
    </footer>
  );
};

export default Footer;