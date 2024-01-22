import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import Navbar from '../../src/frontend/src/components/Navbar';
import Footer from '../../src/frontend/src/components/Footer';
import CustomComponent1 from '../../src/frontend/src/components/CustomComponent1';
import CustomComponent2 from '../../src/frontend/src/components/CustomComponent2';

describe('Frontend component tests for DevFusion', () => {
  test('Navbar renders with correct branding', () => {
    render(<Navbar />);
    const navbarElement = screen.getByTestId('navbar');
    expect(navbarElement).toBeInTheDocument();
    expect(navbarElement).toHaveTextContent('DevFusion');
  });

  test('Footer contains correct copyright notice', () => {
    render(<Footer />);
    const footerElement = screen.getByTestId('footer');
    expect(footerElement).toBeInTheDocument();
    expect(footerElement).toHaveTextContent(`© ${new Date().getFullYear()} DevFusion`);
  });

  test('CustomComponent1 initializes with default state', () => {
    render(<CustomComponent1 />);
    const customComponent1Element = screen.getByTestId('custom-component-1');
    expect(customComponent1Element).toBeInTheDocument();
    // Assuming CustomComponent1 has a default state to check
    expect(customComponent1Element).toHaveTextContent('Default State');
  });

  test('CustomComponent2 responds to user interaction', () => {
    render(<CustomComponent2 />);
    const customComponent2Element = screen.getByTestId('custom-component-2');
    expect(customComponent2Element).toBeInTheDocument();
    // Assuming CustomComponent2 has an interactive element like a button
    const buttonElement = screen.getByRole('button', { name: /interact/i });
    fireEvent.click(buttonElement);
    expect(customComponent2Element).toHaveTextContent('Interaction Handled');
  });
});